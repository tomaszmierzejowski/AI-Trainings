# Moduł 4 — Szablon specyfikacji (+ przykład wypełnienia)

Prompt to prośba. Specyfikacja to kontrakt. Używaj tego szablonu do każdego zadania oddawanego agentowi, które ręcznie zajęłoby Ci więcej niż ~30 minut. Reguły stałe, obowiązujące w *każdym* zadaniu (konwencje, strefy zakazane, komendy weryfikacyjne), należą do pliku reguł — działające szablony CLAUDE.md / AGENTS.md / .cursorrules dostajesz osobno.

---

## Szablon

```
# SPEC: <krótki tytuł w trybie rozkazującym>

## Kontekst
<2–5 zdań: czym jest ten system/dokument, dlaczego to zadanie istnieje
teraz, czego agent sam się nie domyśli. Kontekst biznesowy bije
techniczny, jeśli stać Cię tylko na jeden.>

## Cel
<Jedno zdanie. Jeśli potrzebujesz dwóch, masz dwie specyfikacje.>

## Ograniczenia
- <Co NIE może się zmienić (publiczne API, istniejące zachowanie, plik X, ton Y)>
- <Granice technologii / stylu / długości>
- <Reguły danych: co nigdy nie może pojawić się w wyniku>

## Kryteria akceptacji
- [ ] <Testowalne stwierdzenie — sprawdzenie tak/nie, nie „wrażenie">
- [ ] <Dla kodu: „wszystkie istniejące testy przechodzą">
- [ ] <Dla dokumentów: „każde twierdzenie ma odwołanie do źródła">

## Przykłady
<Jedna para wejście→wyjście pokazująca oczekiwany kształt/jakość.
Dla kodu: przykładowe wywołanie i oczekiwana odpowiedź.
Dla dokumentów: 3 linijki tonu/formatu, którego oczekujesz.>

## Poza zakresem
- <Sąsiednia rzecz, którą agent będzie kuszony zrobić — zakazana wprost>
- <Zakres odkładany celowo>

## Weryfikacja
<Dokładna komenda / procedura, którą wynik zostanie sprawdzony.
Jeśli nie umiesz napisać tej linijki, zadanie należy do trudniejszej
ćwiartki macierzy zaufania — dekomponuj, aż będziesz umieć.>
```

---

## Przykład wypełnienia (zadanie dokumentowe, nietechniczne)

```
# SPEC: Kwartalny brief statusowy dla komitetu sterującego

## Kontekst
Kwartalne spotkanie komitetu sterującego programu migracji platformy.
Odbiorcy to nietechniczni dyrektorzy, którzy czytają tylko pierwsze
pół strony. Wejścia: załączone raporty sprintów (6 plików) i eksport
rejestru ryzyk.

## Cel
Jednostronicowy brief statusowy, który dyrektor programu wyśle bez poprawek.

## Ograniczenia
- Maks. 400 słów; zero żargonu; skróty rozwinięte przy pierwszym użyciu.
- Wyłącznie informacje z załączonych wejść — żadnej wiedzy z zewnątrz.
- Żadnych nazwisk w sekcji ryzyk (tylko role).

## Kryteria akceptacji
- [ ] Każda liczba w briefie występuje dosłownie w załączonym wejściu.
- [ ] Werdykt statusu (zielony/żółty/czerwony) pada w linii 1 z powodem.
- [ ] Każde z 3 głównych ryzyk ma: wpływ, rolę właściciela, następny krok, datę.
- [ ] Mieści się na jednej stronie A4 przy 11 pt.

## Przykłady
Styl pierwszego zdania: „Status programu: ŻÓŁTY — próba generalna
migracji danych przesunięta o dwa tygodnie; data startu bez zmian."

## Poza zakresem
- Nie proponuj nowych mitygacji (o tym decyduje komitet).
- Nie streszczaj całego rejestru ryzyk — tylko top 3.

## Weryfikacja
Recenzent sprawdza każdą liczbę z wejściami (przegląd z Modułu 3:
najpierw liczby, daty, nazwiska), potem czyta na głos w niecałe 3 minuty.
```

---

## Instrukcja ćwiczenia (specyfikacja → agent → wymiana)

1. **Pisz** (20 min): wybierz oznaczone zadanie na przykładowej bazie kodu (ścieżka A) albo zadanie dokumentowe (ścieżka B). Wypełnij każdą sekcję — pusta sekcja „Poza zakresem" oznacza, że nie wyobraziłeś/-aś sobie jeszcze porażki.
2. **Uruchom** (15 min): oddaj specyfikację agentowi dosłownie (tryb agenta w Cursorze / Claude). Nie podpowiadaj w trakcie; niech specyfikacja pracuje.
3. **Przejrzyj** (10 min): oceń wynik **wyłącznie względem swoich kryteriów akceptacji** — nie względem gustu. Zanotuj kryteria, które okazały się nietestowalne.
4. **Wymień się** (15 min): zamień specyfikacje w parze i uruchom cudzą. Każde miejsce, gdzie agent zrobił coś technicznie-zgodnego-ale-nie-o-to-chodziło, to niejednoznaczność — spisz ją; ta lista jest lekcją.
5. **Omówienie:** przynieś swoją najlepszą niejednoznaczność: linijkę specyfikacji, co zrobił agent i jednolinijkową poprawkę.
