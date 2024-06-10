import json
from flask import render_template
from datetime import datetime
# from modules import modules


def configure_routes(app):
    # Define the maximum allowed file size in bytes (e.g., 10 MB)
    MAX_FILE_SIZE_BYTES = 1000 * 1024 * 1024  # 1 GB
    # Define the maximum allowed total folder size in bytes (e.g., 100 MB)
    MAX_FOLDER_SIZE_BYTES = 10000 * 1024 * 1024  # 10 GB
    current_date = datetime.now().strftime('%d.%m.%y')
    '''
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'ascii.json')
    with open(json_path, "r", encoding="utf-8") as json_file:
        ascii_json = json.load(json_file)
    kabluki = ascii_json.get("kabluki", "Default Value")
    '''

    with open("ascii.json", "r", encoding="utf-8") as file:
        ascii_json = json.load(file)
    kabluki = ascii_json["kabluki"]

    @app.route('/')
    def index():
        return render_template('index.html', kabluki=kabluki)

    @app.route('/status')
    def status():
        message = ""
        message += "Hello!"
        if current_date:
            message += "<br>current_date: works"
        if status:
            message += ("<br>File size limit: "
                        f"{round(MAX_FILE_SIZE_BYTES/1000000/1000)} GB, "
                        "Folder size limit: "
                        f"{round(MAX_FOLDER_SIZE_BYTES/1000000/1000)} GB")
        return message
