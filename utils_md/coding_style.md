# Ghid Coding Style

Acest ghid oferă standarde de codare și cele mai bune practici pentru a menține consistența și lizibilitatea codului în cadrul proiectului nostru. Respectând aceste reguli, codul va fi mai ușor de citit, înțeles și întreținut, mai ales pe măsură ce echipa noastră crește și evoluează.

---

## Cuprins

1. [Principii Generale](#principii-generale)
2. [Organizarea Fișierelor](#organizarea-fișierelor)
3. [Convenții de Denumire](#convenții-de-denumire)
4. [Indentare și Spațiere](#indentare-și-spațiere)
5. [Comentarii și Documentație](#comentarii-și-documentație)
6. [Structura și Fluxul Codului](#structura-și-fluxul-codului)
7. [Gestionarea Erorilor](#gestionarea-erorilor)
8. [Cele Mai Bune Practici](#cele-mai-bune-practici)
9. [Unelte și Formatare](#unelte-și-formatare)

---

## 1. Principii Generale

- **Consistența este cheia**: Păstrați același stil de codare pe tot parcursul proiectului.
- **Lizibilitate pe primul loc**: Scrieți cod care este ușor de citit și înțeles. Evitați soluțiile „deștepte”, dar greu de înțeles.
- **DRY (Don’t Repeat Yourself)**: Reutilizați codul ori de câte ori este posibil pentru a evita redundanțele.
- **Modular și de sine stătător**: Funcțiile și clasele ar trebui să fie de sine stătătoare și să aibă o responsabilitate clară.

---

## 2. Organizarea Fișierelor

- **Nume de Fișiere**: Folosiți nume descriptive, cu litere mici și despărțite prin cratimă (ex.: `procesor-date.py`).
- **Structura Folderelor**: Organizați fișierele într-o manieră logică. Puneți codul aferent în același director și separați diferitele componente (ex.: `modele`, `controlere`, `vizualizări`, `teste`).
- **Fișiere de Dimensiuni Reduse**: Limitați dimensiunea fiecărui fișier la 500 de linii sau mai puțin. Dacă un fișier devine prea mare, luați în considerare împărțirea acestuia în module mai mici.

---

## 3. Convenții de Denumire

- **Variabile și Funcții**:
  - Folosiți `snake_case` pentru denumirea variabilelor și a funcțiilor (ex.: `calculeaza_arie`, `input_utilizator`).
  - Numele ar trebui să fie descriptive și să reflecte scopul variabilei sau al funcției.

- **Clase**:
  - Folosiți `PascalCase` pentru denumirea claselor (ex.: `ProfilUtilizator`, `AnalizatorDate`).

- **Constante**:
  - Folosiți `UPPERCASE_SNAKE_CASE` pentru constante (ex.: `MAX_RETRIES`, `API_ENDPOINT`).

- **Variabile Boolean**:
  - Începeți numele variabilelor boolean cu `este`, `are` sau `poate` (ex.: `este_activ`, `are_erori`).

---

## 4. Indentare și Spațiere

- **Indentare**:
  - Folosiți **4 spații** pentru fiecare nivel de indentare.
  - Evitați tab-urile pentru a asigura formatarea consistentă în diferite editoare.

- **Lungimea Liniei**:
  - Limitați lungimea fiecărei linii la **80 de caractere**. Dacă este necesar, împărțiți linia pe mai multe rânduri.

- **Linii Libere**:
  - Folosiți linii libere pentru a separa secțiunile logice ale codului.
  - Puneți o linie liberă între funcții și clase și două linii libere între secțiunile principale de cod.

---

## 5. Comentarii și Documentație

- **Comentarii Inline**:
  - Puneți comentariile inline pe o linie nouă deasupra codului pe care îl descriu.
  - Păstrați comentariile concise, dar semnificative, explicând *de ce* mai degrabă decât *ce* face codul (ex.: `# Transformă input-ul utilizatorului în litere mici pentru consistență`).

- **Documentația Funcțiilor și a Claselor**:
  - Documentați fiecare funcție și clasă folosind docstring-uri.
  - Folosiți următorul format pentru docstring-urile funcțiilor:

    ```python
    def calculeaza_arie(raza):
        """
        Calculează aria unui cerc dată de raza acestuia.

        Parametri:
            raza (float): Raza cercului.

        Returnează:
            float: Aria cercului.
        """
    ```

- **Comentarii TODO**:
  - Folosiți `# TODO` pentru sarcinile care trebuie finalizate ulterior și includeți inițialele voastre și data (ex.: `# TODO: Refactorizați această funcție - ABC 2023-10-15`).

---

## 6. Structura și Fluxul Codului

- **Lungimea Funcțiilor**:
  - Mențineți funcțiile scurte (de preferință sub 15 linii). Dacă o funcție devine prea lungă, luați în considerare divizarea acesteia.

- **Principiul Responsabilității Unice**:
  - Fiecare funcție și clasă ar trebui să aibă o singură responsabilitate. Evitați funcțiile cu multiple scopuri.

- **Evitarea Codului Încapsulat (Nested)**:
  - Evitați codul profund încapsulat (ex.: evitarea utilizării multiplelor declarații `if` sau `for` imbricate).
  - Folosiți clauze de protecție (early returns) pentru a trata cazurile excepționale la început, reducând astfel nivelul de indentare.

---

## 7. Gestionarea Erorilor

- **Utilizați Excepții**:
  - Utilizați excepții pentru a gestiona erorile și evitați ignorarea lor.
  
- **Mesaje de Eroare Descriptive**:
  - Când ridicați excepții, includeți mesaje de eroare descriptive.

- **Blocuri Try-Except**:
  - Limitați codul din interiorul blocurilor `try-except` la instrucțiunile specifice care ar putea eșua.
  - Specificați întotdeauna tipul excepției (ex.: `except ValueError:` în loc de `except:`).

---

## 8. Cele Mai Bune Practici

- **Evitarea Numerelor Magice**:
  - Evitați codificarea numerică directă în cod. Utilizați constante cu nume descriptive.

- **Evitarea Variabilelor Globale**:
  - Minimizați utilizarea variabilelor globale. Transmiteți variabilele explicit între funcții.

- **Date Imutabile**:
  - Utilizați structuri de date imutabile (cum ar fi tuplurile) ori de câte ori este posibil pentru a evita efectele secundare neașteptate.

- **Testare**:
  - Scrieți teste unitare pentru funcțiile și clasele critice.
  - Cazurile de testare trebuie să fie independente și să nu se bazeze pe rezultatul altor teste.

---

## 9. Unelte și Formatare

- **Formatare Automată a Codului**:
  - Utilizați un formator de cod, cum ar fi [Black](https://black.readthedocs.io/en/stable/), pentru a asigura o formatare consistentă automat.

- **Linters**:
  - Utilizați [Flake8](https://flake8.pycqa.org/en/latest/) sau [Pylint](https://pylint.pycqa.org/) pentru linting, pentru a detecta erorile potențiale și pentru a impune standardele de codare.

- **Controlul Versiunilor**:
  - Faceți commit-uri frecvente și logice cu mesaje de commit descriptive.
  - Urmați convenția de denumire a branch-urilor `feature/descriere`, `bugfix/descriere` sau `hotfix/descriere`.

---

## Exemplu de Cod

Iată un exemplu de cod care respectă regulile de mai sus:

```python
# Constante
MAX_RETRIES = 3
API_ENDPOINT = "https://api.exemplu.com/date"

class ProcesatorDate:
    """
    Procesează datele preluate de la un API extern și le

 formatează pentru analiză.
    """

    def __init__(self, cheie_api):
        """
        Inițializează ProcesatorDate cu cheia API furnizată.

        Parametri:
            cheie_api (str): Cheia API pentru autentificare.
        """
        self.cheie_api = cheie_api

    def preia_date(self):
        """
        Preia date de la API-ul extern, cu opțiuni de reîncercare.

        Returnează:
            dict: Datele JSON de la API.
        """
        for incercare in range(MAX_RETRIES):
            try:
                raspuns = requests.get(API_ENDPOINT, headers={"Authorization": f"Bearer {self.cheie_api}"})
                raspuns.raise_for_status()
                return raspuns.json()
            except requests.RequestException as e:
                print(f"Încercarea {incercare + 1} a eșuat: {e}")
        return None
```