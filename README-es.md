# Programación Python para la ciencia de datos
----
Para acceder a la versión en catalán de este documento, haced clic [aquí](README.md).
# 1. Introducción

Este repositorio contiene un conjunto de *notebooks* de jupyter que forman parte de los cursos de programación Python para la ciencia de datos de la Universitat Oberta de Catalunya, y que se distribuyen bajo licencia [`CC-BY-SA`](https://creativecommons.org/licenses/by-sa/4.0/).

El repositorio contiene los notebooks separados en dos carpetas:
1. La carpeta `python_1` contiene los *notebooks* de la asignatura **Fundamentos de programación**, que ofrece una introducción a la programación en lenguaje Python centrada en la resolución de problemas del ámbito de la ciencia de datos.

2. La carpeta `python_2` contiene los *notebooks* de la asignatura **Programación para la ciencia de datos**, profundizando en la comprensión de algunos de los conceptos clave, a la vez que se explican otros conceptos de programación más avanzados , que permitirán a los estudiantes afrontar problemas de programación más complejos y de manera más eficiente, en Python.

El índice de contenidos del material de `python_1` es el siguiente:

* Unidad 1: Instalación y configuración del entorno de programación Python
* Unidad 2: Breve introducción a la programación en Python
* Unidad 3: Estructuras de control y funciones en Python
* Unidad 4: Librerías científicas en Python
* Unidad 5: Captura de datos en Python
* Unidad 6: Preprocesamiento de datos en Python
* Unidad 7: Introducción al análisis de datos en Python
* Unidad 8: Visualización de datos en Python

El índice de contenidos del material de `python_2` es el siguiente:
* Unidad 0: Afianzando conceptos
* Unidad 1: Estructuras de datos avanzadas
* Unidad 2: Uso avanzado de funciones
* Unidad 3: Archivos e interacción con el sistema
* Unidad 4: Optimización: complejidad y profiling
* Unidad 5: Optimización: concurrencia y paralelismo
* Unidad 6: Testing, mantenimiento y desarrollo de aplicaciones

Cada unidad se encuentra dentro de una carpeta que tiene por nombre `unit_x`, donde `x` es el número de la unidad. Dentro de la carpeta de cada unidad, encontraréis tanto el *notebook* que podéis ejecutar, como una exportación a pdf del contenido del *notebook*. Si se utilizan conjuntos de datos para ejemplificar los conceptos explicados en las unidades, también encontraréis una carpeta `data` que contendrá todos los datos necesarios para ejecutar el *notebook*.

# 2. Preparación del entorno

Con el fin de ejecutar los *notebooks* necesitaréis:
* Una instalación de `python3` con algunas librerías adicionales y
* El software `jupyter`.

La máquina virtual que se proporciona en cualquiera de las dos asignaturas ya incorpora todo el software necesario para ejecutar el contenido de este repositorio. Como alternativa, podéis instalar en la máquina el software siguiendo las indicaciones de los apartados siguientes.

## 2.1. Instalación de python3

Descargad e instalad `python3` para vuestro sistema operativo.

Si trabajáis con una distribución linux basada en debian, podéis ejecutar:

```
$ sudo apt-get install python3
```

## 2.2. Instalación de dependencias

Instalad las librerías adicionales necesarias, que se encuentran especificadas en `requirements.txt` ejecutando desde dentro de la carpeta del repositorio:

```
$ pip install -r requirements.txt
```

## 2.3. Instalación de jupyter

Instalad el software jupyter siguiendo las indicaciones de la [web oficial](https://jupyter.org/install)

# 3. Ejecución de los notebooks

Una vez que tengáis el software instalado, iniciad jupyter y abrid los *notebooks*:

```
$ jupyter notebook
```

Si utilizáis la máquina virtual de las asignaturas, también podéis iniciar jupyter ejecutando el *script* `start_uoc`:
```
$ start_uoc.sh
```
