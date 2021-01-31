import os
import shutil
import json

def start_app(app):
    application = os.path.abspath(app)
    shutil.unpack_archive(
        application,
        os.path.expanduser('~/.bpkg'),
        'zip'
    )

    app_json = json.loads(open(os.path.expanduser('~/.bpkg') + '/app.json').read())

    os.system(
        'cd '
        + os.path.expanduser('~/.bpkg')
        + '/'
        + os.path.basename(application)[0 : -4]
        + '; '
        + app_json['run']
    )

        
