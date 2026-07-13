# Moduł 2 — Pakiet laboratorium: „Jedno prawdziwe zadanie, cztery narzędzia"

**Czas:** ~90 min · **Wymagany wynik:** jeden gotowy do użycia artefakt + ślad promptów, który go wytworzył.
**Reguła danych (przeczytaj na głos przed startem):** żadnych nazw klientów, żadnych prawdziwych danych osobowych w żadnym narzędziu. Fikcyjne zestawy danych są dostarczone; Twoje prawdziwe zadanie musi zostać zanonimizowane, zanim trafi do prompta.

---

## Ścieżka A — Techniczna (Cursor + Claude)

**Przygotowanie:** dostarczona próbka kodu legacy (trener: użyj ponownie repo discovery-sample; sprawdź tydzień wcześniej, że otwiera się w Cursorze na służbowym laptopie z restrykcjami).

**Twoje zadanie (wybierz jedno albo przynieś własne):**
1. Odpowiedz, używając wyłącznie Q&A po bazie kodu (bez ręcznego grepa): „Co dzieje się od początku do końca, gdy użytkownik wysyła główny formularz?" Wynik: jednostronicowy opis przepływu z odwołaniami do plików.
2. Znajdź i opisz trzy najbardziej ryzykowne obszary bazy kodu (brak testów, wysokie sprzężenie, martwa konfiguracja). Wynik: mini-rejestr ryzyk.
3. Wprowadź jedną zakresowaną zmianę (trener oznacza kandydatów w repo) — a potem napisz opis PR-a z Claude.

**Wymagane zachowania (oceniamy je, nie wynik):**
- Q&A po bazie kodu *przed* jakąkolwiek edycją.
- R·Z·F w każdym prompcie (Rola, Zadanie, Format).
- Reguła smyczy: przegląd każdego fragmentu każdej zmiany.
- Co najmniej jedna runda doprecyzowania — iteruj, nie generuj od nowa.

## Ścieżka B — Nietechniczna (NotebookLM + Claude/Gemini)

**Przygotowanie:** dostarczony pakiet dokumentów źródłowych (trener: 4–6 fikcyjnych dokumentów — polityka, dwa raporty z celową sprzecznością między nimi, transkrypt spotkania, eksport arkusza).

**Twoje zadanie (wybierz jedno albo przynieś własne):**
1. Zbuduj notatnik z pakietu i przygotuj jednostronicowy brief zarządczy odpowiadający na pytanie: „W czym te źródła się zgadzają, gdzie są sprzeczne i czego brakuje?" Każde twierdzenie z cytowaniem.
2. Zamień transkrypt spotkania na dziennik decyzji + listę działań + otwarte ryzyka (Claude, prompt R·Z·F), a potem zweryfikuj nazwiska/liczby/daty z transkryptem.
3. Wygeneruj przegląd audio pakietu; posłuchaj 3 minut; zapisz jedną rzecz, którą subtelnie przekręcił albo przecenił. (To zarazem zapowiedź Modułu 3.)

**Wymagane zachowania:**
- Źródła wgrane, zanim padną pytania — żadnego czatu „na sucho".
- Kliknij co najmniej trzy cytowania do fragmentu źródła.
- Jedna runda doprecyzowania finalnego artefaktu.

## Reguły zadania własnego (obie ścieżki)
Zadanie musi być: (a) prawdziwe — z Twojego faktycznego backlogu; (b) Twoje — to Ty odpowiadasz za wynik; (c) domykalne do *jednego artefaktu* w 90 minut. Zanonimizuj przed startem.

**Zadania zapasowe** (dla osób z pustymi rękami): szkic opisu stanowiska; zamiana dostarczonego claims.csv na podsumowanie QBR; jednostronicowy onboarding z dostarczonego onboarding.csv; e-mail statusowy z fikcyjnego transkryptu; opisz jeden proces zespołowy, który znasz na pamięć, i pozwól AI przepytać luki.

## Przygotowanie do omówienia (ostatnie 10 min laboratorium)
Wypełnij i przygotuj do pokazania:
1. Zadanie, w jednym zdaniu.
2. Twój pierwszy prompt (dosłownie).
3. Doprecyzowanie, które zrobiło największą różnicę (dosłownie).
4. Artefakt.
5. Jedna rzecz, którą musiałeś/-aś poprawić — i jak ją wyłapałeś/-aś.
