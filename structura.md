# Organizarea proiectului

Acest document explică structura proiectului și oferă detalii despre scopul fiecărui director și fișier, facilitând navigarea și înțelegerea proiectului pentru toți membrii echipei.

---

## Structura Proiectului

```plaintext
PROIECT-MPS/
├── server/
│   ├── proiect/
│   │   ├── bin/                       # Fișiere executabile
│   │   ├── include/                   # Biblioteci și headere incluse
│   │   ├── lib/python3.10/site-packages/
│   │   │   ├── pip/
│   │   │   │   ├── _internal/
│   │   │   │   │   ├── cli/
│   │   │   │   │   ├── commands/
│   │   │   │   │   ├── distributions/
│   │   │   │   │   ├── index/
│   │   │   │   │   ├── locations/
│   │   │   │   │   ├── metadata/
│   │   │   │   │   ├── models/
│   │   │   │   │   ├── network/
│   │   │   │   │   ├── operations/
│   │   │   │   │   ├── req/
│   │   │   │   │   ├── resolution/
│   │   │   │   │   ├── utils/
│   │   │   │   │   └── vcs/
│   │   │   ├── _vendor/               # Pachete de terță parte folosite de pip
│   │   │   ├── pip-22.0.2.dist-info/  # Informații despre versiunea pip
│   │   │   ├── setuptools/            # Unelte pentru configurarea pachetelor
│   │   │   └── setuptools-59.6.0.dist-info/
│   ├── CustomThread.py                # Modul pentru implementarea unui thread personalizat
│   ├── DFSGenerator.py                # Generator de labirint bazat pe algoritmul DFS
│   ├── maze.py                        # Logica labirintului
│   ├── server.py                      # Logica serverului
├── .gitignore                         # Fișiere și directoare de ignorat în Git
├── agent_astar.py                     # Implementare agent A* pentru căutarea căii
├── agent_dfs.py                       # Implementare agent DFS pentru căutarea căii
├── agent.py                           # Modulul de bază pentru agenți
├── client.py                          # Logica clientului pentru comunicarea cu serverul
├── constants.py                       # Constante globale utilizate în proiect
├── da.png                             # Imagini sau resurse media pentru proiect
├── README.md                          # Documentația proiectului
├── requirements.txt                   # Pachetele și dependențele necesare proiectului
```

---

## Descrierea Structurii

### 1. `server/`
Directorul principal al proiectului. Conține subdirectoare și fișiere necesare pentru rularea serverului și a componentelor sale.

#### `server/proiect/`
Directorul principal al aplicației, organizat cu următoarele subfoldere:

- **`bin/`**: Conține fișiere executabile pentru rularea proiectului.
- **`include/`**: Include biblioteci și headere necesare proiectului.
- **`lib/python3.10/site-packages/`**: Depozitul de pachete Python instalate.

##### `lib/python3.10/site-packages/pip/`
Acest director conține fișierele și modulele interne ale `pip`, utilizate pentru gestionarea pachetelor Python.

- **`_internal/`**: Conține submodulele interne ale `pip`, utilizate pentru funcționalități precum operațiuni de rețea, distribuții și modele.

- **`_vendor/`**: Depozit pentru pachete de terță parte utilizate de `pip`.

---

### 2. Fișiere Python Importante

- **`CustomThread.py`**: Modul care definește un thread personalizat, utilizat probabil pentru a gestiona operațiuni în paralel sau pentru a îmbunătăți performanța proiectului.

- **`DFSGenerator.py`**: Implementarea unui generator de labirint folosind algoritmul DFS (Depth-First Search), care generează labirinturi pe baza principiilor DFS.

- **`maze.py`**: Modulul principal pentru logica labirintului. Acesta gestionează aspectele legate de structura și funcționalitatea labirintului.

- **`server.py`**: Conține codul necesar pentru a rula serverul, care va coordona și gestiona comunicarea cu clienții.

- **`agent_astar.py`**: Modul pentru agentul care utilizează algoritmul A* pentru a găsi calea optimă în labirint.

- **`agent_dfs.py`**: Modul pentru agentul care utilizează algoritmul DFS pentru explorarea labirintului.

- **`agent.py`**: Modul de bază pentru agenți. Este posibil ca acest modul să definească funcționalitățile comune pentru `agent_astar.py` și `agent_dfs.py`.

- **`client.py`**: Codul necesar pentru a rula clientul, care se va conecta la server și va interacționa cu acesta.

- **`constants.py`**: Definirea constantelor globale utilizate în proiect, pentru a evita „magic numbers” și a îmbunătăți claritatea codului.

---

### 3. Alte Fișiere și Directoare

- **`.gitignore`**: Specifică fișierele și directoarele care trebuie ignorate în controlul versiunilor Git. De exemplu, directoare temporare (`__pycache__`) și fișiere de configurare locale.

- **`da.png`**: Un fișier de imagine. Acesta poate conține un logo, o schemă sau un element vizual necesar proiectului.

- **`README.md`**: Documentația proiectului, care oferă o prezentare generală a structurii și instrucțiuni de utilizare.

- **`requirements.txt`**: Fișier care conține o listă de pachete și versiuni necesare pentru proiect. Acesta poate fi folosit pentru instalarea rapidă a dependențelor prin `pip install -r requirements.txt`.

---

## Cum să Contribuiți

1. **Crearea unui Branch**: Lucrați pe un branch separat pentru fiecare funcționalitate sau remediere de eroare.
   
2. **Respectarea Stilului de Codare**: Asigurați-vă că urmați [Ghidul de Stil pentru Codare](#) pentru a păstra consistența codului.

3. **Commit-uri Frecvente și Descriptive**: Faceți commit-uri frecvente cu mesaje descriptive, care să reflecte modificările realizate.

4. **Testare**: Testați codul înainte de a face un pull request și asigurați-vă că nu introduceti erori noi.

5. **Revizuire Peer**: Încurajăm revizuirea codului între colegi pentru a îmbunătăți calitatea și a asigura respectarea standardelor.

---

## Instalare

Pentru a instala toate dependențele necesare, folosiți următoarea comandă:

```bash
pip install -r requirements.txt # de testat =))
```