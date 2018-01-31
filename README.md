# ImageKeylogger

La traducción de un idioma a otro es una tarea de producción de lenguaje natural y se han publicado numerosos estudios sobre los procesos cognitivos en la traducción usando la técnica de keylogging y por lo general hacen uso de las herramientas TransLog (Carl, 2012) o InputLog (M. Leijten, 2005). Sin embargo, estas herramientas tienen algunas limitaciones que han motivado el desarrollo de ResearchLogger (Lafuente, 2015). Lo novedoso de esta herramienta es que es opensource, loguea los eventos que ocurren en todas las ventanas abiertas y guarda eventos de click, de mouse y de teclas con precisión de milisegundos. ResearchLogger (RL) se ha empleado satisfactoriamente en estudios naturalistas donde la sesión de traducción sucede en el entorno natural del traductor (Estrella et al., 2017) así como también en sesiones controladas (Estrella et al., 2016).
 
Una de las etapas más importantes del uso del keylogger es el procesamiento de los datos recolectados: dado que los datos se guardan en distintos logs  que contienen una gran cantidad de eventos en formato texto o imágen. Aunque estos logs son complementarios, no siempre es posible automatizar el proceso. En particular, no hay desarrolladas hasta el momento, funcionalidades para el análisis de las imágenes que se guardan, que contienen información sobre los recursos online visitados y sobre las regiones en que se hace click, que podría utilizarse para triangular la información. En al menos dos casos puntuales el investigador debe recurrir a inspeccionar las imágenes para comprender lo que ha sucedido durante la sesión de traducción: 1) cuando se detecta una pausa demasiado larga en el proceso de escritura, porque ha pasado mucho tiempo entre eventos de teclado sucesivos, y 2) cuando se detecta que se han realizado determinadas acciones dentro de una herramienta que no requieren del teclado, por ejemplo, si se guardó un documento en LibreOffice con el menú “Archivo → Guardar como...” el log documenta el nuevo nombre del archivo pero no se puede saber si es un archivo nuevo, uno ya existente o el mismo pero con otro nombre. 
 
El objetivo de este trabajo es utilizar el material recolectado con RL para analizar las imágenes y detectar las regiones que contengan texto que pueda pertenecer al título de un menú o a la url de una página web. Se plantea una tarea limitada ya que las imágenes que conforman el conjunto de entrenamiento suponemos que tienen cierta regularidad (es decir, no son tan complejas como escenas naturales) y al contar con información asociada registrada en los logs, se puede explorar la opción de “anotar” el conjunto de entrenamiento con esta información. Para esta tarea de reconocimiento de texto en imágenes se propone analizar el conjunto de imágenes para determinar la estrategia de procesamiento más apropiada y realizar un  un estudio piloto para detectar las regiones que contienen el texto de interés utilizando Python+OpenCV. Una vez que se ha identificado la región se puede proceder a extraer el texto de manera automática, por ejemplo usando Python+Tesseract, aunque esto constituye una tarea de reconocimiento de texto y puede abordarse en futuros trabajos. 
