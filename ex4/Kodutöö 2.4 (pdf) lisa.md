# Sobivad algoritmid täisarvude sorteerimiseks vahemikus 1-100

Insertion Sort, Bubble Sort ja Counting Sort on kolm sorteerimisalgoritmi, mis võiks sobida 1–100 vahemikus olevate täisarvude sorteerimiseks.

# Insertion Sort:

- Kui andmed on juba osaliselt sorteeritud ja ainult mõned elemendid on valel kohal, võib Insertion Sort olla hea valik. Parimal juhul on ajaline keerukus O(n)
- Sobib kui loendi pikkus on lühike ehk sobib väiksematele andmemahtudele

# Bubble Sort:

- Kui täisarvude arv vahemikus 1-100 on väike (loendi pikkus lühike), võib Bubble Sort olla hea valik, kuna töötab väikeste andmemahtude korral piisavalt hästi. Võiks osutuda valituks antud andmete sorteerimiseks, kuna seda on lihtne implementeerida ning sobib kui on vaja stabiilset algoritmi. 

# Counting Sort:

- Kui arvud on vahemikus 1-100, siis Counting Sort algoritmi korral need arvud loendatakse (mitu korda esineb arv 1, 2, 3 jne) ning kasutab seda loendamist, et järjestada andmed sorteeritult. Nõuab arvude loendamiseks täiendavat mälu, aga vahemik 1-100 ei ole probleemiks.
- Counting Sort võiks osutuda eelmainitud algoritmide seast paremaks valikuks, kui arve vahemikus 1-100 on rohkem. Nt ka loendi 1 000 000 puhul võiks Counting Sort toime tulla, kuna peab salvestama endiselt 100 elemendi arvu (loenduse). Kuigi 1 000 000 on tegemist suure andmehulgaga ja võiks kaaluda ka teisi algortime, mis on mõeldud suurte andmemahtude jaoks. Siiski on suure andmehulga puhul Counting Sort parem valik kui Insertion Sort ja Bubble Sort, kuna ajaline keerukus ei ole ruutsõltuvuses. Ajaline keerukus on Counting Sortil kõige halvimal juhul (O(n+k)), seega Counting Sort on parem valik.
- Sobib kui on vaja mittevõrdlevat ja stabiilset algoritmi

Kokkuvõttes tundub, et kui tegemist on väikese loendiga elementidega vahemikus 1-100, siis võib lihtsam olla implementeerida Insertion Sorti või Bubble Sorti, kui aga loend on pikk, tuleks kaaluda Counting Sort kasuks.
