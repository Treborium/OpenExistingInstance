#!/usr/bin/env python3
import subprocess
import logging
import sys
import os


def get_running_instances():
    return subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8").lower()


def get_id_from_latest_instance_of(application):
    running_applications = get_running_instances().split("\n")
    for line in reversed(running_applications):
        if application in line:
            return line.split(" ")[0]


def is_instance_already_open(application):
    running_applications = get_running_instances()

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
    app_id = get_id_from_latest_instance_of(application)
    if app_id == None:
        # TODO: return meaningfull error message
        raise AttributeError("No app found")
    # Moves the window to the current desktop, raises it und gives it focus
    subprocess.run(["wmctrl", "-i", "-R", app_id])
    logging.debug(
        "focus_instance_of: Putting {0} with ID = {1} in focus".format(application, app_id))


def setup_logging():
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
    file_path = os.getcwd() + "/OpenExistingInstance.log"
    logging.basicConfig(
        filename=file_path, level=logging.DEBUG, format=logFormatter)
    logging.debug("---------------------------------------------")


if __name__ == "__main__":
    setup_logging()

    application = sys.argv[1].lower()
    new_application = sys.argv[2].lower() if len(sys.argv) > 1 else application

    logging.debug("Command Line Arguments: {0} {1}".format(
        sys.argv[1], sys.argv[2]))
    logging.debug("application = {0} new_application = {1}".format(
        application, new_application))

    if (is_instance_already_open(application)):
        focus_instance_of(application)
    else:
        open_new_instance_of(new_application)
