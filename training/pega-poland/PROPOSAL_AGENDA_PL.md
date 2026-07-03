# Pega Business AI Masterclass — Propozycja Szkolenia

---

## Spis Treści (Szybki Przegląd)

**3-dniowe szkolenie AI dla zespołów Pega** | Poziom: Zaawansowany | Język: Polski

- **Dzień 1** — Fizyka Inteligencji i Pega Intelligent Intake
  - Architektura LLM, tokenizacja, kontrola losowości
  - Krajobraz narzędzi AI 2026 (Claude, Gemini, GPT-4o, Cursor, Perplexity)
  - Warsztat: Intake JSON z RTF, Chain-of-Thought, Tree of Thoughts
- **Dzień 2** — Budowanie Systemów: RAG, Agenci i Akcje Pega
  - Embeddingi, przestrzenie wektorowe, podobieństwo kosinusowe
  - Zaawansowane pipeline RAG (chunking, hybrid search, re-ranking)
  - Warsztat: Autonomiczny agent ReAct na danych Pega (claims.csv)
- **Dzień 3** — Bezpieczeństwo, Ewaluacja i Produkcja
  - OWASP Top 10 dla LLM, prompt injection, obrona pipeline
  - Warsztat: Red Teaming — atak i obrona systemów AI
  - Ekonomia produkcji, ROI, Demo Day i Graduacja

**Rezultaty**: Prompt Cookbook, Kalkulator ROI, Architektura Agenta ReAct, Playbook Bezpieczeństwa, Framework Ewaluacji

---

## Streszczenie Wykonawcze

**Imperatyw: Od Czatu AI do Inżynierii Deterministycznej**

Era traktowania AI jako magicznego rozmówcy dobiegła końca. Organizacje enterprise blokują swoje inicjatywy generatywnego AI, ponieważ budują kruche, nieprzewidywalne chatboty zamiast solidnych, mierzalnych systemów. Ta propozycja szkoleniowa ma na celu fundamentalną zmianę podejścia liderów technicznych i decydentów biznesowych Pega do sztucznej inteligencji: przejście od zgadywania promptów do deterministycznej inżynierii oprogramowania.

**Dlaczego to szkolenie, dlaczego teraz?**

Modele frontier w 2026 roku (Claude 3.7, Gemini 2.0, GPT-4o) są zdolne do autonomicznego rozumowania i wieloetapowej egzekucji. Jednak bez głębokiego zrozumienia "fizyki" tych modeli — tokenizacji, rozkładów prawdopodobieństwa, embeddingów wektorowych i orkiestracji agentowej — wdrożenia enterprise są skazane na porażkę z powodu halucynacji, astronomicznych kosztów tokenów i katastrofalnych luk bezpieczeństwa, takich jak prompt injection. Architektura Pega jest wyjątkowo predysponowana do roli zarządzanego "mózgu" i "mięśni" dla tych systemów, ale Wasze zespoły potrzebują technicznej dyscypliny, aby je prawidłowo zintegrować.

**Co zyskają zespoły Pega**

Ten masterclass łączy najnowocześniejszą inżynierię LLM (Tree of Thoughts, Semantic Chunking, Re-ranking, LLM-as-a-Judge) z wzorcami przyspieszania workflow Pega (Intelligent Intake, Confidence-Based Triage, Generative Action). Przestajemy generować powierzchowne makiety UI i zaczynamy projektować autonomicznych agentów ReAct, którzy mogą przeszukiwać prywatne dane korporacyjne i bezpiecznie wywoływać API Pega.

**Profil ROI**

To program o wysokim wpływie, bezpośrednio powiązany z wynikami biznesowymi. Opanowując zaawansowane promptowanie i ekonomię routingu modeli, uczestnicy będą dążyć do 30%+ redukcji AHT, eliminacji ręcznego wprowadzania danych poprzez bezstykowy intake JSON oraz projektowania systemów kosztujących grosze zamiast złotówek za zapytanie.

---

## Agenda 3-Dniowa

### DZIEŃ 1: Fizyka Inteligencji i Pega Intelligent Intake

*Nie dotykamy LLM, dopóki nie zrozumiemy, czym jest token. Dzień 1 przenosi uczestników od "czatowania" do inżynierii deterministycznej.*

| Czas | Moduł | Cele | Format | Wartość Biznesowa |
|---|---|---|---|---|
| 09:00–10:30 | **1.1 Fizyka LLM i Kontrola Losowości** | Zrozumienie Transformerów, Tokenizacji (BPE), Okien Kontekstowych oraz manipulacji Logitami przez Temperature, Top-P i Min-P. | Wykład i Demo | Deweloperzy i VP muszą zrozumieć, że AI to probabilistyczny silnik matematyczny; kontrola jego losowości to jedyny sposób na zagwarantowanie niezawodności enterprise. |
| 10:30–10:45 | *Przerwa kawowa i Mikro-ćwiczenie* | Każdy uczestnik otwiera OpenAI Tokenizer i tokenizuje zdanie ze swojego workflow Pega. Udostępnienie najbardziej zaskakującej liczby tokenów. | Ćwiczenie | Uziemia abstrakcyjne pojęcie "tokena" w codziennej rzeczywistości uczestników. |
| 10:45–12:00 | **1.2 Krajobraz Multi-Modelowy 2026 i Ekonomia** | Ocena kosztów, opóźnień i limitów kontekstu Claude 3.7, Gemini 2.0, GPT-4o, Perplexity i Cursor. | Dyskusja i Demo | Wybór złego modelu niszczy ROI; zespoły nauczą się kierować proste zadania do tanich, szybkich modeli, a złożoną logikę do ciężkich silników rozumowania. |
| 12:00–13:00 | *Obiad* | | | |
| 13:00–14:30 | **Warsztat 1: Pega Intelligent Intake (Prompt Engineering Workbench)** | Opanowanie frameworka RTF, promptowania Zero-shot i Few-shot w celu wymuszenia ścisłego, deterministycznego JSON. | Warsztat (service.csv) | Uczy uczestników, jak wyeliminować ręczne wprowadzanie danych i przyspieszyć tworzenie Case'ów Pega z minut do milisekund. |
| 14:45–16:30 | **1.3 Zaawansowana Orkiestracja (CoT, ToT i Refinement)** | Projektowanie złożonych promptów rozumowania z Chain-of-Thought, Tree of Thoughts i Iterative Refinement. | Wykład i Warsztat | Rozwiązuje problem "halucynacji" w złożonej logice routingu/triażu Pega, dając AI matematyczny brudnopis do serializacji obliczeń. |
| 16:30–17:00 | **Retro Dnia 1 i Mapowanie Architektury** | Mapowanie dzisiejszych koncepcji na rzeczywiste workflow Pega uczestników. Identyfikacja, które workflow skorzystają najbardziej z RAG vs Agentów. | Dyskusja | Utrwala koncepcje techniczne w namacalnej wartości biznesowej Pega i przygotowuje grunt pod Dzień 2. |

### DZIEŃ 2: Budowanie Systemów AI (RAG, Agenci i Akcje Pega)

*Prompt to tylko mózg w słoiku. Dzień 2 podłącza mózg do pamięci (RAG) i rąk (API).*

| Czas | Moduł | Cele | Format | Wartość Biznesowa |
|---|---|---|---|---|
| 09:00–10:30 | **2.1 Matematyka Pamięci (Embeddingi i Przestrzenie Wektorowe)** | Zrozumienie wielowymiarowych Przestrzeni Wektorowych, Embeddingów i Podobieństwa Kosinusowego. | Wykład | Absolutny fundament Enterprise Semantic Search, umożliwiający Pega znalezienie igły w stogu siana bez fine-tuningu. |
| 10:45–12:30 | **2.2 Zaawansowane Pipeline RAG i Grounding** | Budowanie pipeline Retrieval Augmented Generation z Semantic Chunking, Hybrid Search i modelami Re-ranking. | Wykład i Demo | Rozwiązuje problemy "odcięcia wiedzy" LLM i ryzyka halucynacji poprzez bezpieczne zakotwiczenie odpowiedzi wyłącznie w aktualnych, zatwierdzonych dokumentach korporacyjnych. |
| 12:30–13:30 | *Obiad* | | | |
| 13:30–15:00 | **2.3 Tool Calling i Wzorzec ReAct** | Nauczenie LLM generowania deterministycznych schematów JSON do wywoływania zewnętrznych funkcji przez pętlę Thought -> Action -> Observation. | Wykład i Demo | Przekształca AI z pasywnego chatbota w aktywnego "Cyfrowego Pracownika", który może bezpiecznie wywoływać API Pega i przyspieszać rozwiązywanie spraw. |
| 15:00–16:45 | **Warsztat 2: Pega Generative Action Pod Build** | Budowa wieloetapowego autonomicznego agenta, który czyta roszczenie Pega (claims.csv), sprawdza wskaźniki oszustwa i tworzy obronny łańcuch logiki odrzucenia/zatwierdzenia. | Warsztat | Dowodzi, że AI może obsługiwać złożoną, wieloetapową pracę kognitywną, drastycznie redukując Average Handle Time dla starszych pracowników. |
| 16:45–17:00 | **Retro Dnia 2 i Peer Code Review** | Wymiana architektur agentów z sąsiednimi zespołami. Znalezienie jednego ryzyka nieskończonej pętli, jednego brakującego error handlera, jednego problemu bezpieczeństwa. | Dyskusja | Eksponuje uczestników na różne podejścia architektoniczne i ujawnia podatności na Dzień 3. |

### DZIEŃ 3: Wzmacnianie Enterprise (Bezpieczeństwo, Ewaluacja i Produkcja)

*Wysoce zdolne systemy bez governance to zautomatyzowane zobowiązania. Dzień 3 przygotowuje je do produkcji.*

| Czas | Moduł | Cele | Format | Wartość Biznesowa |
|---|---|---|---|---|
| 09:00–10:30 | **3.1 OWASP Top 10 i Obrona Pipeline** | Opanowanie mechaniki bezpośredniego/pośredniego Prompt Injection, wycieku danych i zatrucia RAG. | Wykład | Chroni dane własnościowe i reputację enterprise przed złośliwymi aktorami przejmującymi zautomatyzowane workflow. |
| 10:45–12:30 | **Warsztat 3: Red Teaming Capstone** | Atak na agentów sąsiednich zespołów (zbudowanych w Dniu 2) w celu wymuszenia wycieków PII i halucynacji, następnie przepisanie system promptów ze ścisłymi Guardrails. | Warsztat Gamifikowany | Jedyny sposób na bezpieczne wdrożenie AI to zrozumienie, jak dokładnie się łamie; to buduje wewnętrzny playbook bezpieczeństwa. |
| 12:30–13:30 | *Obiad* | | | |
| 13:30–15:00 | **3.2 LLM-as-a-Judge i Testy Regresyjne** | Budowa zautomatyzowanych zestawów testów regresyjnych z Golden Datasets do matematycznej oceny outputów AI (Faithfulness, Relevance). | Wykład i Warsztat | Zastępuje testowanie "na wyczucie" inżynierską dyscypliną, gwarantując że aktualizacje promptów lub modeli nie zepsują produkcyjnych workflow Pega. |
| 15:15–16:30 | **3.3 Ekonomia Produkcji i Demo Day** | Kalkulacja kosztów tokenów, opóźnień Time-to-First-Token i prezentacja finalnych, zabezpieczonych architektur AI z dołączonym modelem ROI. | Dyskusja i Prezentacje | Zapewnia, że liderzy techniczni mogą uzasadnić swoje wybory architektoniczne przed CFO, używając twardych liczb. |
| 16:30–17:00 | **Graduacja i Następne Kroki** | Podsumowanie 3-dniowego łuku, dystrybucja certyfikatów i 90-dniowy plan działania. | Ceremonia | Wysyła uczestników do domu z rozpędem i konkretną mapą drogową. |

---

## Co Uczestnicy Wyniosą ze Szkolenia

1. **Production-Ready Prompt Cookbook**: Biblioteka starannie zaprojektowanych promptów RTF i Chain-of-Thought, specjalnie dostrojonych do wymuszania deterministycznych outputów JSON dla workflow Pega Intelligent Intake.

2. **Zweryfikowany Kalkulator ROI**: Konkretny model matematyczny mapujący koszty tokenów API (Claude, Gemini, GPT-4o) na zaoszczędzone godziny pracy, udowadniający dokładny punkt rentowności dla konkretnych przypadków użycia.

3. **Funkcjonalna Architektura Agenta ReAct**: Zmapowana wieloetapowa pętla logiczna (Thought -> Action -> Observation) gotowa do integracji z Pega GenAI Connectors do obsługi Generative Action i Case Routing.

4. **Playbook Bezpieczeństwa Red Teaming**: Udokumentowana lista przetestowanych Guardrails i strategii delimiterów XML, aktywnie zapobiegających podatnościom OWASP Top 10, takim jak pośredni prompt injection i wyciek danych.

5. **Zautomatyzowany Framework Ewaluacji**: Kuratorowany pipeline "Golden Dataset" wykorzystujący LLM-as-a-Judge do wykonywania matematycznych testów regresyjnych na języku naturalnym, zapewniający że przyszłe aktualizacje AI nigdy nie zepsują produkcji.
