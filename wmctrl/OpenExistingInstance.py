#!/usr/bin/env python3
""" Open Existing Instance

"""

# TODO: Write script doc string

import subprocess
import logging
import sys
import os


def get_running_instances() -> str:
    """
    Returns a lower case string of instances for all currently running programs
    The string is divided by new lines ("\\n").

    Returns:
        str: a new line delimited string of all running instances
    """
    return subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE) \
        .stdout \
        .decode("utf-8").lower()


def get_id_from_latest_instance_of(application: str) -> int:
    """
    Returns the ID of the most recently opened instance of an app.

    This function assumes that there is at least one instance of
    the app running.

    Parameters:
        application (str): Applications name to search the latest instance of

    Returns:
        int: The ID of the instance of the specified app
    """
    running_applications = get_running_instances().split("\n")
    for line in reversed(running_applications):
        if application in line:
            return line.split(" ")[0]


def is_instance_already_open(application: str) -> bool:
    """
    Check wether a instance of an application is already running.

    Parameters:
     application (str): The application to be checked

    Returns:
        bool: True if there is a instance of the app running, otherwise false
    """
    running_applications = get_running_instances()

    logging.debug("is_instance_already_open:\n{0}".format(
        running_applications))
    return application in running_applications


def open_new_instance_of(application: str) -> None:
    """
    Open a new instance of an application.

    Parameters:
        application (str): The application to be started
    """
    return_code = subprocess.call([application])
    if return_code != 0:
        # TODO: handle error
        logging.error(
            """
            open_new_instance_of: Failed to open new instance of {0}
            Error code: {1}
             """
            .format(application, return_code)
        )
    else:
        logging.debug(
            "open_new_instance_of: Opening new instance of {0}"
            .format(application)
        )


def focus_instance_of(application: str) -> None:
    """
    Focus the latest instance of a running application.

    Parameters:
        application (str): The application to focus
    """
    app_id = get_id_from_latest_instance_of(application)
    if app_id is None:
        # TODO: return meaningfull error message
        raise AttributeError("No app found")
    # Move the window to the current desktop, raise it und give it focus
    subprocess.run(["wmctrl", "-i", "-R", app_id])
    logging.debug(
        "focus_instance_of: Putting {0} with ID = {1} in focus"
        .format(application, app_id)
    )


def setup_logging() -> None:
    """
    Set default properties for logging to a file.

    The default properties include the time, logging level (DEBUG)
    and the log message. The filename is "OpenExistingInstance.log".
    """
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
    file_path = os.path.realpath("OpenExistingInstance.log")
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
