# Bitácora

## Proyecto procesamiento de imágenes para extracción de texto 


### Fecha: Miercoles 24 de enero

Hoy tuvimos la primera reunion con Paula y nos dio una introduccion general a los tres proyectos.

#### Cosas por hacer:
- Instalar, probar y familiarizarse con el keylogger 
- Leer el trabajo de roxana (funcionamiento de keylogger) capitulo 4.
- Primer aporte generar una instalación más transparente.

#### Que voy hacer hoy:
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

```
sudo -H pip install virtualenv
sudo -H pip install virtualenvwrapper
```

Agregar las siguientes líneas al final del archivo ~/.bashrc:
```
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/dev
source /usr/local/bin/virtualenvwrapper.sh
Y refrescar la sesión del shell.
source ~/.bashrc
```

Para crear el ambiente virtual:
```
cd Documents/ImageKeylogger
mkvirtualenv venvImageKeylogger 
```

(Para salir del ambiente utilizar deactivate #nombreEnv
 y para volver a entrar workon #nombreEnv)

Generar archivo de requirements.txt:
```
pip freeze > requirements.txt
```

### Fecha: Jueves 25 de enero

* Instalacion de Keylogger
    * Validate [sudo pip install validate]
    * Xlib [sudo apt-get install python-xlib]
    * Python Image Library (PIL) [sudo apt-get install python-pil]
    * gtk [sudo apt-get install python-gtk2]
    * Tkinter [sudo apt-get install python-tk]

*  Instalación más fácil para Linux, cree un scrip para que la instalación en linux sea mucho más fácil y sencilla para los usuarios.
```
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
```

* Probar el script. Para probar el script voy hacer una máquina virtual con ubuntu 14.04 para verificar que el script sirva desde esa versión hasta la más reciente.
    * Descargar virtual box: wget http://download.virtualbox.org/virtualbox/5.1.16/virtualbox-5.1_5.1.16-113841~Ubuntu~yakkety_amd64.deb
    * Luego instalar el paquete: sudo dpkg -i virtualbox-5.1_5.1.16-113841~Ubuntu~yakkety_amd64.deb
    * Descargar ubuntu 16.04: https://www.ubuntu.com/download/desktop
    
    
### Fecha: Viernes 26 de enero

#### Pruebas

* Empezar hacer pruebas de correr el programa ResearchLoggerInterface.py y ResearchLogger.py 
    * Tengo problemas a la hora de terminar el programa con Ctrl izq + Ctrl der + F12
    * Estoy analizando el archivo onclickimagecapture.py ya que es acá donde se toman las capturas de pantalla que más adelante voy a necesitar.
    
* Intenté hacer una máquina de virtual box en mi computadora pero no me sirvió debido a que no permite la virtualización.
    
* Hice una máquina para probar que el instalador de Linux sirve perfectamente en versiones mayores a 14.04.
    * Baje el instalador el la máquina de test.
    * Clone el proyecto en la máquina test.
    * El instalador funciona correctamente.
    
* Actualice la bitacora.

### Fecha: Domingo 28 de enero

#### Nuevas sugerencias
* Arreglar script para que valide si fue instalado o no.
* Arreglar dependencias
* Que descargue el repositorio de ResearchLogger

- Investigar como se puede atraves de bash poder validar que un paquete este o no instalado en la computadora. 
    * Encontre que con la funcionalidad de "dpkg" se podria realizar una consulta al sistema y saber si este estaba o no instalado.
    * Para solucionar el problema de dependencias lo que hago es tratar de arreglar el sistema en caso de que ya tuviera errores con las dependencias y luego aplicó una actualización de paquetes para que no ocurra ningun error a la hora de instalar.
- Investigar si se podria validar un paquete instalado por pip
    * No encontre la forma intente con $(pip freeze | grep validate) pero en mi computadora aparece como si no estuviera dentro de los paquetes instalados pero si lo tiene.
    * Para minimizar el problema de arriba lo que hice fue ya que como utilizo "pip" para instalar el paquete "validate" lo que hago es actualizar pip para que no haya ningun error cuando instale el nuevo paquete.
- Mostar una salida donde quede más claro que fue lo que occurio.
    * Necesitaba colocar salidas de warning o de su correcto funcinamiento por lo que la salida se imprime de color rojo cuando es un warning y verde cuando su funcionamiento es correcto.


### Fecha: Lunes 29 de enero

