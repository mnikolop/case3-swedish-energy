
import pandas as pd
import numpy as np


leveranser_flytande = pd.read_table(
    'C:/Users/markella.nikolopoulo/OneDrive - Influence AB/Dokument/Cases/case3-swedish-energy/data/to-use/leveranser-flytande-bransle-region-ar.csv', sep=',')
elproduction_bransleanvandning = pd.read_table(
    'C:/Users/markella.nikolopoulo/OneDrive - Influence AB/Dokument/Cases/case3-swedish-energy/data/to-use/elproduction-bransleanvandning-region-produktionssatt-bransletyp-ar.csv', sep=',')
fjarrvarmeproduktion = pd.read_table(
    'C:/Users/markella.nikolopoulo/OneDrive - Influence AB/Dokument/Cases/case3-swedish-energy/data/to-use/fjarrvarmeproduktion-region-produktionssatt-bransletyp-ar.csv', sep=',')
slutanvandning = pd.read_table(
    'C:/Users/markella.nikolopoulo/OneDrive - Influence AB/Dokument/Cases/case3-swedish-energy/data/to-use/slutanvandning-region-forbrukarkategori-bransletyp-kategori-energityp-ar.csv', sep=',')
bransleforbrukning = pd.read_table(
    'C:/Users/markella.nikolopoulo/OneDrive - Influence AB/Dokument/Cases/case3-swedish-energy/data/to-use/branslefarbrukning-far-produktion-per-ar.csv', sep=',')
energidata = pd.read_table('C:/Users/markella.nikolopoulo/OneDrive - Influence AB/Dokument/Cases/case3-swedish-energy/data/to-use/energidata-per-ar.csv', sep=',')

leveranser_flytande.m3 = leveranser_flytande.m3.fillna(method='ffill')
fjarrvarmeproduktion.MWh = fjarrvarmeproduktion.MWh.interpolate()
energidata.MWh = energidata.MWh.fillna(method='ffill')

# leveranser_flytande = leveranser_flytande[leveranser_flytande.region.isin(
#     ['0160 T�by', '0117 �ster�ker', '0180 Stockholm', '0980 Gotland', '01 Stockholms l�n', '22 V�sternorrlands l�n', '09 Gotlands l�n', '00 Riket', '2581 Pite�', '1480 G�teborg'])].reset_index(drop=True)
# elproduction_bransleanvandning = elproduction_bransleanvandning[elproduction_bransleanvandning.region.isin(
#     ['0160 T�by', '0117 �ster�ker', '0180 Stockholm', '0980 Gotland', '01 Stockholms l�n', '22 V�sternorrlands l�n', '09 Gotlands l�n', '00 Riket', '2581 Pite�', '1480 G�teborg'])].reset_index(drop=True)
# fjarrvarmeproduktion = fjarrvarmeproduktion[fjarrvarmeproduktion.region.isin(
#     ['0160 T�by', '0117 �ster�ker', '0180 Stockholm', '0980 Gotland', '01 Stockholms l�n', '22 V�sternorrlands l�n', '09 Gotlands l�n', '00 Riket', '2581 Pite�', '1480 G�teborg'])].reset_index(drop=True)
# slutanvandning = slutanvandning[slutanvandning.region.isin(['0160 T�by', '0117 �ster�ker', '0180 Stockholm', '0980 Gotland',
#                                                            '01 Stockholms l�n', '22 V�sternorrlands l�n', '09 Gotlands l�n', '00 Riket', '2581 Pite�', '1480 G�teborg'])].reset_index(drop=True)
# energidata = energidata[energidata.region.isin(['0160 T�by', '0117 �ster�ker', '0180 Stockholm', '0980 Gotland', '01 Stockholms l�n',
#                                                '22 V�sternorrlands l�n', '09 Gotlands l�n', '00 Riket', '2581 Pite�', '1480 G�teborg'])].reset_index(drop=True)


leveranser_flytande_group = leveranser_flytande.groupby(['region', 'ar', 'fornybar_bransletyp'], as_index=False).agg(
    Mean=('m3', np.mean),
    Sum=('m3', np.sum),
    Avg=('m3', np.average),
    Count=('m3', 'count'),
    Max=('m3', np.max),
    Min=('m3', np.min)
).sort_values(by=['Mean', 'Sum', 'Avg', 'Max', 'Min'])

leveranser_flytande_group.ar = leveranser_flytande_group.ar.astype(int)

elproduction_bransleanvandning_grouped = elproduction_bransleanvandning.groupby(['region', 'ar', 'fornybar_bransletyp', 'fornybar_produktionssatt'], as_index=False
                                                                                ).agg(
    Mean=('MWh', np.mean),
    Sum=('MWh', np.sum),
    Avg=('MWh', np.average),
    Count=('MWh', 'count'),
    Max=('MWh', np.max),
    Min=('MWh', np.min)
).sort_values(by=['Mean', 'Sum', 'Avg', 'Max', 'Min'])

fjarrvarmeproduktion_grouped = fjarrvarmeproduktion.groupby(['region', 'ar', 'fornybar_bransletyp', 'fornybar_produktionssatt'], as_index=False
                                                            ).agg(
    Mean=('MWh', np.mean),
    Sum=('MWh', np.sum),
    Avg=('MWh', np.average),
    Count=('MWh', 'count'),
    Max=('MWh', np.max),
    Min=('MWh', np.min)
).sort_values(by=['Mean', 'Sum', 'Avg', 'Max', 'Min'])

slutanvandning_grouped = slutanvandning.groupby(['region', 'ar', 'fornybar_bransletyp', 'forbrukarkategori'], as_index=False
                                                ).agg(
    Mean=('MWh', np.mean),
    Sum=('MWh', np.sum),
    Avg=('MWh', np.average),
    Count=('MWh', 'count'),
    Max=('MWh', np.max),
    Min=('MWh', np.min)
).sort_values(by=['Mean', 'Sum', 'Avg', 'Max', 'Min'])

bransleforbrukning = bransleforbrukning.replace('..', 0)

bransleforbrukning.branslefarbrukning = bransleforbrukning.branslefarbrukning.astype(
    float)


bransleforbrukning_grouped = bransleforbrukning.groupby(['ar', 'fornybar_bransletyp', 'produktionsslag'], as_index=False
                                                        ).agg(
    Mean=('branslefarbrukning', np.mean),
    Sum=('branslefarbrukning', np.sum),
    Avg=('branslefarbrukning', np.average),
    Count=('branslefarbrukning', 'count'),
    Max=('branslefarbrukning', np.max),
    Min=('branslefarbrukning', np.min)
).sort_values(by=['Mean', 'Sum', 'Avg', 'Max', 'Min'])

energidata = energidata.replace('..', 0)

energidata.MWh = energidata.MWh.astype(float)


energidata_grouped = energidata.groupby(['region', 'ar', 'fornybar_energityp', 'fornybar_kategori'], as_index=False
                                        ).agg(
    Mean=('MWh', np.mean),
    Sum=('MWh', np.sum),
    Avg=('MWh', np.average),
    Count=('MWh', 'count'),
    Max=('MWh', np.max),
    Min=('MWh', np.min)
).sort_values(by=['Mean', 'Sum', 'Avg', 'Max', 'Min'])
