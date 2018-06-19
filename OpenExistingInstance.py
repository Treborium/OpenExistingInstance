#! /usr/bin/python3
import subprocess


def is_instance_already_open(application):
    output = subprocess.run(
        # list all running windows
        ["wmctrl", "-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    return application in output


def open_new_instance_of(application):
    # Open a new instance of given application
    # Focus new instance
    subprocess.run([application])


def focus_instance_of(application):
    # Moves the window to the current desktop, raises it und gives it focus
    subprocess.call(application)


application = "Hyper"
if (is_instance_already_open(application)):
    focus_instance_of(application)
else:
    open_new_instance_of(application)
