Configurare Repository

Acest ghid oferă instrucțiuni pas cu pas pentru configurarea repository-ului local și remote. Urmați acești pași pentru a configura cheile SSH, a genera un token de acces GitLab, a clona repository-ul și a gestiona fluxul de lucru cu Git.

---

# Configurare repo proiect

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

> **Notă:** Dacă sunt necesare pachete suplimentare, cum ar fi OpenCV sau biblioteci MPI, le puteți instala astfel:
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