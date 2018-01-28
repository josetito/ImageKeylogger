#!/bin/bash
#jrarguedas 

#colors of the letters
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`

#start instalation
echo ${GREEN} Starting the installation of Keylogger ${RESET}

#update package and solve dependencies
sudo apt-get update
sudo apt-get install -f
sudo apt-get update

#INSTALL NECESARY SOFTWARE

#Install python-pip
echo installing python-pip
sudo apt-get -y install python-pip 
problem1=$(dpkg -s python-pip|grep installed)
echo  ${GREEN} Checking for python-pip: $problem1 ${RESET}

#install python-xlib
echo installing python-xlib
sudo apt-get -y install python-xlib
problem2=$(dpkg -s python-xlib|grep installed)
echo  ${GREEN} Checking for python-xlib: $problem2 ${RESET}

#install python-pil
echo installing python-pil
sudo apt-get -y install python-pil
problem3=$(dpkg -s python-pil|grep installed)
echo  ${GREEN} Checking for python-pil: $problem3 ${RESET}

#install python-gtk2
echo installing python-gtk2
sudo apt-get -y install python-gtk2
problem4=$(dpkg -s python-gtk2|grep installed)
echo  ${GREEN} Checking for python-gtk2: $problem4 ${RESET}

#install python-tk
echo installing python-tk
sudo apt-get -y install python-tk
problem5=$(dpkg -s python-tk|grep installed)
echo  ${GREEN} Checking for python-tk: $problem5 ${RESET}

#install git
echo installing git
sudo apt-get -y install git
problem6=$(dpkg -s git|grep installed)
echo  ${GREEN} Checking for git: $problem6 ${RESET}

# Update pip
sudo pip install --upgrade pip

#install validate
echo installing validate
sudo pip install validate
problem7=$(pip freeze | grep validate)
echo $problem7
 
echo ""
echo ""
echo " **** VERIFYING INSTALLATION **** "

echo ${GREEN} python-pip: $problem1 ${RESET}
if [ "" == "$problem1" ]; then
	echo ${RED} Instalation failed ${RESET}
	echo -e "${RED} There were problems when trying to install python-pip ${RESET}"
	echo " I could try with: sudo apt-get --force-yes --yes install python-pip"
fi

echo ${GREEN} python-xlib: $problem2 ${RESET}
if [ "" == "$problem2" ]; then
	echo ${RED} Instalation failed ${RESET}
	echo -e "${RED} There were problems when trying to install python-xlib ${RESET}"
	echo " I could try with: sudo apt-get --force-yes --yes install python-xlib"
fi

echo ${GREEN} python-pil: $problem3 ${RESET}
if [ "" == "$problem3" ]; then
	echo ${RED} Instalation failed ${RESET}
	echo -e "${RED} There were problems when trying to install python-pil ${RESET}"
	echo " I could try with: sudo apt-get --force-yes --yes install python-pil"
fi

echo ${GREEN} python-gtk2: $problem4 ${RESET}
if [ "" == "$problem4" ]; then
	echo ${RED} Instalation failed ${RESET}
	echo -e "${RED} There were problems when trying to install python-gtk2 ${RESET}"
	echo " I could try with: sudo apt-get --force-yes --yes install python-gtk2"
fi

echo ${GREEN} python-tk: $problem5 ${RESET}
if [ "" == "$problem5" ]; then
	echo ${RED} Instalation failed ${RESET}
	echo -e "${RED} There were problems when trying to install python-tk ${RESET}"
	echo " I could try with: sudo apt-get --force-yes --yes install python-tk"
fi

echo ${GREEN} git: $problem6 ${RESET}
if [ "" == "$problem6" ]; then
	echo ${RED} Instalation failed ${RESET}
	echo -e "${RED} There were problems when trying to install git ${RESET}"
	echo " I could try with: sudo apt-get --force-yes --yes install git"
fi
echo ""

# OPCIONAL
#Download Repository
echo Download Repository.....................
git clone https://github.com/roxana-lafuente/ResearchLogger.git

#by
#      _                               __       
#     (_)______ ________ ___ _____ ___/ /__ ____
#    / / __/ _ `/ __/ _ `/ // / -_) _  / _ `(_-<
# __/ /_/  \_,_/_/  \_, /\_,_/\__/\_,_/\_,_/___/
#|___/             /___/                        