from flask import Blueprint, render_template, request
from views import get_history_for_history_view, get_data_for_main_view, save_data_for_book_purchase, save_data_for_balance_change
my_blueprint = Blueprint("my_blueprint", __name__)



@my_blueprint.route('/', methods=["GET", "POST"])
def main_view():
    if request.method == "POST":
        form_type = request.form.get("form_type")
        if form_type == "zakup_ksiazki":
            save_data_for_book_purchase(request.form)
        elif form_type == "zmiana_salda":
            save_data_for_balance_change(request.form)
    data = get_data_for_main_view()
    return render_template("index.html", data=data)


@my_blueprint.route('/history/<from_value>/<to_value>')
@my_blueprint.route('/history')
def history_view(from_value=0, to_value=None):
    history = get_history_for_history_view(from_value, to_value)
    return render_template("history.html", history=history)
