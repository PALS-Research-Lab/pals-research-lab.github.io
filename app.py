from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="_site", static_url_path="")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    full_path = os.path.join("_site", path)
    if os.path.isfile(full_path):
        return send_from_directory("_site", path)
    if os.path.isfile(full_path + ".html"):
        return send_from_directory("_site", path + ".html")
    return send_from_directory("_site", "index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
