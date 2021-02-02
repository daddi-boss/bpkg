import os
import shutil
import json

def start_app(app):
    application = os.path.abspath(app)
    
    if not os.path.exists(os.path.expanduser('~/.bpkg') + '/' + os.path.basename(application[0 : -5])):
        os.mkdir(os.path.expanduser('~/.bpkg') + '/' + os.path.basename(application[0 : -5]))

    shutil.unpack_archive(
        application,
        os.path.expanduser('~/.bpkg') + '/' + os.path.basename(application[0 : -5]),
        'zip'
    )

    app_json = json.loads(open(os.path.expanduser('~/.bpkg') + '/' + os.path.basename(application[0 : -5]) + '/app.json').read())

    os.system(
        'cd '
        + os.path.expanduser('~/.bpkg')
        + '/'
        + os.path.basename(application)[0 : -5]
        + '; '
        + app_json['run']
    )

        
