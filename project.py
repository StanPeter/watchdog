from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
import time
import subprocess

"""
DONE    WAV sin Editar only! 
DONE    .wav files only
DONE    all subfolders
DONE    run tharpa-robot-audio-cleanner-002.sh script

programme detects adding .wav files only to 'WAV sin Editar' folder,
works for all subfolders, after adding a .wav to 'WAV sin Editar' runs .sh script which prints 'hello world'

to quit the programm press Control-C
"""

class ExampleHandler(FileSystemEventHandler):
    patterns = ["*.wav"]
    def on_created(self, event): # when file is created
        # do something
        fileDir = os.path.basename(os.path.dirname(event.src_path))
        pyFilePath = os.path.dirname(os.path.abspath(__name__))

        try: 
            if fileDir == 'WAV sin Editar':  
                fileType = os.path.basename(event.src_path)[os.path.basename(event.src_path).index('.')+1:]
                if str(fileType) == 'wav':    
                    subprocess.call(pyFilePath + '/' + 'tharpa-robot-audio-cleanner-002.sh', shell=True)
                    print(f'even type: {event.event_type} path: {event.src_path}')
                else:
                    print('not .wav')
            else:
                print('not WAV sin Editar')
        except ValueError:
            print('not a file')

"""
on_any_event: if defined, will be executed for any event
on_created: Executed when a file or a directory is created
on_modified: Executed when a file is modified or a directory renamed
on_moved: Executed when a file or directory is moved
on_deleted: Executed when a file or directory is deleted.
"""

if __name__ == '__main__':

    abs_path = os.path.dirname(os.path.abspath(__file__))

    observer = Observer()
    event_handler = ExampleHandler() # create event handler

    observer.schedule(event_handler, path=abs_path, recursive=True)
    observer.start()   #recursive apply rules for all subfolders

    print("programme is running, try it by yourself with trial_folder")
    # sleep until keyboard interrupt, then stop + rejoin the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
