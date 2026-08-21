from app import app, db

from app.dtos.comment_dto import CommentDTO
from app.dtos.user_dto import UserDTO
from app.forms.comment.comment_form import CommentForm
from app.framework.decorators.injectable import injectable
from app.mappers.comment_mapper import CommentMapper
from app.models.comment import Comment
from app.models.ticket import Ticket
from app.services.base_service import BaseService


@injectable
class CommentService(BaseService):

    def insert(
        self,
        form: CommentForm,
        ticket_id: int,
        current_user: UserDTO ) -> CommentDTO | None:

        ticket = db.session.get(Ticket, ticket_id)

        if ticket is None or not ticket.active:
            return None

        # un check pour voir si l'utilisateur peut acceder au tickets?

        comment = Comment()

        CommentMapper.form_to_entity(form, comment)

        comment.author_id = current_user.user_id
        comment.ticket_id = ticket.ticket_id

        try:
            db.session.add(comment)
            db.session.commit()

        except Exception as e:
            app.logger.error(f"insert comment: {e}")
            db.session.rollback()
            return None

        return CommentMapper.entity_to_dto(comment)

    def find_by_ticket(self, ticket_id: int) -> list[CommentDTO]:
        comments = (
        Comment.query
        .filter_by(
            ticket_id=ticket_id,
            active=True
        )
        .order_by(Comment.created_at.asc())
        .all()
    )
        
        return [ CommentMapper.entity_to_dto(comment)
			for comment in comments ]

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