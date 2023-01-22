# Cyberpower UPS Shutdown

Welcome to Cyberpower UPS Shutdown, a tool to help users immediately shutdown their Cyberpower UPS and computer and give the option to shedule (or not) the restore time of the UPS. 
With this app, you can avoid the need to set fixed restore times for each day of the week and you can decide the restore time in the moment that you want to turn off the computer.
The app has a simple graphical user interface (GUI) made with PyQt and uses Selenium to automate the shutdown/restore process through the Powerpanel Business web interface.

## How to Use

To use Cyberpower UPS Shutdown, you'll need to have the **Cyberpower Powerpanel Business** software installed on your system. (Note: This app does not work with the personal version of Powerpanel.)

Before running the app, you'll need to create a `config.ini` file in the root folder with the following structure:

```
[DEFAULT]

HOME_URL = http://localhost:3052/local/
SHUTDOWNMENU_URL = http://localhost:3052/local/ups_setting/scheduled_shutdown
USERNAME = admin
PASSWORD = admin

DEFAULT_RESTORE_TIME = 11:00
```

Be sure to fill in the `USERNAME` and `PASSWORD` fields with the ones you've set in the Powerpanel Business app. The `DEFAULT_RESTORE_TIME` field is the default time that will show in the GUI and can be changed.

To run the app, simply execute the `mainGUI.py` file using Python. The GUI will allow you to specify the restore time if desired. 
- If you choose to set a restore time and fill in the required field, the app will schedule the shutdown for the current time + 1min and set the restore time as specified. 
- If you leave the field blank, the UPS and computer will simply shutdown without setting a restore time.

## Tech stack

- Python
- Selenium
- PyQt (for the GUI)

## Future Optimizations

- Improve stability
- Add error handling for cases where the Powerpanel Business web interface is not available or the login credentials are incorrect.
- Attempt to make it work with the headless version of the webdriver
- Add additional features to the GUI, such as a checkbox to decide if you want to set a restore time for the UPS or not.

## Note

Be sure to save any important work before running this app, as the shutdown process will begin immediately.

## Enjoy!

We hope this app makes it easier for you to schedule shutdowns for your Cyberpower UPS. Happy computing!
