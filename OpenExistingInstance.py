#!/usr/bin/env python3
import subprocess
import logging


def is_instance_already_open(application):
    output = subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")

    logging.debug("is_instance_already_open:\n{0}".format(output))
    return application in output


def open_new_instance_of(application):
    return_code = subprocess.call(["hyper"])
    if return_code != 0:
        # TODO: handle error
        logging.error(
            "open_new_instance_of: Failed to open new instance of {0}! Error code: {1}".format(application, return_code))
    else:
        logging.debug(
            "open_new_instance_of: Opening new instance of {0}".format(application))


def focus_instance_of(application):
    # Moves the window to the current desktop, raises it und gives it focus
    subprocess.run(["wmctrl", "-R", application])
    logging.debug(
        "focus_instance_of: Putting {0} in focus".format(application))


def run():
    logging.basicConfig(filename="debug.log", level=logging.DEBUG)
    application = "furo@Ubuntu"
    # application = "Firefox"
    if (is_instance_already_open(application)):
        focus_instance_of(application)
    else:
        open_new_instance_of(application)


if __name__ == "__main__":
    run()
