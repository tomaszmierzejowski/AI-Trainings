> **⚠️ DEPRECATION NOTICE (2026-07-19):** The Alpha–Epsilon codename scheme used throughout this package is **retired**. The 4 approved case studies are now: **Proof of Scale**, **Invisible Risk**, **Proof of Speed**, **The Rescue**. See `SOURCE_OF_TRUTH.md` for current names, approved facts, and banned claims. Do NOT use codenames from this file for any new or published content.

# NotebookLM Package — AI App Modernization Factory
## Przygotowany: lipiec 2026

---

## Cel

Ten folder zawiera zanonimizowane materiały przygotowane jako wsad dla Google NotebookLM.
Materiały są przeznaczone do generowania podcastu w formacie debaty (sceptyk vs. obrońca)
oraz do tworzenia prezentacji i innych treści na temat projektu AI App Modernization Factory.

---

## Ważne: Anonimizacja

Wszystkie nazwy klientów zostały zastąpione nazwami kodowymi.
**Nazwy kodowe Alpha–Epsilon są WYCOFANE.** Poniższa tabela pokazuje mapowanie na aktualne, zatwierdzone nazwy case studies (patrz `SOURCE_OF_TRUTH.md`):

| Nazwa kodowa (RETIRED) | Aktualna nazwa | Kontekst |
|------------------------|----------------|---------|
| **Project Alpha** → | **Proof of Scale** | 20 legacy apps, 187 endpoints, 3 weeks vs 8–14 |
| **Project Beta** → | **Invisible Risk** | 529 unauthenticated endpoints, 97 projects, 17 modules, 100+ business rules |
| **Project Gamma** → | **Proof of Speed** | Xamarin→MAUI in 4 days |
| **Project Delta** → | **The Rescue** | Public Institute, 200+ CVEs, 2-year deployment block |
| **Project Epsilon** | *(brak odpowiednika)* | Retired — nie ma odpowiednika w bieżących 4 case studies |

Sopra Steria pozostaje wymieniona jako organizacja prowadząca projekt (to nasza firma).

---

## Pliki w pakiecie

### 01_AMF_Overview_and_Mission.md
**Dla NotebookLM:** Całościowy przegląd projektu — czym jest Factory, metryki kluczowe, porównanie z tradycyjnym consultingiem, model cenowy.

*Najlepszy punkt startowy — definiuje cały kontekst.*

### 02_AMF_Case_Studies.md
**Dla NotebookLM:** 5 szczegółowych case studies (Projects Alpha–Epsilon) z wynikami, znaleziskami i ROI. Zawiera oryginalną wiadomość od klienta (zanonimizowaną).

*Najsilniejsze materiały dowodowe — konkretne liczby i wyniki.*

### 03_AMF_Methodology_How_We_Work.md
**Dla NotebookLM:** Metodologia — model 60-godzinny, trzy fazy dostarczania, pięć zasad, różnica między factory a tradycyjnym consultingiem.

*Wyjaśnia "dlaczego to działa" — dobre dla strony obrońcy w debacie.*

### 04_AMF_Evidence_and_Customer_Voice.md
**Dla NotebookLM:** Prawdziwe opinie klientów (zanonimizowane), walidacja third-party, wyjaśnienie czym jest "evidence-linked reporting" i dlaczego to inna jakość niż tradycyjne raporty.

*Ludzki wymiar — wiadomość z Wigilii Bożego Narodzenia od klienta Project Gamma.*

### 05_AMF_Security_Intelligence.md
**Dla NotebookLM:** Kompletny raport bezpieczeństwa — wszystkie rodzaje znalezisk, CVEs, compliance gaps, ROI z perspektywy security prevention.

*Materiał dla sceptyka: "skąd wiecie, że te znaleziska są prawdziwe?" — i dla obrońcy: "każde jest linkowane do konkretnej linii kodu".*

### 06_AMF_Business_Case_ROI.md
**Dla NotebookLM:** Argumentacja biznesowa — tabele kosztów, kalkulacje ROI, model AMaaS, cennik portalu, argument Total Cost of Ownership.

*Dla C-level i finansowej strony debaty.*

### 07_AMF_Testing_Zero_Regressions.md
**Dla NotebookLM:** Framework testowy — dlaczego legacy systemy nie mają testów, jak AI generuje testy, wyjaśnienie zero-regression delivery.

*Techniczny fundament dla obrońcy w debacie.*

### 08_AMF_Podcast_Debate_Brief.md
**Dla NotebookLM:** KLUCZOWY PLIK DLA PODCASTU — 6 najsilniejszych argumentów sceptyka + 6 odpowiedzi obrońcy oparte na faktach. Gotowy brief dla obu stron debaty.

*Wgraj ten plik ostatni — to instrukcja dla NotebookLM jak zbudować debatę.*

### 09_AMF_Market_Context_2026.md
**Dla NotebookLM:** Kontekst rynkowy — dlaczego legacy modernization jest pilna, dane rynkowe, regulatory pressure (GDPR, NIS2, PCI-DSS), krajobraz konkurencyjny.

*Szerszy kontekst dla podcastu — "dlaczego teraz?" i "czy to już nie istnieje?".*

### 10_PODCAST_PROMPT_CEO_and_Architects.md
**Dla NotebookLM:** Gotowy prompt do generowania podcastu CEO + architektów — debata o Factory vs. scentralizowana platforma AI.

*Użyj po wgraniu plików 01–09 — wklej prompt z tego pliku w NotebookLM Audio Overview → Customize.*

---

## Instrukcja dla NotebookLM

1. Utwórz nowy notebook
2. Dodaj wszystkie 11 plików .md (00–10) jako źródła
3. Opcjonalnie: dodaj wybrane pliki HTML z folderu Presentations (np. AI_Modernization_Pitch_Deck.html, AI_Factory_CEO_Dashboard.html)
4. Generuj podcast: *"Create a podcast debate where one side challenges whether the AI App Modernization Factory achievements are real and impressive, while the other defends the evidence and results. Use the debate brief in document 08 as your structure."*

---

## Najlepsze pliki HTML z Presentations (opcjonalne dodanie do NotebookLM)

Te pliki zawierają unikalne treści i mogą uzupełnić pakiet:

| Plik | Dlaczego warto |
|------|----------------|
| AI_Modernization_Pitch_Deck.html | Najbardziej kompletny pitch — już używa Project Alpha/Beta/Gamma kodowania |
| AI_Factory_CEO_Dashboard.html | Kompaktowy dashboard z CEO-level metrykami |
| Autosync_Discovery_Slide.html | Szczegółowy raport discovery — uwaga: zawiera "Autosync" (anonimizować przed uploadem) |
| AI_Testing_Framework_Presentation.html | Framework testowy z wynikami |
| TechTribe_AI_App_Modernization_Section.html | Najnowsze pozycjonowanie 2026 |

---

## Pliki pominięte (nie dołączać do NotebookLM)

- Pliki PL i FR — wersje językowe, nie dodają nowych faktów
- `AMaaS_LinkedIn_Campaign_Prompts.md` — instrukcje promptów, nie treść
- `Poland_Customer_Discovery_Presentation_Prompt.md` — instrukcje promptów
- `AI_Modernization_Executive_Presentation_2026_Outline.md` — outline bez treści
- `generate_dashboard.py` — skrypt techniczny
- Stare wersje PPTX (2025-v1, Sopra C-Level v2) — zastąpione przez nowsze

---

## Pliki usunięte z Presentations (10.2025–06.2026 cleanup)

Usunięte jako jednoznacznie zastąpione przez nowsze wersje:
- `Poland_Discovery_Presentation_v2.html` → zastąpiony przez v3
- `LWT_App_Modernization_Factory_EN.html` → zastąpiony przez EN_v2
- `AI_Modernization_Executive_Presentation_2026_Static.html` → zastąpiony przez interaktywną wersję
