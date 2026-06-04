# NOTES — [Stoica Paul-Isaac]

Vrem să fie scurt — maxim 1 pagină. Mai mult contează claritatea decât lungimea.

---

## 1. Probleme găsite și fixate

Pentru fiecare problemă, scrie 2-3 propoziții:

### Problemă #1 (docker-compose.yml)
- **Simptom (ce eroare ai văzut?):** Am deschis in browser http://localhost:8000/health si scrie "Can't connect to server" (dupa ce am dat docker compose up) asa ca, am deschis docker-compose.yml file-ul si am gasit o problema la port 8080:8000
- **Cum am diagnosticat-o:** am considerat ce e o problema care trebuie sa rezolv, deoarece in tasks se cere explicit portul 8000 pe localhost. 
- **Cum am fixat-o și de ce:** am schimbat din 8080 in 8000, ca sa pot accesa dupa cum se cerea si in README, asa ca acum portul e expus pe 8000 nu 8080.

### Problemă #2 (main.py)
- **Simptom:** redis:true pe http://localhost:8000/health
- **Cum am diagnosticat-o:** parea totul ok, pana am intrat sa ma uit prin cod, si am gasit in main.py o greseala de logica pentru endpointul health, orice ar fi arata true
- **Cum am fixat-o și de ce:** am schimbat codul astfel incat daca redis trimite eroare se afiseaza pe endpoint.

### Problemă #3 (docker-compose.yml)
- **Simptom:** am gasit eroare cand am vrut sa apelez http://localhost:8000/visits cu: "cannot connect to Error 111 connecting to localhost:6379"
- **Cum am diagnosticat-o:** nu ar trebui sa apeleze localhost6379. Ar fi trebuit sa se apeleze cu numele serviciului. Am vazut si comentariul #redis
- **Cum am fixat-o și de ce:** am schimbat din localhost in redis, deoarece docker compose creeaza o retea interna intre containere, iar serviciul se numeste redis, (lucrul acesta se vede cu cateva randuri mai jos).

### Problemă #4 (CI)
- **Simptom:** in github, la actions am observat ca nu e in regula
- **Cum am diagnosticat-o:** m-am uitat in ci.yml si am citit ce e acolo, si am corelat cu ce imi zicea in actions ca error si warning
- **Cum am fixat-o și de ce:** am schimbat versiunea de python, ca sa fie acceasi in github, ca si cea locala, si cea in care a fost scris codul. 

### Problemă #5 (CI)
- **Simptom:** am gasit 2 warnings in actions
- **Cum am diagnosticat-o:** am cautat in log si am gasit ca versiunile de actions/setuo-python si actions/setup/checkout era depreciate
- **Cum am fixat-o și de ce:** am schimbat in versiunea curenta

### Problemă #5 (main.py)
- **Simptom:** apelarea main.py nu afisa nimic.
- **Cum am diagnosticat-o:** visits_count e gresit
- **Cum am fixat-o și de ce:** am schimbat din requests in r.get("visits") ca si in codul de mai sus, fixand logica


(Adaugă/șterge secțiuni dacă ai găsit mai multe sau mai puține.)

---

## 2. Healthcheck-ul adăugat

- **Cum funcționează:** dupa cele 15 secunde care le-am pus sa astepte pana incepe sa verifice, o sa verifice din 30 in 30 de secunde daca aplicatia e vie si functioneaza, daca nu raspunde de 3 ori la rand in cate 2 secunde, healtcheckul devine "unhealthy". 
- **De ce ai ales configurarea asta (interval, retries, timeout):**  asa am gasit un examplu in documentele oficiale de la git. Am ajustat parametrii incat sa fie cat mai mici dar si responsive si am ajuns la valorile acestea, invervalul fiind destul de rapid incat sa detectez daca serviciul nu mai raspunde, dar timeoutul mic deoarece serviciul e mic si ar trebui sa raspunda foarte rapid. Retries am ales 3 deoarece evita un false negative (daca ar fi fost 1), dar nici mare incat sa ruleze aplicatia mult timp fara sa semnaleze ca e unhealthy

---

## 3. Folosirea AI-ului

Fii cinstit. Nu pierzi puncte dacă spui adevărul, dimpotrivă.

- **Ce ai folosit:** Claude
- **Unde te-a ajutat cel mai mult:** la implementarea healthcheckului, unde m-a atentionat ca versiunea de python 3.11-slim nu are curl, si mi-a sugerat ce sa fac. Dar cel mai important, cand nu imi zicea ca e healthy in urma unui docker compose ps, mi-a sugerat sa sterg cache-ul, lucru la care nu m-am gandit 
- **Unde te-a încurcat sau ți-a dat un răspuns greșit:** (foarte interesant pentru noi!)
- **Cum ai verificat ce-a generat:** ruland codul, verificand eventualele erori

---

## 4. Ce-ai face cu mai mult timp

(Lista scurtă, 3-5 puncte. Arată-ne că ai văzut limitele actuale.)

Idei posibile (nu trebuie să fie toate):
- Securitate (non-root user, secrets management)
- Optimizări de imagine
- Monitoring / logging
- Resilience (retries, circuit breaker)
- Pipeline mai bun (linting, security scan, deploy)

---

## 5. Întrebări / observații

(Orice nu a fost clar, orice ai vrea să discuți cu noi.)
