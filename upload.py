import os, flask


app = flask.Flask(__name__)

def handle(file):
  name = file.filename

  fp = f"files/{name}"

  
  file.save(fp)

def main(file):
  @app.route("/")
  def index():
    return flask.render_template(file)

def onupload(function):
  @app.route("/upload", methods=["POST"])
  def upload():
    return function(flask.request.files)

    