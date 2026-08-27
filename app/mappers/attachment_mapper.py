from app.dtos.attachment_dto import AttachmentDTO
from app.forms.attachment.attachment_form import AttachmentForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.attachment import Attachment


class AttachmentMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Attachment) -> AttachmentDTO:
        return AttachmentDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(
        form: AttachmentForm,
        attachment: Attachment
    ) -> Attachment:
        raise NotImplementedError("géré dans le service")