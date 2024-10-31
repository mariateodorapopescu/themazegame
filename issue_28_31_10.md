## Alocare taskuri

>>>>>>> 0aa9f8b (adaugare comentarii si info in README)

- pentru testare -> testarea functiei get_field_of_view() + sugestii imbunatatire
- Claudia -> A* + un agent -> DONE
- Andreea -> interfata grafica + terminare labirint -> IN PROGRESS
- Alfred -> comunicarea server client  + agent -> IN PROGRESS
- Maria -> de inceput lucrul la SDD

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

