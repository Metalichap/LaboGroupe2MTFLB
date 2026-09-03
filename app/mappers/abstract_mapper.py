from abc import ABC, abstractmethod
from flask_wtf import FlaskForm
from app.models.base_entity import BaseEntity


class AbstractMapper[DTO, U: BaseEntity, V: FlaskForm](ABC):
    """Contrat des mappers: la traduction entre les couches.

    Trois représentations d'une même donnée coexistent dans le projet:

        Form  (ce que le navigateur envoie)
          |  form_to_entity
          v
        Entity (ce que la base stocke)
          |  entity_to_dto
          v
        DTO   (ce que la vue affiche)

    Centraliser ces conversions ici évite de les réécrire dans chaque service
    et donne un seul endroit à corriger quand un champ change de nom.
    """

    @staticmethod
    @abstractmethod
    def entity_to_dto(entity: U) -> DTO:
        pass

    @staticmethod
    @abstractmethod
    def form_to_entity(form: V, entity: U) -> U:
        pass
