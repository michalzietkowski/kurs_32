from flask.views import MethodView


def show_main_view():
    return "Hello World!"


class UsersView(MethodView):
    def get(self):
        return "Hello Users!"

    def post(self):
        return "Hello Users you made post request!"