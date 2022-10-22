import streamlit as st
import ui.template as template
from daten.datenbank import df_p3
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

cat_order = ['aktiv', 'vermutlich stillgelegt', 'geschlossen']
df_p3_melt = pd.melt(df_p3, value_vars=cat_order, id_vars=['Unternehmen'])
color_scale = alt.Scale(
    domain=cat_order,
    range=['#15C2FF', 'lightgrey', 'grey']
)

c = alt.Chart(df_p3_melt).mark_bar().encode(
        x=alt.X('sum(value)', title='Anteil', stack='normalize', axis=alt.Axis(format='.0%', grid=False, tickCount=6)),
        y=alt.Y('Unternehmen', sort=alt.SortField('sum(value)', order='descending'), title='Unternehmenstyp'),
        color=alt.Color('variable:N', sort=cat_order, scale=color_scale, title='Status'),
        order=alt.Order('color:Q'),
        tooltip=[alt.Tooltip('variable', title='Status'), alt.Tooltip('value', title='Anteil', format='.0%')]
    ).properties(width=800, height=250)

# text = alt.Chart(df_p3_melt).mark_text(
#             align='right', color='white', dx=-2.5
#        ).encode(
#             x=alt.X('value', stack='normalize'),
#             y=alt.Y('Unternehmen'),
#             detail='variable',
#             order='cat_order:O',
#             text=alt.Text('value:Q', format='.0%')
# )

st.altair_chart(c)

text = '''Der Einsatz von KI zeigt auch positive Auswirkungen, auf weitere Faktoren:
So haben Startups, die KI nutzen, eine wesentlich höhere Überlebensrate als der Gesamtdurchschnitt von 45%.
Immer noch nicht überzeugt? '''
st.write(text)

want_to_contribute = st.button("Dann erfahren Sie hier in welchen Unternehmensbereichen KI am häufigstein eingesetzt wird!")
if want_to_contribute:
    switch_page("unternehmensbereiche")

st.write('Quelle: [BMWK, 2021](https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-startups.pdf?__blob=publicationFile&v=3) (Abgerufen am 18.10.2022)')