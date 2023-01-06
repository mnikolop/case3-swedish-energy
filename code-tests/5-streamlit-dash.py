import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import urllib3


# try:
leveranser_flytande = pd.read_table(
    'data/to-use/leveranser-flytande-bransle-region-ar.csv', sep=',')

leveranser_flytande = leveranser_flytande.set_index(leveranser_flytande.region)


regions = st.multiselect(
    "Choose regions", list(leveranser_flytande.region.drop_duplicates(
        keep='first').reset_index(drop=True)), [])

if not regions:
    st.error("Please select at least one country.")
else:
    data = leveranser_flytande.loc[regions]
    st.write("### Flutande bransle (m3)", data.sort_index())

    chart = plt.plot(x=leveranser_flytande.ar,
                     y=leveranser_flytande.region, hue=leveranser_flytande.fornybar_bransletyp)

    st.altair_chart(chart, use_container_width=True)
# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )
