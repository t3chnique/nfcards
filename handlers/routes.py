from flask import render_template
from datetime import datetime
from modules import modules


def configure_routes(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        return render_template("index.html", hello=hello, content=content)

    @app.route('/status')
    def status():
        MAX_FILE_SIZE_BYTES = modules.file_size()
        MAX_FOLDER_SIZE_BYTES = modules.file_size()
        current_date = datetime.now().strftime('%d.%m.%y')
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
