#!/usr/bin/env python3
import subprocess
import logging
import sys


def get_running_applications():
    return subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")


def get_id_of_latest_instance_of(application):
    running_applications = get_running_applications().split("\n")
    for line in reversed(running_applications):
        if application in line:
            return line.split(" ")[0]
    return -1


def is_instance_already_open(application):
    running_applications = get_running_applications()

    logging.debug("is_instance_already_open:\n{0}".format(
        running_applications))
    return application in running_applications


def open_new_instance_of(application):
    return_code = subprocess.call([application])
    if return_code != 0:
        # TODO: handle error
        logging.error(
            "open_new_instance_of: Failed to open new instance of {0}! Error code: {1}".format(application, return_code))
    else:
        logging.debug(
            "open_new_instance_of: Opening new instance of {0}".format(application))


def focus_instance_of(application):
    # Moves the window to the current desktop, raises it und gives it focus
    app_id = get_id_of_latest_instance_of(application)
    if (app_id < 0):
        # TODO: Handle Error!
        logging.error("")
    else:
        subprocess.run(["wmctrl", "-i", "-R", app_id])
        logging.debug(
            "focus_instance_of: Putting {0} with ID = {1} in focus".format(application, app_id))


if __name__ == "__main__":
    # TODO: create log file relative to script path instead of home directory
    logging.basicConfig(
        filename="OpenExistingInstance.debug", level=logging.DEBUG)

    # application = sys.argv[1]
    # new_application = sys.argv[2] if len(sys.argv) > 1 else application
    application = "furo@Ubuntu"
    new_application = "hyper"

    if (is_instance_already_open(application)):
        focus_instance_of(application)
    else:
        open_new_instance_of(new_application)
