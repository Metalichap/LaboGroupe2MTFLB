from app.dtos.ticketstatushistory_dto import TicketStatusHistoryDTO
from app.framework.decorators.injectable import injectable
from app.mappers.ticketstatushistory_mapper import TicketStatusHistoryMapper
from app.models.ticketstatushistory import TicketStatusHistory
from app.services.base_service import BaseService


@injectable
class TicketStatusHistoryService(BaseService):

    def find_by_ticket(
        self,
        ticket_id: int
    ) -> list[TicketStatusHistoryDTO]:

        histories = (
            TicketStatusHistory.query
            .filter_by(
                ticket_id=ticket_id,
                active=True)
            .order_by(TicketStatusHistory.created_at.asc())
            .all()
        )

        return [
            TicketStatusHistoryMapper.entity_to_dto(history)
            for history in histories
        ]


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