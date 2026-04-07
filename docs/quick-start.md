# Kom i gang

Du har nettopp kjøpt en Derbi Senda 50cc — hva nå? Denne siden guider deg gjennom det viktigste.

---

## 1. Finn ut hvilken modell du har

Sjekk VIN-nummeret på styrehodet (høyre side av rammen). De viktigste sifrene:

| VIN-posisjon | Betydning |
|---|---|
| 4–5: **SR** | Senda-modell |
| 6: **1** = R (Enduro), **2** = SM (Supermotard) | Variant |
| 8: **1** | EBS/EBE-motor (50cc) |
| 10: **4** = 2004, **5** = 2005 … | Årsmodell |

Full VIN-dekoding: [Hovedsiden](README.md#vin-dekoding)

---

## 2. Sjekk det viktigste først

Før du kjører — gå gjennom disse punktene:

### Væsker

| Hva | Sjekk | Spesifikasjon |
|---|---|---|
| Kjølevæske | Ekspansjonsbeholder på rammen | 50/50 G12/G13 + destillert vann |
| 2-taktsolje | Oljebeholder (om oljepumpe brukes) | JASO FD syntetisk |
| Girolje | Nivåskrue på motorblokkens høyre side | 10W-40 eller 75W90 GL-4, 650–750 ml |
| Bremsevæske | Beholderen på styrehåndtaket | DOT 4 |

Detaljer: [Væskeoversikt](maintenance/fluids.md)

### Tenning

Motoren starter ikke? Sjekk i denne rekkefølgen:

1. **Tennplugg** — NGK BR9ES, gap 0,6 mm. Bytt om i tvil.
2. **Bensin** — Noe i tanken? Er bensinkranen åpen (vakuumstyrt)?
3. **Gnist** — Hold pluggen mot blokken og spark. Ingen gnist? → [Feilsøking: ingen gnist](troubleshooting/no-spark.md)

Full feilsøking: [Starter ikke](troubleshooting/no-start.md)

---

## 3. Kjenn igjen de vanlige problemene

| Symptom | Mest sannsynlig årsak | Guide |
|---|---|---|
| Starter ikke | Tennplugg, forgasser, bensin | [Starter ikke](troubleshooting/no-start.md) |
| Ingen gnist | CDI, stator, kill-switch | [Ingen gnist](troubleshooting/no-spark.md) |
| Overoppheting | Kjølevæske, termostat, vannpumpe | [Overoppheting](troubleshooting/overheating.md) |
| Går dårlig / hakker | Skitten forgasser, luftlekkasje | [Forgasser](carburetors/dellorto-phva.md) |

---

## 4. Grunnleggende vedlikehold

### Hver 500 km
- Rens luftfilter
- Sjekk kjede (20–30 mm slakk)
- Sjekk bremser

### Hver 2000 km
- Bytt tennplugg
- Rens forgasser
- Sjekk kjølevæskenivå

### Årlig / sesongstart
- Bytt girolje
- Sjekk kjølevæske
- Smør kabler og kjede
- Sjekk bremsevæske

Full plan: [Vedlikeholdsplan](maintenance/schedule.md)

---

## 5. Viktige spesifikasjoner

| Parameter | Verdi |
|---|---|
| Tennplugg | NGK BR9ES, gap 0,6 mm |
| Dekk foran (R) | 80/90-21 |
| Dekk foran (SM) | 100/80-17 |
| Dekk bak (R) | 110/80-18 |
| Dekk bak (SM) | 130/70-17 |
| Kjede | 420, slakk 20–30 mm |
| Fremre tannhjul | 14T (ubegrenset) |
| Bakre tannhjul | 52T |
| Tennplugg-moment | 18 Nm |
| Sylinderhode-moment | 12 Nm |

Alle moment: [Momentspesifikasjoner](maintenance/torque-specs.md)

---

## 6. Neste steg

- [Din modell i detalj](models/) — komplett spesifikasjon og historie
- [Motor (EBS/EBE)](engines/ebs050.md) — smøring, kjøling, stempelkoder
- [Forgasser](carburetors/dellorto-phva.md) — jetting, montering, slanger
- [Koblingsskjema](wiring/euro2.md) — CDI, stator, feilsøking
- [Deler og leverandører](parts/oem-links.md) — hvor du handler
