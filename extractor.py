import os
import shutil

def extract(application):
    app = os.path.abspath(application)

    shutil.unpack_archive(app, app[0 : -4], 'zip')
