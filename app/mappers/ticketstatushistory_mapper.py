from app.dtos.ticketstatushistory_dto import TicketStatusHistoryDTO
from app.mappers.abstract_mapper import AbstractMapper
from app.models.ticketstatushistory import TicketStatusHistory


class TicketStatusHistoryMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(
        entity: TicketStatusHistory) -> TicketStatusHistoryDTO:
        return TicketStatusHistoryDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(
        form, entity: TicketStatusHistory) -> TicketStatusHistory:
        raise NotImplementedError(
            "Never created from a form.")