from app.dtos.abstract_dto import AbstractDTO


class AttachmentDTO(AbstractDTO):

    def __init__(self):
        self.attachment_id = None
        self.attachment_filename = None
        self.attachment_path = None
        self.attachment_size = None
        self.ticket_id = None
        self.author_id = None
        self.created_at = None
        
    @staticmethod
    def build_from_entity(attachment) -> "AttachmentDTO":
        attachment_dto = AttachmentDTO()

        attachment_dto.attachment_id = attachment.attachment_id
        attachment_dto.attachment_filename = attachment.attachment_filename
        attachment_dto.attachment_path = attachment.attachment_path
        attachment_dto.attachment_size = attachment.attachment_size
        attachment_dto.ticket_id = attachment.ticket_id
        attachment_dto.author_id = attachment.author_id
        attachment_dto.created_at = attachment.created_at

        return attachment_dto

    def get_json_parsable(self):
        return dict(self.__dict__)