---
marp: true
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
---

# Mistrzostwo w Promptingu
## Podejście Inżynieryjne

---

# Fundament: Model RTF

- **Rola (Role)**: Kim jest AI? (np. Senior Architekt)
- **Zadanie (Task)**: Co ma zrobić? (np. Napisz kod)
- **Format (Format)**: Jak ma to wyglądać? (np. JSON)

> "Jeśli masz zapamiętać jedną rzecz, zapamiętaj RTF."

---

# Technika 1: Few-Shot (Uczenie na przykładach)

- Nie tylko mów; **pokaż**.
- Podaj 2-3 przykłady Wejście -> Wyjście.
- Kluczowe dla formatów JSON, SQL lub reguł Pega.

---

# Technika 2: Chain-of-Thought (Łańcuch Myśli)

- Poproś model: **"Myśl krok po kroku"**.
- Wymusza rozumowanie przed udzieleniem odpowiedzi.
- Redukuje błędy logiczne o ponad 40%.

---

# Technika 3: Iteracyjne Udoskonalanie

- Nigdy nie akceptuj pierwszego szkicu.
- **Test "Odmowy"**: "Jeśli brakuje informacji, napisz to."
- Poproś AI o krytykę własnego wyniku.

---

# Zaawansowane: Drabinki i Dekompozycja

- **Drabinka (Laddering)**: Zacznij prosto -> Sprawdź -> Dodaj ograniczenia.
- **Dekompozycja**: Podziel duże zadania (Buduj Aplikację) na małe kroki (Definiuj Dane -> Definiuj Etapy).

---

# Bezpieczeństwo i Nadzór

- **Brak danych osobowych (PII)**: Używaj zamienników jak `[Client_ID]`.
- **Zatwierdzone punkty końcowe**: Nie wklejaj sekretów do publicznych narzędzi.
- Traktuj okno promptu jak publiczny billboard.
