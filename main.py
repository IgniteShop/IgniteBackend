from flask import Flask
from routes.generate import generate

app = Flask(__name__)

# routes
app.register_blueprint(generate)

if __name__ == "__main__":
    app.run()