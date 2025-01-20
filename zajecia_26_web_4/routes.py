from flask import Blueprint
from views import show_main_view, UsersView
my_blueprint = Blueprint("my_blueprint", __name__)


@my_blueprint.route('/')
def main_view():
    return show_main_view()

my_blueprint.add_url_rule("/users/", view_func=UsersView.as_view("users_view"))