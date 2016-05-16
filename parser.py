import os
from math import ceil

class Parser:
    def __init__(self, out_dir):
        """
        Parser constructor.
        Initializes the parsing process and calls methods.
        :param out_dir: The out directory where the tasks_quality files are collected.
        """
        self.parsed = {} ## Parsed data, filled in parse_tasks_qualities
        self.out_dir = out_dir
        self.parse_tasks_qualities()
        self.obtain_information()

    def parse_tasks_qualities(self):
        """
        Compiles all the final results into a dictionary with the following indexing:
            filename => final result
        """
        results = {}

        for dir in os.listdir(self.out_dir):
            with open(os.path.join(self.out_dir, dir)) as f:
                last = None

                ## This loops to the last line of the file.
                for last in (line for line in f if line.rstrip('\n')):
                    pass

                last = last.split()
                last.pop(0) ## We don't want the first element of the last line.

                for i in range(len(last)):
                    last[i] = float(last[i]) ## Convert strings to floats.

                results[dir] = last

        self.parsed = results

    def obtain_information(self):
        """
        Retrieves the information needed from the tasks_quality files. This includes:
            1. The maximum task quality for each grid.
            2. The average task quality of the dominant task qualities for each run.
        This information will be output to a text file called taskmaster_out.
        """
        out = "" ## The text output

        grids = len(list(self.parsed.values()[0]))## Gets the number of grids in the experiment

        print "Found " + str(grids / 2) + " grids..."

        ## Output some Avida style file information.
        out += "# Data column information: \n"

        i = 0
        for i in range(grids/2):
            out += "# " + str(i + 1) + ": State Grid " + str(i + 1) + " Max Task Quality\n"
        out += "# " + str(i + 2) + ": Average For Single Run\n\n"

        max_quality = 0
        all_qualities = {} ## Keep track of all qualities.
        where_max = "" ## Retains which TQ file has the maximum fitness.
        grid_max = 0 ## Retains which grid had the max fitness.


        ## We want to go through in order of output by Avida.
        ## So we sort based on the number in our output files name.
        keys = self.parsed.keys()
        keys.sort(key = lambda x: [int(s) for s in x.split("_") if s.isdigit()][0])

        for key in keys:
            qualities = self.parsed[key]
            count = 0

            ## out += key + ": "
            for i in range(0, grids, 2): ## step by twos, then add one for odd values
                if qualities[i + 1] > max_quality:
                    max_quality = qualities[i + 1]
                    where_max = key
                    grid_max = int(ceil(i / 2)) + 1

                out += str(qualities[i + 1]) + " "
                count += qualities[i + 1]

            out += str(count / (grids / 2)) + "\n" ## Average


        out += "\n"
        out += "# Max task quality: " + str(max_quality) + "\n"
        out += "# Found in: " + str(where_max) + " on grid number " + str(grid_max) + "\n"
        target = open("./" + self.out_dir + "/taskmaster_out", "w")
        target.truncate()
        target.write(out)
        target.close()

        print "Results successfully output to ./" + self.out_dir + "/taskmaster_out"

