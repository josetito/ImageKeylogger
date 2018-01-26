# Bitácora

## Proyecto procesamiento de imágenes para extracción de texto 


# Dia 1: Miercoles 24 de enero

Hoy tuvimos la primera reunion con Paula y nos dio una introduccion general a los tres proyectos.

#### cosas por hacer:
- Instalar, probar y familiarizarse con el keylogger 
- Leer el trabajo de roxana (funcionamiento de keylogger) capitulo 4.
- Primer aporte generar una instalación más transparente.

#### que voy hacer hoy:
- Configurar mi nueva computadora.
- Descargar pycharm.
- Clonar repositorio de Roxana.
- Tratar de instalar el keylogger.
- Familiarizarme con el keylogger.

### Informe de Trabajo 
* Se instalo ubuntu en la máquina que me presto Paula para desarollar el proyecto, además configure las llaves ssh para posteriormente trabajar con git.
* Se descargo y se instalo el IDE PYCHARM ya que al ser un proyecto a desarrollar en python, esta herramienta me va ayudar a desarrollar más rápido mi código.
    * Lo descargue del siguiente link: https://www.jetbrains.com/pycharm/
* Clone el proyecto de Roxana del link: https://github.com/roxana-lafuente/ResearchLogger.git
* Crear el ambiente virtual de trabajo con los siguientes pasos:

El primer paso es definir un ambiente de trabajo basado en virtualenv:

sudo -H pip install virtualenv
sudo -H pip install virtualenvwrapper
Agregar las siguientes líneas al final del archivo ~/.bashrc:

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/dev
source /usr/local/bin/virtualenvwrapper.sh
Y refrescar la sesión del shell.

source ~/.bashrc
Para crear el ambiente virtual:

cd Documents/ImageKeylogger
mkvirtualenv venvImageKeylogger 

(Para salir del ambiente utilizar deactivate RutasTransitWand y para volver a entrar workon RutasTransitWand)

Generar archivo de requirements.txt:

pip freeze > requirements.txt  

### Dia 2: Jueves 25 de enero

* Instalacion de Keylogger
    * validate [sudo pip install validate]
    * Xlib [sudo apt-get install python-xlib]
    * Python Image Library (PIL) [sudo apt-get install python-pil]
    * gtk [sudo apt-get install python-gtk2]
    * Tkinter [sudo apt-get install python-tk]

*  Instalación más fácil para Linux, cree un scrip para que la instalación en linux sea mucho más fácil y sencilla para los usuarios.
```

#!/bin/bash

echo Starting the installation of Keylogger

sudo apt-get update

sudo apt-get install validate python-xlib python-pil python-gtk2 python-tk

echo Installation completed
```

* Probar el script. Para probar el script voy hacer una máquina virtual con ubuntu 14.04 para verificar que el script sirva desde esa versión hasta la más reciente.
    * Descargar virtual box: wget http://download.virtualbox.org/virtualbox/5.1.16/virtualbox-5.1_5.1.16-113841~Ubuntu~yakkety_amd64.deb
    * Luego instalar el paquete: sudo dpkg -i virtualbox-5.1_5.1.16-113841~Ubuntu~yakkety_amd64.deb
    * Descargar ubuntu 16.04: https://www.ubuntu.com/download/desktop
    
* Empezar hacer pruebas de correr el programa ResearchLoggerInterface.py y ResearchLogger.py 
    * Tengo problemas a la hora de terminar el programa con Ctrl izq + Ctrl der + F12
    
* Hice una máquina para probar que el instalador de Linux sirve perfectamente en versiones mayores a 14.04.
    * Baje el instalador el la máquina de test.
    * Clone el proyecto en la máquina test.
    *  


