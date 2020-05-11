# Programació Python per a la ciència de dades
----
Per a accedir a la versió en castellà d'aquest document, feu clic [aquí](README-es.md).
# 1. Introducció

Aquest repositori conté un conjunt de *notebooks* de jupyter que formen part dels cursos de programació Python per a la ciència de dades de la Universitat Oberta de Catalunya, i que es distribueixen sota llicència [`CC-BY-SA`](https://creativecommons.org/licenses/by-sa/4.0/).

El repositori conté els notebooks separats en dues carpetes: 
1. La carpeta `python_1` conté els *notebooks* de l'assignatura **Fonaments de programació**, que ofereix una introducció a la programació en llenguatge Python centrada en la resolució de problemes de l'àmbit de la ciència de dades.

2. La carpeta `python_2` conté els *notebooks* de l'assignatura **Programació per a la ciència de dades**, aprofundint en la comprensió d'alguns dels conceptes clau, alhora que s'expliquen altres conceptes de programació més avançats, que permetran als estudiants afrontar problemes de programació més complexos i de manera més eficient, en Python.

L'índex de continguts del material de `python_1` és el següent:

* Unitat 1: Instal·lació i configuració de l'entorn de programació Python
* Unitat 2: Breu introducció a la programació en Python
* Unitat 3: Estructures de control i funcions en Python
* Unitat 4: Llibreries científiques en Python
* Unitat 5: Captura de dades en Python
* Unitat 6: Preprocessament de dades en Python
* Unitat 7: Introducció a l'anàlisi de dades en Python
* Unitat 8: Visualització de dades en Python

L'índex de continguts del material de `python_2` és el següent:
* Unitat 0: Refermant conceptes
* Unitat 1: Estructures de dades avançades
* Unitat 2: Ús avançat de funcions
* Unitat 3: Fitxers i interacció amb el sistema
* Unitat 4: Optimització: complexitat i profiling
* Unitat 5: Optimització: concurrència i paral·lelisme
* Unitat 6: Testing, manteniment i desplegament d'aplicacions

Cada unitat es troba dins d'una carpeta que porta per nom `unit_x`, on `x` és el número de la unitat. Dins de la carpeta de cada unitat, hi trobareu tant el *notebook* que podeu executar, com una exportació a pdf del contingut del *notebook*. Si es fan servir conjunts de dades per a exemplificar els conceptes explicats a les unitats, també hi trobareu una carpeta `data` que contindrà totes les dades necessàries per a executar el *notebook*.

# 2. Preparació de l'entorn

Per tal d'executar els *notebooks* necessitareu:
* una instal·lació de `python3` amb algunes llibreries addicionals i 
* el programari `jupyter`. 

La màquina virtual que es proporciona en qualsevol de les dues assignatures ja incorpora tot el programari necessari per a executar el contingut d'aquest repositori. Com a alternativa, podeu instal·lar a la vostra màquina el programari seguint les indicacions dels apartats següents.

## 2.1. Instal·lació de python3

Descarregueu i instal·leu `python3` per al vostre sistema operatiu.

Si treballeu en una distribució linux basada en debian, podeu fer:

```
$ sudo apt-get install python3
```

## 2.2. Instal·lació de dependències

Instal·leu les llibreries addicionals necessàries, que es troben especificades al fitxer `requirements.txt` executant des de dins de la carpeta del repositori:

```
$ pip install -r requirements.txt
```

## 2.3. Instal·lació de jupyter

Instal·leu el programari jupyter seguint les indicacions de la [web oficial](https://jupyter.org/install)

# 3. Execució dels notebooks

Una vegada tingueu el programari instal·lat, inicieu jupyter i obriu els *notebooks* amb les activitats:

```
$ jupyter notebook
```

Si utilitzeu la màquina virtual de les assignatures, també podeu iniciar jupyter executant l'*script* `start_uoc`:
```
$ start_uoc.sh
```
