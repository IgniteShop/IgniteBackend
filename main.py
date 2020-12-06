from flask import Flask
from routes.generate import generate
from routes.names import image_name
import random

app = Flask(__name__)

# routes
app.register_blueprint(generate)
app.register_blueprint(image_name)

if __name__ == "__main__":
    app.run()