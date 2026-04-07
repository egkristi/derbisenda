# Derbi Senda – Dokumentasjon

Samlet teknisk dokumentasjon, vedlikeholdsguider og eierinformasjon for Derbi Senda 50cc mopeder (L1e).

> **Ny eier?** Start her → [Kom i gang](quick-start.md)

---

## Mine kjøretøy

| Modell | Reg.nr | VIN | Motor | Variant |
|--------|--------|-----|-------|---------|
| [Senda R 50 – 2004](models/senda-r-2004/) | NL 3874 | VTHSR1B1A4H248026 | EBS050 | Enduro (21"/18" hjul) |
| [Senda SM X-Trem 50 – 2005](models/senda-sm-xtrem-2005/) | AU 7933 | VTHSR2B1A5H281277 | EBE050 | Supermotard (17" hjul) |

---

## VIN-dekoding

Derbi Senda bruker 17-tegns VIN etter følgende struktur:

| Posisjon | Kode | Betydning |
|----------|------|-----------|
| 1–3 (WMI) | **VTH** | Produsent: Derbi / Nacional Motor S.A., Spania |
| 4–5 | **SR** | Modell: Senda |
| 6 | **1** / **2** | Variant: **1** = R (Enduro), **2** = SM (Supermotard) |
| 7 | **B** | Karosseritype |
| 8 | **1** | Motortype: EBS050/EBE050 (50cc) |
| 9 | **A** | Kontrollsiffer |
| 10 | **4** / **5** / **6** … | Modellår: 4=2004, 5=2005, 6=2006 osv. |
| 11 | **H** | Produksjonsanlegg (Martorelles, Spania) |
| 12–17 | xxxxxx | Løpende produksjonsnummer |

### Mine VIN-er

```
NL 3874:  V T H S R 1 B 1 A 4 H 248026
                    │       │   └── 2004
                    │       └────── EBS050-motor
                    └────────────── Senda R (Enduro)

AU 7933:  V T H S R 2 B 1 A 5 H 281277
                    │       │   └── 2005
                    │       └────── EBE050-motor
                    └────────────── Senda SM (Supermotard)
```

> ⚠️ I overgangsåret 2005–2006 eksisterte to parallelle motorarkitekturer. VIN posisjon 8 = **1** betyr EBS/EBE-motor. **D50B0-deler er IKKE kompatible** – verifiser alltid.

---

## Kompatibilitetsmatrise

| Modell | Motor | Forgasser | Koblingsskjema | Ramme | Plattformdeling |
|--------|-------|-----------|----------------|-------|-----------------|
| Senda R 2004 | EBS050 | Dell'Orto PHVA 17,5 | Euro 2 | Stål perimeter | Gilera RCR 50 |
| Senda SM X-Trem 2005 | EBE050 | Dell'Orto PHVA 17,5 | Euro 2 | Stål perimeter | Gilera SMT 50 |

---

## Felles dokumentasjon

### Teknisk

| Emne | Fil |
|------|-----|
| Motor – EBS050/EBE050 | [engines/ebs050.md](engines/ebs050.md) |
| Forgasser – Dell'Orto PHVA 17,5 | [carburetors/dellorto-phva.md](carburetors/dellorto-phva.md) |
| Koblingsskjema – Euro 2 | [wiring/euro2.md](wiring/euro2.md) |
| Fargekodetabell | [wiring/color-codes.md](wiring/color-codes.md) |

### Vedlikehold

| Emne | Fil |
|------|-----|
| Vedlikeholdsplan | [maintenance/schedule.md](maintenance/schedule.md) |
| Momentspesifikasjoner | [maintenance/torque-specs.md](maintenance/torque-specs.md) |
| Væskeoversikt | [maintenance/fluids.md](maintenance/fluids.md) |

### Feilsøking

| Emne | Fil |
|------|-----|
| Ingen gnist | [troubleshooting/no-spark.md](troubleshooting/no-spark.md) |
| Starter ikke | [troubleshooting/no-start.md](troubleshooting/no-start.md) |
| Overoppheting | [troubleshooting/overheating.md](troubleshooting/overheating.md) |

### Deler og manualer

| Emne | Fil |
|------|-----|
| Deler-kompatibilitet | [parts/compatibility.md](parts/compatibility.md) |
| OEM-leverandører | [parts/oem-links.md](parts/oem-links.md) |
| Manualer og dokumentasjon | [manuals/](manuals/) |

---

## Norsk L1e-begrensning

Begge syklene er registrert som moped klasse L1e med topphastighet **45 km/t**. For å oppfylle dette er følgende typisk begrenset fra fabrikk:

| Begrensningspunkt | Metode |
|-------------------|--------|
| CDI | Begrenset til ~9400 RPM |
| Forgasser | Redusert hoveddyse (modellspesifikk størrelse) |
| Luftfilter | Kvelningsplate i innsugskanal |
| Eksosrør | Restriktor-baffler i ekspansjonskammer |
| Fremre tannhjul | Redusert fra 14T til 11–13T |

---

## Derbi-historie

Derbi (*DERivados de BIcicleta*) ble grunnlagt i **1922** av Simeó Rabasa i Singla som et sykkelverksted i Mollet del Vallès nær Barcelona, med fabrikk i Martorelles fra 1931. Selskapet ble Nacional Motor S.A. i 1950, vant **21 VM-titler** (50cc/80cc/125cc GP), og ble kjøpt av **Piaggio i 2001** (€34,99M). Martorelles-fabrikken stengte **22. mars 2013**.

Senda-plattformen ble lansert i **1993**, redesignet i 1995 med væskekjølt motor og 6-trinns girkasse, og produsert gjennom 22 generasjoner til 2023. Plattformen deles med **Gilera SMT/RCR 50**.

---

## Verksteder (Agder)

| Verksted | Lokalitet | Tjenester |
|----------|-----------|-----------|
| **Agder Teknikk AS** | Grimstad | Reparasjon, service, diagnose. CNC dreiing/fresing. [agderteknikk.no](https://agderteknikk.no/) |
| **Jorkjen MC A/S** | Arendal | Autorisert MC-verksted. Splitting av veivhus, lagerskifte, vinterlagring. [jorkjenmc.no](http://jorkjenmc.no/) |
| **Motor-Teknikk AS** | Kristiansand | BMW Motorrad, Honda. Deler og kompetanse. [motor-teknikk.no](https://motor-teknikk.no/) |
| **Bil og Bobil** | Grimstad | CFMoto/Ligier-forhandler. Vedlikehold, diagnostikk. [bilogbobil.no](https://www.bilogbobil.no/) |
| **TR Båt & Fritid** | Grimstad | Batterier, smøremidler, 2-taktsolje. [trbaat.no](https://trbaat.no/) |
| **MC-senteret** | Kristiansand | Dekk, drev, sikkerhetsutstyr. [mcsenteret.no](https://mcsenteret.no/) |
| **Runes Scooter & MC** | Nettbasert/region | Rask og rimelig. Brukte OEM-deler. [runes-scooter-mc.com](https://runes-scooter-mc.com/) |

---

## Forum og fellesskap

| Fellesskap | Detaljer |
|------------|---------|
| **Mopedportalen.com** | Norges største mopedforum. «Alt innen DERBI»-tråd: 17 834+ innlegg |
| **Twostrokerider.se** | Svensk forum med sterk norsk deltakelse |
| **GPR Camp** | Premier engelskspråklig Derbi-teknisk forum – [gprcamp.com/foro/](https://gprcamp.com/foro/) |
| **Derbi Senda Owners Club** | [Facebook-gruppe](https://facebook.com/groups/343346065709300/) |
| **Derbi-forum.nl** | Nederlandsk forum med verkstedmanualer |
| **ApriliaForum** | Delt plattform-diskusjoner – [apriliaforum.com](https://www.apriliaforum.com/) |

---

## Repo-struktur

```
derbisenda/
├── README.md                     ← du er her
├── models/
│   ├── senda-r-2004/             ← Senda R 50 Enduro (NL 3874)
│   └── senda-sm-xtrem-2005/      ← Senda SM X-Trem 50 (AU 7933)
├── engines/
│   └── ebs050.md
├── carburetors/
│   └── dellorto-phva.md
├── wiring/
│   ├── euro2.md
│   └── color-codes.md
├── maintenance/
│   ├── schedule.md
│   ├── torque-specs.md
│   └── fluids.md
├── troubleshooting/
│   ├── no-spark.md
│   ├── no-start.md
│   └── overheating.md
├── parts/
│   ├── compatibility.md
│   └── oem-links.md
├── manuals/
├── diagrams/
└── images/
```

---

*Sist oppdatert: April 2026*
