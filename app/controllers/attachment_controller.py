from flask import flash, redirect, url_for, abort, send_from_directory

from app import app
from app.forms.attachment.attachment_form import AttachmentForm
from app.framework.decorators.auth_required import auth_required
from app.services.auth_service import AuthService
from app.framework.decorators.inject import inject
from app.services.attachment_service import AttachmentService
from pathlib import Path

@app.post('/attachments/<int:attachment_id>/download')
@auth_required()
@inject
def attachment_download(
     attachment_id: int,
     attachment_service: AttachmentService,
     auth_service: AuthService):

        current_user = auth_service.get_current_user()

        if current_user is None:
            abort(404)

        attachment = attachment_service.find_for_download(
        attachment_id=attachment_id,
        current_user=current_user)

        if attachment is None:
            abort(404)

        upload_path = Path(app.instance_path) / "attachments"

        return send_from_directory(
            upload_path,
            attachment.attachment_path,
            as_attachment=True,
            download_name=attachment.attachment_filename)

@app.post('/ticket/<int:ticket_id>/attachments')
@auth_required()
@inject
def attachment_add(
    ticket_id: int,
    attachment_service: AttachmentService,
    auth_service: AuthService ):

    form = AttachmentForm()

    if not form.validate_on_submit():
        flash('Fichier invalide', "danger")
        return redirect(url_for("ticket_detail", ticket_id=ticket_id))

    current_user = auth_service.get_current_user()

    if current_user is None:
            flash("Utilisateur introuvable.", "danger")
            return redirect(url_for('index'))

    attachment = attachment_service.insert(
         form=form,
         ticket_id=ticket_id,
         current_user=current_user)

    if attachment is None:
         flash("Unable to upload attachment", "danger")
    else:
         flash("Upload successful", "success")

    return redirect(url_for('ticket_detail', ticket_id=ticket_id))