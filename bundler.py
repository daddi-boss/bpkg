import os
import shutil
import zipfile

def bundle(proj_dir):
    project_dir = os.path.abspath(proj_dir)

    shutil.make_archive(project_dir, 'zip', project_dir)

    if not os.path.exists(project_dir + '/app.json'):
        with zipfile.ZipFile(project_dir + '.zip', 'w') as zipped_file:
            zipped_file.write('./defaults/app.json', 'app.json')

    os.rename(project_dir + '.zip', project_dir + '.bpkg')

    
