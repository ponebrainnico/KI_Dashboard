import streamlit as st
import ui.template as template
from daten.datenbank import df_p4
import altair as alt
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

c = alt.Chart(df_p4).mark_bar().encode(
        x=alt.X('Anteil', axis=alt.Axis(format='.0%', grid=False), title='Anteil'),
        y=alt.Y('Unternehmensbereich', sort=alt.EncodingSortField(field='Anteil', order='descending')),
        tooltip=alt.Tooltip('Anteil', format='.0%')
    ).configure_mark(color='#15C2FF')

st.altair_chart(c)

want_to_contribute = st.button("Was ist nötig um KI erfolgreich einzusetzen?")
if want_to_contribute:
    switch_page("erfolgsfaktoren")

st.write('Quelle: [Bitkom, 2021](https://www.bitkom.org/sites/default/files/2021-04/bitkom-charts-kunstliche-intelligenz-21-04-2021_final.pdf) (Abgerufen am 18.10.2022)')