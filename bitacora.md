# Bitácora

## Proyecto procesamiento de imágenes para extracción de texto 


### Fecha: Miércoles 24 de enero

Hoy tuvimos la primera reunión con Paula y nos dio una introducción general a los tres proyectos.

#### Cosas por hacer:
- Instalar, probar y familiarizarse con el keylogger 
- Leer el trabajo de Roxana (funcionamiento de keylogger) capitulo 4.
- Primer aporte generar una instalación más transparente.

#### Que voy hacer hoy:
- Configurar mi nueva computadora.
- Descargar pycharm.
- Clonar repositorio de Roxana.
- Tratar de instalar el keylogger.
- Familiarizarme con el keylogger.

### Informe de Trabajo 
* Se instalo ubuntu en la máquina que me presto Paula para desarrollar el proyecto, además configure las llaves ssh para posteriormente trabajar con git.
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

* Instalación de Keylogger
    * Validate [sudo pip install validate]
    * Xlib [sudo apt-get install python-xlib]
    * Python Image Library (PIL) [sudo apt-get install python-pil]
    * gtk [sudo apt-get install python-gtk2]
    * Tkinter [sudo apt-get install python-tk]

*  Instalación más fácil para Linux, cree un script para que la instalación en linux sea mucho más fácil y sencilla para los usuarios.
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
    * Leí del libro los primeros dos capítulos y los anexos técnicos.

#### Pruebas

* Empezar hacer pruebas de correr el programa ResearchLoggerInterface.py y ResearchLogger.py 
    * Tengo problemas a la hora de terminar el programa con Ctrl izq + Ctrl der + F12
    * Estoy analizando el archivo onclickimagecapture.py ya que es acá donde se toman las capturas de pantalla que más adelante voy a necesitar.
    
* Intenté hacer una máquina de virtualbox en mi computadora pero no me sirvió debido a que no permite la virtualización.
    
* Hice una máquina para probar que el instalador de Linux sirve perfectamente en versiones mayores a 14.04.
    * Baje el instalador el la máquina de test.
    * Clone el proyecto en la máquina test.
    * El instalador funciona correctamente.
    
* Actualice la bitácora.

### Fecha: Domingo 28 de enero

#### Nuevas sugerencias
* Arreglar script para que valide si fue instalado o no.
* Arreglar dependencias
* Que descargue el repositorio de ResearchLogger

- Investigar como se puede a través de bash poder validar que un paquete este o no instalado en la computadora. 
    * Encontré que con la funcionalidad de "dpkg" se podría realizar una consulta al sistema y saber si este estaba o no instalado.
    * Para solucionar el problema de dependencias lo que hago es tratar de arreglar el sistema en caso de que ya tuviera errores con las dependencias y luego aplicó una actualización de paquetes para que no ocurra ningún error a la hora de instalar.
- Investigar si se podría validar un paquete instalado por pip
    * No encontré la forma intente con $(pip freeze | grep validate) pero en mi computadora aparece como si no estuviera dentro de los paquetes instalados pero si lo tiene.
    * Para minimizar el problema de arriba lo que hice fue ya que como utilizo "pip" para instalar el paquete "validate" lo que hago es actualizar pip para que no haya ningún error cuando instale el nuevo paquete.
- Mostar una salida donde quede más claro que fue lo que ocurrió.
    * Necesitaba colocar salidas de warning o de su correcto funcionamiento por lo que la salida se imprime de color rojo cuando es un warning y verde cuando su funcionamiento es correcto.


### Fecha: Lunes 29 de enero

1. Tarea de iniciar con la herramienta Tesseract
    utilice los siguientes links para iniciar
    - https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
    - https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/
    - https://www.pyimagesearch.com/wp-content/uploads/2014/02/ImageSearchEngineResourceGuide.pdf
2. Instalar tesseract
    Primero instale los paquetes
    ``` 
        pip install pillow
        pip install pytesseract
        pip install cv2
        pip install opencv-python
    ```
    Tuve problemas lo solucione con crear un ambiente virtual, lo que pasaba era que pillow tenia una doble referencia por lo que se necesita hacer el ambiente virtual y que lo único que este dentro de este ambiente sea este paquete.
    ```
            
        pip install pillow
        pip install pytesseract
        pip install cv2
        pip install opencv-python
    ```

3. Pruebas con la herramienta tesseract-ocr
    - Primero inicie con la imagen de prueba con letras grandes y la herramienta trabaja muy bien, el resultado fue excelente.
    - Luego utilice una imagen “salt and pepper” osea que tenga ruido en el fondo de la imagen, esto con el fin de ver si se tiene el mismo resultado.
    - La siguiente imagen era un código el cual tenia letras de colores y a la hora de aplicar la herramienta esta borra las palabras de color.
    - Hice pruebas con las imágenes de los LOGS del ResearchLogger al pasarlo por la herramienta el resultado no es para nada bueno, fue donde note que existe una necesidad de una buena resolución.

4. Mejorar Resolución
    * Para observar la resolución de la imágenes en el servidor utilice:
    ```
    identify -ping image.png 
    ```
    * Resolución 150*150, este tipo de imagen carece de información en la resolución, al probar este tipo de imagen con la herramienta se pierde información al extraer el texto dando como resultado erróneo. 
    * Resolucion 350*350
    * Resolución 500*250

Nota:
Pienso que no del todo es responsabilidad de la resolución también la herramienta tiene dificultades al ser imágenes con colores. Para que el resultado sea bueno debería de tener fondo blanco y letras negras.


### Fecha: Martes 30 de enero

1. hice el archivo ocr.py
    * Este archivo lo que hace es procesar un archivo con la herramienta tesseract
    * Tiene tres formas de correr:
        - python ocr.py --image example_01.png
        - python ocr.py --image example_01.png --preprocess thresh
        - python ocr.py --image example_01.png --preprocess blur

2. Trate de correr el ejemplo de pochetti para tratar de encontrar respuestas. 
    * Puedo correr solo la mitad del proyecto de pochetti pero me da la parte que necesitaba, la parte del reconocimiento de objetos dentro de la imagen. Con esto puedo darme una idea de como es que se realiza este proceso.

3. Leí capitulo 3 y 4 keyloger para los procesos del traductor.

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

1. Estoy pensando si es necesario o no sacar también a la hora de parsear:
    ```
    Xdown,Ydown, evento, Nombre de la imagen, Xup, Yup, evento
    30,58,left_down,20180131_123027_241486_gnome-terminal-server_tito.png,30,58,left_up

    cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,4-6,8 -d',' | tr ' ' ','

    ```
2. Voy a verificar si arrastro un click
    * La idea es correr el ResearchLogger y hacer algunas pruebas subrayando algún texto. Teniendo esas pruebas se le corre el software coordenadas.py que lo que hace es leer el Log de los clicks y saca la información de las coordenadas para poder identificarla en las imágenes. Con esto vamos a saber si las coordenadas son distintas de los dos diferentes eventos(presionar click, soltar click).

3. Paula me paso para que leyera este link: https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/


### Fecha: Viernes 2 de febrero

1. Reunión con todos.


### Fecha: Lunes 5 de febrero

1. Estoy haciendo el fork del proyecto y ordenando las cosas del repositorio anterior(imageKeylogger)

2. Haciendo pruebas con la biblioteca de pynput para tratar de loguear todos los movimientos posibles y clicks del mouse.
Esta herramienta utiliza las funciones:
    on_click: esta función lo que hace es obtener todos los eventos relacionados con la captura de los botones del mouse, se puede saber cuando presiona una tecla y suelta una tecla. tiene las 3 teclas(click izquierdo,derecho y centro)

    on_move: esta función logra captar todos los movimientos del mouse a lo largo de la pantalla, por ejemplo si mueve el mouse sobre una palabra o si no lo esta moviendo.

    on_scroll: es la función que obtiene el scroll hacia arriba y scroll hacia abajo con esto podemos saber si se encuentra en un documento analizando ciertos detalles o navegando por la web.

3. Pruebas para definir el cropbox. el tamaño de la ventana.
    Se necesita calcular un tamaño adecuado o un valor por default que con base en algo podamos determinar cual es el tamaño ideal que debería de tener la imágenes que se toman para que el post análisis sea más fácil y el resultado sea lo más exacto posible. 

4. pyscreenshot es una biblioteca que toma tanto captura completa, pero también cuenta con la funcionalidad de poder tomar solo un pedacito(cropbox).


### Fecha: Martes 6 de febrero

1. Hacer un script que capture cualquier movimiento con el mouse.
    Para realizar este script utilice la documentación que tiene la biblioteca https://pypi.python.org/pypi/pynput
    para familiarizarme con la herramienta utilizó los ejemplos por defecto de la herramienta.

2. Voy a hacer el mismo script de prueba para windows(con el fin de ver si al cambiar el código tenemos la compatibilidad)
    * Problemas con el click derecho, cada vez que se utiliza ese click se detiene y ocurre un error
    * El error se solucionó determinando que era solo si el click derecho se realiza sobre la terminal de windows donde se ejecuta, si es en cualquier otro lugar funciona bien.
3. Realizar cambios al anteproyecto para que quedé listo para mañana.


### Fecha: Miércoles 7 de febrero

1. Empece a realizar cambios en el proyecto de ReseachLogger.
    Necesito arreglar necesariamente el como se toman las imágenes de la herramienta para que me sea más fácil la captura de elementos dentro de las imágenes por lo que voy a hacer es ver el código por encima para ver que funcionalidades son necesarias y cuales no.
    * Empece con las constantes
    * La funcionalidad de agregar scroll podría ser interesante.
    * Existe posibilidad de agregar ruta donde el usuario este trabajando.
    * Existe posibilidad de agregar status del proceso, ej: running 

Empece a ver todo el código y me esta costando entender algunas cosas. tiene muchas clases dentro de los archivos y hay muchas funciones repetidas dentro del código, me estoy frustrando un poco, estoy viendo otras posibilidades. Estoy llegando a pensar que tal vez es mejor empezar hacerla desde cero.

2. Reunion de seguimiento con Paula. 


### Fecha: Jueves 8 de febrero

1. Pienso en hacer otro ResearchLogger con solo la biblioteca pynput. 

2. Realice un mapeo de todos los archivos que debo tocar para realizar los cambios.
    * constantes.py
    * detailLogWritter.py
    * onClickImageCapture.py
    * pyxhook.py
    * ResearchLogger.py
    * timedScreenshot.py

3. No se que hacer pero voy a seguir.


### Fecha: Viernes 9 de febrero

1. Reunión de seguimiento con Aurelio
2. Reunión con Paula.

Lo que voy a empezar hacer es hacer pequeños cambios de algunas funcionalidades y ir testando si todavía a pesar de los cambios la herramienta Reseach logger sigue funcionando con normalidad.

3. Empece realizando cambios para obtener el process_name y verifique los logs para ver si todo sigue bien.
4. Lo del process_name no anda bien. Lo estoy probando dentro de la herramienta pero a la hora de verificar en el log no se esta mostrando nada. 

### Fecha: Lunes 12 y martes 13 de febrero 
 
FERIADO

### Fecha: Miércoles 14 de febrero

1. Estoy realizando un documento que resume lo que he hecho por semana en las semanas anteriores.
2. Reunion con Aurelio.
3. La reunión me aclaro mucho las ideas ya que me volvió a poner en claro que es lo que debo hacer y cual es mi objetivo en este proyecto.


### Fecha: Jueves 15 de febrero

Hoy voy a testear la toma de screenshots en la Herramienta
    Cambie la biblioteca de tomar los screenshot por pyautogui uso lo mismo que la biblioteca anterior pero esta tiene una mayor compatibilidad con la biblioteca cv2 por lo que me va ayudar más cuando tenga que hacer procesamiento de imágenes.


### Fecha: Viernes 16 de febrero

1. Estoy tratando de asegurar de que todas las imágenes que se tomen, su respectivo x,y quede dentro del cropbox. El asegurarlo se me esta haciendo difícil ya que depende del lugar donde se tome queda fuera de la pantalla. Quiero no cambiar todo el código que ya se tiene para esta funcionalidad trató de reutilizarlo.
Voy a tratar de buscar una biblioteca que lo haga.

2. Cree el archivo saveimage.py
    La idea detrás de este script es poder hacer un caso de prueba donde yo pueda tener a partir de un x,y que yo establezca tomar el respectivo screnshot y un cropbox del mismo tratando de simular lo que ocurre en la herramienta pero sin tener que correr las otras funcionalidades de la herramienta y otros errores que no nos interesan.


### Fecha: Lunes 19 de febrero 

1. Hoy voy a cambiar para que las capturas completas de pantalla se hagan con la nueva biblioteca.
2. Las capturas de pantalla(pantalla total) están listas.
3. Los procesos no se van a poder cambiar a este formato, El problema es que el evento no trae el id o el proceso actual por lo que no encuentro una manera de hacer este proceso genérico para que funcione multiplataforma.

```
p = psutil.Process(os.getpid())
p.name()

```

### Fecha: Martes 20 de febrero 

1. Hoy termine de modificar todas las funciones de las imágenes, las imágenes ya están perfectas para empezar analizarlas.
2. Realice modificaciones al saveimage.py

Voy a dejar hasta acá los cambios del research logger y voy a empezar con el análisis de las imágenes porque siento que me estoy atrasando un poco. si queda tiempo realizo los respectivos cambios.

### Fecha: Miércoles 21 de febrero

1. Reunión con Paula y con los demás compañeros analizamos en conjunto los problemas que teníamos cada uno y nos hacíamos sugerencias.

2. Tuve una conversación con Paula y le dije sobre que me iba a enfocar en lo de las imágenes, que iba a dejar un poco de lado lo de agregar nuevas funcionalidades y fijamos un nuevo norte.

Hablamos sobre los paper y dijimos lo que pensábamos hacer en las próximas semanas ya que Paula no va a estar en el país.

NECESITO SABER EN QUE ÁMBITO PUEDE SER BUENO ENFOCAR MI INVESTIGACIÓN
    * Buscar plagio


3. Le dije a paula que necesitaba ir conociendo las actividades que realizaba Laura para sacar información observando las imágenes.
    + Me dio un borrador de la tesis que esta realizando Laura para ser master en traductología


### Fecha: Jueves 22 de febrero
1. Hoy me voy a dedicar a leer la tesis de Laura

2. Cosas importantes de la tesis
    + Es muy importante el uso de la herramienta OmegaT
        * cuenta con 10 pasos que todo traductor necesita hacer dentro de esta herramienta se podría utilizar el análisis de imágenes para reconocer estos pasos.
        * Reconocer cuando trabaja en LibreOffice writter
        * Reconocimiento de archivos (puede ser también la extención ej: .png, .jpg, etc.)
        * Es importante los 18 screenshots de análisis 
        * Lograr saber cuando un usuario se da cuenta de un error y lo corrige
        * Encontrar segmentos sin traducir dentro de la herramienta(figura 31 muestra 2)
        * Verificación de etiquetas (vendría siendo parte de los pasos)
        * Crear documentos finales
        * Activación del glosario (screenshot)
        * Activar coincidencias parciales (screenshot)
        * Activar Diccionario (screenshot)
        * Subrayado de texto


3. Le ayude con algunas funcionalidades a Walter
    * Verificar que las flechas funcionen correctamente en Linux
    * Que el "tab" se captado por la herramienta


### Fecha: viernes 23 de febrero
Detección de objetos

Existen tres procedimientos principales en el análisis de BLOB:
1. Extracción: En esta parte del procesamiento se encuentran los pixeles conectados entre si osea pixeles vecinos que coinciden con las especificaciones, para lograrlo usualmente se utilizan algoritmos como el algoritmo Grass-Fire Recursivo o el algoritmo Grass-Fire Secuencial

2. Representación: Es la de representar las características de los pixeles que hemos extraído anteriormente, esto se hace por medio de números que indica la cantidad de características y luego puede ser comparado por medio de un método para asegurarse de que cumple con las características propuestas, por ejemplo si es un rectángulo, los pixeles deben representar cuatro lineas intercontectadas, dos paralelas entre si horizontalmente y dos paralelas entre si verticalmente.

3. Clasificación: Se compara directamente con un prototipo para verificar que realmente concuerda con las características que queremos filtrar, por ejemplo en el caso anterior compararíamos los pixeles con un conjunto de pixeles que representan un rectángulo.

https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
https://planetachatbot.com/introducci%C3%B3n-a-la-detecci%C3%B3n-de-objetos-con-python-y-simplecv-ccbbe33a5bc4

Estoy realizando pruebas para entender como puedo solucionar el problema de seleccionar el centro como región de interés y si a la hora de analizar toda la imagen se puede seleccionar que analice solo una parte de la imagen.


### Fecha: Lunes 26 de febrero 

Hoy estoy tratando de resolver como identificar que dio click sobre un menú y sobre que parte del menú hizo click.

1. Estoy realizando el script textDetect.
    * Quiero intentar detectar solo los objetos del centro de la imagen
    * Estoy realizando diferentes funciones con diferentes contornos y kernels para poder observar cual me sirve mejor.

2. Puedo tener la región de interés con:
cv2.selectROI(im) # esta debe ser con un humano

3. ya puedo tener todos los objetos que hay en una imagen

### Fecha: Martes 27 de febrero

Desde el día de ayer estuve viendo como enfocarme en la parte central de la imagen, ya que como es acá donde esta el click es la zona donde voy analizar para identificar que voy hacer.
    * Estaba realizando una extracción de la parte central(forma de rectángulo) pero esta no me servia me parecía extraño que me estuviera ocurriendo eso.
    El problema era el siguiente:
    En la función yo me encontraba realizando el orden de parametros de esta forma 
      

```
  
    (x1,y1),(x2,y2)
    
    pero realmente era 
    
    (y1:y2),(x1:x2)

```
   
   El orden cambiaba... creo que estaba demasiado estresado... :(

Mi otra teoría de hoy es comprobar si se puede sacar de una imagen por algún color en especifico.
    * Observe que esta teoria no me funcionaba si lo hacia con el color que yo necesitaba. Creo que solo sirve con el color rojo,azul,amarillo y gris.

### Fecha: Miércoles 28 de febrero

1. Posibles Soluciones:
    * Sikuli http://www.sikuli.org/
    * Scikit-image  http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html
    * Blob análisis:
        + Bounding box of a blob is the minimum
        + object detection using blob tracing
2. Reunión con Aurelio.

### Fecha: Jueves 1 de marzo
1.  En la reunión de ayer con Aurelio me dijo que era muy necesario realizar mis informes de avances por lo que hoy decidí empezar hacer todos los informes desde que inicie mi proyecto.
2. Realizó algunos cambios en mi bitácora.
3. Voy hacer una carpeta en google drive donde voy a ir haciendo cada informe de avance.
4. Termine los informes de avance de las primeras 5 semanas.

### Fecha: Viernes 2 de marzo

Hoy sentía que debia irme para atras y repasar algunas cosas. por lo que elimine los scripts que ya no servian y comente que es lo que hace cada uno. Con esto ver todas las ideas que ya he probado y volver a replantear.

* Observando el script saveImage.py me doy cuenta de que ya no debo saber el x,y donde se dio click ya que la funcion que programe para que quedara en el centro hace que con solo obtener el tamaño de la pantalla y dividirlo entre 4, pueda tener el punto exacto donde se dio el click.
'''
puntoX = screensize.x/4 
puntoY = screensize.y/4 

'''

* Realice una corrida del Research logger dando clicks en varios menus como el de google chrome, sublime, termianal todo esto con el fin de observar como van cambiando estas imágenes. 
    + Este analisis a pie logre entender que si sigo el analisis por saturacion de la imagen no voy a tener siempre el resultado correcto, ya que depende de la imagen puede:
        - Tener varios lugares con una saturacion alta lo que va hacer que tenga varios resultados
        - No tener saturación alta donde realmente hizo click
        - 


### Fecha: Lunes 5 de marzo

No hubo internet en todo el día.


### Fecha: Martes 6 de marzo
- Se logró solucionar el problema del internet a la 1:00pm
- Se terminó el borrador del primer informe.
- Se realizó el informe de avance de la semana 6.

### Fecha: Miércoles 7 de marzo

No use jpg porque Compresión JPEG (crea artefactos no visibles para el ojo humano, pero perjudiciales para los algoritmos)

Hoy tengo pensado hacer:
    - instalar omegat
    - intentar capturar los blobs de texto
    - Analisis de gradiente
    - ColorDistance

Voy a cambiar a python 3:
    + Empece con este tutorial pero tuve errores de dependencias a la hora de hacer el built daba error https://www.learnopencv.com/install-opencv3-on-ubuntu/

    en el comando: make -j4


'''
    modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/build.make:134: recipe for target 'modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/src/wbdetector.cpp.o' failed
    make[2]: *** [modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/src/wbdetector.cpp.o] Error 1
    make[2]: *** Waiting for unfinished jobs....
    modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/build.make:86: recipe for target 'modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/src/waldboost.cpp.o' failed
    make[2]: *** [modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/src/waldboost.cpp.o] Error 1
    CMakeFiles/Makefile2:8973: recipe for target 'modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/all' failed
    make[1]: *** [modules/xobjdetect/CMakeFiles/opencv_xobjdetect.dir/all] Error 2
    Makefile:160: recipe for target 'all' failed
    make: *** [all] Error 2
'''

Lo solucione con este otro: https://medium.com/@debugvn/installing-opencv-3-3-0-on-ubuntu-16-04-lts-7db376f93961

Python2 y Python3 quedaron con la version:
'''
>>> import cv2
>>> cv2.__version__
'3.4.0'
'''


Para la nueva prueba con python3 no logro que esta funcion me sirva

'''
channels = cv.text.computeNMChannels(img)
'''

### Fecha: Jueves 8 de marzo

1. Tuve la reunión con Paula y discutimos la posibilidad de hacer diferente lo de la extraccion de las imagenes.
    * Lo primero es que se va hacer una primera parte donde se va hacer una prueba en la que el script va a tener la asistencia de un humano para la detección de las zonas de interés
    * Segunda parte sin asistencia que se logren detectar automáticamente.

2. Instalando el paquete gtk, yo puse el parametro -y lo que hizo fue eliminar muchos paquetes y la máquina dejo de funcionar.
    * La máquina se quedo sin internet por lo que fue dificil de arreglar.
    * No queria perder toda la informacion ni la de Paula por lo que realice una copia de seguridad. 
    * La copia de seguridad duro 4 horas.

### Fecha: Viernes 9 de marzo

1. Termine de arreglar la computadora y de instalar unos paquetes que se borraron.
2. Tuve la reunion semanal con Aurelio
    * Me dijo que los informes semanales estaban bien
    * Me hizo anotaciones  sobre el informe:
        + cambiar el contexto
        + cambiar steakholders
        + agregar necesidades y expectativas
        + tiene que estar los requerimientos no funcionales
        + alcanses: hacerlo mas a que va hacer un prototipo
        + agregar modelo conceptual
        + agregar un diagrama de metodologia

3. 


### Fecha: Lunes 12 de marzo

1. Solucione los problemas que tengo con gtk instalando
'''
 sudo apt-get install python-gtk2
'''

2. Realice un script llamado selectBox.py para probar como seleccionar una parte de la imagen

3. Realice una carpeta para hacer una prueba donde se seleccione el area que se quiere capturar
'''
    AreaAsistida/
        coordinates.log
        seleccion.png
        selectBox.py
'''
cordinates.log es el archivo en el que simplifico la cantidad de cosas que quiero del LOG original.
seleccion.png es el resultado que se produce al humano ir realizando cada recorte.
SelectBox es el código que logra hacer que todo pueda funcionar.

el ejemplo de area asistida quedo listo.


### Fecha: Martes 13 de marzo

1. Hoy le enseñe a Paula la solucion propuesta Asistida

2. Llegamos a una conclusion luego de ver algunos casos, las imagenes con click_up solo son importantes cuando se realiza un subrayado en la imagen por lo que sugerimos que puede ser un camino viable para hacer el problema un poco más pequeño.

3. Realice una prueba con Research logger, la idea es iniciar libre office y escribir palabras y luego subrayarlas con el fin de generar los logs con estas caracteristicas. 
    * Problema: El archivo log no contiene las imagenes. (no tiene todas las imagenes)

4. Termine las correciones del primer informe.


### Fecha: Miércoles 14 de marzo

1. Realice el script diffImage.py este da como resultado la diferencia entre dos imagenes.

2. Estaba teniendo un error a la hora de leer el  archivo del log y estaba perdiendo lineas ya que cada entrada no viene como una linea sino que cada vez que utiliza un programa es una linea. Por lo que el comando que uso para sacar solo lo que necesito va a cambiar.
'''
anterior  = "cat "+file+" | cut -f8 -d'|' | cut -f 1-2,4-6,8-9 -d',' | tr ' ' ',' > " + nameLog + ""

nuevo = "cat "+file+" | cut -f8 -d'|' | tr ' ' '\n' | sed '/^$/d' > " + nameLog + ""

y luego para que en click down y click up queden en una sola linea se agrgará esto:

nuevoMod = "cat "+file+" | cut -f8 -d'|' | tr ' ' '\n' | sed '/^$/d' | paste -s -d'\t\n' > " + nameLog + ""


'''

3. Aplique los nuevos cambios a selectBox.py la que es asistida.

4. De un total de 38 imágenes tomadas se encuentran en el archivo un total de 34


### fecha Jueves 15 de marzo

Estoy intentando mejorar la diferencia entre imagenes para poder sacar el texto que se encuantre entre ellas.

Esto lo estoy haciendo para añadirlo a la parte del analisis de imagenes cuando se realiza un subrayado.

### fecha Viernes 16 de marzo

sigo perdido.

1. Logre obtener una imagen unicamente con la diferencia de las imagenes. Lo bueno de esto es que esta con el color original de la imagen original.

imagenOriginal - imagenCambio = imagenDiferencia 


### fecha Lunes 19 de marzo

1. Estoy tratando de agregarle tesseract a lo logrado el viernes pero no se porque no esta funcionando.


2. Voy a explorar algún otro modo de extraer el texto. 

3. Voy a probar textract
http://textract.readthedocs.io/en/stable/installation.html

4. voy a probar con pyocr
sudo pip install pyocr
https://github.com/openpaperwork/pyocr

### fecha Martes 20 de marzo

1. instale el lang español
'''
 sudo apt-get install tesseract-ocr-spa
'''
2. instalar ingles
'''
 sudo apt-get install tesseract-ocr-eng

'''
3. Reunion con paula, le dije lo que habia hecho.

### fecha Miércoles 21 de marzo

1. El problema de la no extraccion de texto con tesseract se debia a que la herramienta esta especializada para que el texto venga de color negro y lo demas este blanco. Estas condiciones no se estaban dando en la imagen por lo que le era imposible dar un resultado.

2. Cuando hago uso del dilate y erode tengo que tener especial cuidado ya que si las letras son muy pequeñas esto podria hacer que se vea peor de lo que ya esta. 

3. Realice pruebas para mejorar por medio de un procesamiento de la imagen de modo que permita ser más clara para la extracción del texto de una imagen.

4. Encontre esta funcion cv2.bitwise_not(thresh) lo que me ayuda es cuando estoy procesando las imagenes me pasa el negro a blanco, y lo blanco a negro. Con esto tengo mejores resultados a la hora de aplicar tesseract.

### fecha Jueves 22 de marzo

1. Dado que no estoy teniendo como resultado una buena extraccion de texto se me ocurrió una idea:
    * Vamos a mandar los datos a un excel, de manera que se pueda visualizar tanto la imagen como el texto extraído por tesseract.


### fecha Viernes 23 de marzo

cumpleaños de Randall


### fecha Lunes 26 de marzo

1. Estoy haciendo los documentos de avance de la semana 7,8 y 9.

2. Voy a poner a correr un algoritmo de clasificación: https://github.com/llvll/imgcluster 
    * instalación
    sudo pip install numpy scipy scikit-learn
    sudo pip install -U scikit-image
    sudo pip install pyssim


### fecha Martes 27 de marzo

1. Estoy probando el imgcluster con el demo para ver los resultados:
'''
Building the similarity matrix using SIFT algorithm for 20 images
Done - total calculation time: 97 seconds

Performance metrics for Spectral Clustering
Number of clusters: 4
Silhouette coefficient: -0.77
Completeness score: 0.19
Homogeneity score: 0.18

Performance metrics for Affinity Propagation Clustering
Number of clusters: 3
Silhouette coefficient: -0.66
Completeness score: 0.13
Homogeneity score: 0.10

Selected Affinity Propagation for the labeling results

 --- Images from cluster #0 ---
3
Image field-of-poppies.jpg
5
Image sailing-ship.jpg
8
Image macbook.jpg
11
Image iphone.jpg
16
Image fox.jpg
17
Image poppies.jpg
18
Image ferry-boat.jpg
19
Image sea.jpg

 --- Images from cluster #1 ---
1
Image yacht.jpg
4
Image yacht-copy.jpg
13
Image bear.jpg

 --- Images from cluster #2 ---
0
Image office.jpg
2
Image raccoon.jpg
6
Image wanderer.jpg
7
Image mobile.jpg
9
Image bike.jpg
10
Image freerider.jpg
12
Image winter.jpg
14
Image wolf.jpg
15
Image imac.jpg






Agregando copia de dos imagenes más
Building the similarity matrix using SIFT algorithm for 22 images
Done - total calculation time: 108 seconds

Performance metrics for Spectral Clustering
Number of clusters: 4
Silhouette coefficient: -0.77
Homogeneity score: 0.32
Completeness score: 0.34

Performance metrics for Affinity Propagation Clustering
Number of clusters: 3
Silhouette coefficient: -0.44
Homogeneity score: 0.18
Completeness score: 0.22

Selected Affinity Propagation for the labeling results

 --- Images from cluster #0 ---
0
Image office.jpg
1
Image yacht.jpg
4
Image yacht-copy.jpg
5
Image sailing-ship.jpg
13
Image office (copy).jpg
14
Image winter.jpg
15
Image bear.jpg
17
Image imac.jpg
20
Image ferry-boat.jpg

 --- Images from cluster #1 ---
3
Image field-of-poppies.jpg
6
Image iphone (copy).jpg
9
Image macbook.jpg
12
Image iphone.jpg
18
Image fox.jpg
19
Image poppies.jpg
21
Image sea.jpg

 --- Images from cluster #2 ---
2
Image raccoon.jpg
7
Image wanderer.jpg
8
Image mobile.jpg
10
Image bike.jpg
11
Image freerider.jpg
16
Image wolf.jpg

'''

2. Voy hacer un set de imagenes de prueba con mis imagenes para someterlas a prueba en este cluster

el set me quedo de 198 imágenes

Prueba:
Building the similarity matrix using SIFT algorithm for 198 images
Done - total calculation time: 6484 seconds
error..........



### fecha Jueves 12 de abril

1. Volvimos a Costa Rica, y tuvimos algunas reuniones con aurelio, kevin y diego. Para tratar temas de como iban a funcionar las cosas.

Con Aurelio:
- Sobre los documentos que debemos presentar 
- Realizar una presentación sobre el proyecto y experiencia para centro Alajuela

Kevin:
- Necesidad de equipo para continuar con el proyecto

Diego: 
- Necesidad de prestamo de alumnos para la toma de datos.


### fecha viernes 13 de abril

1. Empece con la instalacion de ubuntu a la computadora.

2. Instalación de los programas necesarios(pycharm, sublime,...)

3. Descargar el proyecto e github (Researchlogger,imageKeylogger)

4. Instalacion de los requerimientos para el proyecto

5. ResearchLogger ya se encuentra funcionando


### fecha lunes 16 de abril

Estuve pensando en que el proyecto se encuentra en la parte de pos-procesamiento por lo que voy a integrarlo con el Reseach Analizer ya que tambien voy hacer uso de algunas de las funciones que ya se encuentran en este proyecto.

El proyecto quedo completamente montado en Research Analizer


### fecha martes 17 de abril 

1. Realize el archivo images_interpreter el cual se va a encargar de la interpretacion de todas las imagenes.

2. La solución A que es la del subrayado dentro de las imagenes, realice un archivo image_underline que es el que estoy trabajando.


### fecha miércoles 18 de abril 

1. Empece a trabajar en la revision de Research Logger para windows pero tengo un problema con el driver de wifi por lo que lo voy a dejar para despues








Función para cambiar

   def capture_image(self, event):
        #screensize width heigth
        screensize = self.get_screen_size()

        #Position x,y
        x = event.Position[0]
        y = event.Position[1]

        #take the highest point left and the lowest point right. (to form a rectangle cropbox)
        x1 = x - (screensize.x / 4)
        x2 = x + (screensize.x / 4)
        y1 = y - (screensize.y / 4)
        y2 = y + (screensize.y / 4)

        #width and height
        w = x2 - x1
        h = y2 - y1

        #take a cropbox
        image_data = pyautogui.screenshot(region=((x1,y1, w, h)))

        return image_data



links:

https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
https://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
https://mmeysenburg.github.io/image-processing/08-contours/
https://www.pyimagesearch.com/2015/02/09/removing-contours-image-using-python-opencv/
https://henrydangprg.com/2016/06/26/color-detection-in-python-with-opencv/
https://henrydangprg.com/2016/12/11/canny-edge-detection-in-python-with-opencv/
https://www.blog.pythonlibrary.org/2016/10/11/how-to-create-a-diff-of-an-image-in-python/
https://robologs.net/2016/04/21/detectar-diferencias-entre-dos-imagenes-con-opencv-y-python/
https://codeyarns.com/2015/08/20/how-to-apply-mask-in-opencv/
https://stackoverflow.com/questions/47062216/replace-mask-with-original-image-opencv-python
http://www.learnopencv.com/blob-detection-using-opencv-python-c/
http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html
http://layer0.authentise.com/object-detection-using-blob-tracing.html
http://what-when-how.com/introduction-to-video-and-image-processing/blob-analysis-introduction-to-video-and-image-processing-part-1/
https://stackoverflow.com/questions/46003033/extract-contours-from-bounding-box
https://docs.adaptive-vision.com/current/studio/machine_vision_guide/BlobAnalysis.html
https://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/

compare tesseract, ocr
https://medium.com/@winston.smith.spb/python-ocr-for-pdf-or-compare-textract-pytesseract-and-pyocr-acb19122f38c

porque use png
https://docs.adaptive-vision.com/current/studio/machine_vision_guide/ImageProcessing.html

