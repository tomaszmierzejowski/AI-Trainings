# Szablon skryptu 60 s — v2 (po audycie 2026-07-06)

## Anatomia filmu

| Sekcja | Czas | Zadanie | Zasada |
|---|---|---|---|
| HOOK | 0–3 s | zatrzymać kciuk | **mówiony hook ≤ 8 słów**; kontekst idzie na nakładkę tekstową (overlay), nie w usta |
| STAKE | 3–10 s | "dlaczego mnie to dotyczy" | widz, nie technologia |
| MEAT | 10–45 s | JEDNA zmiana zachowania | badge-stempel na ekranie przy każdej liczbie: [BADANIE] / [MOJA PRAKTYKA] / [OPINIA] |
| CTA | 45–58 s | pytanie na 1 szczere zdanie | komentarze > "obserwuj mnie" |
| SYGNATURA | ostatnie 2 s | dżingiel słowny | **zawsze, w każdym filmie, te same słowa:** "AI to Twój pierwszy krok. Nie jedyny. Pierwszy." |

## Reguły niezmienne

1. **Hook mówiony ≤ 8 słów.** Stary, dłuższy hook nie ginie — zostaje jako text overlay i pierwsze zdanie opisu.
2. **Sygnatura zamyka każdy film** — bez wyjątków, także LIFE i ZK. Sygnatura audio = rozpoznawalność.
3. **Reguła błędu warunkowego (DEMO):** halucynacji nie da się zaplanować. Każdy skrypt DEMO ma dwa
   zakończenia sekcji weryfikacji:
   - **(a) AI się pomyliło** → pokaż błąd i korektę na ekranie;
   - **(b) AI czyste** → powiedz wprost: *"Dziś czysto. Ale błędy są losowe — dlatego weryfikacja jest stała."*
   Inscenizowanie błędu = zakaz absolutny.
4. Żaden MIND bez historii lub artefaktu (zdjęcie, prawdziwy ekran, prawdziwa poprawka).
5. Napisy zawsze; cięcie co 3–5 s; 9:16; jedna idea na film.
6. Opis + hashtagi generuje Claude per platforma (TT luźny / YT z keywordami "AI po polsku").

## Przykład kompletny: odcinek 1.1 — patrz `Scripts/Week1_Scripts.md`.
## Format ZNAJDŹ KŁAMSTWO — patrz `Scripts/ZK_Znajdz_Klamstwo.md`.

---

## Prompt produkcyjny (wklej do Claude w poniedziałek)

```
Przygotuj skrypty wideo na tydzień VN wg Content_Calendar.md.
Użyj szablonu Video_Script_Template.md v2: hook mówiony ≤8 słów + overlay,
sygnatura na końcu, reguła błędu warunkowego w DEMO, badge przy każdej liczbie,
zakazy z README (sekcja 7). Dla MIND adaptuj copy_PL z LinkedIn_Mindset_Campaign/posts/.
Dodatkowo: materiał ZK#N wg ZK_Znajdz_Klamstwo.md (typ błędu z rotacji, rozwiązanie ZK#N-1).
Do każdego odcinka: 3 warianty hooka ≤8 słów, opis TT/IG/YT, hashtagi.
Po polsku, mój ton: dowody + suchy humor.
```
