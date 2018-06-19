#!/usr/bin/env python3
import subprocess


def is_instance_already_open(application):
    print("Checking if isntance of " + application + " is open...")
    output = subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    return application in output


def open_new_instance_of(application):
    # Open a new instance of given application
    # Focus new instance
    print("Open new instance of " + application)
    subprocess.call(["hyper"])


def focus_instance_of(application):
    # Moves the window to the current desktop, raises it und gives it focus
    print("Put " + application + " in focus...")
    subprocess.run(["wmctrl", "-R", application])


def run():
    application = "furo@Ubuntu"
    if (is_instance_already_open(application)):
        focus_instance_of(application)
    else:
        open_new_instance_of(application)


if __name__ == "__main__":
    run()
