#!/usr/bin/env python3

import logging
import os
import subprocess
import sys
import time


def extract_output_from_completed_process(process):
    # Removes trailing new lines
    return process.stdout.decode('utf-8').rstrip()


def get_id_of(app_id):
    output = extract_output_from_completed_process(
        subprocess.run(["xdotool", "search", app_id], stdout=subprocess.PIPE))

    if not output:
        return None

    # NOTE: the output for hyper is incorrect if the window is on a different dektop.
    # The Value that should be last (which is therefor the correct ID for the window)
    # is on the first postion if hyper is on a differenct desktop

    id = output.split('\n')[-1]
    return id


def is_instance_already_open(app_id):
    return app_id != None


def move_and_raise_instance_of(app_id):
    desktop_number = extract_output_from_completed_process(
        subprocess.run(["xdotool", "get_desktop"], stdout=subprocess.PIPE))

    subprocess.run(
        ["xdotool", "set_desktop_for_window", app_id, desktop_number])

    time.sleep(0.1)

    subprocess.run(["xdotool", "windowactivate", "--sync", app_id])


def setup_logging():
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
    file_path = os.path.realpath("OpenExistingInstance.log")
    logging.basicConfig(
        filename=file_path, level=logging.DEBUG, format=logFormatter)
    logging.debug("---------------------------------------------")


if __name__ == "__main__":
    # setup_logging()

    app_id = get_id_of("whatsapp")
    if (is_instance_already_open(app_id)):
        move_and_raise_instance_of(app_id)

