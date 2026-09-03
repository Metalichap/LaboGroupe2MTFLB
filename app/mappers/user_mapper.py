from app.dtos.user_dto import UserDTO
from app.forms.user.user_login_form import UserLoginForm
from app.forms.user.user_register_form import UserRegisterForm
from app.forms.user.user_update_form import UserUpdateForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.user import User


class UserMapper(AbstractMapper[UserDTO, User, UserRegisterForm]):
    @staticmethod
    def entity_to_dto(entity: User) -> UserDTO:
        return UserDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: UserRegisterForm, entity: User) -> User:
        """Reporte les champs du formulaire sur l'entité.

        Un seul mapper pour plusieurs formulaires: on regarde le type reçu.
        Chaque branche ne copie QUE les champs de ce formulaire — c'est ce qui
        garantit qu'un POST sur /profile/edit ne peut pas modifier le mot de
        passe ou le username, même si le navigateur les envoie.

        Le mot de passe est copié tel quel (en clair): c'est UserService qui le
        hashe juste après. Le mapper ne fait que traduire.
        """
        if isinstance(form, UserRegisterForm):
            entity.username = form.username.data
            entity.user_email = form.email.data
            entity.user_password = form.password.data
            entity.user_firstname = form.firstname.data
            entity.user_lastname = form.lastname.data


        elif isinstance(form, UserUpdateForm):
            entity.user_email = form.email.data
            # Les rôles ne sont PAS appliqués ici: c'est une opération
            # privilégiée, gérée par UserService.update après vérification des
            # droits de l'utilisateur connecté.

        elif isinstance(form, UserLoginForm):
            entity.username = form.username.data
            entity.user_password = form.password.data

        return entity
