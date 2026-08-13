from flask import flash, redirect, url_for

from app import app
from app.forms.comment.comment_form import CommentForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService
from app.services.comment_service import CommentService


@app.post('/tickets/<int:ticket_id>/comments')
@auth_required()
@inject
def comment_add(
    ticket_id: int,
    comment_service: CommentService,
    auth_service: AuthService
):
    form = CommentForm()

    if not form.validate_on_submit():
        flash("Commentaire invalide.", "danger")
        return redirect(url_for('ticket_detail', ticket_id=ticket_id))

    current_user = auth_service.get_current_user()

    if current_user is None:
        flash("Utilisateur introuvable.", "danger")
        return redirect(url_for('index'))

    comment = comment_service.insert(
        form,
        ticket_id,
        current_user
    )

    if comment is None:
        flash("Impossible d'ajouter le commentaire.", "danger")
    else:
        flash("Commentaire ajouté.", "success")

    return redirect(url_for('ticket_detail', ticket_id=ticket_id))