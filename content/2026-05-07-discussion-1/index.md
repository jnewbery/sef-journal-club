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
- This exposes DHN operators to volatile electricity prices.
- [Pit Thermal Energy Storage (PTES)](https://www.sciencedirect.com/topics/engineering/pit-thermal-energy-storage) are large bodies of water used to store
  thermal energy in water as sensible heat. They've often been used for _seasonal_
  storage to maximise the share of solar thermal energy in a DHN.
- The paper investigates whether a PTES can be used for short-term thermal
  energy storage, by using heat-to-power to charge when electricity prices
  are low, and discharging within hours or days to meet heat demand.
- Short-term thermal energy storage has usually been provided by Tank Thermal
  Energy Storage (TTES). PTES can be much cheaper on a per-kWh basis.
- The paper uses a a TRNSYS simulation of a real Danish city with a
  linear-programming dispatch controller
- The study finds that adding a 60,000 m³ PTES reduces the levelised cost of
  heat by 14%, with an investment payback period of approximately one year.

<img src="2026-05-07-discussion-1/model.png" width="80%"></img>

---

### Key result

| Scenario | LCOH (€/MWh) | Payback |
|---|---|---|
| Reference (heat pumps + boilers, no storage) | 44.4 | — |
| + PTES (60,000 m³, 90 MW charge rate, optimised) | 38.1 | ~1 year |
| + lower charge temperature (80°C) | 36.8 | < 1 year |
| + 3-week optimisation horizon | 37.7 | < 1 year |

---

### Discussion questions

1. The dispatch controller assumes perfect foresight of electricity prices and
   heat demand over a 14-day horizon. How realistic is this? What other models
   could be used? Are there other sources of uncertainty?
2. Do you think that thermal energy storage will play a significant role in the
   energy transition in the UK or your own country? What advantages does it have
   over other forms of flexibility? What barriers or challenges exist preventing
   wider deployment?
3. _For the economic calculations in this study, simulations were run for a
   period of 25 years at a 1-hour timestep. However, since only data for 2021
   were available, they were repeated for each year of the simulation period._
   
   The simulation repeats 2021 data which had an atypical electricity price
   spike driven by the European gas crisis. How sensitive are the payback and
   LCOH figures to the assumed electricity price profile, and what does a more
   conservative scenario look like?

<img src="2026-05-07-discussion-1/variables.png" height="600px"></img>

---

### Further reading

- **Sifnaios et al.** — paper reporting the performance
  analysis of the first real short-term PTES, built in Høje Taastrup, Denmark
  [https://doi.org/10.1016/j.est.2025.117504](https://doi.org/10.1016/j.est.2025.117504)
- **Tosatto et al.** — simulation-based performance evaluation
  of large-scale thermal energy storage coupled with heat pumps in district
  heating. *J. Energy Storage*, 61, 106721.
  [doi.org/10.1016/j.est.2023.106721](https://doi.org/10.1016/j.est.2023.106721)
- **Sifnaios** — the lead author's PhD thesis, providing a broader
  treatment of PTES in district heating systems. DTU.
  [doi.org/10.11581/DTU.00000291](https://doi.org/10.11581/DTU.00000291)
