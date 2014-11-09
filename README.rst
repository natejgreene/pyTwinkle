pyTwinkle
======================================

Python application for iTwinkle lights.  Currently supports only the 36 count strand.  The current iTwinkle mobile application only supports 3 strands of lights on the iPhone and iPad, the Android application only supports 1 strand at a time.  I currently have this installed on a Raspberry Pi and connect the iTwinkle mobile app to it.  I am now controlling 4 strands with my Android device.  At this time iOS will not work.

Requires pybluez.

Quick Start
------------
Rename your bluetooth device to begin with "00651"  It should be picked up by the Android app.

python main.py

Status
------
I have deciphered all of the commands for these lights and am working on:
HTTP server
Custom patterns

This is still a work in progress and PRs are welcome :)

