import os
import fnmatch

class Collector:
    def __init__(self):
        """
        Collector constructor.
        Initializes the collection process by verifying the Avida directory and getting the task_quality files.
        """
        self.findAvida()

    def findAvida(self):
        """
        Finds Avida.
        Note that the Taskmaster directory should be in the same directory as the Avida directory.
        :return:
        """

        dirname = ""
        for dir in os.listdir('..'):
            if fnmatch.fnmatch(dir, '*avida*'):
                dirname = dir
                print "Found Avida directory: ", dirname
                break

        if dirname == "":
            print("Couldn't find Avida directory.")
            print("Make sure the Taskmaster directory is in the same directory as Avida.")
            print("Quiting...")

        abspath = os.path.abspath(dirname)
