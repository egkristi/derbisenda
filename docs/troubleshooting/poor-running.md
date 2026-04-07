# Feilsøking: Dør på gass / går dårlig

## Symptom
Motoren starter og går på tomgang, men hakker, nøler eller dør ved gasspådrag. Kan også vise seg som ujevn gange, plutselige turtallsfall eller manglende kraft.

## Viktig: Isolér gassposisjonen

Forgasseren har **tre kretser** som styrer ulike gassposisjoner. Identifiser hvor problemet oppstår:

| Gassposisjon | Styres av | Justerbar komponent |
|---|---|---|
| Tomgang – ¼ gass | Luftskrue + tomgangsdyse | Luftskrue (1,5–2 svinger ut), pilot jet |
| ¼ – ¾ gass | Nål og nålposisjon | Nålklips (A13/A25) |
| ¾ – full gass | Hoveddyse | Main jet |

## Årsaker og løsninger

### Forgasserrelatert (vanligst)

| Årsak | Diagnose | Løsning |
|---|---|---|
| Tilstoppet tomgangsdyse | Hakker ved lav gass, staller ved forsiktig åpning | Rens pilot jet med forgasserrens + trykkluft |
| Tilstoppet hoveddyse | Mister kraft fra ¾ gass og opp | Rens main jet |
| Feil nålposisjon | Flat spot eller nøling ved ¼–¾ gass | Flytt nålklips ett hakk (ned = rikere, opp = magrere) |
| For liten hoveddyse | Dør / hakker ved full gass, hvit tennplugg | Større dyse (+2–3 numre) |
| For stor hoveddyse | Svart/våt plugg, treg respons, «boblende» lyd | Mindre dyse (−2–3 numre) |
| Flottørnivå feil | Over/undersvømmelse, ujevn tomgang | Juster flottør (mål: 18 ± 0,5 mm) |
| Skitten luftfilter | Rik blanding over hele registeret, svart plugg | Rens eller bytt luftfilter |

### Luftlekkasje (falsk luft)

| Årsak | Diagnose | Løsning |
|---|---|---|
| Sprukket innsugsgummi | Spray forgasserrens rundt manifolden med motor i gang – turtallsendring = lekkasje | Bytt innsugsgummi |
| Slitte veivakselsimringer | Ujevn tomgang, staller, dårlig respons. Lekkasje påvirker kveveompumping | Bytt simringer (krever motorsplitting) |
| Løs forgasser på manifold | Slangeklemme ikke stram nok | Stram / bytt slangeklemme |
| Ublendet oljepumpenippel | Kjører premix men oljepumpe-nippelen er åpen | Tett nippelen helt |

### Eksosrelatert

| Årsak | Diagnose | Løsning |
|---|---|---|
| Karbontilstoppet eksospotte | Kraftig ytelsestap over ~5000 RPM, svart røyk | Brenn ut eksospot (gassbrener) eller bytt |
| Karbontilstoppet eksosport | Turtallet «kapper seg» tidlig | Skrap karbon fra eksosporten (demonter sylinder) |

### Tenningsrelatert

| Årsak | Diagnose | Løsning |
|---|---|---|
| Svak gnist | Motoren går, men hakker under belastning | Sjekk plugghette (~5 kΩ), tennspole, CDI |
| Feil tennplugg/gap | Feil varmeverdi eller gap ≠ 0,6 mm | Bytt til NGK BR9ES, gap 0,6 mm |
| Defekt CDI (intermitterende) | Sporadiske mistenninger, dør tilfeldig | Bytt CDI |

## Diagnostikkflyt

```
1. Når oppstår problemet?
   ├── Ved all gasspådraging →
   │   2. Sjekk luftfilter (rent?)
   │      ├── Skittent → Rens/bytt → test igjen
   │      └── Rent →
   │          3. Sjekk for luftlekkasje (spray-test)
   │             ├── Lekkasje funnet → Fiks pakninger/simringer
   │             └── Ingen lekkasje →
   │                 4. Sjekk tennplugg (farge?)
   │                    ├── Hvit → For mager. Større dyse / senk nål
   │                    ├── Svart/våt → For rik. Mindre dyse / hev nål
   │                    └── Brun → OK, sjekk eksospotte
   │
   ├── Kun ved lav gass (tomgang–¼) →
   │   Tilstoppet pilot jet eller feil luftskrue.
   │   Rens tomgangsdyse, juster luftskrue (1,5–2 svinger ut)
   │
   ├── Kun ved mellomgass (¼–¾) →
   │   Feil nålposisjon. Flytt klips ett hakk ned (rikere)
   │   eller opp (magrere). Prøvekjør.
   │
   └── Kun ved full gass (¾–WOT) →
       Feil hoveddyse. Gjør plug chop:
       Kjør full gass 30 sek → kill switch → les plugg
```

## «Plug chop»-referanse

| Plugg-farge | Betydning | Tiltak |
|---|---|---|
| Hvit / lys | For mager (farlig!) | Større dyse +2–3 |
| Lys brun / beige | Korrekt | Ingen endring |
| Mørk brun / svart | For rik | Mindre dyse −2–3 |
| Våt / oljete | Oversvømt eller for mye olje | Sjekk flottør, oljeblanding |

## Se også

- [Forgasser – Dell'Orto PHVA](../carburetors/dellorto-phva.md)
- [Feilsøking: Starter ikke](no-start.md)
- [Feilsøking: Ingen gnist](no-spark.md)
- [Vedlikeholdsplan](../maintenance/schedule.md)
