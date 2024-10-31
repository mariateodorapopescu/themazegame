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

## 2. cum fac sa dau push sau commit doar la anumite lucruri pe branch-ul meu/sau pe main?
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

## 3. variatiune 2: cum fac sa dau push sau commit la tot ce e pe branch-ul meu?
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

## 4. Alte comenzi de baza
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