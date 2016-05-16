# taskmaster
A tool for gathering and parsing tasks_quality files in Avida.

Before running, ensure that you have only one experiment in your Avida destination directory. You will get unexpected results otherwise.

Else, simply navigate to the taskmaster directory and execute `python ./taskmaster.py`. 
You will then be prompted to enter the absolute path to your Avida destination directory (some file in cbuild).

Task master will then copy your tasks_quality files to whatever directory `taskmaster.py` is in.
Inside this file (called `taskmaster_out`) there will be the only the dominant task qualities as well as an average.
At the end of the file, you will find the top task quality and which grid it occurred in.