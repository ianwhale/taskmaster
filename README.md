# taskmaster
A tool for gathering and parsing tasks_quality files in Avida.

Before running, ensure that you have only one expierement in your Avida destination directory. You will get unexpected results otherwise.

Else, simply navigate to the taskmaster directory and execute `python ./taskmaster.py`. 
You will then be prompted to enter the absolute path to your Avida destination directory (some file in cbuild).

Taskmaster will then build a dictionary of your task_quality files.
