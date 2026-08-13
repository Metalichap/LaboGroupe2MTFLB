from app.dtos.comment_dto import CommentDTO
from app.forms.comment.comment_form import CommentForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.comment import Comment


class CommentMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Comment) -> CommentDTO:
        return CommentDTO.build_from_entity(entity)

	# je ne map que le content pour éviter une manipulation des user datas
    # les user datas seront ajoutés dans le service
    @staticmethod
    def form_to_entity(
        form: CommentForm,
        comment: Comment
    ) -> Comment:

        comment.comment_content = form.comment_content.data

        return comment