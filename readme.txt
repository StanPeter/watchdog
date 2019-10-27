DESCRIPTION 


Programme uses watchdog library which observe the changes (here only CREATE changes) within the parent folder  of .py location + all its subfolders and was created to help with a creation of an audiobook(each part of audio would go to its own specific folder and nowhere else + no more than once --> then it would launch automatically .sh file to clean up all the background noises)


Programme detects adding .wav files only to 'WAV sin Editar' folder,
works for all subfolders, after adding a .wav to 'WAV sin Editar' runs .sh script which prints 'hello world'


Feel free to use this script as you wish!



INSTRUCTION MANUAL


1. keep .py file and .sh file in the "projects" directory 
2. open your terminal and navigate to the "projects" directory
3. install all required packages by executing    "  pip install -r requirements.txt   "  (PS: recommend create a new env first)
4. execute command   "    chmod u+x tharpa-robot-audio-cleanner-002.sh    " to give the sh file permission rights
5. run " project.py" file with command          "   python project.py    "


And that's it!

To quit the programm press   CONTROL+C






