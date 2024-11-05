# **Determinarea Statusului Proiectului la 05.11.2024**

## **1. Descrierea activităților și progresul realizat până la data de 05.11.2024:**

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

- **Procent realizat**: Actualizat în funcție de progresul raportat de echipă până la data de 05.11.2024.

## **2. Calculul SPI (Schedule Performance Index):**

Calculăm **EV** pentru 05.11.2024:

\[
EV = (2 \cdot 100 + 1 \cdot 100 + 1 \cdot 100 + 2 \cdot 100 + 5 \cdot 90 + 5 \cdot 70 + 3 \cdot 90 + 3 \cdot 70 + 1 \cdot 100) / 100
\]

Calculăm fiecare valoare:

- **Inițializare și stabilirea obiectivelor**: \(2 \cdot 100 = 200\)
- **Planificare și alocare roluri**: \(1 \cdot 100 = 100\)
- **Configurare tool-uri și canale de comunicare**: \(1 \cdot 100 = 100\)
- **Creare backlog inițial și task-uri**: \(2 \cdot 100 = 200\)
- **Dezvoltare maze generator**: \(5 \cdot 90 = 450\)
- **Dezvoltare viewer**: \(5 \cdot 70 = 350\)
- **Implementare agent A***: \(3 \cdot 90 = 270\)
- **Implementare agent DFS**: \(3 \cdot 70 = 210\)
- **Testare `field_of_view`**: \(1 \cdot 100 = 100\)

Astfel:

\[
EV = 200 + 100 + 100 + 200 + 450 + 350 + 270 + 210 + 100 = 1980
\]
\[
PV = 2300
\]

Calculul final:

\[
SPI = \frac{EV}{PV} = \frac{1980}{2300} \approx 0.86
\]

### **Interpretarea rezultatului SPI**

- **SPI = 0.86**, ceea ce indică o **ușoară întârziere** față de planificare. Proiectul a recuperat puțin din întârziere, dar nu este încă la zi cu planificarea inițială. 

## **Analiză și Recomandări**

1. **Cauzele întârzierii**:
   - **Complexitatea task-urilor**: Componentele principale, cum ar fi viewer-ul și implementarea completă a agenților, sunt încă în progres și necesită optimizare.
   - **Prioritizarea task-urilor critice**: Unele activități esențiale au fost întârziate, dar echipa a făcut progrese semnificative în această săptămână.

2. **Acțiuni corective**:
   - **Revizuirea task-urilor și re-planificare** pentru a ajusta estimările și pentru a ne concentra pe finalizarea viewer-ului și optimizarea agenților.
   - **Identificarea blocajelor și suport suplimentar**, dacă membrii echipei au dificultăți cu anumite componente tehnice.

3. **Monitorizare continuă**:
   - Organizarea unor sesiuni de progres mai frecvente, pentru a ajusta planul și a asigura că proiectul rămâne pe drumul corect.

## **Concluzie**

Cu un **SPI de 0.86**, proiectul este în continuare puțin întârziat, dar recuperarea parțială a întârzierii arată un progres constant. Prin concentrarea pe task-urile rămase și identificarea blocajelor tehnice, proiectul ar putea ajunge la termen conform planificării ajustate.