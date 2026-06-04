# NOTES — Stoica Paul-Isaac

---

## 1. Probleme găsite și fixate

### Problemă #1 (docker-compose.yml)
- **Simptom (ce eroare ai văzut?):** Am deschis în browser http://localhost:8000/health și scria "Can't connect to server" (după ce am dat docker compose up), așa că am deschis fișierul docker-compose.yml și am găsit o problemă la porturi (8080:8000).
- **Cum am diagnosticat-o:** Am considerat că e o problemă pe care trebuie să o rezolv, deoarece în tasks se cere explicit portul 8000 pe localhost. Claude mi-a confirmat, explicând de ce am acea eroare și ajutându-mă să înțeleg complet.
- **Cum am fixat-o și de ce:** Am schimbat din 8080 în 8000, ca să pot accesa 8000/health după cum se cerea și în README, astfel portul e expus pe 8000, nu pe 8080.

### Problemă #2 (main.py)
- **Simptom:** redis era true pe http://localhost:8000/health indiferent de starea actuala a redis-ului.
- **Cum am diagnosticat-o:** Părea totul ok, până am intrat să mă uit prin cod și am găsit în main.py o greșeală de logică pentru endpoint-ul health — orice s-ar întâmpla, afișa true.
- **Cum am fixat-o și de ce:** Am schimbat codul astfel încât dacă Redis trimite eroare, se afișează false pe endpoint.

### Problemă #3 (docker-compose.yml)
- **Simptom:** Am găsit eroare când am vrut să apelez http://localhost:8000/visits cu: "cannot connect to Error 111 connecting to localhost:6379".
- **Cum am diagnosticat-o:** Am consultat Claude, care mi-a explicat că nu ar trebui să apeleze localhost:6379, deoarece redis e un serviciu de sine stătător. Ar fi trebuit să se apeleze cu numele serviciului. Am văzut și comentariul #redis care m-a ajutat.
- **Cum am fixat-o și de ce:** Am schimbat din localhost în redis, deoarece Docker Compose creează o rețea internă între containere, iar serviciul se numește redis (lucrul acesta se vedea cu câteva rânduri mai jos în fișier).

### Problemă #4 (CI)
- **Simptom:** În GitHub, la Actions am observat că nu e în regulă, deoarece aveam erori.
- **Cum am diagnosticat-o:** M-am uitat în ci.yml și am citit ce e acolo, corelând cu ce îmi zicea în Actions ca eroare, unde scria explicit ce schimbări să fac și unde.
- **Cum am fixat-o și de ce:** Am schimbat versiunea de Python ca să fie aceeași în GitHub ca și cea locală și cea în care a fost scris codul.

### Problemă #5 (CI)
- **Simptom:** Am găsit 2 warnings în Actions.
- **Cum am diagnosticat-o:** Am căutat în log și am găsit că versiunile de actions/setup-python și actions/checkout erau depreciate, lucruri scrise explicit în log.
- **Cum am fixat-o și de ce:** Am schimbat la versiunea curentă, după un research rapid.

### Problemă #6 (main.py)
- **Simptom:** Apelarea /index nu afișa niciun număr.
- **Cum am diagnosticat-o:** Logica implementării visits_count era greșită.
- **Cum am fixat-o și de ce:** Am schimbat din requests în visits()["visits"] ca să obțin datele din endpoint-ul /visits declarat mai sus, fixând logica și respectând principiul DRY.

---

## 2. Healthcheck-ul adăugat

- **Cum funcționează:** Se va verifica din 30 în 30 de secunde dacă aplicația e vie și funcționează. Dacă nu răspunde de 3 ori la rând în câte 2 secunde, healthcheck-ul devine "unhealthy".
- **De ce ai ales configurarea asta (interval, retries, timeout):** Am găsit un exemplu în documentația oficială Docker. Am ajustat parametrii să fie cât mai mici, dar și responsive. Intervalul e destul de rapid încât să detectez dacă serviciul nu mai răspunde, timeout-ul e mic deoarece serviciul e simplu și ar trebui să răspundă foarte rapid. Retries am ales 3 deoarece evită un fals negativ (dacă ar fi fost 1), dar nici atât de mare încât aplicația să ruleze mult timp fără să semnaleze că e unhealthy.

---

## 3. Folosirea AI-ului

- **Ce ai folosit:** Claude(Sonet 4.6 low) și Gemini(3.1 Pro)
- **Unde te-a ajutat cel mai mult:** La implementarea healthcheck-ului, unde m-a atenționat că imaginea python:3.11-slim nu are curl instalat și mi-a sugerat ce să fac. Dar cel mai important, când nu îmi arăta healthy în urma unui docker compose ps, mi-a sugerat să șterg cache-ul, lucru la care nu m-am gândit.
- **Unde te-a încurcat sau ți-a dat un răspuns greșit:** Nu a ținut cont de principii de programare precum DRY, a prioritizat livrarea unui răspuns rapid în loc de corectitudine și explicații clare.
- **Cum ai verificat ce-a generat:** Rulând codul, verificând eventualele erori și citind log-urile — acest lucru m-a ajutat mult.

---

## 4. Ce-ai face cu mai mult timp

- Implementarea unui UI mai frumos
- Teste complete
- Securitate
- Implementarea HTTPS
- Orchestrare (Kubernetes)
- Monitoring (LGTM stack)

---

## 5. Întrebări / observații

- Apelarea http://localhost:8000/index returnează că pagina a fost vizitată cel puțin o dată, nu începe de la 0. Ar fi trebuit sa fie 0, și doar când se apelează http://localhost:8000/visits să crească?
- Healthcheck-ul folosește curl instalat manual în imagine — e abordarea corectă?
- Care e procesul de onboarding pentru practică, există documentație sau înveți direct din cod?
- Ce ar trebui să știu cel mai bine pentru interviul ce urmează?
- Pe baza codului scris, ce ar face ca eu să nu trec mai departe?