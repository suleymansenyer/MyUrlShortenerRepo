from flask import Flask
from app import myapp


app = Flask(__name__)
app.secret_key = 'yoursecretkey'
app.register_blueprint(myapp)


if __name__ == '__main__':
    app.run(debug=True)
