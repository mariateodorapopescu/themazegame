# 👋 Pagina Pornire

## Link-uri utile:

- **Gitlab**: [https://gitlab.cs.pub.ro/mps-2024](https://gitlab.cs.pub.ro/mps-2024/joi_8_echipa1/proiect-mps.git)
- **Teams (MPS)**: https://teams.microsoft.com/l/team/19%3AsdzzSFaRBbEaSr6AZxFiKb0p-LqWTY5dtNA_2Ms52f81%40thread.tacv2/conversations?groupId=bd49bfb0-3625-4311-9b96-f1b04cbe8c97&tenantId=2d8cc8ba-8dda-4334-9e5c-fac2092e9bac

## Resurse:

- **OCW** https://ocw.cs.pub.ro/courses/mps/proiect

## Limbaj/tehnologie:

- **Python3**

## Biblioteci:

- **numpy**

## Tooluri folosite:

- **VSCode**
- **Jira**
- **Discord** 
- **Whatsapp** 

## Metodologie:

- **Scrum** 

## Echipa

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

## Cerința pe scurt - Ce avem de făcut?

### **Introducere**

Acest proiect implică dezvoltarea unui joc competitiv în care mai mulți agenți AI navighează prin labirinturi generate programatic. Echipele dezvoltă atât agenții, cât și serverul care conectează acești agenți. Serverul încarcă labirinturile și acționează ca un vizualizator al jocului.

Scopul este de a determina soluția AI cea mai eficientă prin competiție directă între agenții AI. Agentul AI care iese primul din labirint este declarat câștigător, iar serverul monitorizează condițiile de victorie și acordă puncte corespunzătoare.

### **Generatorul**

- Trebuie să producă o imagine în format 8bpp.
- Trebuie să poată primi aceeași imagine înapoi pentru reproducere.

Fiecare pixel reprezintă o structură specifică din labirint:
- **0**: perete
- **255**: cale
- **64**: intrare
- **182**: ieșire
- Alte valori pentru capcane, portale, plăci speciale.

### **Funcționalități principale**

- **Vizibilitate**: Fiecare jucător poate vedea o zonă de 5×5 în jurul poziției curente, indicând direcțiile de mișcare (N, E, S, W).
- **Mișcare pe rânduri**: Fiecare agent trimite o secvență de până la 10 pași către server. Mișcările nereușite reduc secvențele din următoarele ture.
- **Puncte X-RAY**: Fiecare jucător începe cu 10 puncte X-RAY, care extind vizibilitatea cu n pași (ex. 2 puncte cresc vizibilitatea la 7×7).

### **Tipuri de plăci speciale**:

- **Fog tile**: Limitează vizibilitatea la 3×3.
- **Tower tile**: Oferă o vizibilitate extinsă de 7×7.
- **Capcane**: Multiple tipuri, care fie reduc numărul de pași, fie anulează mișcări anterioare, împing înainte sau înapoi.
- **Portale**: Leagă două puncte din labirint, fiecare portal având un id specific.

Puncte X-RAY suplimentare pot fi colectate în joc.

---

### **Serverul**

- Răspunde unei comenzi JSON cu numele comenzii, rezultate de succes/eșec și vizibilitatea în jurul agentului după fiecare mișcare.
- Poate stoca și retrimite labirinturi salvate sub formă de imagini.

---

### **Viewer-ul**

- **Rezoluție**: 1920×1080, cu 20 pixeli pe fiecare tile.
- **Moduri de vizualizare**: Vizualizare completă a labirintului sau vizualizare limitată la ce a explorat fiecare agent.
- **Funcții adiționale**: Scroll, zoom și moduri de vizualizare a drumurilor parcurse și a pașilor planificați de agenți.
- **Elemente vizuale**: Capcanele vor fi etichetate cu valoarea "n", iar drumul parcurs va fi afișat cu o linie solidă, iar pașii planificați cu o linie punctată.

---

### **Agenți AI**

- Fiecare agent AI poate funcționa în două moduri:
  - **Real-time**: trimite comenzi și primește rezultate în timp real.
  - **Await input**: trimite comenzi și așteaptă inputul utilizatorului pentru următoarea comandă.
- Performanța agenților va fi evaluată în trei moduri:
  - Timpul minim necesar pentru a rezolva labirintul.
  - Numărul minim de ture.
  - Numărul minim de mișcări.
- **Real-time**: Agenții vor avea un timp limitat pentru a trimite comenzi, iar depășirea acestui timp duce la descalificare.

--

# TODO
- de facut Readme cu setup environment si how to run
