import sys
sys.dont_write_bytecode = True

import collector

def main():
    print """

    Welcome to Taskmaster.

    """

    env_name = raw_input("Enter the absolute path of your Avida destination path: ")

    collect = collector.Collector(env_name)

    return

main()