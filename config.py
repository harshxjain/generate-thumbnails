class Config(object):
   DEBUG = False
   UPLOADED_IMAGES = "app\\static\\uploadedImages\\"
   THUMBNAILS = "app\\static\\thumbnails\\"
   DOWNLOADS = "app\\downloadables\\"
   ABSOLUTE = "D:\\Python\\webApplication\\app\\downloadables\\"

class DevelopmentConfig(Config):
   DEBUG = True

class ProductionConfig(Config):
   pass