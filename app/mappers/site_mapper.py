from app.dtos.site_dto import SiteDTO
from app.mappers.abstract_mapper import AbstractMapper
from app.models.site import Site
from app.forms.site.site_form import SiteForm

class SiteMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(site: Site) -> SiteDTO:
        return SiteDTO.build_from_entity(site)

    @staticmethod
    def form_to_entity(form, site: Site):
        if isinstance(form, SiteForm):
            site.site_name = form.name.data
            site.site_address = form.address.data or ""
            site.site_city = form.city.data or ""