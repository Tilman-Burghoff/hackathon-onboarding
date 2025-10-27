# Starting the pandas
To start the pandas, switch them on at the control boxes below the table.
Connect to the Panda L and, if you use both Pandas, also to the Panda R network.
open chromium and open 172.16.0.2 for panda l and 172.17.0.2 for panda r (those are also bookmarked).
If you need to log in, use user admin and pw ***
Unlock the robots in the joints section. Now they can be controlled with botop if the light is blue.
If the light is white they are in user mode. Switch to control mode by untwisting the E-stops (see next section).

# E-stops
The two grey buttons on the table labeled L and R are E-Stops for the pandas.
Those will stop their respective robot and them into user-mode (white light) where no commands can be send.
Do not hesitate to push them if something seems wrong. To return control to BotOp untwist the E-stop.
If libfranka tells you "command not possible in the current mode!" even though you are in control mode,
it sometimes helps to press and untwist the e-stops.
The red E-stop instantly cuts power to both pandas. Use this one only for worst case scenarios.

# shutting down
When finished, lock the pandas in the control interface and then shut them down bz using the context menu at the top.
When they have finished shutting down switch off the control boxes.
