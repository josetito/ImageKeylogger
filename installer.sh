#!/bin/bash

#start
echo Starting the installation of Keylogger

#update package
sudo apt-get update

#install necessary software
sudo apt-get -y install python-pip python-xlib python-pil python-gtk2 python-tk git
sudo pip install validate

#finish
echo Installation completed