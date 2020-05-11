# LPSkylineBot

El projecte SkylineBot per GEI-LP (edició primavera 2020).. 
L’objectiu general de la pràctica consisteix en desenvolupar un chatbot en Telegram per a la manipulació d’Skylines  mitjançant un compilador a través de Telegram i generant gràfiques i les seves dades.

![Skyline](img/skyline.png)

## Començem

Aquestes instruccions t'ajudaran a executar el projecte en la teva màquina local i testejar-lo.

### Prerequisits

Per realitzar la nostra pròpia gramàtica necessitem tenir instal·lat ANTLR4

A més, es necessiten tenir instalades les següents llibreries de Python:

```
matplotlib -> per graficar dades.
pickle -> per guardar i carregar estructures de dades en binari.
python-telegram-bot -> per interactuar amb Telegram.
```

### Instal·lant...

Per realitzar la instal·lació de [ANTLR4](https://www.antlr.org//):

* [jar file](https://www.antlr.org/download/antlr-4.7.1-complete.jar)
* [Getting started](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

Per realitzar la instal·lació de les llibreries:

```
pip3 install antlr4-python3-runtime
pip3 install matplotlib
pip3 install python-telegram-bot
```

## Execució

Per executar el bot de Telegram, utilitzarem la següent comanda:

```
python3 bot.py
```

### Bot de Telegram

Una vegada executat el programa, cal anar a Telegram i iniciar una conversa amb el Bot.

### Comandes del bot

- `/start` inicia la conversa amb el Bot.

- `/help`  llista totes les comandes possibles del bot amb una breu descripcio

- `/author`  mostra el nom complet de l'autor del projecte i el seu correu electrònic de la facultat.

- `/operacions` mostra tot els tipus d'operacions per crear, assignar i modificar skylines.

- `/lst` mostra els identificadors definits i la seva corresponent àrea.
            
- `/clean` esborra tots els identificadors definits
            
- `/save id` guarda un skyline definit amb el nom id.sky
            
- `/load id` carrega un skyline de l’arxiu id.sky

## Creacions dels skylines

  - Simple: `(xmin, alçada, xmax)` on `xmin` i `xmax` especifiquen la posició d'inici i final a la coordenada horizontal i `alçada` l'alçada de l'edifici.
  
  - Compostos: `[(xmin, alçada, xmax), ...]` permet definir diversos edificis
mitjançant una llista d'edificis simples.

  - Aleatoris: `{n, h, w, xmin, xmax}` construeix `n` edificis, cadascun d'ells amb una alçada aleatòria entre 0 i `h`,
  amb una amplada aleatòria entre 1 i `w`, i una posició d'inici i de final aleatòria entre `xmin` i `xmax`.

### Operacions del bot

  - `skyline + skyline`: unió
  - `skyline * skyline`: intersecció
  - `skyline * N`: replicació `N` vegades de l'skyline
  - `skyline + N`: desplaçament a la dreta de l'skyline `N` posicions
  - `skyline - N`: desplaçament a l'esquerra de l'skyline `N` posicions
  - `- skyline`: retorna l'skyline reflectit
  
### Exemples del funcionament del bot 

##### #Exemple 1: Assignació + Unió + Desplaçament

<img  width="300" src="img/exemple1.gif">


##### #Exemple 2: Creació aleatòria del Skyline definit per {100000,20,3,1,10000} en pocs segons

<img  width="300" src="img/aleatori.gif">


##### #Exemple 3: Intersecció entre tres Skylines
            
<img  width="300" src="img/exemple2.gif">

## Referències

* [Matplotlib](https://matplotlib.org/) - Per gràficar les dades
* [Pickle](https://rometools.github.io/rome/) - Per guardar i carregar estructures de dades en binari.
* [Python-telegram-bot](https://python-telegram-bot.org/) - Per interactuar amb Telegram.

## Autor

* **David Carballo** - *david.carballo@est.fib.upc.edu*

## Enunciat

Aquest projecte s'ha realitzat segons les tasques demanades en l'enunciat de la [pràctica](https://gebakx.github.io/SkylineBot/). 
