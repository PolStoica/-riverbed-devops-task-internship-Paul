# NOTES — [Stoica Paul-Isaac]

Vrem să fie scurt — maxim 1 pagină. Mai mult contează claritatea decât lungimea.

---

## 1. Probleme găsite și fixate

Pentru fiecare problemă, scrie 2-3 propoziții:

### Problemă #1 (docker-compose.yml)
- **Simptom (ce eroare ai văzut?):** Am deschis in browser http://localhost:8000/health si scrie "Can't connect to server" (dupa ce am dat docker compose up) asa ca, am deschis docker-compose.yml file-ul si am gasit o problema la port 8080:8000
- **Cum am diagnosticat-o:** am considerat ce e o problema care trebuie sa rezolv, deoarece in tasks se cere explicit portul 8000 pe localhost. 
- **Cum am fixat-o și de ce:** am schimbat din 8080 in 8000, ca sa pot accesa dupa cum se cerea si in README, asa ca acum portul e expus pe 8000 nu 8080.

### Problemă #2 (Dockerfile)
- **Simptom:**
- **Cum am diagnosticat-o:**
- **Cum am fixat-o și de ce:**

### Problemă #3 
- **Simptom:**
- **Cum am diagnosticat-o:**
- **Cum am fixat-o și de ce:**

### Problemă #4 (CI)
- **Simptom:**
- **Cum am diagnosticat-o:**
- **Cum am fixat-o și de ce:**

(Adaugă/șterge secțiuni dacă ai găsit mai multe sau mai puține.)

---

## 2. Healthcheck-ul adăugat

- **Cum funcționează:**
- **De ce ai ales configurarea asta (interval, retries, timeout):**

---

## 3. Folosirea AI-ului

Fii cinstit. Nu pierzi puncte dacă spui adevărul, dimpotrivă.

- **Ce ai folosit:** (ChatGPT / Cursor / Copilot / altele)
- **Unde te-a ajutat cel mai mult:**
- **Unde te-a încurcat sau ți-a dat un răspuns greșit:** (foarte interesant pentru noi!)
- **Cum ai verificat ce-a generat:**

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
