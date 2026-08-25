from app import app, db
from pathlib import Path
from uuid import uuid4

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app.dtos.attachment_dto import AttachmentDTO
from app.dtos.user_dto import UserDTO
from app.forms.attachment.attachment_form import AttachmentForm
from app.framework.decorators.injectable import injectable
from app.mappers.attachment_mapper import AttachmentMapper
from app.models.attachment import Attachment
from app.models.ticket import Ticket
from app.services.base_service import BaseService
from app.services.ticket_service import TicketService

@injectable
class AttachmentService(BaseService):

    def insert(
        self,
        form: AttachmentForm,
        ticket_id: int,
        current_user: UserDTO ) -> AttachmentDTO | None:

        ticket = db.session.get(Ticket, ticket_id)

        if ticket is None or not ticket.active:
            return None

        if not TicketService.is_authorised(ticket, current_user):
                    return None
        
        file = form.file.data

        if file is None:
            return None

        original_filename = secure_filename(file.filename)

        if not original_filename:
            return None

        extension = Path(original_filename).suffix.lower()
        
        if extension not in {
                ".pdf", ".png", ".jpg", ".jpeg"}:
            return None

        if file.mimetype not in {
                "application/pdf",
                "image/png",
                "image/jpeg"}:
            return None

        if not file.content_length or file.content_length > 5 * 1024 * 1024:
            return None

        storage_filename = f"{uuid4().hex}{extension}"

        upload_path = Path(app.instance_path) / "attachments"

        upload_path.mkdir(parents=True, exist_ok=True)

        file_path = upload_path / storage_filename

        try:
            file.save(file_path)

            attachment = Attachment()

            attachment.attachment_filename = original_filename
            attachment.attachment_path = storage_filename
            attachment.attachment_size = file.content_length
            attachment.ticket_id = ticket.ticket_id
            attachment.author_id = current_user.user_id

            db.session.add(attachment)
            db.session.commit()

        except Exception as e:
            app.logger.error(f"insert attachment: {e}")
            db.session.rollback()

            if file_path.exists():
                file_path.unlink()

            return None

        return AttachmentMapper.entity_to_dto(attachment)


    def find_by_ticket(self,
                       ticket_id: int,
                       current_user: UserDTO) -> list[AttachmentDTO]:

        ticket = db.session.get(Ticket, ticket_id)

        if ticket is None or not ticket.active:
            return []

        if not TicketService.is_authorised(ticket, current_user):
            return []
        
        attachments = Attachment.query.filter_by(
            ticket_id=ticket_id,
            active=True
        ).order_by(Attachment.created_at.asc()).all()

        return [AttachmentMapper.entity_to_dto(attachment)
                for attachment in attachments]

    def find_for_download(
        self,
        attachment_id: int,
        current_user: UserDTO) -> AttachmentDTO | None:

        attachment = db.session.get(Attachment, attachment_id)

        if attachment is None or not attachment.active:
            return None

        ticket = db.session.get(Ticket, attachment.ticket_id)

        if ticket is None or not ticket.active:
            return None

        if not TicketService.is_authorised(ticket, current_user):
            return None

        return AttachmentMapper.entity_to_dto(attachment)

    def find_all(self):
        raise NotImplementedError

    def find_one(self, entity_id: int):
        raise NotImplementedError

    def find_one_by(self, **kwargs):
        raise NotImplementedError

    def update(self, entity_id: int, data):
        raise NotImplementedError

    def delete(self, entity_id: int):
        raise NotImplementedError

	

	
