import upload

def onup(files):
  print(files)

  file = files["file"]

  upload.handle(file)

  return "OK"

upload.onupload(onup)

upload.main("index.html")

upload.app.run(host="0.0.0.0", port=80)