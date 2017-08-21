#!/bin/bash
# This script will set up a RAM drive in the current user's name
# in order to reduce wear on the SD card.

# create a directory to serve as the RAM drive
mkdir /home/$USER/ram

# the python script creates an entry in fstab that
# identifies the RAM drive on boot (you may have to
# modify this to be an absolute path in your system)
/usr/bin/python3 ./tmpfs_modify.py
