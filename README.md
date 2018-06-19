# OpenExistingInstance
This little python script moves a given application in focus. If no instance of the application is currently running a new one will be launched.

## Usage
simply call the script file from your terminal or via a keyboard shortcut with the application you want to focus as the 1st argument and the application you want to launch as the 2nd argument. If no 2nd argument is provided it will use the first as the launch application. 

### Example
`./OpenExistingInstance.py "Firefox" "Chrome"`

Here we try to focus Firefox, if no instance of Firefox is currently running we'll launch Chrome.

