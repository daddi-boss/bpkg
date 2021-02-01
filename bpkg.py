import sys
import os
import shutil

from bundler import bundle
from app_starter import start_app
from extractor import extract

def main():
    if not os.path.exists(os.path.expanduser('~/.bpkg')):
        os.mkdir(os.path.expanduser('~/.bpkg'))
    
    # Change this each time version changes
    if sys.argv[1] == '-v':
        print('bpkg application packaging utility version 1.0.0')
        exit()
    
    if sys.argv[1] == '-h':
        print(
            '''
            bpkg syntax - bpkg [-h|-v|start|bundle|extract|cleanup] foldername

            bpkg is a tool used to bundle applications.

              cleanup - Cleans up the bpkg cache
              start - This command is used to start the application.
              bundle - This command is used to bundle an application hence the name.
              extract - This command is used to extract the contents of an application from its bundle.
            '''
        )
        exit()
    
    if not sys.argv[1] == 'cleanup':
        if sys.argv[2] == None:
            print('The directory of the project you want to package should be the second argument')
    
    if sys.argv[1] == 'start':
        start_app(sys.argv[2])
    elif sys.argv[1] == 'cleanup':
        for root, dirs, files in os.walk(os.path.expanduser('~/.bpkg')):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
    elif sys.argv[1] == 'bundle':
        bundle(sys.argv[2])
    elif sys.argv[1] == 'extract':
        extract(sys.argv[2])
    else:
        print('bundle, start, cleanup or extract should be present as the second argument')
        exit()

if __name__ == '__main__':
    main()
