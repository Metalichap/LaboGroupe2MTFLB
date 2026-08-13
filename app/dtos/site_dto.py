from app.dtos.abstract_dto import AbstractDTO
from app.models.site import Site

class SiteDTO(AbstractDTO):
    """
    """

    def __init__(self):
        self.site_id = None
        self.site_name = None
        self.site_address = None
        self.site_city = None
        #self.users =
        #self.equipments =
    
    @staticmethod
    def build_from_entity(site: Site) -> "SiteDTO":
        site_dto = SiteDTO()

        site_dto.site_id = site.site_id
        site_dto.site_name = site.site_name
        site_dto.site_address = site.site_address
        site_dto.site_city = site.site_city

        return site_dto

    def get_json_parsable(self):
        return self.__dict__