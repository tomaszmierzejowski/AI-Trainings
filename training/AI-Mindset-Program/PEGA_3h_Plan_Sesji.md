# PEGA (pega.gg) - plan sesji 3 h · [data: za 3 dni od 2026-07-18]

**Deck:** `Decks/PL/PEGA_Sesja_3h.html` (36 slajdów, bez przełącznika ścieżek; slajdy 1, 21 i 36 są ciemne: otwarcie, przerwa, zamknięcie). Slajd 19b (nowy): tabela „kto co dostaje" z konkretnymi narzędziami i kosztami per osoba.
**Cel biznesowy dnia:** sala ma wyjść z poczuciem „to było o NAS” + na stole leży konkretny, nazwany warsztat 2 (slajd 34). Sprzedaje personalizacja i dema, nie pitch.
**Uzupełnia:** `First_Delivery_Runbook_PL.md` (logistyka, plany B, reguły debiutanta - obowiązuje w całości).

---

## Pokrycie ankiety (sprawdzone, każda potrzeba ma adres)

| Potrzeba z ankiety | Kto | Gdzie w sesji |
|---|---|---|
| Prezentacje ofertowe i koncepcje | Rafał T. | Demo 1b (slajd 23) + warsztat 2 „Maszyna ofertowa” |
| Research klientów przed rozmowami | Rafał T. | Demo 1a (slajd 22) + R·Z·F przed/po (14) |
| „Kiedy który model?” | Rafał T. | Mapa narzędzi (17) + drzewo decyzyjne (18) |
| Halucynacje / „głupoty” | Rafał T. | Poszarpana granica (12) + nawyk 60 sekund (27) |
| Plany komunikacji medialnej | Adrian | Demo 2 (24): brief - plan (data·kanał·cel·struktura) |
| Copy bez powtarzalności | Adrian | Demo 2 (24): bank struktur + plik głosu marki |
| „Model zapomina wytyczne” | Adrian | Nawyk 3: stała instrukcja (16) + licencje (19) |
| Faktury i płatności | Rafał R. | Demo 4 (26) + warsztat 2 „Faktury na autopilocie” |
| Wprowadzanie osób do płatności | Rafał R. | tylko warsztat 2 (za mało czasu na sali - powiedz to wprost) |
| Grafika (Firefly/Gemini/NotebookLM) | Maciej | Demo 3 „Brief zamiast telepatii” (25) + Domek (8) + warsztat 2 „Linia graficzna” |
| Niestandaryzowane narzędzia / licencje | wszyscy | Mapa (17), drzewo (18), rekomendacja licencyjna (19) |

## Strategia odpowiedzi na potrzeby z ankiety — ściąga

Główna teza: przy 4-osobowym zespole wąskie gardło to **nawyk i kontekst**, nie model ani automatyzacja.
Droga jest: dobry prompt + płatne konto z projektami, nie multi-agentowa orkiestracja.

### Rekomendacja per osoba

| Kto | Problem z ankiety | Rozwiązanie | Narzędzie | Koszt |
|---|---|---|---|---|
| Adrian | Powtarzalne posty, zły ton, AI gubi wytyczne | Plik głosu marki + bank 12-15 struktur + Projekt ze stałą instrukcją | Claude Pro lub ChatGPT Plus | ~100 zł/mies. |
| Rafał T. | Research klientów, prezentacje, „kiedy który model?" | Perplexity Pro do researchu + Claude Pro do szkieletów ofert | Perplexity Pro + Claude Pro | ~160 zł/mies. |
| Rafał R. | Przepisywanie faktur i danych płatności | Dziś: ChatGPT Plus + upload PDF. Docelowo (warsztat 2): n8n + GPT-4o-mini API, ~0,05 zł/faktura | ChatGPT Plus, potem n8n | ~100 zł/mies. |
| Maciej | Ma narzędzia, brak procesu | Lepsze briefy z asystenta (Demo 3), spójność brief-copy-grafika | Obecne licencje | 0 zł |

### Dlaczego NIE multi-agent (mów to na sali tylko jeśli ktoś pyta)

- Automatyzacja wielomodelowa (np. 2 modele generują → 3. porównuje) ma sens przy >20 postów/tydzień i zespole 10+ osób.
- Przy skali PEGA: ten sam słaby prompt przez 3 modele = 3 przeciętne wyniki. Jeden dobry prompt przez 1 model = świetny wynik.
- Różnorodność treści pochodzi z **banku struktur**, nie z różnych modeli. Prompt: „użyj struktury: historia zawodnika" vs. „użyj struktury: pytanie do społeczności" — to daje różnorodność.
- API ≠ licencja Pro/Plus. Nie da się zautomatyzować interfejsu webowego. Automatyzacja = osobny koszt tokenowy.
- Dla PEGA sensowna automatyzacja to JEDNO miejsce: faktury (warsztat 2, n8n + tani model wizyjny).

### Kalibracja modeli (smart alternative, temat na warsztat 2/3)

Zamiast multi-agenta na co dzień: raz na kwartał weź 3 sample briefs → przepuść przez Claude, GPT, Gemini z identycznym kontekstem → zespół ocenia blind → wybieram najlepszy model dla marki → ten używany na co dzień. Rekalibracja co kwartał.

## Timing (180 min) + bezpieczniki

| Czas | Blok | Slajdy | Bezpiecznik przy poślizgu |
|---|---|---|---|
| 0:00–0:10 | Otwarcie: hak esportowy - ankieta - agenda - zasady gry - kim jestem | 1–5 | nie skracać - tu kupują zaufanie |
| 0:10–0:45 | Mindset: złe pytanie, Domek (historia + slajd), wpadki, LVL 1–4, kolejność, granica | 6–12 | tnij blok Domku do 2 min łącznie; wpadek NIE wycinaj |
| 0:45–1:20 | 3 nawyki + mapa narzędzi PEGA + drzewo + licencje + kto-co-dostaje (19b) | 13–19b | 19b mów max 60s — tabela mówi sama za siebie; licencje skróć do 1 zdania + „szczegóły w mailu” |
| 1:20–1:35 | ☕ Przerwa | 21 | max 15 min, pilnuj powrotu |
| 1:35–2:30 | Cztery dema (intro + 1a/1b + 2 + 3 + 4) | 22–27 | kolejność cięcia: najpierw 1b (opowiedz na slajdzie), potem skróć 3 (grafika) do 3 min; **demo 2 i 4 zostają zawsze** |
| 2:30–2:45 | Weryfikacja + dane wrażliwe + Lidka | 28–30 | Lidkę można opowiedzieć w 60 s. Slajd 27 otwórz własną wpadką (stopka: „ktoś na LinkedIn napisał mi, że brzmię jak bot”) - historia z blizną buduje więcej zaufania niż zasada; nie tłumacz się, jedno zdanie i dalej |
| 2:45–2:55 | Master prompt (WHY·HOW·WHAT) + ćwiczenie (kartki) | 31–32 | **nigdy nie wycinać** - master prompt daje pretekst do maila, ćwiczenie daje pretekst do kontaktu w dniu 30 |
| 2:55–3:00 | Mapa + Data is the key + warsztat 2 + zamknięcie | 33–36 | nie skracać - „Data is the key" max 2 min; to moment sprzedażowy |

Przerwa wypada po ~80 min - zgodnie z regułą „co ~75 min” z runbooka.

## Golden Circle - oś narracji (do głowy, nie na slajd)

Deck już ma tę strukturę; wystarczy ją wypowiedzieć, nic nie przebudowywać:

- **WHY** (slajdy 1, 6, 11, 12): wierzę, że przewaga z AI nie leży w narzędziach, tylko w kolejności pracy i nawykach - jak w esporcie: wygrywa ten, kto lepiej gra, nie ten, kto ma lepszy sprzęt. Zdanie-kotwica do wypowiedzenia przy slajdzie 11: „Nie jestem tu, żeby sprzedać Wam narzędzie. Jestem tu, żeby zmienić kolejność, w jakiej pracujecie.”
- **HOW** (slajdy 13–19): trzy nawyki (R·Z·F, iteruj, stała instrukcja) + mapa ról narzędzi + drzewo decyzyjne + rekomendacja licencyjna. To jest metoda, nie katalog.
- **WHAT** (slajdy 21–26, 30, 32): cztery dema na ich zadaniach, jedno zobowiązanie od poniedziałku, warsztat 2 jako następny krok.

Kolejność decka celowo idzie Why - How - What - jeśli ktoś zapyta „po co nam to”, odpowiedź padła w pierwszych 45 minutach, zanim pojawiło się jakiekolwiek narzędzie.

## Rozkład dem w bloku 1:35–2:30 (55 min)

intro 2 min · 1a research 12 min · 1b oferta 8 min · 2 plan+copy 15 min · 3 grafika 6 min · 4 faktury 10 min - 53 min + luz.

### Demo 1a - research klienta (Rafał T.) · ~12 min
- **Narzędzie: Perplexity Pro** — najlepszy do researchu z cytatami. Lepszy niż jakikolwiek wielomodelowy pipeline, bo robi search + syntezę + źródła w jednym kroku. Zdanie do powiedzenia: „Perplexity robi jedną rzecz lepiej od wszystkich: szuka i podaje źródła. Za ~80 zł miesięcznie masz asystenta, który nigdy nie cytuje z pamięci."
- Klient przykładowy: **publiczna** marka realistyczna dla PEGA (np. duży producent sprzętu gamingowego obecny w PL). Nie używaj prawdziwego prospekta PEGA bez zgody na sali.
- Najpierw prompt „leniwy” (slajd 14, lewa strona) - pokaż miałkość. Potem R·Z·F z obowiązkową kolumną linków. Kliknij 1–2 linki na żywo - weryfikacja u źródła jako odruch, nie wykład.
- Finisz: „Jakie 3 pytania ten klient zada nam na spotkaniu, na które nie mamy dziś dobrej odpowiedzi?” - to zdanie robi największe „aha” u marketingu.

### Demo 1b - szkielet oferty · ~8 min (pierwszy kandydat do cięcia)
- Wejście: wynik z 1a + 3-zdaniowy brief. Prośba: szkielet 10 slajdów z notatkami prelegenta.
- Wtrącenie dla Rafała T. (nowe, 2026-07-20): gdy koncepcja siedzi w głowie eksperta, nie
  zaczynaj od pisania promptu - nagraj 2 minuty mówienia o koncepcji (telefon wystarczy),
  wklej transkrypcję i dopiero każ AI szkicować oraz wyłapać luki. „AI-first nie zawsze znaczy
  prompt-first - czasem pierwszym narzędziem jest dyktafon.” Jedno zdanie, nie osobne demo.
- Obowiązkowo „adwokat kupującego”: „Jesteś dyrektorem marketingu po stronie klienta. Gdzie ta koncepcja traci punkty?”
- NIE generuj gotowego decka w Canvie na żywo (za dużo zmiennych) - forma to ostatni krok, pokaż samo wklejenie szkieletu.

### Demo 2 - plan komunikacji + copy (Adrian) · ~15 min, interaktywne
- Zbuduj **plik głosu marki na żywo, pytając Adriana**: ton (3 przymiotniki), odbiorcy, zakazane frazy, 1–2 posty „po naszemu” (poproś go wcześniej mailem o 2 ulubione posty PEGA).
- Wklej jako instrukcję projektu - jeden brief eventu - **najpierw plan komunikacji** (tabela: data · kanał · cel · struktura - to jego „plany komunikacji medialnej” z ankiety) - potem 2–3 posty z planu, każdy z **jawnie wskazaną inną strukturą z banku**.
- Puenta: powtarzalność = brak wytycznych + darmowe konto bez projektów. Łączy się ze slajdem 19 i z warsztatem 2 (pełny pakiet - celowo niedokończony dziś).
- **Klucz do różnorodności to bank struktur, nie więcej modeli.** Prompt „użyj struktury: historia zawodnika" daje inny post niż „użyj struktury: pytanie do społeczności" — nawet na tym samym modelu. Gdyby ktoś zapytał o puszczanie treści przez kilka AI naraz: „przy 10–20 postach tygodniowo to przerost formy. Jeden dobrze poinstruowany model bije trzy źle poinstruowane."
- Jedno zdanie o artykułach na strony (też z ankiety Adriana): ten sam plik głosu marki + R·Z·F obsługuje artykuł tak samo jak post - zmienia się tylko Format. Nie rób osobnego dema, wystarczy powiedzieć.

### Demo 3 - brief graficzny (Maciej) · ~6 min
- Kontynuacja demo 2: z tego samego planu komunikacji poproś o **brief graficzny do jednego posta**: przekaz, tekst na grafice, format na kanał, prompt do Firefly, specyfikacja do Canvy.
- Oddaj głos Maćkowi: „czego tu brakuje, żebyś usiadł i zrobił?” - jego uwagi to darmowy research pod warsztat 2 „Linia graficzna".
- Nawiąż do domku (slajd 8): warianty są tanie, gust Maćka jest bramką.

### Demo 4 - faktura - arkusz (Rafał R.) · ~10 min · NIE WYCINAĆ
- Przygotuj **fikcyjną fakturę PDF/JPG** (wymyślony sprzedawca, NIP 0000000000, realny układ). Miej drugą, „trudną” (zdjęcie pod kątem / słaby skan) na dogrywkę.
- Prompt ze slajdu 26 (z ⚠️ przy polach niepewnych). Wklej wynik do prostego arkusza na żywo.
- Dwa zdania bezpieczeństwa: numer konta zawsze człowiek u źródła; firmowe faktury dopiero po ustaleniu polityki danych (slajd 28).
- Teaser warsztatu 2: „to, co zrobiłem ręcznie w 3 minuty, da się zautomatyzować do zera kliknięć - ale to temat warsztatu, nie 10 minut demo”. Tam też: wprowadzanie osób do płatności.
- **Automatyzacja na warsztacie 2:** n8n (darmowy, self-hosted) + GPT-4o-mini API (~0,05 zł/faktura). Trigger: mail z załącznikiem PDF lub folder na Dysku → ekstrakcja danych → wiersz w arkuszu. To jedyne miejsce w PEGA, gdzie automatyzacja ma natychmiastowy ROI. Nie mów tego na sali — pokaż dopiero na warsztacie 2 jako „wow moment".

### Master Prompt (slajd 30) · ~5 min + przejście w ćwiczenie (slajd 31)
- Slajd 30 pokazuje WHY / HOW / WHAT tworzenia master promptu. Na ekranie szablon z polami do uzupełnienia.
- Ćwiczenie na żywo: budujesz master prompt dla Rafała T. (marketing), pytając go o rolę, typowe zadania i preferowany format wyjścia. Pokazujesz, jak R·Z·F + persona + reguły („nie zmyślaj”, „⚠️ przy niepewności”) dają gotowy skill.
- Jedno zdanie dla reszty: „Każdy z Was dostanie w mailu prompt uszyty pod swoje zadanie z ankiety - wersja starter, na której od poniedziałku pracujecie.”
- **Bridge do ćwiczenia (slajd 31):** „Skoro wiecie już, jak wygląda master prompt - zapiszcie jedno powtarzalne zadanie, które od poniedziałku zaczynacie od AI. Prompt od poniedziałku macie, zostaje pytanie: NA CZYM go użyjecie?”

### Data is the key (slajd 33) · ~2 min teaser
- Slajd 33 to celowo niedokończony temat - rzuca ziarno pod warsztat 2 (wspólne repozytoria, instrukcje zespołowe, pamięć długoterminowa).
- Jedno zdanie wystarczy: „Im dłużej trzymacie briefy, analizy i teksty w jednym miejscu, tym mniej musicie tłumaczyć AI od nowa. Na warsztacie 2 ustawiamy tę strukturę.”
- Nie rozwijaj w wykład - jeśli ktoś pyta, powiedz: „dobre pytanie, właśnie dlatego to jest na mapie warsztatu 2.”

---

## Autopromocja - jak jest wpleciona (nie dokładaj więcej)

- Dowody z plakietkami ZWERYFIKOWANE: slajd 5 (14 lat / 5+ lat / codziennie), 8 (Domek dla dzieci - ~1 h z AI, ~700 zł materiałów + 3 dni własnej pracy, wyceny wykonawców 6–10 tys. zł; liczby potwierdzone 2026-07-20), 29 (Lidka). Zero liczb spoza Evidence Register; celowo nie ma pary 500K/2,3M NOK ani „87%” - nie dodawaj ich ustnie.
- Pozycjonowanie: praktyk-architekt („w moich projektach”), trzy wpadki (slajd 9), „Daję wędkę” (35). **Nie mów „na moich szkoleniach”** - zasada z runbooka obowiązuje.
- Stopki z tomaszmierzejowski.pl tylko na pierwszym i ostatnim slajdzie - wystarczy.

## Sprzedaż warsztatu 2 - mechanika

1. **Głód budują niedokończenia**, rozmieszczone celowo: pakiet promptów (24), automatyzacja faktur (26), kawałek mapy (32). Przy każdym mów wprost: „to jest materiał na warsztat, nie na kwadrans”.
2. Slajd 34 nazywa cztery warsztaty **imiennie pod ludzi z ankiety** - oferta podana jako plan rozwoju zespołu, nie cennik. O pieniądzach na sali nie rozmawiasz; „format i wycenę wyślę w mailu do 48 h - Wasza rozmowa na sali decyduje, który temat pierwszy”.
3. Pytanie o warsztat 2 zadaj na sali, przy zamknięciu (slajd 35): „Który temat warsztatu 2 najbardziej pomógłby Wam w pracy?” - upsell staje się ich wyborem. Jeśli nie pada odpowiedź, powtórz w mailu follow-up.
4. Mail follow-up (do 48 h): materiały + prompty z dem + odpowiedzi z flipchartu + **4 imienne master prompty „starter”** (`Handouts/PL/PEGA_Master_Prompty.md` - wersje do wklejania na darmowych kontach; pełne „maszyny” z projektami i automatyzacją zostają materiałem warsztatu 2) + **jedna strona oferty warsztatu 2** (temat wybrany ankietą jako pierwszy, pozostałe jako kolejne kroki) + data kontaktu w dniu 30. Na sali zapowiedz master prompty przy ćwiczeniu (slajd 30): „każdy z Was dostanie w mailu swój prompt startowy pod swoje zadanie” - podnosi open rate maila i wzmacnia zobowiązanie.
5. Dzień 30 (wpisz do kalendarza od razu): pytasz o zobowiązania z kartek - naturalny moment domknięcia decyzji o warsztacie 2, jeśli mail jej nie domknął.

## Przygotowanie (delta względem runbooka, T-3)

- [ ] Mail przygotowawczy dziś: każdy przynosi laptop + działające konto w min. 1 asystencie; Adrian - 2 ulubione posty PEGA; wszyscy - jedno prawdziwe (niewrażliwe) zadanie w głowie.
- [ ] Fikcyjna faktura ×2 (czysta + trudna), przykładowy klient do demo 1a wybrany i sprawdzony, brief eventu do demo 2.
- [ ] Nagrania fallback wszystkich dem (ekran + kursor), deck przetestowany offline, wydrukowany ten plan + kartki na zobowiązania.
- [x] ~~Ankieta po sesji~~ - zastąpiona pytaniem na żywo przy zamknięciu + w mailu follow-up.
- [ ] Do Maćka: 2 minuty rozmowy przed startem - nie wypełnił pytań o zadania; zapytaj wprost, co mu zjada czas w grafice. Wpleć odpowiedź w demo 3.

## Ryzyka specyficzne dla tej sali

- **Maciej (jedyny z licencjami, brak odpowiedzi w ankiecie):** ryzyko „to nie o mnie”. Antidotum: demo 3 jest jego, Domek mówi do niego wprost, warsztat „Linia graficzna” na slajdzie 34.
- **Rafał R. (tylko admin):** nie przeciążaj go mindsetem; jego kupuje demo 4 i wizja „zero przepisywania”.
- **Darmowe konta na sali:** demo 2 wymaga projektów/instrukcji - rób na SWOIM koncie, na ich danych briefowych. Nie zamieniaj sesji w zakładanie kont (reguła z runbooka).
- Sala 4-osobowa: to rozmowa, nie wykład. Pytaj po imieniu, licz do 7 po pytaniu, parking lot od minuty 1.
- Gamingowa stylizacja (LVL, „gramy”) jest **przyprawą, nie sosem** - jeśli na sali nie zaskoczy, po prostu przestań jej używać w mowie; slajdy bronią się same.
