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
* Se asigno la lectura "Keylogger para el estudio de los procesos cognitivos del traductor"
    * Lei del libro los primeros dos cápitulos y los anexos técnicos.

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

* Tarea de iniciar con la herramienta Tesseract
    utilice los siguientes links para iniciar
    - https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
    - https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/
    - https://www.pyimagesearch.com/wp-content/uploads/2014/02/ImageSearchEngineResourceGuide.pdf
* Instalar tesseract
    Primero instale los paquetes
    ``` 
        pip install pillow
        pip install pytesseract
        pip install cv2
        pip install opencv-python
    ```
    Tuve problemas lo solucione con crear un ambiente virtual, lo que pasaba era que pillow tenia una doble referencia por lo que se necesita hacer el ambiente virtual y que lo unico que este dentro de este ambiente sea este paquete.
    ```
            
        pip install pillow
        pip install pytesseract
        pip install cv2
        pip install opencv-python
    ```

* Pruebas con la herramienta tesseract-ocr
    - Primero inicie con la imagen de prueba con letras grandes y la herramienta trabaja muy bien, el resultado fue excelente.
    - Luego utilice una imagen “salt and pepper” osea que tenga ruido en el fondo de la imagen, esto con el fin de ver si se tiene el mismo resultado.
    - La siguiente imagen era un codigo el cual tenia letras de colores y a la hora de aplicar la herramienta esta borra las palabras de color.
    - Hice pruebas con las imagenes de los LOGS del ResearchLogger al pasarlo por la herramienta el resultado no es para nada bueno, fue donde note que existe una necesidad de una buena resolución.

* Mejorar Resolucion
    * Para observar la resolucion de la imagenes en el servidor utilice:
    ```
    identify -ping image.png 
    ```
    * Resolucion 150*150, este tipo de imagen carece de informacion en la resolución, al probar este tipo de imagen con la herramienta se pierde información al extraer el texto dando como resultado erroneo. 

    * Resolucion 350*350

    * Resolución 500*250,


Nota:
Pienso que no del todo es responsabilidad de la resoluccion tambien la herramienta tiene dificultades al ser imagenes con colores. Para que el resultado sea bueno deberia de tener fondo blanco y letras negras.


### Fecha: Martes 30 de enero

1. hice el archivo ocr.py
    * Este archivo lo que hace es procesar un archivo con la herramienta tesseract
    * Tiene tres formas de correr:
        - python ocr.py --image example_01.png
        - python ocr.py --image example_01.png --preprocess thresh
        - python ocr.py --image example_01.png --preprocess blur

2. Trate de correr el ejemplo de pochetti para tratar de encontrar respuestas. 
    * Puedo correr solo la mitad del proyecto de pochetti pero me da la parte que necesitaba, la parte del reconocimiento de objetos dentro de la imagen. Con esto puedo darme una idea de como es que se realiza este proceso.

3. Lei capitulo 3 y 4 keyloger para los procesos del traductor.

### Fecha: Miércoles 31 de enero
1. Reunión con Mariona de Lérida para la instalación de ResearchLogger 

2. Necesito parsear el Log de los clicks.
    * Lo que hice fue hacerlo con bash. 
        ```
        cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,5-6 -d',' | tr ' ' ',' > coordinates.log
        ```
    * Estoy sacando:
        ```
        Xdown,Ydown, Nombre de la imagen, Xup, Yup
        30,58,20180131_123027_241486_gnome-terminal-server_tito.png,30,58 
        ```

3. Al parsear el archivo pretendo hacer:
    * Sacar el texto de las imágenes.
    * Verificar donde dio click dentro de la imagen.
    * Verificar si arrastro un click (con esto pretendo saber si subrayo algo o no)

4. Solo hice lo de Verificar donde dio click dentro de la imagen.

### Fecha: Jueves 1 de febrero

1. Estoy pensando si es necesario o no sacar tambien a la hora de parsear:
    ```
    Xdown,Ydown, evento, Nombre de la imagen, Xup, Yup, evento
    30,58,left_down,20180131_123027_241486_gnome-terminal-server_tito.png,30,58,left_up

    cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,4-6,8 -d',' | tr ' ' ','

    ```
2. Voy a verificar si arrastro un click
    * La idea es correr el ResearchLogger y hacer algunas pruebas subrayando algún texto. Teniendo esas pruebas se le corre el software coordenadas.py que lo que hace es leer el Log de los clicks y saca la informacion de las coordenadas para poder identificarla en las imagenes. Con esto vamos a saber si las coordenadas son distintas de los dos diferentes eventos(presionar click, soltar click).

3. Paula me paso para que leyera este link: https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/


### Fecha: Viernes 2 de febrero

1. Reunion con todos


### Fecha: Lunes 5 de febrero

1. Estoy haciendo el fork del proyecto y ordenando las cosas del repo anterior(imageKeylogger)

2. Haciendo pruebas con la biblioteca de pynput para tratar de loguear todos los movimientos posibles y clicks del mouse.
Esta herramienta utiliza las funciones:
    on_click: esta funcion lo que hace es obtener todos los eventos relacionados con la captura de los botones del mouse, se puede saber cuando presiona una tecla y suelta una tecla. tiene las 3 teclas(click izquierdo,derecho y centro)

    on_move: esta funcion logra captar todos los movimientos del mouse a lo largo de la pantalla, por ejemplo si mueve el mouse sobre una palabra o si no lo esta moviendo.

    on_scroll: es la funcion que obtiene el scroll hacia arriba y scroll hacia abajo con esto podemos saber si se encuentra en un documento analizando ciertos detalles o navegando por la web.

3. Pruebas para definir el crop box. el tamño de la ventana.
    Se necesita calcular un tamaño adecuado o un valor por default que con base en algo podamos determinar cual es el tamaño ideal que deberia de tener la imagenes que se toman para que el post análisis sea más fácil y el resultado sea lo más exacto posible. 

4. pyscreenshot es una biblioteca que toma tanto captura completa, pero también cuenta con la funcionalidad de poder tomar solo un pedacito(crop box).


### Fecha: Martes 6 de febrero

1. Hacer un script que capture cualquier movimiento con el mouse.
    Para realizar este script utilice la documentación que tiene la biblioteca https://pypi.python.org/pypi/pynput
    para familiarizarme con la herramienta utilizó los ejemplos por defecto de la herramienta.

2. Voy a hacer el mismo script de prueba para windows(con el fin de ver si al cambiar el código tenemos la compatibilidad)
    * Problemas con el click derecho, cada vez que se utiliza ese click se detiene y ocurre un error
    * El error se solucionó determinando que era solo si el click derecho se realiza sobre la terminal de windows donde se ejecuta, si es en cualquier otro lugar funciona bien.
3. Realizar cambios al anteproyecto para que quedé listo para mañana.


### Fecha: Miercoles 7 de febrero

1. Empece a realizar cambios en el proyecto de ReseachLogger.
    Necesito arreglar necesariamente el como se toman las imagenes de la herramienta para que me sea más fácil la captura de elementos dentro de las imagenes por lo que voy a hacer es ver el código por encima para ver que funcionalidades son necesarias y cuales no.
    * Empece con las constantes
    * La funcionalidad de agregar scroll podria ser interesante.
    * Existe posibilidad de agregar ruta donde el usuario este trabajando.
    * Existe posibilidad de agregar status del proceso, ej: running 

Empece a ver todo el código y me esta costando entender algunas cosas. tiene muchas clases dentro de los archivos y hay muchas funciones repetidas dentro del código, me estoy fustrando un poco, estoy viendo otras posibilidades. Estoy llegando a pensar que talvez es mejor empezar hacerla desde cero.


2. Reunion de seguimiento con Paula. 


### Fecha: Jueves 8 de febrero

1. Pienso en hacer otro ResearchLogger con solo la biblioteca pynput. 

2. Realice un mapeo de todos los archivos que debo tocar para realizar los cambios.
    * Constantes.py
    * detailLogWritter.py
    * onClickImageCapture.py
    * pyxhook.py
    * ResearchLogger.py
    * timedScreenshot.py

3. No se que hacer pero voy a seguir.


### Fecha: Viernes 9 de febrero

1. Reunion de segimiento con Aurelio
2. Reunion con Paula.

Lo que voy a empezar hacer es hacer pequeños cambios de algunas funcionalidades y ir testando si todavia apesar de los cambios la herramienta Reseach logger sigue funcionando con normalidad.

3. Empece realizando cambios para obtener el process_name y verifique los logs para ver si todo sigue bien.
4. Lo del process_name no anda bien. Lo estoy probando dentro de la herramienta pero a la hora de verificar en el log no se esta mostrando nada. 

### Fecha: Lunes 12 y martes 13 de febrero 
 
FERIADO

### Fecha: Miércoles 14 de febrero

1. Estoy realizando un documento que resume lo que he hecho por semana en las semanas anteriores.
2. Reunion con Aurelio.
3. La reunión me aclaro mucho las ideas ya que me volvio a poner en claro que es lo que debo hacer y cual es mi objetivo en este proyecto.


### Fecha: Jueves 15 de febrero

Hoy voy a testear la toma de screenshots en la Herramienta
    Cambie la biblioteca de tomar los screenshot por pyautogui uso lo mismo que la biblioteca anterior pero esta tiene una mayor compatibilidad con la biblioteca cv2 por lo que me va ayudar más cuando tenga que hacer procesamiento de imagenes.


### Fecha: Viernes 16 de febrero

1. Estoy tratando de asegurar de que todas las imagenes que se tomen, su respectivo x,y quede dentro del cropbox. El asegurarlo se me esta haciendo dificil ya que depende del lugar donde se tome queda fuera de la pantalla. Quiero no cambiar todo el código que ya se tiene para esta funcionalidad trató de reutilizarlo.
Voy a tratar de buscar una biblioteca que lo haga.

2. Cree el archivo saveimage.py
    La idea detras de este script es poder hacer un caso de prueba donde yo pueda tener a partir de un x,y que yo establezca tomar el respectivo screnshot y un cropbox del mmismo tratando de simular lo que ocurre en la herramienta pero sin tener que correr las otras funcionalidades de la herramienta y otros errores que no nos interesan.


### Fecha: Lunes 19 de febrero 

1. Hoy voy a cambiar para que las capturas completas de pantalla se hagan con la nueva biblioteca.
2. Las capturas de pantalla(pantalla total) estan listas.
3. Los procesos no se van a poder cambiar a este formato, El problema es que el evento no trae el id o el proceso actual por lo que no encuentro una manera de hacer este proceso generico para que funcione multiṕlataforma.

```
p = psutil.Process(os.getpid())
p.name()

```

### Fecha: Martes 20 de febrero 

1. Hoy termine de modificar todas las funciones de las imagenes, las imagenes ya estan perfectas para empezar analizarlas.
2. Realice modificaciones al saveimage.py

Voy a dejar hasta aca los cambios del research logger y voy a empezar con el analisis de las imagenes porque siento que me estoy atrasando un poco. si queda tiempo realizo los respectivos cambios.

### Fecha: Miércoles 21 de febrero

1. Reunión con Paula y con los demás compañeros analizamos en conjunto los problemas que teniamos cada uno y nos haciamos sugerencias.

2. Tuve una conversacion con Paula y le dije sobre que me iba a enfocar en lo de las imágenes, que iba a dejar un poco de lado lo de agregar nuevas funcionalidades y fijamos un nuevo norte.

Hablamos sobre los paper y dijimmos lo que pensabamos hacer en las próximas semanas ya que Paula no va a estar en el país.

NECESITO SABER EN QUE AMBITO PUEDE SER BUENO ENFOCAR MI INVESTIGACION
    * buscar plageo


3. Le dije a paula que necesitaba ir conociendo las actividades que realizaba Laura para sacar información observardo las imágenes.
    + Me dio un borrador de la tesis que esta realizando Laura para ser master en traductología


### Fecha: Jueves 22 de febrero
1. Hoy me voy a dedicar a leer la tesis de Laura

2. Cosas importantes de la tesis
    + Es muy importante el uso de la herramienta OmegaT
        * cuenta con 10 pasos que todo traductor necesita hacer dentro de esta herramienta se podria utilizar el analisis de imagenes para reconocer estos pasos.
        *Reconocer cuando trabaja en LibreOffice writter
        * REconocimiento de archivos (puede ser tambien la extención)
        *Es importante los 18 screen de analisis 
        * Lograr saber cuando un usuario se da cuenta de un error y lo corrige
        * Encontrar segmentos sin traducir dentro de la herramienta(figura 31 muestra 2)
        * verificacion de etiquetas (vendria siendo parte de los pasos)
        *Crear documentos finales
        * Activación del glosario (screenshot)
        * Activar coincidencias parciales (screenshot)
        * activar Diccionario (screenshot)
        * Subrayado de texto
        

3. Le ayude con algunas funcionalidades a Walter
    * Verificar que las flechas funcionen correctamente en Linux
    * Que el tab se captado por la herramienta

