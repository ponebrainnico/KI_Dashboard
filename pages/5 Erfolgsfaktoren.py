import streamlit as st
import ui.template as template
from daten.datenbank import df_p5
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

df_p3_melt = pd.melt(df_p5, value_vars=['stark', 'weniger stark', 'gar nicht'], id_vars=['Faktor'])
c = alt.Chart(df_p3_melt).mark_bar().encode(
    x=alt.X('sum(value)', stack='normalize'),
    y=alt.Y('Faktor'),
    color='variable',
    tooltip='value'
).properties(width=800, height=250)

text = alt.Chart(df_p3_melt).mark_text(dx=-35, dy=1.5, color='white').encode(
        x=alt.X('sum(value)', stack='normalize'),
        y=alt.Y('Faktor'),
        detail='variable',
        text=alt.Text('sum(value)', format='.0f')
)

st.altair_chart(c + text)

st.button("CTA")

st.write('Quelle: [BMWK, 2021](https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-startups.pdf?__blob=publicationFile&v=3) (Abgerufen am 18.10.2022)')
