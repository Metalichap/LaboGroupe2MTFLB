from flask import flash, redirect, render_template, request, url_for


from app import app
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.models.role import RoleStatus
from app.services.team_service import TeamService
from app.forms.team.team_form import TeamForm

@app.route("/teams", methods=["GET"])
@auth_required()
@inject
def team_list(team_service: TeamService):
    return render_template("teams/list.html", teams=team_service.find_all())

@app.route("/teams/add", methods=["GET", "POST"])
@auth_required(level=RoleStatus.ADMIN)
@inject
def team_add(team_service: TeamService):
    form = TeamForm()

    if form.validate_on_submit():
        team = team_service.insert(form)

        if team is None:
            flash("Ce nom d'équipe est déjà utilisé.", "danger")
        else:
            flash("Equipe créée.", "success")
            return redirect(url_for("team_list"))

    return render_template("teams/add_or_update.html", form=form, team=None)

@app.route('/teams/<int:team_id>/update', methods=['GET', 'POST'])
@auth_required()
@inject
def team_update(team_id: int, team_service: TeamService):
    team = team_service.find_one(team_id)

    if team is None:
        flash("Equipe introuvable.", "warning")
        return redirect(url_for('team_list'))

    # obj=team pré-remplit les champs de même nom en GET.
    form = TeamForm(obj=team)

    if form.validate_on_submit():
        updated = team_service.update(team_id, form)

        if updated is None:
            flash("Ce nom de équipe est déjà utilisé.", "danger")
        else:
            flash("Equipe mise à jour.", "success")
            return redirect(url_for('team_list'))

    return render_template("teams/add_or_update.html", form=form, team=team)

@app.post('/teams/<int:team_id>/delete')
@auth_required()
@inject
def team_delete(team_id: int, team_service: TeamService):
    """Désactive une équipe (soft delete).

    En POST et pas en GET: une action qui modifie l'état ne doit jamais être
    accessible par un simple lien.
    """
    if team_service.delete(team_id) is None:
        flash("Suppression impossible.", "danger")
    else:
        flash("Equipe désactivée.", "success")

    return redirect(url_for('team_list'))
