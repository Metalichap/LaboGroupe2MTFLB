from app.dtos.abstract_dto import AbstractDTO


class TicketStatusHistoryDTO(AbstractDTO):

    def __init__(self):
        self.history_id = None
        self.ticket_id = None
        self.user_id = None
        self.old_status = None
        self.new_status = None
        self.created_at = None

    @staticmethod
    def build_from_entity(history) -> "TicketStatusHistoryDTO":
        history_dto = TicketStatusHistoryDTO()

        history_dto.history_id = history.history_id
        history_dto.ticket_id = history.ticket_id
        history_dto.user_id = history.user_id
        history_dto.old_status = history.old_status
        history_dto.new_status = history.new_status
        history_dto.created_at = history.created_at

        return history_dto

    def get_json_parsable(self):
        return dict(self.__dict__)