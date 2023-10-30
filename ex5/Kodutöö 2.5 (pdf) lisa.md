# Stabiilsed algoritmid:

## 1. Bubble Sort

Kuna vahetab numbrite järjekorda ainult siis, kui indeksil i olev element on suurem kui indeksil i+1 olev element. Kui elemendid on võrdsed, siis ei muuda järjekorda.

### Näide:

Loend [5, 5, 2, 3, 1]. Võrdlus esimese elemendi (5) ja teise elemendiga (5): Kuna need elemendid on võrdsed, ei toimu vahetust ning loend jääb samaks: [5, 5, 2, 3, 1].

## 2. Insertion Sort

Kui element, mida hakatakse võrdlema sorteeritud osaga, on võrdne eelmise elemendiga, jääb element samale kohale, ning midagi ei pea muutma. 

### Näide:

Loend [2, 3, 5, 5, 2] ([2, 3, 5] - sorteeritud [5, 2] - sorteerimata). Võrdleme elementi 5 eelmise elemendiga (5). Kuna 5 ja 5 on võrdsed, ei pea midagi muutma.



# Adaptiivsed algoritmid:

Kui andmed on juba sorteeritud, siis algoritm ei muuda elementide järjestus. 

## 1. Bubble Sort

Kuna vahetab numbrite järjekorda ainult siis, kui indeksil i olev element on suurem kui indeksil i+1 olev element.

### Näide:

Loend [4, 2, 7, 1, 5]. 
Võrdlus esimese elemendi (4) ja teise elemendiga (2): Kuna 4 on suurem kui 2, vahetatakse nende positsioon ja loend näeb välja järgmine: [2, 4, 7, 1, 5].

Seejärel võrdleb Bubble Sort järgmise elemendi (4) ja selle järel oleva elemendiga (7): Kuna 4 on väiksem kui 7, ei toimu vahetust ning loend jääb samaks: [2, 4, 7, 1, 5]

## 2. Insertion Sort

Asendab elemente ainult siis, kui üks elementidest on suurem kui teine. Kui element, mida hakatakse sorteeritud osaga võrdlema on suurem kui eelmine element, siis ei pea midagi muutma ning element jääb oma kohale. 

### Näide:

Loend [2, 5, 9, 3, 6] ([2, 5] - sorteeritud [9, 3, 6] - sorteerimata). Võrdleme elementi 9 eelmise elemendiga (5). Kuna 9 on suurem kui 5, ei pea midagi muutma.