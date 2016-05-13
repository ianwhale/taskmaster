import sys
sys.dont_write_bytecode = True

import collector

def main():
    print """

    Welcome to Taskmaster.

    """

    env_name = raw_input("Please enter the absolute path of your Avida destination directory: ")

    collect = collector.Collector(env_name)

    ## All our tasks_quality files are in a single directory.
    print collect.get_out_path()

    return

main()