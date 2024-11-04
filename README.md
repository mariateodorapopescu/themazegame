# 👋 Pagina Pornire

# Link-uri utile:

- **Gitlab**: [https://gitlab.cs.pub.ro/mps-2024](https://gitlab.cs.pub.ro/mps-2024/joi_8_echipa1/proiect-mps.git)
- **Teams (MPS)**: https://teams.microsoft.com/l/team/19%3AsdzzSFaRBbEaSr6AZxFiKb0p-LqWTY5dtNA_2Ms52f81%40thread.tacv2/conversations?groupId=bd49bfb0-3625-4311-9b96-f1b04cbe8c97&tenantId=2d8cc8ba-8dda-4334-9e5c-fac2092e9bac

# Resurse:

- **OCW** https://ocw.cs.pub.ro/courses/mps/proiect

# Limbaj/tehnologie:

- **Python3**

# Biblioteci:

- **numpy**

# Instrumente folosite:

- **VSCode**
- **Jira**
- **Discord** 
- **Whatsapp** 

# Metodologie:

- **Scrum** 

# Echipa

- **Project Manager**: @Maria-Teodora Popescu  
  - Responsabilă pentru coordonarea generală a echipei și asigurarea unei bune organizări a proiectului.
  - Monitorizează progresul fiecărei componente, organizează Sprint Planning, Daily Stand-ups, și se asigură că termenele sunt respectate.
  - Gestionează comunicarea între membri și documentația de proiect.

- **Team Lead (Dev1)**: @Alfred Andrei Pietraru  
  - Coordonează echipa tehnică și este responsabil pentru dezvoltarea serverului și implementarea AI-ului agentului, asigurând integrarea corectă a tuturor componentelor.

- **Dev2**: @Andreea Budulan  
  - Dezvoltă generatorul de labirint procedural, implementând logica pentru crearea pereților, căilor și elementelor speciale din labirint.

- **Dev3**: @Alexandra-Claudia Girnita  
  - Se ocupă de dezvoltarea interfeței vizuale (Viewer), sincronizând vizualizarea labirintului și mișcările agenților cu serverul în timp real.

- **Tester 1**: @Delia Rosu  
  - Se concentrează pe testarea interacțiunii dintre server și agenți, asigurându-se că AI-ul și serverul funcționează corect.

- **Tester 2**: @Amalia Stoian  
  - Testează labirintul generat și vizualizarea maze-ului în viewer, verificând că mișcările agenților sunt afișate corect și că labirintul respectă regulile impuse.

---

# Cerința pe scurt - Ce avem de făcut?

## **Introducere**
Acest proiect implică dezvoltarea unui joc competitiv în care mai mulți agenți AI navighează prin labirinturi generate programatic. Echipele dezvoltă atât agenții, cât și serverul care conectează acești agenți. Serverul încarcă labirinturile și acționează ca un vizualizator al jocului.
Scopul este de a determina soluția AI cea mai eficientă prin competiție directă între agenții AI. Agentul AI care iese primul din labirint este declarat câștigător, iar serverul monitorizează condițiile de victorie și acordă puncte corespunzătoare.

## **Generatorul**
- Trebuie să producă o imagine în format 8bpp.
- Trebuie să poată primi aceeași imagine înapoi pentru reproducere.

Fiecare pixel reprezintă o structură specifică din labirint:
- **0**: perete
- **255**: cale
- **64**: intrare
- **182**: ieșire
- Alte valori pentru capcane, portale, plăci speciale.

## **Funcționalități principale**
- **Vizibilitate**: Fiecare jucător poate vedea o zonă de 5×5 în jurul poziției curente, indicând direcțiile de mișcare (N, E, S, W).
- **Mișcare pe rânduri**: Fiecare agent trimite o secvență de până la 10 pași către server. Mișcările nereușite reduc secvențele din următoarele ture.
- **Puncte X-RAY**: Fiecare jucător începe cu 10 puncte X-RAY, care extind vizibilitatea cu n pași (ex. 2 puncte cresc vizibilitatea la 7×7).

## **Tipuri de plăci speciale**:
- **Fog tile**: Limitează vizibilitatea la 3×3.
- **Tower tile**: Oferă o vizibilitate extinsă de 7×7.
- **Capcane**: Multiple tipuri, care fie reduc numărul de pași, fie anulează mișcări anterioare, împing înainte sau înapoi.
- **Portale**: Leagă două puncte din labirint, fiecare portal având un id specific.
- Puncte X-RAY suplimentare pot fi colectate în joc.

## **Serverul**
- Răspunde unei comenzi JSON cu numele comenzii, rezultate de succes/eșec și vizibilitatea în jurul agentului după fiecare mișcare.
- Poate stoca și retrimite labirinturi salvate sub formă de imagini.

## **Viewer-ul**
- **Rezoluție**: 1920×1080, cu 20 pixeli pe fiecare tile.
- **Moduri de vizualizare**: Vizualizare completă a labirintului sau vizualizare limitată la ce a explorat fiecare agent.
- **Funcții adiționale**: Scroll, zoom și moduri de vizualizare a drumurilor parcurse și a pașilor planificați de agenți.
- **Elemente vizuale**: Capcanele vor fi etichetate cu valoarea "n", iar drumul parcurs va fi afișat cu o linie solidă, iar pașii planificați cu o linie punctată.

## **Agenți AI**
- Fiecare agent AI poate funcționa în două moduri:
  - **Real-time**: trimite comenzi și primește rezultate în timp real.
  - **Await input**: trimite comenzi și așteaptă inputul utilizatorului pentru următoarea comandă.
- Performanța agenților va fi evaluată în trei moduri:
  - Timpul minim necesar pentru a rezolva labirintul.
  - Numărul minim de ture.
  - Numărul minim de mișcări.
- **Real-time**: Agenții vor avea un timp limitat pentru a trimite comenzi, iar depășirea acestui timp duce la descalificare.

# Documentatie

## Cerinte
```
getch==1.0
numpy==2.1.2
opencv-python==4.10.0.84
```

## Rulare
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

## Rulare agenti si server
python3 server/server.py
python3 client.py --id 1 --agent astar
python3 client.py --id 1 --agent dfs
```

## CustomThread.py:
in mod normal thread-urile in python nu returneaza niciun tip de date in momentul
in care isi termina executia, cu ajutorul acestei clase, avem thread-uri asemenatoare
cu cele din C, care returneaza tipuri de date.

## server/maze.py:
Se regasesc clasele MazeCell si Maze, Maze este o matrice de celule MazeCell, la inceput
neconectate intre ele. clasa MazeCell este alcatuita din variabila interna value, care indica
ce se afla acolo, si poate lua una din valorile din fisierul constants.py, x si y 
Maze._computeFinalMatrix() -> aici a trebuit sa adaptez putin codul, dar cel mai bine se 
explica printr-un exemplu: sa zicem ca am urmatorul grid de celule:
```
1 2 3 
4 5 6
7 8 9 
```
- SE POATE DEPLASA DOAR PE LINII SI COLOANE ! NUUU DIAGONALA
- parcurgerea din DFS incepe de la celula 1: si merge in felul urmator:
1 -> 4 -> 5 -> 8 -> 7 (in 7 ajunge si vede ca totul in jurul lui e explorat, se 
foloseste de coada si se intoarce inapoi pana la prima celula care mai poate fi explorata, 
adica 9, si gaseste ca poate sa mearga doar inspre 9 si parcurge):
7 <- 8 -> 9 -> 6 -> 3 -> 2 ( a explorat intreaga matrice, si se goleste coada)
in situatia asta nu avem niste path-uri stabilite dar nu avem cum sa le reprezentam 
printr-o matrice in mod clar -> asa ca am creat o matrice de 2 * 3 + 1,
```
0 0 0 0 0 0 0
0 1 0 2 0 3 0
0 0 0 0 0 0 0
0 4 0 5 0 6 0
0 0 0 0 0 0 0
0 7 0 8 0 9 0
0 0 0 0 0 0 0
```
acum in functie de cum sunt conectate celule, vom stabili daca exista drum 255 / sau este zid 0
in parcurgerea dfs de exemplu a fost 1 -> 4, 4 -> 5 deci acele path-uri primesc 255 (initial
voi seta acolo valoarea de 1, ca in self.N / self.W / self.E si dupa fac operatii pe matrici)
```
0 0 0 0 0 0 0
0 1 1 2 1 3 0
0 1 0 0 0 1 0
0 4 1 5 0 6 0
0 0 0 1 0 1 0
0 7 1 8 1 9 0
0 0 0 0 0 0 0
```
dupa se transforma tot ceea ce e mai mare ca zero in 255 
```
0  0   0   0   0   0  0
0 255 255 255 255 255 0
0 255  0   0   0  255 0
0 255 255 255  0  255 0
0  0   0  255  0  255 0
0 255 255 255 255 255 0
0  0   0   0   0   0  0
```
se elimina 0 -urile suplimentare si aceasta este matricea finala 

Good luck! 

## DFSGenerator.py:
creez o matrice de obiecte de tip MatrixCell (in fisierul server/maze.py), iar algoritmul
trece prin fiecare din aceste celule, pana cand le exploreaza pe toate, modul in care 
parcurge aceste celule, indica path-urile posibile pe care va putea merge agentul prin
labirint, cea mai mare problema a fost ca algoritmul se opreste abia in momentul in care 
fiecare MatrixCell a fost explorat, din cauza aceasta a fost nevoie de niste functii 
suplimentare pentru a diferentia intre obiectele de tip MatrixCell prin care a trecut si pe 
cele pe care le-a ignorat in procesul de explorare.
in clasa din DFS_Generator.py in functia carve_maze.py -> se pleaca de la matricea de 
celule, neconectate intre ele, si parcurgandu-se DFS, se leaga celule intre ele.   

---

## Probleme
28-31.10.2024
Adaugare taskuri noi (pentru mai multe detalii, vezi Jira)
- pentru testare -> testarea functiei get_field_of_view() + sugestii imbunatatire 
- Claudia -> A*
- Andreea -> interfata grafica + terminare labirint
- Alfred -> comunicarea server client  + agent

> Intrebare 1

5 * 5 view ce inseamna ? 5 elemente vazute in fiecare directie? sau lungimea view-ului - solved la lab4
```
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * 0 * * * * *
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * * * * * * * 
 * * * * * * * * * * *
```
sau
```
 * * * * *
 * * * * *
 * * 0 * *
 * * * * *
 * * * * *
```

*Raspuns:* a doua varianta, care poate creste la 7x7 sau scadea la 3x3

7x7:
```
 * * * * * * *
 * * * * * * *
 * * * * * * *
 * * * 0 * * *
 * * * * * * *
 * * * * * * *
 * * * * * * *
```

3x3:
```
 * * * 
 * 0 * 
 * * * 
```

> Intrebare 2
- Readme si wiki in engleza sau in romana?
- sunt necesare graficele din lab3 si documentele din lab4?

*Raspuns:* 1. in orice limba, dar sa fie consistent; 2. documente per-se - nu. la grafice, doar daca va ajuta

> Intrebare 3
- Agentul are voie sa memoreze zonele prin care a trecut, reconstruind astfel labirintul?
- Avem voie sa trimitem agentului dimensiunea totala a labirintului, pt alocari de memorie?

*Raspuns:* 1. Da, poti sa memorezi pe unde ai fost, tocmai sa fie mai "rapid" daca este cazul.
2. to be to