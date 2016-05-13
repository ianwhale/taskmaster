import os
import fnmatch
import filecmp

class Collector:
    def __init__(self, runspath):
        """
        Collector constructor.
        Initializes the collection process by verifying the Avida directory and getting the task_quality files.
        """
        self.runspath = runspath

        ### Dictionary
        self.task_qualities = self.collect_task_qualities()

        if not self.task_qualities:
            return

    def collect_task_qualities(self):
        """
        Collects all the task quality files from the data_out directory in Avida.
        :return: list, collection of task_quality absolute file paths.
        """
        dirs = {}

        for dir in os.listdir(self.runspath):
            dir = os.path.join(self.runspath, dir)
            if os.path.isdir(dir):
                dirs[dir] = os.path.join(dir, "/data/tasks_quality.dat")

        print str(len(dirs)) + " output directories have been found."

        return {}
