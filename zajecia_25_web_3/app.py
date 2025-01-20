from flask import Flask, render_template, request


app = Flask(__name__)


users = [
    {
        "name": "Michal",
        "surname": "Zietkowski",
        "email": "michalzietkowski@gmail.com"
    },
    {
        "name": "Adam",
        "surname": "Malysz",
        "email": "adammalysz@interia.pl"
    },
    {
        "name": "Mariusz",
        "surname": "Pudzianowski",
        "email": "mariusz.sila.pudzian@wp.pl"
    }
]


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/hello/")
@app.route("/hello/<name>/")
def hello(name=None):
    # print("Tutaj jestem")
    # wynik = 2 + 2
    # print(wynik)
    # if name:
    #     return f"Witaj, {name}!"
    # return "Hello, World!"
    return render_template("hello_user.html", imie=name)

@app.route("/users/", methods=["GET", "POST"])
def show_users():
    if request.method == "POST":
        users.append({
            "name": request.form.get("fname"),
            "surname": request.form.get("lname"),
            "email": request.form.get("email_name")
        })
    return render_template("users.html", users=users)

@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users.append({
            "name": request.form.get("fname"),
            "surname": request.form.get("lname"),
            "email": request.form.get("email_name")
        })
        return render_template("show_users.html", users=users)
    return render_template("create_user.html")

@app.route("/show_existing_users/")
def show_existing_users():
    return render_template("show_users.html", users=users)


@app.route("/multiple", methods=["GET", "POST"])
def multiple_forms():
    if request.method == "POST":
        print(request.form.get("form_type"))
        pass
    return render_template("example_with_multilple_forms.html")



if __name__ == "__main__":
    app.run(debug=True)
