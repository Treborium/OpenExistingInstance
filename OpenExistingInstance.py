#!/usr/bin/env python3
import subprocess
import logging
import sys


def get_running_instances_of(application):
    return subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")


def get_id_from_latest_instance_of(application):
    running_applications = get_running_instances_of(application).split("\n")
    for line in reversed(running_applications):
        if application.lower() in line.lower():
            return line.split(" ")[0]


def is_instance_already_open(application):
    running_applications = get_running_instances_of(application)

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
    # Moves the window to the current desktop, raises it und gives it focus
    subprocess.run(["wmctrl", "-i", "-R", app_id])
    logging.debug(
        "focus_instance_of: Putting {0} with ID = {1} in focus".format(application, app_id))


def setup_logging():
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        filename="OpenExistingInstance.log", level=logging.DEBUG, format=logFormatter)


if __name__ == "__main__":
    application = sys.argv[1]
    new_application = sys.argv[2] if len(sys.argv) > 1 else application

    if (is_instance_already_open(application)):
        focus_instance_of(application)
    else:
        open_new_instance_of(new_application)
