from app import app
from flask import render_template, request, redirect, url_for, send_from_directory, send_file
import os
from PIL import Image
import zipfile

def generateThumbnails():
   size = 128, 128
   imagesList = os.listdir(app.config["UPLOADED_IMAGES"])
   for image in imagesList:
      thumbnailImage = Image.open(app.config["UPLOADED_IMAGES"] + image)
      thumbnailImage.thumbnail(size, Image.ANTIALIAS)
      filePath = app.config["THUMBNAILS"] + image
      thumbnailImage.save(filePath, "JPEG")

def zipThumbnails():
   filename = os.path.join(app.config["DOWNLOADS"], "thumbnails.zip").replace("\\", '/')
   zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
   for files in os.listdir(app.config["THUMBNAILS"]):
      for file in [files]:
         zipf.write(app.config["THUMBNAILS"] + file, file)
   zipf.close()
   return filename

@app.route('/', methods = ["POST", "GET"])
def uploadImage():
   if request.method == "POST":
      images = request.files.getlist("image")
      for image in images:
         image.save(os.path.join(app.config["UPLOADED_IMAGES"], image.filename))
      generateThumbnails()
      filename = os.path.basename(zipThumbnails())
      return redirect(url_for("downloadThumbnails", filename = filename))

   return render_template("uploadImage.html")

@app.route("/download/<filename>")
def downloadThumbnails(filename):
   return send_from_directory(
      os.path.abspath(app.config["DOWNLOADS"]) + '/', filename = filename, as_attachment = True
   )