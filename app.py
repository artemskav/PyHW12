from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['JSON_AS_ASCII'] = False
app.config['POST_PATH'] = "posts.json"
app.config["UPLOAD_FOLDER"] = "uploads/images"
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

if __name__ == "__main__":
    app.run(debug=True)
