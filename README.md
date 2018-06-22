# OpenExistingInstance
This little python script moves a given application in focus. If no instance of the application is currently running a new one will be launched.

## Usage
Simply call the script file from your terminal or via a keyboard shortcut with the application you want to focus as the 1st argument and the application you want to launch as the 2nd argument. If no 2nd argument is provided it will use the first as the launch application. 

### Requirements
In order to use this script you need to have a window manager that is supported by the wmctrl module

### Getting Started
From a Terminal:
`./OpenExistingInstance.py "Firefox" "Chrome"`

Via a Keyboardshortcut in Gnome:
`python3 ./OpenExistingInstance.py "Firefox "Chrome"`

Here we try to focus Firefox, if no instance of Firefox is currently running we'll launch Chrome.

