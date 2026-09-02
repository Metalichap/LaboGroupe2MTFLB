"""Controller des tickets: listing, listing par technicien, création, édition.

Même motif POST/Redirect/GET que dans user_controller.py.
Accès simplement authentifié pour l'instant (@auth_required() sans niveau).
La gestion des permissions (technicien, admin, ... ) sera fignolée avec Théo.
"""
from flask import flash, redirect, render_template, request, url_for

from app import app
from app.errors import MissingDataException
from app.forms.ticket.ticket_create_form import TicketCreateForm
from app.forms.ticket.ticket_update_form import TicketUpdateForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.models.role import RoleStatus
from app.models.ticket import TicketStatus
from app.models.priority import PriorityLevel
from app.services.auth_service import AuthService
from app.services.category_service import CategoryService
from app.services.priority_service import PriorityService
from app.services.ticket_service import TicketService
from app.services.user_service import UserService
from app.mappers.ticket_mapper import TicketMapper


def _populate_category_and_priority_choices(form, category_service: CategoryService,
                                             priority_service: PriorityService):
    """Commun aux deux formulaires: catégories et priorités viennent de la DB,
    donc peuplées ici plutôt qu'en dur dans la classe du formulaire (voir
    ticket_create_form.py / ticket_update_form.py)."""
    form.category_id.choices = [(category.category_id, category.category_name)
                                 for category in category_service.find_all()]
    form.priority_id.choices = [(priority.priority_id, priority.priority_name)
                                 for priority in priority_service.find_all()]


# --- listing ------------------------------------------------------------

@app.get('/tickets')
@auth_required()  # TODO: probablement réservé aux techniciens/admins plus tard
@inject
def ticket_list(ticket_service: TicketService, user_service: UserService):
    return render_template('tickets/list.html',
                          tickets=ticket_service.find_all(),
                          technicians=user_service.find_all_by_role(RoleStatus.TECHNICIAN),
                          selected_technician_id=None)


@app.get('/tickets/technician/<int:technician_id>')
@auth_required()  # TODO: Limit access
@inject
def ticket_list_by_technician(technician_id: int, ticket_service: TicketService,
                              user_service: UserService):
    technician = user_service.find_one(technician_id)

    if technician is None:
        flash("Technicien introuvable.", "warning")
        return redirect(url_for('ticket_list'))

    tickets = ticket_service.find_all_by_technician(technician_id)

    return render_template('tickets/list.html',
                          tickets=tickets,
                          technician=technician,
                          technicians=user_service.find_all_by_role(RoleStatus.TECHNICIAN),
                          selected_technician_id=technician_id)


# --- création -------------------------------------------------------------

@app.route('/tickets/add', methods=['GET', 'POST'])
@auth_required()  # TODO: probablement ouvert à tout utilisateur connecté (auteur = lui-même)
@inject
def ticket_add(ticket_service: TicketService, category_service: CategoryService,
               priority_service: PriorityService, auth_service: AuthService):
    form = TicketCreateForm()
    _populate_category_and_priority_choices(form, category_service, priority_service)

    current_user = auth_service.get_current_user()

    if current_user is None:
        flash("Utilisateur introuvable.", "warning")
        return redirect(url_for('index'))

    #Selectionnée priorité normal par défaut dans le formulaire, en GET
    if request.method == 'GET' :
        default_priority = priority_service.find_one_by(priority_level = PriorityLevel.NORMAL)
        if default_priority is not None :
            form.priority_id.data = default_priority.priority_id



    if form.validate_on_submit():
        if form.ticket_title.data is None:
            raise MissingDataException("missing ticket_title !")
        command  = TicketMapper.form_to_create_command(form)
        # L'auteur n'est jamais un champ du formulaire: c'est toujours
        # l'utilisateur connecté qui crée le ticket, jamais une valeur postée
        # (même raisonnement que pour user_id/roles dans user_controller.py).
        ticket = ticket_service.insert(command, author_id=current_user.user_id)

        if ticket is None:
            flash("Impossible de créer le ticket.", "danger")
        else:
            flash("Ticket créé.", "success")
            return redirect(url_for('ticket_list'))

    return render_template('tickets/add.html', form=form)


# --- édition ----------------------------------------------------------------

@app.route('/tickets/<int:ticket_id>/edit', methods=['GET', 'POST'])
@auth_required()  # TODO: probablement réservé à l'auteur, au technicien assigné, ou à un admin
@inject
def ticket_update(ticket_id: int, ticket_service: TicketService,
                  category_service: CategoryService, priority_service: PriorityService,
                  user_service: UserService):
    ticket = ticket_service.find_one(ticket_id)

    if ticket is None:
        flash("Ticket introuvable.", "warning")
        return redirect(url_for('ticket_list'))

    # obj=ticket pré-remplit les champs de même nom en GET.
    form = TicketUpdateForm(obj=ticket)
    _populate_category_and_priority_choices(form, category_service, priority_service)

    # ticket_status: enum Python fixe, pas de requête DB nécessaire.
    form.ticket_status.choices = [(status.name, status.value) for status in TicketStatus]

    # technician_id: uniquement les techniciens actifs, plus une option vide
    # pour "non assigné".
    form.technician_id.choices = [('', '-- Non assigné --')] + [
        (str(technician.user_id), technician.username)
        for technician in user_service.find_all_by_role(RoleStatus.TECHNICIAN)
    ]

    if form.validate_on_submit():
        if form.ticket_title.data is None:
            raise MissingDataException("missing ticket_title !")

        
        command  = TicketMapper.form_to_update_command(form)
        updated = ticket_service.update(ticket_id, command)

        if updated is None:
            flash("Impossible de mettre à jour le ticket.", "danger")
        else:
            flash("Ticket mis à jour.", "success")
            return redirect(url_for('ticket_list'))

    # En GET, préremplir le statut et le technicien actuels dans les selects.
    if request.method == 'GET':
        form.ticket_status.data = TicketStatus(ticket.ticket_status).name if ticket.ticket_status else None
        form.technician_id.data = str(ticket.technician_id) if ticket.technician_id else ''

    return render_template('tickets/update.html', form=form, ticket=ticket)