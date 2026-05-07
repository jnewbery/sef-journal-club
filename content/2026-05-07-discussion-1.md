Title: Integration of pit thermal energy storages into district heating networks – a techno-economic case study
Date: 2026-05-07
Slug: 2026-05-07-discussion-1
Meeting: 2026-05-07
Topic: 1
Presenter: John
Link: https://doi.org/10.1016/j.applthermaleng.2025.127770

**Full citation:** Sifnaios I., Fan J., Jensen A.R. (2025). *Applied Thermal Engineering*, 279, 127770.

---

### Summary of Paper


- District Heating Network (DHN) operators are replacing fossil fuel based
  boilers and CHPs with heat pumps and electric boilers for several reasons:
  - To utilise cheap electricity and increase the utilisation of renewable
    energy sources.
  - To reduce carbon emissions and meet climate targets.
  - To improve air quality by eliminating local combustion.
- This exposes DHN operators to volatile electricity prices, w
As district heating operators replace gas plant with heat pumps and electric
boilers, their costs become tightly coupled to volatile electricity prices.

This paper investigates whether a pit thermal energy storage (PTES) — a large
water-filled excavation, much cheaper than conventional steel tanks — can act
as a short-term thermal battery: charging when electricity is cheap,
discharging when it is expensive. Using a TRNSYS simulation of a real Danish
city with a linear-programming dispatch controller, the study finds that adding
a 60,000 m³ PTES reduces the levelised cost of heat by 14%, with an investment
payback period of approximately one year.

---

### Key result

| Scenario | LCOH (€/MWh) | Payback |
|---|---|---|
| Reference (heat pumps + boilers, no storage) | 44.4 | — |
| + PTES (60,000 m³, 90 MW charge rate, optimised) | 38.1 | ~1 year |
| + lower charge temperature (80°C) | 36.8 | < 1 year |
| + 3-week optimisation horizon | 37.7 | < 1 year |

A counterintuitive finding: for short-term operation, increasing the
charge/discharge *power* (MW) is often more cost-effective than increasing the
storage *volume* (MWh). Beyond a charge rate matching the system's peak load
(~90 MW here), larger volumes bring diminishing returns.

---

### Discussion questions

1. The dispatch controller assumes perfect foresight of electricity prices and
   heat demand over a 14-day horizon. The authors show that a 3-week horizon is
   worth 4% LCOH compared to 1 week. How much of the reported economic benefit
   depends on this assumption, and how would imperfect forecasts change the
   picture?
2. The 25-year simulation repeats 2021 data, a year with an atypical
   electricity price spike driven by the European gas crisis. How sensitive are
   the payback and LCOH figures to the assumed electricity price profile, and
   what does a more conservative scenario look like?
3. Land costs are excluded from the analysis. The PTES modelled is 60,000 m³,
   requiring a substantial footprint. In what urban or peri-urban contexts
   would land costs change the investment calculus, and how should planners
   account for this?

---

### Further reading

- **Sifnaios et al. (2025b)** — companion paper reporting the performance
  analysis of the first real short-term PTES, built in Høje Taastrup, Denmark
  (89% energy efficiency, 75% exergy efficiency).
  [doi.org/10.1016/j.est.2025.116232](https://doi.org/10.1016/j.est.2025.116232)
- **Tosatto, Dahash & Ochs (2023)** — simulation-based performance evaluation
  of large-scale thermal energy storage coupled with heat pumps in district
  heating. *J. Energy Storage*, 61, 106721.
  [doi.org/10.1016/j.est.2023.106721](https://doi.org/10.1016/j.est.2023.106721)
- **Sifnaios (2023)** — the lead author's PhD thesis, providing a broader
  treatment of PTES in district heating systems. DTU.
  [doi.org/10.11581/DTU.00000291](https://doi.org/10.11581/DTU.00000291)
