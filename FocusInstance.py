#!/usr/bin/env python3

import logging
import os
import subprocess
import sys


def extract_output_from_completed_process(process):
    return process.stdout.decode('utf-8')


def get_id_of(app):
    output = extract_output_from_completed_process(
        subprocess.run(["xdotool", "search", app], stdout=subprocess.PIPE))

    if not output:
        return None
    # return second last element because the last one is an empty string
    return output.split('\n')[-2]


def is_instance_already_open(app):
    return get_id_of(app) != None


def move_and_raise_instance_of(app):
    desktop_number = extract_output_from_completed_process(
        subprocess.run(["xdotool", "get_desktop"], stdout=subprocess.PIPE))
    subprocess.run(["xdotool", "set_desktop_for_window", app, desktop_number])


def setup_logging():
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
    file_path = os.path.realpath("OpenExistingInstance.log")
    logging.basicConfig(
        filename=file_path, level=logging.DEBUG, format=logFormatter)
    logging.debug("---------------------------------------------")


if __name__ == "__main__":
    # setup_logging()

    print(is_instance_already_open("gedit"))
