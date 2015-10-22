pyTwinkle
======================================

Python application for iTwinkle lights.  Currently supports only the 36 count strand.  The current iTwinkle mobile application only supports 3 strands of lights on the iPhone and iPad, the Android application only supports 1 strand at a time.  I currently have this installed on a Raspberry Pi and connect the iTwinkle mobile app to it.  I am now controlling 4 strands with my Android device.  At this time iOS will not work.

Requires pybluez.

Quick Start
------------
Rename your bluetooth device to begin with "00651"  It should be picked up by the Android app.

python main.py

Protocol
--------

Single Light	0xFF	0x06	LL	DD	BB	GG	RR	??	??	??	FF
Whole Strand	0xFF	0x28	DD	BB	GG	RR	??	??	??	??	FF
Whole Strand Saved	0xFF	0x15	DD	BB	GG	RR	??	??	??	??	FF
Red/White	0xFF	0x1A	??	??	??	??	??	??	??	??	FF

Frames are started with 0xFF and end with 0xFF
And Hex values for the following:
LL = Light Id 
DD = Brightness
BB = Blue
GG = Green
RR = Red
?? = Unknown

Status
------

This is still a work in progress and PRs are welcome :) :)

