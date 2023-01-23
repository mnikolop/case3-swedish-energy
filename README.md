# Energy consumption/production in sweden

# Background infromation

This project was performed as an internal case for Adage ab. It aimed to create a forecasting model for resource management/planning. It was run as a data science project simulating interactions with the client and processes.

Original Dataset: All the [datasets](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/) stored under the energy tag, of the SCB (Statistikmyndigheten) database (Statistikdatabasen). That was then reduced significantly, see Implementation.

Duration: 01.12.2022 - x.01.2023

---

# Problem definition

## Situation

Energy is being produced and consumed around sweden in different types and levels of renewability. It has been identified that there is a difference of what types of energy each region produces though time as well as what types of energy is being consumed byt the different sectors in each region
With energy consumption needs staying the same (if not increasing over time), it is important to identify more sustainable ways to cover those needs.

## Complication

## Question

We are hypothesizing that it is possible to create forecasting models to satisfy the energy needs that are forecasted for the same periods.

## Answer

It is possible to create forecasting models to match consumption to production of energy.

---

# Implementation

## Data preparation

### Dataset preparation

- original files extracted: 107
  - Contain fragments of datasets
  - Action:
    - Grouped to create full datasets
- After grouping: 37 datasets
  - Contain different levels of seasonality
  - Contain irrelevant information
  - Action:
    - Selecting relevant datasets with the same seasonality
- Datasets to use after selection: 6
  - Have yearly data
  - Have regions (except 1)
  - Contain info about production and consumption of energy

### Data grouping

The energy types in the data were too many, so they were grouped in the following way.

#### Bränsletyp

| typ                 | icke-förnybar/förnybar | bransletyp namn                                       |
| ------------------- | ---------------------- | ----------------------------------------------------- |
| flytande bransletyp | icke-förnybar          | motorbensin                                           |
| flytande bransletyp | icke-förnybar          | bensin                                                |
| flytande bransletyp | icke-förnybar          | diesel                                                |
| flytande bransletyp | icke-förnybar          | diesel/EO1                                            |
| flytande bransletyp | icke-förnybar          | stenkol                                               |
| flytande bransletyp | icke-förnybar          | fotogen                                               |
| flytande bransletyp | icke-förnybar          | naturgas                                              |
| flytande bransletyp | icke-förnybar          | varav diesel                                          |
| flytande bransletyp | icke-förnybar          | dieselbr�nsle                                         |
| flytande bransletyp | icke-förnybar          | E85                                                   |
| flytande bransletyp | icke-förnybar          | avfall                                                |
| flytande bransletyp | icke-förnybar          | propan och butan                                      |
| flytande bransletyp | icke-förnybar          | torv och torvbriketter<!--peat and peat briquettes--> |
| flytande bransletyp | icke-förnybar          | stadsgas och koksugnsgas                              |
| flytande bransletyp | icke-förnybar          | masugnsgas inkl. LD-gas                               |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 1                                     |
| flytande bransletyp | icke-förnybar          | eldningsolja 1                                        |
| flytande bransletyp | icke-förnybar          | varav eldningsolja 1                                  |
| flytande bransletyp | icke-förnybar          | eldningsolja 2                                        |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 2                                     |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 2 och 3                               |
| flytande bransletyp | icke-förnybar          | eldningsolja 2-6                                      |
| flytande bransletyp | icke-förnybar          | eldningsolja 3-6                                      |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 3-5                                   |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 1 d�rav ej SNI 05-33, 35              |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 2 inkl. WRD                           |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 2 inkl. WRD d�rav ej SNI 05-33        |
| flytande bransletyp | icke-förnybar          | Eldningsolja nr 2-5                                   |
| flytande bransletyp | icke-förnybar          | Eldningsolja nr 2-5 d�rav ej SNI 05-33, 35            |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 3-6                                   |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 3-6 d�rav ej SNI 05-33, 35            |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 4                                     |
| flytande bransletyp | icke-förnybar          | eldningsolja nr 5 och d�r�ver                         |
| flytande bransletyp | icke-förnybar          | flytande (icke f�rnybara)                             |
| fast bransletyp     | icke-förnybar          | fast (icke f�rnybara)                                 |
| gas bransletyp      | icke-förnybar          | gas (icke f�rnybara)                                  |
| --------------      | -------------          | ---------------------                                 |
| flytande bransletyp | förnybar               | FAME                                                  |
| flytande bransletyp | förnybar               | f�r�dlade tr�dbr�nslen                                |
| flytande bransletyp | förnybar               | tr�dbr�nslen exklusive f�r�dlade tr�dbr�nslen         |
| flytande bransletyp | förnybar               | HVO                                                   |
| flytande bransletyp | förnybar               | etanol                                                |
| flytande bransletyp | förnybar               | biogas                                                |
| flytande bransletyp | förnybar               | svartlutar, tall- och beckolja                        |
| flytande bransletyp | förnybar               | flytande (f�rnybara)                                  |
| fast bransletyp     | förnybar               | fast (f�rnybara)                                      |
| gas bransletyp      | förnybar               | gas (f�rnybara)                                       |
| --------------      | -------------          | ---------------------                                 |
| okand bransletyp    | ökand                  | NAN                                                   |
| okand bransletyp    | ökand                  | elproduktion                                          |
| okand bransletyp    | ökand                  | el                                                    |
| okand bransletyp    | ökand                  | fj�rrv�rme                                            |
| okand bransletyp    | ökand                  | annat br�nsle                                         |
| --------------      | -------------          | ---------------------                                 |
| okand bransletyp    | summa                  | summa br�nsle och drivmedel                           |
| okand bransletyp    | summa                  | summa produktionss�tt                                 |
| okand bransletyp    | summa                  | summa f�rbrukarkategori                               |

#### Produktionssatt

| typ              | icke-förnybar/förnybar | bransletyp namn                                   |
| ---------------- | ---------------------- | ------------------------------------------------- |
|                  | icke-förnybar          | kraftv�rmeverk + industriellt mottryck            |
|                  | icke-förnybar          | �vrig v�rmekraft (k�rnkraft, kondenskraft o.dyl.) |
|                  | icke-förnybar          | kraftv�rmeverk                                    |
|                  | icke-förnybar          | frist�ende v�rmeverk                              |
|                  | icke-förnybar          | spillv�rme                                        |
|                  | icke-förnybar          | r�kgaskondens                                     |
|                  | icke-förnybar          | kraftv�rme-v�rmeverk, kraftv�rmedrift             |
|                  | icke-förnybar          | kraftv�rme-v�rmeverk, enbart v�rmeproduktion      |
|                  | icke-förnybar          | frist�ende v�rmeverk                              |
| ---              | ---------------------- | ---------------                                   |
|                  | förnybar               | vattenkraft                                       |
|                  | förnybar               | vindkraft                                         |
| ---              | ---------------------- | ---------------                                   |
|                  | kärnkraft              | �vrig v�rmekraft (k�rnkraft, kondenskraft o.dyl.) |
| ---              | ---------------------- | ---------------                                   |
| okand bransletyp | okand                  | elpannor (1)                                      |
| okand bransletyp | okand                  | v�rmepumpar (2)                                   |
| okand bransletyp | summa                  | summa                                             |
| okand bransletyp | summa                  | summa br�nsletyp                                  |

#### Kategori

| typ              | icke-förnybar/förnybar | bransletyp namn                                  |
| ---------------- | ---------------------- | ------------------------------------------------ |
|                  | icke-förnybar          | 3.4 insats V�rmekraftverk (ej k�rn-)             |
|                  | icke-förnybar          | 3.5 insats Indust.mottrycksanl.                  |
|                  | icke-förnybar          | 3.6.1 insats Kraftv�rmeverk, fj�rrv�rmeprod.     |
|                  | icke-förnybar          | 3.6.2 insats Kraftv�rmeverk, elprod.             |
|                  | icke-förnybar          | 3.7 insats Frist�ende v�rmeverk                  |
|                  | icke-förnybar          | 4.4 omvandlat V�rmekraftverk (ej k�rn-)          |
|                  | icke-förnybar          | 4.5 omvandlat Industr.mottrycksanl.              |
|                  | icke-förnybar          | 4.6 omvandlat Kraftv�rmeverk                     |
|                  | icke-förnybar          | 4.6.2 omvandlat Spec. Kraftv.spillv�rme          |
|                  | icke-förnybar          | 4.7 omvandlat Frist�ende v�rmeverk               |
|                  | icke-förnybar          | 4.7.2 omvandlat Spec.Frist.v�rmev. spillv�rme    |
|                  | icke-förnybar          | 5.4 AnvEnSektor V�rmekraftverk (ej k�rn-)        |
|                  | icke-förnybar          | 5.5 AnvEnSektor Industr.mottrycksanl�ggning      |
|                  | icke-förnybar          | 5.6 AnvEnSektor Kraftv�rmeverk                   |
|                  | icke-förnybar          | 5.7 AnvEnSektor Frist�ende v�rmeverk             |
|                  | icke-förnybar          | 7 �verf�ringsf�rluster                           |
|                  | icke-förnybar          | 9.2 slutanv. Industri, byggverks.                |
| ---              | ---------------------- | ---------------                                  |
|                  | kärnkraft              | 5.3 AnvEnSektor K�rnkraftverk                    |
|                  | kärnkraft              | 3.3 insats K�rnkraftverk                         |
|                  | kärnkraft              | 4.3 omvandlat K�rnkraftverk                      |
| ---              | ---------------------- | ---------------                                  |
|                  | förnybar               | 9.1 slutanv. Jordbruk,skogsbruk,fiske            |
|                  | förnybar               | 3.1 insats Vattenkraftstationer                  |
|                  | förnybar               | 3.2 insats Vindkraftverk                         |
|                  | förnybar               | 4.1 omvandlat Vattenkraftstationer               |
|                  | förnybar               | 4.2 omvandlat Vindkraftverk                      |
|                  | förnybar               | 5.1 AnvEnSektor Vattenkraftstationer             |
|                  | förnybar               | 5.2 AnvEnSektor Vindkraftverk                    |
| ---              | ---------------------- | ---------------                                  |
| okand bransletyp | okand                  | 5 anv i energisektor totalt                      |
| okand bransletyp | okand                  | 3.6.1.1 insats Spec. Fj�rrv�rme m. v�rmepumpar   |
| okand bransletyp | okand                  | 3.7.1 insats Spec.Frist�ende v�rmev. v�rmepumpar |
| okand bransletyp | okand                  | 4 omvandlat totalt                               |
| okand bransletyp | okand                  | 4.6.1omvandlat Spec. Kraftv.v�rmepumpar          |
| okand bransletyp | okand                  | 4.7.1 omvandlat Spec.Frist.v�rmev. v�rmepumpar   |
| okand bransletyp | okand                  | 5.6.1 AnvEnSektor Spec.Kraftv.v�rmepumpar        |
| okand bransletyp | okand                  | 5.7.1 AnvEnSektor Frist.v�rmev.v�rmepumpar       |
| okand bransletyp | okand                  | 9 slutlig anv�ndning totalt                      |
| okand bransletyp | okand                  | 2 bruttotillf�rsel                               |
| okand bransletyp | okand                  | 3 insatt f�r omvandling totalt                   |
| okand bransletyp | okand                  | 9.3 slutanv. Offentlig verksamhet                |
| okand bransletyp | okand                  | 9.4 slutanv. Transporter                         |
| okand bransletyp | okand                  | 9.5 slutanv. �vriga tj�nster                     |
| okand bransletyp | okand                  | 9.6 slutanv. Hush�ll                             |
| okand bransletyp | okand                  | 9.6.1 slutanv. Spec Hush�ll sm�hus               |
| okand bransletyp | okand                  | 9.6.1.1 slutanv. Spec Hush�ll eluppv.sm�hus      |
| okand bransletyp | okand                  | 9.6.2 slutanv. Spec Hush�ll flerbostadshus       |
| okand bransletyp | okand                  | 9.6.3 slutanv. Spec Hush�ll fritidshus           |

#### Energityp

| typ              | icke-förnybar/förnybar | bransletyp namn |
| ---------------- | ---------------------- | --------------- |
|                  | icke-förnybar          | stenkol         |
|                  | icke-förnybar          | koks            |
|                  | icke-förnybar          | bensin          |
|                  | icke-förnybar          | diesel          |
|                  | icke-förnybar          | eldningsolja 1  |
|                  | icke-förnybar          | eldningsolja>1  |
|                  | icke-förnybar          | gasol           |
|                  | icke-förnybar          | naturgas        |
|                  | icke-förnybar          | torv            |
|                  | icke-förnybar          | avlutar         |
|                  | icke-förnybar          | avfall          |
| ---              | ---------------------- | --------------- |
|                  | förnybar               | tr�br�nsle      |
| ---              | ---------------------- | --------------- |
| okand bransletyp | okand                  | �vrigt          |
| okand bransletyp | okand                  | fj�rrv�rme      |
| okand bransletyp | okand                  | el              |
| okand bransletyp | okand                  | total energi    |

<!-- #### Förbrukarkategori

jordbruk, skogsbruk, fiske
industri
el- och v�rmeverk
offentlig f�rvaltning
enbostadshus
flerbostadshus
�vriga fastigheter
v�gtransporter
bygg- och transporttj�nster, luftfart, j�rnv�g...
totalt
bygg, luftfart, j�rnv�g, bunkring
slutanv. jordbruk,skogsbruk,fiske
slutanv. industri, byggverks.
slutanv. offentlig verksamhet
slutanv. transporter
slutanv. �vriga tj�nster
slutanv. sm�hus
slutanv. flerbostadshus
slutanv. fritidshus
summa br�nsletyp
NaN
slutanv. jordbruk,skogsbruk,fiske
slutanv. industri, byggverks.
slutanv. offentlig verksamhet
slutanv. transporter
slutanv. �vriga tj�nster
slutanv. sm�hus
slutanv. flerbostadshus
slutanv. fritidshus
summa br�nsletyp -->

### Region selection

The dataset contains information for all 312 regions in sweden. There was a selction of the following regions to reduce the amount of data proccessed in this version of teh project.

- 0160 T�by
- 0117 �ster�ker
- 0180 Stockholm
- 0980 Gotland
- 01 Stockholms l�n
- 22 V�sternorrlands l�n
- 09 Gotlands l�n
- 00 Riket
- 2581 Pite�
- 1480 G�teborg’

## Data investigation & descriptive analysis

To increase the efficiany of the analysis the datasets were grouped by all the categorical variables they contain.  
For eas of analysis Power BI (PBI) was used to create graphs.

## Model generation

## Results

---

## Next steps
