import streamlit as st
import ui.template as template
from daten.datenbank import df_p5
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

st.title('Was ist für einen erfolgreichen Einsatz nötig?')

cat_order = ['stark', 'weniger stark', 'gar nicht']
df_p5_melt = pd.melt(df_p5, value_vars=cat_order, id_vars=['Faktor'])
color_scale = alt.Scale(
    domain=cat_order,
    range=['#15C2FF', '#2E75FD', '#434343']
)

c = alt.Chart(df_p5_melt).transform_calculate(
        key='datum.variable=="stark"'
    ).transform_joinaggregate(
        sort_key='argmax(key)', groupby=['Faktor']
    ).mark_bar().encode(
        x=alt.X('sum(value)', title='Anteil', stack='normalize', axis=alt.Axis(grid=False, format='.0%', tickCount=6)),
        y=alt.Y('Faktor', sort=alt.SortField('sort_key', order='descending'), title=None),
        color=alt.Color('variable:N', sort=cat_order, scale=color_scale, legend=alt.Legend(title=None)),
        tooltip=[alt.Tooltip('Faktor', title='Faktor'), alt.Tooltip('variable', title='Wichtigkeit'), alt.Tooltip('value', format='.0%', title='Anteil')],
        order=alt.Order('color_variable_sort_key:Q')
    ).properties(width=800, height=250).configure_axis(labelLimit=400)

# text = alt.Chart(df_p5_melt).mark_text(dx=-35, dy=1.5, color='white').encode(
#         x=alt.X('sum(value)', stack='normalize'),
#         y=alt.Y('Faktor'),
#         detail='variable',
#         text=alt.Text('sum(value)', format='.0f')
# )

st.altair_chart(c)

text = '''Es gibt eine große Anzahl an Faktoren, die die Wahrscheinlichkeit eines KI Einsatzes beeinflussen.
Viele Unternehmen, die noch keine KI nutzen, geben an, dass eine bessere IT Austattung und datenschutzkonforme Cloud-Angebote entscheidende Faktoren sind.
Aber auch die Verfügbarkeit von Daten und Fachkräften sind wichtig. Genau hierbei können wir Sie unterstützen!
Unser Expertenteam berät Sie gerne, wie Sie KI gewinnbringend in Ihrem Unternehmen einsetzen können.'''
st.write(text)
st.caption('Quelle: [BMWK, 2021](https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-herausforderungen.pdf?__blob=publicationFile&v=4) (Abgerufen am 18.10.2022)')
st.write('#')

st.write('Nächster Schritt:')
st.write('Haben Sie ein paar Ideen sammeln können, wie KI Ihr Unternehmen optimieren könnte? Sprechen Sie uns gerne an, damit wir Ihnen individualisierte Lösungen vorschlagen können!')
st.button("Kontakt")
