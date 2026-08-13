# Keep it up to date for every new controller and route
from app.controllers.home_controller import index
from app.controllers.comment_controller import comment_add
from app.controllers.user_controller import (
    login,
    logout,
    register,
    email_verify,
    email_verify_resend,
    password_forgot,
    password_reset,
    user_list,
    user_profile,
    profile,
    user_update,
    user_delete,
)

__all__ = [
    "index",
    "login",
    "logout",
    "register",
    "email_verify",
    "email_verify_resend",
    "password_forgot",
    "password_reset",
    "user_list",
    "user_profile",
    "profile",
    "user_update",
    "user_delete",
	"comment_add",
]
