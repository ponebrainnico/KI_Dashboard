import streamlit as st
import ui.template as template
from daten.datenbank import df_p5
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

cat_order = ['stark', 'weniger stark', 'gar nicht']
df_p5_melt = pd.melt(df_p5, value_vars=cat_order, id_vars=['Faktor'])
color_scale = alt.Scale(
    domain=cat_order,
    range=['#15C2FF', 'lightgrey', 'grey']
)

c = alt.Chart(df_p5_melt).transform_calculate(
        key='datum.variable=="stark"'
    ).transform_joinaggregate(
        sort_key='argmax(key)', groupby=['Faktor']
    ).mark_bar().encode(
        x=alt.X('sum(value)', title='Anteil', stack='normalize', axis=alt.Axis(grid=False, format='.0%', tickCount=6)),
        y=alt.Y('Faktor', sort=alt.SortField('sort_key', order='descending')),
        color=alt.Color('variable:N', sort=cat_order, scale=color_scale, legend=alt.Legend(title=None)),
        tooltip=[alt.Tooltip('variable', title='Wichtigkeit'), alt.Tooltip('value', format='.0%', title='Anteil')],
        order=alt.Order('color_variable_sort_key:Q')
    ).properties(width=800, height=250)

# text = alt.Chart(df_p5_melt).mark_text(dx=-35, dy=1.5, color='white').encode(
#         x=alt.X('sum(value)', stack='normalize'),
#         y=alt.Y('Faktor'),
#         detail='variable',
#         text=alt.Text('sum(value)', format='.0f')
# )

st.altair_chart(c)

st.button("CTA")

st.write('Quelle: [BMWK, 2021](https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-startups.pdf?__blob=publicationFile&v=3) (Abgerufen am 18.10.2022)')
