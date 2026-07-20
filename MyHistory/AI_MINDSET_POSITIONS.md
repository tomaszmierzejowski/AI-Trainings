# Moje stanowiska — AI Mindset w moich słowach

Źródło: wywiad-przesłuchanie (Gemini, 2026-07-20), w którym sceptyczny "CTO" cisnął mnie o
wszystko. Odpowiedzi są moje, nagrane na żywo, nieprzepisane przez model. To jest materiał
źródłowy dla szkoleń, postów i portfolio — kiedy AI pisze w moim imieniu, ma czerpać STĄD,
nie wymyślać. Liczby skorygowane po wywiadzie oznaczone [SKORYGOWANE].

## Czym jest AI Mindset (moja definicja robocza)

AI Mindset to przede wszystkim zdolność do delegowania swoich zadań — szczególnie tych,
których nie lubimy. Zespół, którym dysponujesz, to nie eksperci. To zespół ambitnych
juniorów, którzy znają się na jednej rzeczy. Pomysł pojawia się w głowie → zanim zaczniesz
go mocno analizować, zlecasz go AI → AI przygotowuje szkic → ty zastanawiasz się tylko,
jak zrobić z tego profesjonalny produkt.

## Kiedy NIE zaczynać od promptu (wyjątek, który sam stosuję)

Gdy mam głowę pełną pomysłów, prompt zaburza flow. Wtedy: nagrywam siebie (monolog albo
spotkanie eksperckie) → transkrypcja → dopiero CAŁOŚĆ myśli trafia do AI, z zadaniem:
wyłap luki, zaudytuj rozwiązanie, naszkicuj i pociągnij dalej. Potem znów spotkanie
eksperckie, uwagi, transkrypcja, kolejna iteracja szkicu. Im więcej informacji dostanie
AI, tym lepiej wykona zadanie. To nadal jest "AI first" — tylko pierwszym narzędziem jest
dyktafon, nie prompt.

## Obrona METR (dlaczego seniorzy byli 19% wolniejsi)

Nie da się wskazać jednej przyczyny; moje trzy, z praktyki:
1. Brak nawyku pracy z AI — to była rewolucja, nie ewolucja; nikt nie mógł być gotowy.
2. Dzięki AI eksperci nagle robią rzeczy, na które nigdy nie było czasu — wyższe pokrycie
   testami, obsługa skrajnych przypadków. Wolniej ≠ mniej wartości.
3. Złe użycie: AI do dopieszczania gotowego rozwiązania zamiast do zarysowania go na
   początku. AI ma załatwiać najprostszą pracę, a ekspert oceniać i poprawiać.

## Spec-driven development (moje stanowisko, Moduł 4)

Kod jest tani i łatwy w produkcji. To, co naprawdę się liczy, to reguły biznesowe,
zachowania i wymagania spisane logicznie i strukturalnie w języku naturalnym (pliki .md).
Na tej podstawie każdy LLM wytworzy kod w każdym tech-stacku — trzeba zadbać o jakość
specyfikacji. Weryfikacji podlegają głównie scenariusze testowe ze specyfikacji: wymuszamy
implementację wszystkich + prosimy model o wymyślenie własnych. Jak wszystko jest na
zielono, mamy większą pewność co do logiki biznesowej niż w tradycyjnej inżynierii, gdzie
ślepo ufamy osobie piszącej kod.
Cytat: "Kiedyś mówiono o samodokumentującym się kodzie — teraz mamy dobrą dokumentację
i samopiszący się kod."

## Obrona 87% (discovery)

Tradycyjnie zespół analizował 5–15% kodu enterprise, resztę musiał sobie dowymyślić — nie
było czasu na przeczytanie całości. [MOJA PRAKTYKA/OPINIA — obserwacja z projektów, nie
badanie.] Dziś analizujemy 100% plików i oceniamy jakość każdego fragmentu. Redukujemy
koszt discovery I dostarczamy raport wyższej jakości — oparty o cały kod, nie strzępki.
Zaufanie: confidence score per finding + odnośnik do konkretnej linii kodu.

## Monetyzacja projektów prywatnych (uczciwie)

- Domek dla dzieci: [SKORYGOWANE] ~700 zł materiałów + 3 dni własnej pracy, wobec wycen
  wykonawców 6–10 tys. zł. Realna, policzalna oszczędność.
- Lidka: realny sklep z realnym produktem koleżanki. Działa i zarabia.
- PresoGen: zbudowany dla mnie — nie lubię robić prezentacji, więc robi je za mnie.
  Może kiedyś zarobi.
- Mana Menu: faza przedprodukcyjna.
- LifeAutomations: nie umiem przeczytać wszystkich maili i wiadomości w ciągu dnia —
  triage zmienia moje życie.
- Monetyzacja nie jest teraz priorytetem. Przyjdzie z czasem.

## Wpadka z LinkedIn (moja blizna — używać, nie ukrywać)

Ktoś na LinkedIn zarzucił mi, że jestem botem i chciałby porozmawiać z prawdziwym
człowiekiem. Zbyt mocno zawierzyłem AI i próbowałem robić zbyt wiele projektów naraz.
Nauczka: czyścić repozytoria z halucynacji AI i nie przyzwyczajać się do zaufania.
"Błędy nie są zarezerwowane dla AI — to rzecz ludzka. Ale te związane z AI są bardziej
kosztowne, bo istnieje duży front anty-AI, który tylko czeka na potknięcie."
Decyzja: ta historia idzie do Modułu 3 jako case study. Ludzie ufają trenerom z bliznami.

## Wsparcie naukowe dla Spektrum (nowe, 2026-07-20)

Dell'Acqua i in. 2023 ("jagged frontier") definiuje dwa profile pracy z AI: "Centaury"
(dzielą pracę, AI dostaje zadania poboczne — mój Poziom 2) i "Cyborgi" (integrują AI od
pierwszego kroku każdego zadania — mój Poziom 3). Badanie pokazało przewagę podejścia
Cyborga. Spektrum pozostaje moją heurystyką z obserwacji [OPINIA], ale przejście 2→3 jest
zbieżne z opublikowanymi wynikami [BADANIE — zweryfikować cytat przed drukiem].
Formuła treningu: T(szkic AI) + T(weryfikacja eksperta) < T(szkic eksperta) + T(szlif AI).
Poziom 2 tkwi w miejscu, bo ludziom się wydaje, że weryfikacja zajmie więcej niż własny
szkic. Trening ma udowodnić, że matematyka działa inaczej.

## Staż z AI (rozróżnienie, 2026-07-20)

Trzy lata codziennego używania AI (prywatnie i zawodowo). Dwa lata AI Discoveries i AI
Modernization w skali delivery (2024→2026). Nie mieszać tych dwóch liczb.

## Luki do rozwinięcia (znalezione w wywiadzie — nie udawać, że ich nie ma)

1. **AI w incident response / na produkcji pod presją.** Dwa razy uciekłem od tego
   pytania w stronę discovery i designu. Zanim wejdę z programem do zespołów DevOps/SRE,
   potrzebuję taktyki gaszenia pożarów z AI. [DO ROZWINIĘCIA]
2. **Weryfikacja ponad "zielone testy".** Scenariusze testowe nie łapią deadlocków,
   wycieków pamięci, N+1, luk security w wygenerowanym kodzie. Pipeline AMF ma etap
   security-scan i bramki ludzkie — częściowa odpowiedź istnieje, ale nie jest spisana
   ostro (jak filtrujemy false-positives zanim findingi trafią do ludzi; jak nie kazać
   seniorom klikać 529 linków). [DO ROZWINIĘCIA — częściowo istnieje w praktyce AMF]

## Cytaty (naturalne, moje — do użycia w materiałach)

- "AI mindset to przede wszystkim zdolność do delegowania swoich zadań, szczególnie tych,
  których nie lubimy."
- "Nie potrzebujesz zespołu ekspertów. AI to zespół ambitnych juniorów."
- "Zanim zaczniesz analizować pomysł, zleć go sztucznej inteligencji — a ty zastanawiaj
  się tylko, jak zrobić z tego profesjonalny produkt."
- "AI ma załatwiać najprostszą pracę, a ekspert oceniać i poprawiać."
- "Kiedyś mówiono o samodokumentującym się kodzie — teraz mamy dobrą dokumentację
  i samopiszący się kod."
- "Błędy nie są zarezerwowane dla AI — to rzecz ludzka."
