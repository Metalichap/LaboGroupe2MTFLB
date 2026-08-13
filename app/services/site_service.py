from app import app, db
from app.framework.decorators.injectable import injectable
from app.services.base_service import BaseService
from app.dtos.site_dto import SiteDTO
from app.models.site import Site
from app.mappers.site_mapper import SiteMapper
from app.forms.site.site_form import SiteForm


@injectable
class SiteService(BaseService):
    """Gestion des sites"""
    def find_all(self) -> list[SiteDTO]:
        return [SiteMapper.entity_to_dto(site) for site in Site.query.filter_by(active=True).order_by(Site.site_name).all()]
        
    def find_one(self, entity_id: int) -> SiteDTO | None:
        site = self.find_one_entity(entity_id)

        return SiteMapper.entity_to_dto(site) if site else None

    def find_one_entity(self, entity_id: int) -> Site | None:
        return Site.query.filter_by(site_id=entity_id).first()

    def find_one_by(self, **kwargs) -> SiteDTO | None:
        site = Site.query.filter_by(**kwargs).first()

        return SiteMapper.entity_to_dto(site) if site else None
    # Ecriture
    def insert(self, form: SiteForm) -> SiteDTO | None:
        """
        Ajout d'un nouveau site
        """
        site = Site()
        SiteMapper.form_to_entity(form, site)
        try:
            db.session.add(site)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert site: {e}")
            db.session.rollback()
            return None
        return SiteMapper.entity_to_dto(site)

    def update(self):
        """
        """
        raise NotImplementedError("")

    def delete(self):
        """
        """
        raise NotImplementedError("")
