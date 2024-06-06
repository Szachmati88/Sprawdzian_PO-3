from flask import Flask
from backend.controllers.air_quality_controller import air_quality_blueprint

app = Flask(__name__)
app.register_blueprint(air_quality_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
