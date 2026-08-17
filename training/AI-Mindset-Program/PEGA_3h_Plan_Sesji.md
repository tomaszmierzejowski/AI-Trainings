# PEGA (pega.gg) - plan sesji 3 h · [data: za 3 dni od 2026-07-18]

**Ściąga dem:** `PEGA_Demo_Sciaga.md` — otwórz na laptopie obok decka; zawiera gotowe prompty do kopiowania i instrukcje krok po kroku.

**Deck:** `Decks/PL/PEGA_Sesja_3h.html` (41 slajdów, w tym 4 slajdy z promptami do dem; slajd tytułowy, przerwa i zamknięcie są ciemne). Slajd 19b: tabela „kto co dostaje" z narzędziami i kosztami per osoba. **Slajdy 19c–19e (nowe, fundament przed przerwą): master prompt jako JEDNO narzędzie + szablon do przeklejenia + „Data is the key".** To jest teraz punkt wyjścia — demy po przerwie są zastosowaniem tego samego ruchu.
**Cel biznesowy dnia:** sala ma wyjść z poczuciem „to było o NAS” + z jednym prostym narzędziem (master prompt), które działa od poniedziałku + na stole leży konkretny, nazwany warsztat 2 (slajd 32). Sprzedaje personalizacja i dema, nie gadka sprzedażowa.
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
| Copy bez powtarzalności | Adrian | Demo 2 (24): bank struktur + wytyczne głosu marki |
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
| Adrian | Powtarzalne posty, zły ton, AI gubi wytyczne | Wytyczne głosu marki + bank 12-15 struktur + Projekt ze stałą instrukcją | Claude Pro lub ChatGPT Plus | ~100 zł/mies. |
| Rafał T. | Research klientów, prezentacje, „kiedy który model?" | Perplexity Pro do researchu + Claude Pro do konspektów ofert | Perplexity Pro + Claude Pro | ~160 zł/mies. |
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
| 0:10–0:40 | Mindset: złe pytanie, Domek (historia + slajd), wpadki, LVL 1–4, kolejność, granica | 6–12 | tnij blok Domku do 2 min łącznie; wpadek NIE wycinaj |
| 0:40–1:02 | 3 nawyki + mapa narzędzi PEGA + drzewo + licencje + kto-co-dostaje (19b) | 13–19b | 19b mów max 60s; licencje skróć do 1 zdania + „szczegóły w mailu”; mapa/drzewo mów szybko — to podkład pod master prompt |
| 1:02–1:30 | **★ GŁÓWNE DANIE: master prompt — workshop na żywo + szablon + „Data is the key"** | 19c–19e | **nigdy nie wycinać, tu daj sobie czas.** Buduj 1 pełny master prompt (Rafał T.) + 3 błyskawiczne po jednym polu (Adrian, Rafał R., Maciej) — to zastępuje personalizację z dem. „Data is the key" max 2 min na koniec |
| 1:30–1:45 | ☕ Przerwa | 20 | max 15 min, pilnuj powrotu |
| 1:45–2:15 | Dema: **2 na żywo (research 1a + faktury 4)** + 3 opowiedziane ze slajdów (1b, 2, 3) | 21–26 | LIVE tylko 1a i 4. 1b/2/3 opowiadasz przy slajdach z promptami (22b/24b/25b) — NIE klikasz. Goni czas? Skracaj narrację, live zostają |
| 2:15–2:28 | Weryfikacja + dane wrażliwe + Lidka | 27–29 | Lidkę można opowiedzieć w 60 s. Slajd 27 otwórz własną wpadką (stopka: „ktoś na LinkedIn napisał mi, że brzmię jak bot”) - historia z blizną buduje więcej zaufania niż zasada; nie tłumacz się, jedno zdanie i dalej |
| 2:28–2:40 | Ćwiczenie (kartki) | 30 | **nigdy nie wycinać** - ćwiczenie daje pretekst do kontaktu w dniu 30 |
| 2:40–3:00 | Mapa + warsztat 2 + zamknięcie **+ BUFOR** | 31–33 | **~18 min z buforem — Twoja poduszka na poślizg.** Jeśli masz zapas: wróć do pytań z parking lotu. Sam finał (31–33) to ~7 min |

Przerwa wypada dokładnie po ~75 min - zgodnie z regułą „co ~75 min” z runbooka. **Master prompt (główne danie) ląduje TUŻ przed przerwą:** efekt świeżości + sala idzie na kawę z jedną myślą („mam jedno narzędzie na wszystko”). Świadomy wybór trenera (2026-07-20): workshop > liczba dem, bo z nim się utożsamia i prowadzi bez przygotowania; live demy ograniczone do 2 najpewniejszych, żeby nie rozjechać czasu. **20-minutowy bufor na końcu jest celowy — wykorzystaj go, nie dokładaj treści.**

## Golden Circle - oś narracji (do głowy, nie na slajd)

Deck już ma tę strukturę; wystarczy ją wypowiedzieć, nic nie przebudowywać:

- **WHY** (slajdy 1, 6, 11, 12): wierzę, że przewaga z AI nie leży w narzędziach, tylko w kolejności pracy i nawykach - jak w esporcie: wygrywa ten, kto lepiej gra, nie ten, kto ma lepszy sprzęt. Zdanie-kotwica do wypowiedzenia przy slajdzie 11: „Nie jestem tu, żeby sprzedać Wam narzędzie. Jestem tu, żeby zmienić kolejność, w jakiej pracujecie.”
- **HOW** (slajdy 13–19e): trzy nawyki (R·Z·F, iteruj, stała instrukcja) + mapa ról narzędzi + drzewo decyzyjne + rekomendacja licencyjna, a na końcu **fundament: master prompt jako jedno narzędzie + „Data is the key"** (19c–19e). To jest metoda, nie katalog — i kulminuje w jednym prostym narzędziu, które sala zabiera do domu.
- **WHAT** (slajdy 19c–19e, 21–26, 30, 32): **główne danie to workshop master promptów** (budujesz 1 pełny + 3 błyskawiczne, po jednym na osobę — to niesie personalizację). Potem 2 demy na żywo (research + faktury) + 3 opowiedziane pokazują to samo narzędzie w akcji. Do tego jedno zobowiązanie od poniedziałku i warsztat 2 jako następny krok.

Kolejność decka celowo idzie Why - How - What - jeśli ktoś zapyta „po co nam to”, odpowiedź padła w pierwszych 45 minutach, zanim pojawiło się jakiekolwiek narzędzie.

## Rozkład dem w bloku 1:45–2:15 (30 min) — 2 LIVE + 3 opowiadane

**Zmiana (2026-07-20): główne danie to workshop master promptów, nie demy.** Demy skurczone:
- **1a research (Rafał T.) — LIVE ~11 min**
- **4 faktury (Rafał R.) — LIVE ~10 min**
- **1b oferta, 2 plan+copy, 3 grafika — OPOWIADANE ze slajdów, ~2–3 min każde, NIE klikasz.**

Personalizację niosą teraz przede wszystkim master prompty budowane w workshopie (1 pełny + 3 błyskawiczne). Demy opowiadane to „a tak to samo narzędzie działa u Ciebie" — pokazujesz slajd z promptem (22b/24b/25b), tłumaczysz w 2 zdaniach, idziesz dalej. Live zostają nawet przy dużym poślizgu.

intro 2 min · 1a research LIVE 11 min · 1b oferta (opowiadane) 2 min · 2 plan+copy (opowiadane) 3 min · 3 grafika (opowiadane) 2 min · 4 faktury LIVE 10 min = 30 min.

### Demo 1a - research klienta (Rafał T.) · LIVE · ~11 min
- **Narzędzie: Perplexity Pro** — najlepszy do researchu z cytatami. Lepszy niż jakikolwiek wielomodelowy pipeline, bo robi search + syntezę + źródła w jednym kroku. Zdanie do powiedzenia: „Perplexity robi jedną rzecz lepiej od wszystkich: szuka i podaje źródła. Za ~80 zł miesięcznie masz asystenta, który nigdy nie cytuje z pamięci."
- Klient przykładowy: **publiczna** marka realistyczna dla PEGA (np. duży producent sprzętu gamingowego obecny w PL). Nie używaj prawdziwego prospekta PEGA bez zgody na sali.
- Najpierw prompt „leniwy” (slajd 14, lewa strona) - pokaż miałkość. Potem R·Z·F z obowiązkową kolumną linków. Kliknij 1–2 linki na żywo - weryfikacja u źródła jako odruch, nie wykład.
- Finisz: „Jakie 3 pytania ten klient zada nam na spotkaniu, na które nie mamy dziś dobrej odpowiedzi?” - to zdanie robi największe „aha” u marketingu.

### Demo 1b - konspekt oferty · OPOWIADANE ze slajdu · ~2 min
- Nie klikasz. Pokaż slajd 23b (gotowe prompty) i opowiedz sekwencję: 1a → konspekt 10 slajdów → adwokat kupującego. Pointa w jednym zdaniu.
- Wejście: wynik z 1a + 3-zdaniowy brief. Prośba: konspekt 10 slajdów z notatkami prelegenta.
- Wtrącenie dla Rafała T. (nowe, 2026-07-20): gdy koncepcja siedzi w głowie eksperta, nie
  zaczynaj od pisania promptu - nagraj 2 minuty mówienia o koncepcji (telefon wystarczy),
  wklej transkrypcję i dopiero każ AI szkicować oraz wyłapać luki. „AI-first nie zawsze znaczy
  prompt-first - czasem pierwszym narzędziem jest dyktafon.” Jedno zdanie, nie osobne demo.
- Obowiązkowo „adwokat kupującego”: „Jesteś dyrektorem marketingu po stronie klienta. Gdzie ta koncepcja traci punkty?”
- NIE generuj gotowego decka w Canvie na żywo (za dużo zmiennych) - forma to ostatni krok, pokaż samo wklejenie konspektu.

### Demo 2 - plan komunikacji + copy (Adrian) · OPOWIADANE ze slajdu · ~3 min
- **Nie klikasz na żywo — ale to demo ma najmocniejszy pomost do workshopu.** Powiedz wprost: „wytyczne głosu marki Adriana, które zbudowaliśmy przy master prompcie, to jest dokładnie to. Tu widzicie je w akcji." Pokaż slajd 24b (trzy prompty), przejdź palcem po sekwencji głos marki → plan → posty. Jeśli Adrian dopytuje i jest czas z bufora — możesz kliknąć na żywo, ale domyślnie opowiadasz.
- (materiał do narracji) Zbuduj **wytyczne głosu marki, pytając Adriana**: ton (3 przymiotniki), odbiorcy, zakazane frazy, 1–2 posty „po naszemu” (poproś go wcześniej mailem o 2 ulubione posty PEGA).
- Wklej jako instrukcję projektu - jeden brief eventu - **najpierw plan komunikacji** (tabela: data · kanał · cel · struktura - to jego „plany komunikacji medialnej” z ankiety) - potem 2–3 posty z planu, każdy z **jawnie wskazaną inną strukturą z banku**.
- Puenta: powtarzalność = brak wytycznych + darmowe konto bez projektów. Łączy się ze slajdem 19 i z warsztatem 2 (pełny pakiet - celowo niedokończony dziś).
- **Klucz do różnorodności to bank struktur, nie więcej modeli.** Prompt „użyj struktury: historia zawodnika" daje inny post niż „użyj struktury: pytanie do społeczności" — nawet na tym samym modelu. Gdyby ktoś zapytał o puszczanie treści przez kilka AI naraz: „przy 10–20 postach tygodniowo to przerost formy. Jeden dobrze poinstruowany model bije trzy źle poinstruowane."
- Jedno zdanie o artykułach na strony (też z ankiety Adriana): te same wytyczne głosu marki + R·Z·F obsługuje artykuł tak samo jak post - zmienia się tylko Format. Nie rób osobnego dema, wystarczy powiedzieć.

### Demo 3 - brief graficzny (Maciej) · OPOWIADANE ze slajdu · ~2 min
- Nie klikasz. Pokaż slajd 25b (gotowy prompt) i powiedz Maćkowi: „z tego samego briefu master prompt robi Ci komplet — przekaz, tekst na grafice, prompt do Firefly, specyfikacja do Canvy." Oddaj mu głos na 1 pytanie.
- (materiał do narracji) Kontynuacja demo 2: z tego samego planu komunikacji poproś o **brief graficzny do jednego posta**: przekaz, tekst na grafice, format na kanał, prompt do Firefly, specyfikacja do Canvy.
- Oddaj głos Maćkowi: „czego tu brakuje, żebyś usiadł i zrobił?” - jego uwagi to darmowy research pod warsztat 2 „Linia graficzna".
- Nawiąż do domku (slajd 8): warianty są tanie, gust Maćka jest bramką.

### Demo 4 - faktura - arkusz (Rafał R.) · LIVE · ~10 min · NIE WYCINAĆ
- Przygotuj **fikcyjną fakturę PDF/JPG** (wymyślony sprzedawca, NIP 0000000000, realny układ). Miej drugą, „trudną” (zdjęcie pod kątem / słaby skan) na dogrywkę.
- Prompt ze slajdu 26 (z ⚠️ przy polach niepewnych). Wklej wynik do prostego arkusza na żywo.
- Dwa zdania bezpieczeństwa: numer konta zawsze człowiek u źródła; firmowe faktury dopiero po ustaleniu polityki danych (slajd 28).
- Teaser warsztatu 2: „to, co zrobiłem ręcznie w 3 minuty, da się zautomatyzować do zera kliknięć - ale to temat warsztatu, nie 10 minut demo”. Tam też: wprowadzanie osób do płatności.
- **Automatyzacja na warsztacie 2:** n8n (darmowy, self-hosted) + GPT-4o-mini API (~0,05 zł/faktura). Trigger: mail z załącznikiem PDF lub folder na Dysku → ekstrakcja danych → wiersz w arkuszu. To jedyne miejsce w PEGA, gdzie automatyzacja ma natychmiastowy ROI. Nie mów tego na sali — pokaż dopiero na warsztacie 2 jako „wow moment".

## ★ GŁÓWNE DANIE: master prompt — workshop (slajdy 19c–19e) · ~28 min

**To jest teraz serce sesji, nie dodatek na końcu.** Świadomy wybór trenera: workshop > liczba dem,
bo z tym rozwiązaniem się utożsamiasz i prowadzisz je bez przygotowania. Tu daj sobie czas — masz
na to najwięcej minut w całym planie. Teza do wypowiedzenia:
„Nieważne, co robicie później — jeśli opanujecie AI mindset i to jedno narzędzie, a do tego
dobrze trzymacie swoje dane i sprawdzone prompty, każde następne zadanie jest już dużo
łatwiejsze. Z dobrym master promptem AI samo Wam podpowie, którego narzędzia użyć, i da lepszy
szkic, bo pyta, zanim zgaduje."

### Master prompt — jedno narzędzie (slajd 19c) · ~3 min
- Slajd pokazuje: co to jest / dlaczego to fundament / jak go używamy dziś. Rama: to R·Z·F z nawyku 1 + persona + stałe zasady, zapisane RAZ.
- Powiedz wprost, że to jest główne danie: „Jeśli z dzisiaj zapamiętacie jedną rzecz, niech to będzie to."

### Master prompt — budowa na żywo (slajd 19d) · ~20 min · TU JEST WORKSHOP
- **Krok 1 — 1 pełny master prompt na żywo (Rafał T., marketing) · ~10 min.** Na ekranie szablon uniwersalny (`Handouts/PL/PEGA_Master_Prompty.md` → „Szablon uniwersalny"). Wypełniacie pola `[w nawiasach]` razem: dziedzina, kontekst, typowe zadania, format. Potem wklejasz do modelu i pokazujesz, jak **dopytuje** (2–4 pytania), zanim odpowie.
- **Krok 2 — 3 błyskawiczne, po jednym na osobę · ~10 min łącznie.** Ten sam szablon, tylko zmieniacie dziedzinę: Adrian (copywriting social media), Rafał R. (faktury/księgowość), Maciej (briefy graficzne). Po 2–3 min każdy — wypełniacie tylko dziedzinę + 1–2 zadania, reszta zostaje z szablonu. **To zastępuje personalizację, którą dawały demy: każdy wychodzi ze SWOIM master promptem naszkicowanym na sali.**
- **Zainspirowane Lyrą (optymalizator promptów):** kluczowa reguła to „zadaj mi 2–4 pytania doprecyzowujące, zanim odpowiesz". Pokaż to na żywo przy Kroku 1 — model dopytuje, a nie zgaduje.
- **Tryb MISTRZ = uczciwa wersja „100% mocy":** plan → wykonanie → autokrytyka → poprawka. Powiedz wprost: „Nie da się promptem dołożyć modelowi mocy obliczeniowej. Da się kazać mu zaplanować, sprawdzić siebie i poprawić — i to realnie podnosi jakość." (spójne z zasadą uczciwości z reguł gry, slajd 4).
- Jedno zdanie domykające: „Każdy z Was dostanie w mailu ten szablon + gotowy przykład pod swoje zadanie z ankiety — wersja na start, na której od poniedziałku pracujecie."
- **Pomost do dem:** „Po przerwie zobaczycie ten sam master prompt w akcji — research i faktury pokażę na żywo, resztę szybko opowiem."

### Data is the key (slajd 19e) · ~2 min
- Druga połowa fundamentu: master prompt mówi AI KIM być, dane mówią CO już wiecie. Im dłużej trzymacie briefy, analizy, teksty i sprawdzone prompty w jednym miejscu, tym mniej tłumaczycie od nowa.
- Zostawiasz ziarno pod warsztat 2 (wspólne repozytoria, instrukcje zespołowe, pamięć długoterminowa), ale zasada jest fundamentem, nie tylko teaserem. Jeśli ktoś dopytuje o wdrożenie zespołowe: „dobre pytanie, właśnie tak głęboko wchodzimy na warsztacie 2."
- Puenta przed przerwą: „AI mindset + jeden master prompt + dobrze trzymane dane = każde następne zadanie łatwiejsze. Idziemy na kawę, po niej zobaczycie to samo narzędzie w akcji na Waszych zadaniach."

### Ćwiczenie (slajd 30, po demach) · ~10 min
- **Bridge:** „Master prompt już znacie sprzed przerwy. Zapiszcie teraz jedno powtarzalne zadanie, do którego zrobicie sobie własny — i które od poniedziałku zaczynacie od AI."
- Kartki zostają u uczestników; pytasz o nie w dniu 30.

---

## Autopromocja - jak jest wpleciona (nie dokładaj więcej)

- Dowody z plakietkami ZWERYFIKOWANE: slajd 5 (14 lat / 5+ lat / codziennie), 8 (Domek dla dzieci - ~1 h z AI, ~700 zł materiałów + 3 dni własnej pracy, wyceny wykonawców 6–10 tys. zł; liczby potwierdzone 2026-07-20), 29 (Lidka). Zero liczb spoza Evidence Register; celowo nie ma pary 500K/2,3M NOK ani „87%” - nie dodawaj ich ustnie.
- Pozycjonowanie: praktyk-architekt („w moich projektach”), trzy wpadki (slajd 9), „Daję wędkę” (33). **Nie mów „na moich szkoleniach”** - zasada z runbooka obowiązuje.
- Stopki z tomaszmierzejowski.pl tylko na pierwszym i ostatnim slajdzie - wystarczy.

## Sprzedaż warsztatu 2 - mechanika

1. **Głód budują niedokończenia**, rozmieszczone celowo: pakiet promptów (24), automatyzacja faktur (26), kawałek mapy (31). Przy każdym mów wprost: „to jest materiał na warsztat, nie na kwadrans”.
2. Slajd 32 nazywa cztery warsztaty **imiennie pod ludzi z ankiety** - oferta podana jako plan rozwoju zespołu, nie cennik. O pieniądzach na sali nie rozmawiasz; „format i wycenę wyślę w mailu do 48 h - Wasza rozmowa na sali decyduje, który temat pierwszy”.
3. Pytanie o warsztat 2 zadaj na sali, przy zamknięciu (slajd 33): „Który temat warsztatu 2 najbardziej pomógłby Wam w pracy?” - upsell staje się ich wyborem. Jeśli nie pada odpowiedź, powtórz w mailu follow-up.
4. Mail follow-up (do 48 h): materiały + prompty z dem + odpowiedzi z flipchartu + **uniwersalny szablon master promptu + 4 imienne gotowe przykłady** (`Handouts/PL/PEGA_Master_Prompty.md` - wersje do wklejania na darmowych kontach; pełne „maszyny” z projektami i automatyzacją zostają materiałem warsztatu 2) + **jedna strona oferty warsztatu 2** (temat wybrany ankietą jako pierwszy, pozostałe jako kolejne kroki) + data kontaktu w dniu 30. Na sali zapowiedz master prompty przy ćwiczeniu (slajd 30): „każdy z Was dostanie w mailu szablon i swój gotowy przykład pod swoje zadanie” - podnosi otwieralność maila i wzmacnia zobowiązanie.
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
- **Darmowe konta na sali:** dwa live demy (research 1a + faktury 4) rób na SWOIM koncie, na danych fikcyjnych/publicznych. Workshop master promptów działa na darmowych kontach (format „wklej na start"), więc uczestnicy budują u siebie bez blokad. Nie zamieniaj sesji w zakładanie kont (reguła z runbooka).
- Sala 4-osobowa: to rozmowa, nie wykład. Pytaj po imieniu, licz do 7 po pytaniu, parking lot od minuty 1.
- Gamingowa stylizacja (LVL, „gramy”) jest **przyprawą, nie sosem** - jeśli na sali nie zaskoczy, po prostu przestań jej używać w mowie; slajdy bronią się same.
