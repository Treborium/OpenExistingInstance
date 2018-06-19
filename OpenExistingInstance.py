#!/usr/bin/env python3
import subprocess


def is_instance_already_open(application):
    output = subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    return application in output


def open_new_instance_of(application):
    print("Open new instance of " + application)
    return_code = subprocess.call(["hyper"])
    if return_code != 0:
        # TODO: handle error
        print("Error")


def focus_instance_of(application):
    # Moves the window to the current desktop, raises it und gives it focus
    print("Put " + application + " in focus...")
    subprocess.run(["wmctrl", "-R", application])



def run():
    application= "furo@Ubuntu"
    # application = "Firefox"
    if (is_instance_already_open(application)):
        focus_instance_of(application)
    else:
        open_new_instance_of(application)

if __name__ == "__main__":
    run()
