# Contributing to Escape the Maze Project

Mulțumim pentru interesul de a contribui la proiectul **Escape the Maze**! Acest document descrie regulile și bunele practici pentru contribuțiile la proiect. Vă rugăm să citiți și să respectați aceste instrucțiuni pentru a menține o colaborare eficientă și pentru a minimiza conflictele.

---

# Cuprins
1. Intro
2. Configurare Repository
3. Comenzi utile git
4. Reguli pentru Managementul Versiunilor de Cod
5. Ghid Coding Style

---

# Intro

## Structura și Organizarea Generală

1. **Branch-ul `main`**:
   - `main` este branch-ul central, care conține versiunea stabilă și testată a proiectului.
   - Doar PM-ul și Team Lead-ul au permisiunea de a face merge în `main` pentru a menține stabilitatea codului.

2. **Branch-uri Individuale pentru Dezvoltare**:
   - Fiecare membru al echipei are un branch propriu pentru dezvoltare (ex: `andreea`, `claudia`, `maria` etc.).
   - Fiecare membru își dezvoltă și testează funcționalitățile pe propriul branch.
   - Branch-urile personale sunt sincronizate regulat cu `main` pentru a evita conflictele la momentul Pull Request-urilor.

## Workflow pentru Contribuții

1. **Dezvoltare pe Branch-ul Personal**:
   - Fiecare membru al echipei își dezvoltă și testează funcționalitățile pe branch-ul personal.
   - Fiecare commit trebuie să fie clar și descriptiv, pentru a explica modificările aduse.
   - Asigurați-vă că ați testat funcționalitatea pe branch-ul personal înainte de a solicita un Pull Request.

2. **Notificarea PM-ului și Team Lead-ului**:
   - După ce o funcționalitate este finalizată și testată, notificați PM-ul și Team Lead-ul că sunteți gata pentru revizuire.
   - PM-ul sau Team Lead-ul va crea un Pull Request (PR) din branch-ul vostru personal către `main`.

3. **Pull Request și Revizuirea Codului**:
   - PM-ul și Team Lead-ul vor revizui PR-ul, vor testa funcționalitatea și vor oferi feedback, dacă este necesar.
   - Dacă este nevoie de modificări, acestea trebuie implementate pe branch-ul personal, iar PR-ul va fi actualizat automat.

4. **Aprobarea și Merge-ul**:
   - După ce PR-ul este aprobat, PM-ul sau Team Lead-ul va face merge-ul în `main`.
   - Asigurați-vă că sincronizați branch-ul personal cu `main` după fiecare merge, pentru a rămâne la zi cu ultimele modificări.

5. **Sincronizarea Branch-urilor Personale**:
   - Este recomandat să sincronizați regulat branch-ul personal cu `main` pentru a evita conflicte. Pentru aceasta, folosiți comenzile:
     ```bash
     git checkout <branch-ul personal>
     git fetch origin
     git merge origin/main
     ```
   - Rezolvați conflictele (dacă există) pe branch-ul personal înainte de a solicita un nou PR.

## Convenții de Commit și Mesaje

- Folosiți mesaje de commit clare și concise.
- Exemple de mesaje bune de commit:
  - `Implementare funcționalitate de generare maze`
  - `Optimizare algoritm DFS`
  - `Rezolvare bug la afișarea viewer-ului`
  
## Reguli pentru Testare

1. **Testare locală**:
   - Testați întotdeauna codul pe branch-ul personal înainte de a solicita un Pull Request.
   - Asigurați-vă că funcționalitatea implementată nu introduce erori în proiect.

2. **Testare de integrare pe `main`**:
   - PM-ul și Team Lead-ul vor face testarea finală înainte de merge în `main`.
   - Dacă există conflicte sau erori, acestea trebuie rezolvate înainte de aprobarea PR-ului.

## Reguli de Git pentru a Evita Conflictele

1. **Actualizați branch-urile personale**:
   - Sincronizați regulat branch-urile personale cu `main` pentru a minimiza conflictele.
   - Dacă apar conflicte, le rezolvați pe branch-ul personal înainte de PR.

2. **Colaborați pentru rezolvarea conflictelor**:
   - Dacă întâmpinați dificultăți în rezolvarea unui conflict, anunțați Team Lead-ul pentru asistență.

## Reguli pentru Documentație

- **Documentație de cod**:
  - Asigurați-vă că adăugați comentarii explicative pentru funcționalitățile complexe.
  
- **Actualizarea `README.md` și `CONTRIBUTING.md`**:
  - PM-ul și Team Lead-ul vor actualiza aceste fișiere dacă apar schimbări majore în workflow-ul echipei.

## Contact

Pentru orice întrebări sau probleme, contactați PM-ul sau Team Lead-ul. Mulțumim pentru contribuție și pentru efortul depus în acest proiect!

---

Prin respectarea acestor reguli și bune practici, vom putea menține o structură coerentă și o colaborare eficientă în cadrul echipei. Vă mulțumim pentru implicare și contribuții!

---

# Altele

---

# Configurare Repository

- Acest ghid oferă instrucțiuni pas cu pas pentru configurarea repository-ului local și remote. 
- Urmați acești pași pentru a configura cheile SSH, a genera un token de acces GitLab, a clona repository-ul și a gestiona fluxul de lucru cu Git.

---

## Cerințe Preliminare

Asigurați-vă că aveți instalate următoarele:
- **Git**
- **Python 3** și **pip/pip3**
- **Unelte pentru mediu virtual** (de exemplu, `venv`)
- Dependențe suplimentare (cum ar fi `opencv`, `numpy` dacă este necesar)

---

## 1. Generare Cheie SSH (Dacă Nu a Fost Creată Deja)

Pentru a vă conecta la repository prin SSH, generați o cheie SSH nouă dacă nu aveți deja una:

```
ssh-keygen -t rsa -b 2048
```

Cheia va fi generată implicit în locația `/home/nume_utilizator/.ssh/id_rsa`. Urmați instrucțiunile din terminal pentru a completa procesul de generare.

### Startați SSH Agent și Adăugați Cheia

Inițializați agentul SSH și adăugați cheia SSH generată:

```
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

### Adăugați Cheia SSH în GitLab

1. Afișați cheia publică SSH:
    ```
    cat ~/.ssh/id_rsa.pub
    ```

2. Copiați output-ul și accesați contul dvs. de GitLab:
   - Navigați la **Settings > SSH Keys**.
   - Lipiți cheia publică și salvați-o.

---

## 2. Generare Token de Acces GitLab

Dacă folosiți HTTPS pentru a clona repository-ul, va fi necesar să generați un **token de acces personal** pentru autentificare. Acest token înlocuiește parola pentru accesul securizat la repository.

1. Accesați **GitLab > Settings > Access Tokens**.
2. Generați un nou token cu permisiuni `read_repository` și `write_repository`.
3. Salvați token-ul generat, deoarece va fi necesar pentru clonarea și gestionarea repository-ului prin HTTPS.

> **Notă:** Dacă folosiți SSH, nu este necesar token-ul de acces; autentificarea se face prin cheia SSH.

---

## 3. Clonați Repository-ul

Navigați în directorul unde doriți să clonați repository-ul, apoi folosiți una dintre următoarele comenzi:

- **Clone prin HTTPS** (dacă utilizați token de acces):
    ```
    git clone https://gitlab.cs.pub.ro/mps-2024/joi_8_echipa1/proiect-mps.git
    ```

    La prompt-ul pentru autentificare, introduceți token-ul de acces generat anterior în locul parolei.

- **Clone prin SSH** (recomandat dacă SSH este configurat):
    ```
    git clone git@gitlab.cs.pub.ro:mps-2024/joi_8_echipa1/proiect-mps.git
    ```

---

## 4. Configurarea Mediului Virtual Python

Navigați în directorul proiectului și creați un mediu virtual:

```
cd proiect-mps/
python3 -m venv proiect
```

Activați mediul virtual:
- **Linux/macOS**:
    ```
    source proiect/bin/activate
    ```
- **Windows**:
    ```
    .\proiect\Scripts\activate
    ```

---

## 5. Instalarea Dependențelor Proiectului

Cu mediul virtual activat, instalați dependențele necesare:

```
pip install -r requirements.txt # de testat
```

> **Notă:** Dacă sunt necesare pachete suplimentare, cum ar fi OpenCV sau numpy (sau altele, ca de ce nu?), le puteți instala astfel:
>
> ```
> pip install opencv-python
> ```

## Depanare

- Dacă întâmpinați probleme cu SSH, asigurați-vă că cheia SSH este corect configurată și adăugată la SSH agent.
- Dacă dependențele nu se instalează, verificați dacă lipsesc librării sau pachete de sistem, în special dacă folosiți OpenCV sau MPI.

---

## Note Suplimentare

- Fișierul `.gitignore` este configurat pentru a exclude fișiere inutile, cum ar fi `__pycache__` și directoarele pentru mediul virtual.
- Amintiți-vă să urmați [Ghidul de Stil pentru Codare](#) pentru a asigura consistența codului pe parcursul proiectului.

--- 

## Also, istoric comenezi folosite de mine la configurare repo, poate ajuta ~~
```
cd <undevreisapuiproiectul>
ssh-keygen
vim /home/popi/.ssh/id_rsa.pub
eval $(ssh-agent -s)
ssh-add ~/.ssh/ceva_cheiee
git clone https://gitlab.cs.pub.ro/mps-2024/joi_8_echipa1/proiect-mps.git # la mine nu a mers, este cea de wget
git clone git@gitlab.cs.pub.ro:mps-2024/joi_8_echipa1/proiect-mps.git # este cea de ssh, fail
eval $(ssh-agent -s)
git pull
ls
cd proiect-mps/
ls
git add .
git commit -m "test"
git push
pip install opencv-python
python3 server.py
python3 -m venv proiect
python3 server.py
```

---

# Comenzi utile git

## 1. cum fac sa iau de pe un anumit branch pe branch-ul meu, dar fara sa pierd lucruri pe care le-am commis?
1. **Asigură-te că ești pe branch-ul tău**:
   ```
   git checkout nume_branch
   ```

2. **Actualizează branch-ul `main` de la remote**:
   ```
   git fetch origin main
   ```

3. **Integrează modificările din `main` în branch-ul tău**:
   
   - Folosind `merge`:
     ```
     git merge origin/main
     ```

   - Sau, dacă preferi un istoric liniar, folosește `rebase`:
     ```
     git rebase origin/main
     ```


4. **Rezolvă posibilul conflict**:

   - Git va semnala conflictul în anumite fisiere și va marca în acestea părțile aflate în conflict. Arată astfel:

```diff
     <<<<<<< HEAD
     # versiunea ta din branch-ul de lucru
     =======
     # versiunea din `main`
     >>>>>>> origin/main
```

   - Editează manual acele fisiere pentru a păstra sau combina liniile de cod dorite. După ce ai terminat editarea, salvează fișierul.
  

5. **Marchează conflictul ca rezolvat**:
   ```
   git add <nume fisiere>
   ```

6. **Finalizează merge-ul sau rebase-ul**:
   - Dacă folosești `merge`, fă commit pentru a finaliza:
     ```
     git commit -m "Resolved merge conflict"
     ```

   - Dacă folosești `rebase`, continuă rebase-ul:
     ```
     git rebase --continue
     ```

7. **Push la branch-ul tău** (cu modificările din `main` incluse):
   ```
   git push origin nume_branch
   ```
   sau
    rebase-ul rescrie istoria, deci va fi nevoie de un push forțat:
   ```
   git push origin nume_branch --force
   ```

8. **Creează un Merge Request (MR) pentru a integra branch-ul tău în `main`**:
   - Pe GitLab, in GUI, creează un Merge Request pentru a integra branch-ul tău actualizat în `main`.

9. **Daca iti apare ceva eroare ` ! [rejected]        main -> main (non-fast-forward)`**:
Acest mesaj de eroare indică faptul că branch-ul `main` din repository-ul local este în urmă față de `main` din repository-ul remote de pe GitLab. 

Pentru a rezolva problema, trebuie să aduci modificările recente din `main` de pe remote în branch-ul tău local `main` și apoi să le împingi la GitLab.

9.1. **Asigură-te că ești pe branch-ul `main`**:
   ```
   git checkout main
   ```

9.2. **Adu modificările din remote pe `main` local**:
   ```
   git pull origin main
   ```

   Acest lucru va aduce modificările din `main` de pe GitLab în `main` local. 
   
   Dacă există conflicte, Git îți va semnala fișierele în conflict, iar tu va trebui să le rezolvi manual.

9.3. **Rezolvă conflictele (dacă există)**:
   - vezi pasii 4, 5, 6 de mai sus

9.4. **Împinge branch-ul `main` actualizat la remote**:
   ```
   git push origin main
   ```

---

## 2.cum fac sa dau push numai la anumite **fisiere** pe un branch anume sau pe main?
1. **Schimbă-te pe branch-ul `main`:**
   ```bash
   git checkout main
   ```

2. **Folosește `git checkout` pentru a aduce doar `file6` din `mybranch`:**
   ```bash
   git checkout mybranch -- file6
   ```

   Această comandă va copia doar `file6` din `mybranch` în branch-ul `main` fără să aducă și alte fișiere sau modificări.

3. **Stagiază modificările pentru `file6`:**
   ```bash
   git add file6
   ```

4. **Fă commit pentru `file6` în `main`:**
   ```bash
   git commit -m "Adaug doar file6 din mybranch"
   ```

Acum, `file6` va fi prezent în branch-ul `main` fără să fi adus și alte fișiere sau modificări din `mybranch`. 

Dacă vei vrea mai târziu să integrezi și restul fișierelor din `mybranch`, poți face un merge complet cu comanda:

```bash
git merge mybranch
```

---

## 3. cum fac sa dau push sau commit doar la anumite **commit-uri** pe branch-ul meu/sau pe main?
- Mai pe scurt, fiecare lucru pe care vrei sa-l adaugi sau nu, il faci cate un commit. Cu greu se poate face cherry-pick pe commit-uri (for some reason aici nu merge ca pe github), asa ca dupa ce faci acel commit ii dai push. and so on =)))
- Oricum, aceasta sectiune este in progess, asa ca e posibil sa apara modificari, pe masura ce ma documentez
- mai intai vezi Issue 1 de mai sus, caci, in mare parte, vei avea o eroare care iti zice ca trebuie sa ai la zi cu main-ul
- Pentru a face push și merge doar la anumite modificări și nu la toate, poți utiliza diverse metode Git precum **cherry-picking**, **staging selectiv** și **interactive rebase**.
- Aceste tehnici îți permit să selectezi exact ce modificări să trimiți sau să îmbini în branch-ul de destinație.

### 1. **Staging Selectiv (git add -p)**
Dacă ai mai multe modificări în lucru, dar vrei să faci commit doar la anumite secțiuni dintr-un fișier, poți folosi `git add -p` pentru a stabili selectiv ce modificări să fie incluse într-un commit.

1. **Selectează modificările pentru commit**:
   ```
   git add -p
   ```
- Git îți va afișa blocuri de modificări și îți va permite să alegi pe care să le adaugi la `staging`.

2. **Fă commit**:
   ```
   git commit -m "<mesaj>"
   ```

3. **Push doar la commit-urile selectate**:
   ```
   git push origin branch_name
   ```

### 2. **Cherry-pick**
Dacă ai deja mai multe commit-uri și vrei să selectezi doar anumite commit-uri pentru a le trimite sau a le integra în alt branch, poți folosi `cherry-pick`.

1. **Identifică hash-ul commit-urilor dorite**:
   ```
   git log # sau din GUI =))
   ```

2. **Schimbă branch-ul în cel unde vrei să faci merge**
   ```
   git checkout branch_name
   ```

3. **Aplică commit-urile dorite folosind cherry-pick**:
   ```
   git cherry-pick <commit_hash1> <commit_hash2> # etc
   ```

4. **Fă push la branch-ul destinație**:
   ```
   git push origin branch_name
   ```

### 3. **Rebase Interactiv (git rebase -i)**
Dacă ai mai multe commit-uri în branch-ul tău și vrei să organizezi sau să elimini unele dintre ele înainte de a le împinge, poți folosi `rebase` interactiv.

1. **Pornește un rebase interactiv**:
   ```
   git rebase -i HEAD~N # înlocuiește `N` cu numărul de commit-uri recente pe care vrei să le editezi
   ```
   
2. Git va deschide o listă cu commit-urile, unde le poți marca pe cele pe care vrei să le păstrezi (`pick`) sau să le elimini (`drop`), să le modifici sau să le combini (`squash`).

3. **Finalizează rebase-ul și fă push**:
   ```
   git push origin branch_name --force
   ```

### 4. **Push Selectiv cu Referințe de Commit (forțat)**
Dacă vrei să împingi doar o anumită porțiune din istoria branch-ului, poți specifica explicit intervalul de commit-uri:

```
git push origin <start_commit>:<end_commit> branch_name
```

---

## 4. variatiune 2: cum fac sa dau push sau commit la tot ce e pe branch-ul meu?
- mai intai vezi Issue 1 de mai sus, caci, in mare parte, vei avea o eroare care iti zice ca trebuie sa ai la zi cu main-ul

1. **Asigură-te că branch-ul `main` local este la zi cu remote-ul** (ca să te asiguri că nu vei întâmpina conflicte în momentul integrării):

   ```
   git checkout main          # Comută pe branch-ul `main`
   git pull origin main       # Adu ultimele modificări din `main` de pe GitLab în branch-ul `main` local
   ```

   Dacă apar conflicte, va trebui să le rezolvi. Git îți va arăta fișierele cu probleme și va trebui să editezi și să alegi modificările pe care să le păstrezi. După rezolvarea conflictelor:

   ```
   # Marchez conflictele ca rezolvate și finalizez operațiunea
   git add .                   # Adaug toate modificările rezolvate în staging
   git commit -m "Resolve merge conflicts in main"  # Commit pentru a finaliza integrarea modificărilor
   ```

2. **Push branch-ul `main` actualizat la GitLab**:

   ```
   git push origin main       # Trimite branch-ul `main` actualizat pe remote (GitLab)
   ```

3. **Revenim la branch-ul de lucru și aducem modificările din `main`**:

   ```
   git checkout <nume_branch> # Comută înapoi pe branch-ul tău de lucru (înlocuiește `<nume_branch>` cu numele branch-ului tău)
   git fetch origin main      # Adu modificările noi din `main` remote fără a le integra direct
   git merge origin/main      # Integrează modificările din `main` remote în branch-ul tău de lucru
   ```

4. **Pregătește modificările și dă commit la tot ce ai lucrat pe branch-ul tău**:

   ```
   git add .                  # Adaugă toate modificările (toate fișierele modificate) pentru commit
   git commit -m "<mesaj>"    # Creează un commit cu un mesaj descriptiv (înlocuiește `<mesaj>` cu ce descrie modificările tale)
   ```

5. **Push la branch-ul tău de lucru pentru a salva tot pe remote**:

   ```
   git push origin <nume_branch>  # Trimite branch-ul tău pe GitLab (înlocuiește `<nume_branch>` cu numele branch-ului tău)
   ```

---

## 5. Alte comenzi de baza
**1. Setare și inițializare:**
- Inițializează un director existent ca un repository Git.
   ```
   git init
   ```

- Recuperează un repository complet de la o locație gazduită prin URL.
   ```
   git clone
   ```

**2. Staging și snapshot:**
- Afișează fișierele modificate în directorul de lucru, pregătite pentru următorul commit.
   ```
   git status
   ```

- Adaugă un fișier în starea sa actuală pentru următorul commit (staging).
   ```
   git add [fisier]
   ```

- Scoate un fișier din staging, dar păstrează modificările în directorul de lucru.
   ```
   git reset [fisier]
   ```

- Afișează diferențele din fișierele modificate, dar ne-staged.
   ```
   git diff
   ```

- Afișează diferențele pentru ceea ce este staged, dar încă necomis.
   ```
   git diff --staged
   ```

- Realizează commit la conținutul din staging ca un nou snapshot.
   ```
   git commit -m <mesaj descriptiv>
   ```

**3. Branching și merge:**
- Listează branch-urile. Un `*` va apărea lângă branch-ul activ curent.
   ```
   git branch
   ```

- Creează un nou branch la commit-ul curent.
   ```
   git branch [nume-branch]
   ```

- Afișează istoricul commit-urilor.
   ```
   git log
   ```

- Îmbină istoricul unui branch specificat în cel curent.
   ```
   git merge [branch]
   ```

- Schimbă-te pe un alt branch și adu-l în directorul de lucru.
   ```
   git checkout [branch]
   ```

**4. Inspectare și comparare:**
- Afișează commit-urile din branch-ul A care nu sunt în branch-ul B.
   ```
   git log B..A
   ```

- Afișează diferențele din branch-ul A care nu sunt în branch-ul B.
   ```
   git diff B..A
   ```

- Afișează commit-urile care au modificat un fișier, chiar și în caz de redenumiri.
   ```
   git log --follow <fisier>
   ```

- Afișează un obiect din Git într-un format ușor de citit.
   ```
   git show <SHA>
   ```

**5. Urmărirea modificărilor de fișiere:**
- Versionare pentru ștergerea fișierelor și schimbarea căilor.

- Șterge fișierul din proiect și adaugă ștergerea la staging pentru commit.
   ```
   git rm <fisier>
   ```

- Schimbă calea unui fișier existent și adaugă mutarea în staging.
   ```
   git mv <cale_existentă> <cale_nouă>
   ```

- Afișează toate commit-urile cu indicații despre căile care s-au schimbat.
   ```
   git log --stat -M
   ```

**6. Ignorarea tiparelor:**
- Prevenirea adăugării accidentale a fișierelor în staging sau commit.

- Salvează un fișier cu tiparele dorite în `.gitignore` cu potriviri exacte sau caractere wildcard.
   ```plaintext
   .gitignore
   logs/
   *.notes
   pattern*/
   ```

- Ignorare globală pentru toate repository-urile locale.
   ```
   git config --global core.excludesfile <fisier>
   ```

**7. Partajare și actualizare:**
- Recuperarea actualizărilor dintr-un alt repository și actualizarea repository-ului local.

- Adaugă un URL Git ca alias.
   ```
   git remote add <alias> <url>
   ```

- Preia toate branch-urile din acel remote Git.
   ```
   git fetch <alias>
   ```

- Transmite commit-urile locale dintr-un branch către branch-ul corespunzător din remote.
   ```
   git push <alias> <branch>
   ```

- Îmbină un branch remote în branch-ul curent pentru a-l actualiza.
   ```
   git merge <alias>/<branch>
   ```

- Șterge staging-ul și rescrie directorul de lucru de la un commit specificat.
   ```
   git reset --hard [commit]
   ```

- Preia și îmbină orice commit-uri din branch-ul remote urmărit.
   ```
   git pull
   ```

- Salvează modificările staged și modificate.
   ```
   git rebase
   ```

**8. Rescrierea istoriei:**
- Rescrierea branch-urilor, actualizarea commit-urilor și curățarea istoricului.

- Aplică commit-urile branch-ului curent înainte de unul specificat.
   ```
   git rebase [branch]
   ```

**9. Commit-uri temporare:**
- Stocarea temporară a fișierelor modificate și urmărite pentru a schimba branch-urile.

- Salvează temporar modificările și listează-le.
   ```
   git stash
   ```

- Afișează modificările stocate în ordine.
   ```
   git stash list
   ```

- Elimină modificările din vârful stivei de stash.
   ```
   git stash drop
   ```

- Aplică modificările din vârful stivei de stash în directorul de lucru.
   ```
   git stash pop
   ```

**10. comenzi rapide VSCode:**
### Taste și descrieri ale comenzilor rapide:
- `Ctrl + /` - Comutare comentariu pe linie
- `Alt + ↑ / ↓` - Mută linia în sus/jos
- `Ctrl + Shift + K` - Șterge linia
- `Ctrl + Enter` - Inserează o linie dedesubt
- `Ctrl + ↑ / ↓` - Derulează linia în sus/jos
- `Shift + Alt + ↑ / ↓` - Copiază linia în sus/jos
- `Ctrl + Shift + Enter` - Inserează o linie deasupra
- `Ctrl + G` - Mergi la o anumită linie
- `Ctrl + P` - Mergi la un fișier
- `Ctrl + ,` - Setări utilizator
- `Ctrl + F` - Căutare

### Alte comenzi:
- `Ctrl + H` - Înlocuire
- `Ctrl + L` - Selectează linia curentă
- `Ctrl + .` - Reparație rapidă
- `Ctrl + F4` - Închide fereastra curentă
- `Ctrl + Shift + N` - Fereastră nouă
- `Ctrl + B` - Comutare bara laterală
- `Ctrl + Tab` - Schimbă între tab-urile editorului
- `Ctrl + Shift + E` - Afișează bara laterală Explorer
- `Ctrl + Shift + F` - Căutare în fișiere
- `Ctrl + Shift + H` - Înlocuire în fișiere
- `Ctrl + Shift + T` - Redeschide editorul închis

- Todo

---

## 5. Link-uri utile
- [Git Immersion Tutorial](https://gitimmersion.com/)
- [GitHub Docs - Hello World Guide](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [GitHub Support](https://support.github.com/)
- [GitLab Flow Explanation](https://about.gitlab.com/topics/version-control/what-is-gitlab-flow/)
- [GitHub Flow Guide](https://docs.github.com/en/get-started/using-github/github-flow)

---

# Reguli pentru Managementul Versiunilor de Cod

Pentru a menține consistența codului și a evita conflictele, vă rog să urmați acești pași **înainte de a începe să lucrați** la cod.

---

## 1. Alinierea Versiunii Codului cu Branch-ul `main`

Înainte de a lucra pe branch-ul vostru, asigurați-vă că aveți aceeași versiune de cod cu branch-ul `main`. Pentru a face acest lucru, urmați pașii de mai jos:

```bash
git checkout main
git pull
git checkout <branch-ul vostru>
git merge main
```

> **Notă:** Este posibil să apară conflicte la merge. Vă rugăm să le rezolvați înainte de a continua.

## 2. Realizarea Commit-urilor și Crearea unui Merge Request

După ce ați rezolvat conflictele și ați actualizat branch-ul vostru, executați:

```bash
git push
```

După `push`, creați un **merge request** pentru a integra modificările în branch-ul `main`.

---

## 3. Verificarea Finală După Lucrare

Pentru o siguranță sporită, după ce ați terminat lucrul, repetați procesul de sincronizare a branch-ului vostru cu `main`:

```bash
git checkout main
git pull
git checkout <branch_vostru>
git merge main
```

> **Notă:** Rezolvați din nou conflictele, dacă este cazul, și apoi executați din nou `push`.

---

## 4. Gestionarea Conflictelor și Colaborarea cu Alți Membri

Este posibil ca, în paralel cu voi, să lucreze și alte persoane pe același proiect. Aceasta poate duce la suprapunerea modificărilor, deci fiți pregătiți să rezolvați conflictele și să verificați ce conflicte au apărut pe `main`.

> **NB:** Fiecare membru al echipei este responsabil să treacă prin conflictele existente și să se asigure că rezolvările sunt corecte.

---

Respectând acest flux de lucru, ne asigurăm că toți membrii echipei lucrează pe aceeași bază de cod și evităm problemele care pot apărea din conflictele de versiune.

---

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
