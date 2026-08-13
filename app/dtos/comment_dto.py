from app.dtos.abstract_dto import AbstractDTO


class CommentDTO(AbstractDTO):
    def __init__(self):
        self.comment_id = None
        self.comment_content = None
        self.author_id = None
        self.ticket_id = None

    @staticmethod
    def build_from_entity(comment) -> "CommentDTO":
        comment_dto = CommentDTO()

        comment_dto.comment_id = comment.comment_id
        comment_dto.comment_content = comment.comment_content
        comment_dto.author_id = comment.author_id
        comment_dto.ticket_id = comment.ticket_id

        return comment_dto

    def get_json_parsable(self):
        return self.__dict__