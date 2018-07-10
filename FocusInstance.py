#!/usr/bin/env python3

import logging
import os
import subprocess
import sys


def is_instance_already_open(app):
    return subprocess.run(["xdotool", "search", "--sync", app], stdout=subprocess.PIPE).stdout.decode('utf-8')


def setup_logging():
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
    file_path = os.path.realpath("OpenExistingInstance.log")
    logging.basicConfig(
        filename=file_path, level=logging.DEBUG, format=logFormatter)
    logging.debug("---------------------------------------------")


if __name__ == "__main__":
    # setup_logging()
    print(is_instance_already_open("gedit"))
