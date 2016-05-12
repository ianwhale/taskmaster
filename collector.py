import os
import fnmatch
import filecmp

class Collector:
    def __init__(self):
        """
        Collector constructor.
        Initializes the collection process by verifying the Avida directory and getting the task_quality files.
        """
        self.avida_path = self.find_avida() ## String, absolute path of Avida directory.

        if self.avida_path == "":
            return

        self.task_qualities = self.collect_task_qualities() ## List, absolute paths of task_quality files.

        if not self.task_qualities:
            return

    def find_avida(self):
        """
        Finds Avida.
        Note that the Taskmaster directory should be in the same directory as the Avida directory.
        :return: string, the Avida absolute path.
        """

        dirname = ""
        for dir in os.listdir('..'):
            if fnmatch.fnmatch(dir, '*avida*'):
                dirname = dir
                print "Found Avida directory: ", dirname
                break

        if dirname == "":
            #TODO: Allow user to enter their own absolute file path here.

            print "Couldn't find Avida directory."
            print "Make sure the Taskmaster directory is in the same directory as Avida."
            print "Quiting..."
            return ""

        print "Avida absolute path: " + os.path.abspath("../" + dirname)
        return os.path.abspath("../" + dirname)

    def collect_task_qualities(self):
        """
        Collects all the task quality files from the data_out directory in Avida.
        :return: list, collection of task_quality absolute file paths.
        """
        data_out_path = self.avida_path + "/cbuild/data_out"

        if not os.path.exists(data_out_path):
            return []

        #
        # Loop through the contents of the data_out file.
        # We keep track of the first env-nav.cfg that we see.
        # If we encounter an env-nav that is different, that means there are two
        #   experiment results in the data_out directory and we should quit.
        #
        env = "" # The env-nav.cfg file used for comparison.
        dirs = [] # The directories we're looking for.
        for dir in os.listdir(data_out_path):
            dir = os.path.join(data_out_path + '/' + dir)

            if os.path.isdir(dir):
                #TODO: Allow user to choose which run they want if 2 or more env files conflict.

                temp_env = os.path.join(dir + '/env-nav.cfg')

                if env == "":
                    env = temp_env

                else:
                    if filecmp.cmp(env, temp_env):
                        # The two env-nav files that were found are identical.
                        # We can add the data_out directory to our collection.
                        dirs.append(dir)

                    else:
                        # The env-name files there were found are not identical.
                        # Inform the user and quit.

                        print"""

        Found two conflicting env-nav.cfg files:
        """ + env + """
        """ + temp_env + """
        You may have two separate run outputs in your data_out directory.
        Remove one of the run results to continue.
        """
                        return [] #Quit



        return []
