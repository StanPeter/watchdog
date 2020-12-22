Information:


    Programme uses watchdog library which observe the changes (here only CREATE changes) within the parent folder  of .py location + all its 
    subfolders and was created to help with a creation of an audiobook(each part of audio would go to its own specific folder and 
    nowhere else + no more than once --> then it would launch automatically .sh file to clean up all the background noises)

    Programme detects adding .wav files only to 'WAV sin Editar' folder,
    works for all subfolders, after adding a .wav to 'WAV sin Editar' runs .sh script which prints 'hello world'

    After executing all the instructions try to add .wav files into WAV sin Editar folder vs somewhere else (or try to add different types of files)


Instructions: (works for UNIX, check out yourself commands for windows)


    1. Create a new environment                                 "  python -m venv venv  " 

    2. Activate it                                              "  source venv/bin/activate  "

    3. install required libraries by executing                  "  pip install -r requirements.txt  "

    4. to give the sh file permission rights                    "  chmod u+x tharpa-robot-audio-cleanner-002.sh  " 

    5. launch project.py


PS: keep .py file and .sh file in the "projects" directory 

    To quit the programm press   CONTROL+C

