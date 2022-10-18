import streamlit as st
import ui.template as template
from daten.datenbank import df_p2
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

df_p2_melt = pd.melt(df_p2, value_vars=['Anteil Umsatz', 'Anteil Ausgaben'], id_vars=['Branche'])
df_p2_melt_empty = pd.melt(df_p2, value_vars=['Anteil Umsatz', ' '], id_vars=['Branche'])

invest = False

chart = st.empty()
invest = st.button('Mit welchem Invest?')


if invest:
    c = alt.Chart(df_p2_melt).mark_bar().encode(
        column=alt.Column('Branche', header=alt.Header(orient='bottom')),
        x=alt.X('variable', axis=alt.Axis(ticks=False, labels=False, title='')),
        y=alt.Y('value', axis=alt.Axis(grid=False)),
        color='variable',
        tooltip=['Branche', 'variable', 'value']
    ).configure_view(stroke=None)
else:
    c = alt.Chart(df_p2_melt_empty).mark_bar().encode(
        column=alt.Column('Branche', header=alt.Header(orient='bottom')),
        x=alt.X('variable', axis=alt.Axis(ticks=False, labels=False, title='')),
        y=alt.Y('value', axis=alt.Axis(grid=False)),
        color='variable',
        tooltip=['Branche', 'variable', 'value']
    ).configure_view(stroke=None)

chart.altair_chart(c)



want_to_contribute = st.button("KI hat nicht nur positive Auswirkungen auf den Umsatz!")
if want_to_contribute:
    switch_page("unternehmenslebensdauer")

st.write('Quelle: [BMWK, 2019](https://www.bmwk.de/Redaktion/DE/Publikationen/Wirtschaft/einsatz-von-ki-deutsche-wirtschaft.pdf?__blob=publicationFile&v=8) (Abgerufen am 18.10.2022)')