from flask import Flask
from routes import my_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint)


if __name__ == "__main__":
    app.run(debug=True)