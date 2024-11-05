### **Statusul Proiectului la 05.11.2024, ora 22:30**

Pentru a determina statusul proiectului, actualizăm **SPI (Schedule Performance Index)** pe baza activităților desfășurate până la ora actuală, 05.11.2024.

#### **1. Progresul realizat până acum**

| Activitate                               | Procent realizat | Pondere activitate (efort) |
|------------------------------------------|------------------|----------------------------|
| Inițializare și stabilirea obiectivelor  | 100%            | 2                          |
| Planificare și alocare roluri            | 100%            | 1                          |
| Configurare tool-uri și canale de comunicare | 100%            | 1                          |
| Creare backlog inițial și task-uri       | 100%            | 2                          |
| Dezvoltare maze generator                | 90%             | 5                          |
| Dezvoltare viewer                        | 70%             | 5                          |
| Implementare agent A*                    | 90%             | 3                          |
| Implementare agent DFS                   | 70%             | 3                          |
| Testare inițială a funcției `field_of_view` | 100%            | 1                          |
| Creare thread pentru clasa View          | 0%              | 1                          |
| Implementare comunicare Server-View      | 0%              | 1                          |
| Implementare comunicare View-Server      | 0%              | 1                          |

#### **2. Calculul SPI**

**Valoarea Obținută (EV)** și **Valoarea Planificată (PV)** se calculează astfel:

1. **Calculul EV**:

Continuăm calculul pentru **SPI**:

#### **Calculul EV (Valoare Obținută)**

Calculăm fiecare valoare individual pentru EV:

- **Inițializare și stabilirea obiectivelor**: \(2 \cdot 100 = 200\)
- **Planificare și alocare roluri**: \(1 \cdot 100 = 100\)
- **Configurare tool-uri și canale de comunicare**: \(1 \cdot 100 = 100\)
- **Creare backlog inițial și task-uri**: \(2 \cdot 100 = 200\)
- **Dezvoltare maze generator**: \(5 \cdot 90 = 450\)
- **Dezvoltare viewer**: \(5 \cdot 70 = 350\)
- **Implementare agent A***: \(3 \cdot 90 = 270\)
- **Implementare agent DFS**: \(3 \cdot 70 = 210\)
- **Testare `field_of_view`**: \(1 \cdot 100 = 100\)

Total EV:

\[
EV = 200 + 100 + 100 + 200 + 450 + 350 + 270 + 210 + 100 = 1980
\]

2. **Calculul PV (Valoare Planificată)**:

- **PV** este suma ponderilor activităților la 100%:  
  \[ PV = 2 + 1 + 1 + 2 + 5 + 5 + 3 + 3 + 1 = 23 \cdot 100 = 2300 \]

3. **Calculul SPI**:

\[
SPI = \frac{EV}{PV} = \frac{1980}{2300} \approx 0.86
\]

### **Interpretarea rezultatului SPI la data de 05.11.2024, ora 22:30**

- **SPI = 0.86**, ceea ce indică o **ușoară întârziere față de planificarea inițială**. Echipa este aproape la zi cu activitățile planificate, însă mai sunt câteva task-uri în întârziere care necesită atenție.

### **Analiză și Recomandări**

1. **Identificarea cauzelor întârzierii**:
   - **Complexitatea task-urilor recente**, cum ar fi dezvoltarea viewer-ului și implementarea optimizării agenților AI.
   - **Probleme de merge și conflicte de cod**, care au fost soluționate în timpul întâlnirii neprevăzute, dar au adăugat la timpul necesar pentru progres.

2. **Acțiuni corective**:
   - **Revizuirea și prioritizarea task-urilor rămase**, în special task-urile critice de comunicare între Server și Viewer.
   - **Stabilirea unor reguli clare de Git**, astfel încât conflictele de merge să fie evitate în viitor. Aceste reguli au fost consemnate într-un fișier markdown, realizat în cadrul întâlnirii.

3. **Monitorizare și ajustare continuă**:
   - Continuarea organizării de sesiuni de progress review și ajustarea planului pentru a asigura finalizarea componentelor critice în timp util.

---

### **Concluzie**

Cu un **SPI de 0.86**, proiectul "Escape the Maze" este ușor întârziat, dar echipa a realizat progrese semnificative în rezolvarea conflictelor de cod și în stabilirea regulilor pentru colaborarea pe Git. Prin continuarea prioritizării task-urilor și optimizarea activităților de lucru, proiectul poate ajunge la termen în condiții favorabile.