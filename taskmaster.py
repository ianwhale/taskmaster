import sys
sys.dont_write_bytecode = True

import collector
import parser

def main():
    print """

    Welcome to Taskmaster.

    """

    env_name = raw_input("Please enter the absolute path of your Avida destination directory: ")

    collect = collector.Collector(env_name)

    ## All our tasks_quality files are in a single directory.
    print "Tasks_quality files copied to " + collect.out_path + " now parsing..."

    parse = parser.Parser(collect.out_path)

    return

main()