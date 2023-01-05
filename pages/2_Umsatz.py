import streamlit as st
import ui.template as template
from daten.datenbank import df_p2
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="KI Dashboard",
    page_icon="📈",
    layout="wide"
)

#--- UI laden ---
template.local_css()
# template.max_width()

st.markdown('<img class="center" src="https://brain.performance.one/wp-content/uploads/2019/05/Logo_P.ONE_BRAIN_weiss.png">', unsafe_allow_html=True)
st.markdown('#')

df_p2_melt = pd.melt(df_p2, value_vars=['Umsatz', 'Ausgaben'], id_vars=['Branche']).rename({'value': 'Anteil'}, axis=1)
df_p2_melt_empty = pd.melt(df_p2, value_vars=['Umsatz', ' '], id_vars=['Branche']).rename({'value': 'Anteil'}, axis=1)

invest = False

st.header('Wie wirkt sich der KI-Einsatz auf den Umsatz aus?')
chart = st.empty()

text = '''Da nur relativ wenige Unternehmen bis jetzt KI nutzen, ist es nicht verwunderlich, dass der Anteil des Umsatzes am Gesamtumsatz, der mit Produkten, bei denen KI genutzt wird,
generiert wird, noch relativ gering ist. Selbst bei IT-Unternehmen sind es gerade einmal 3,3 %. Doch mit welchem Invest wird dieser Umsatz generiert?'''

text2 = '''Die Kosten für KI sind weit unter den generierten Umsätzen.
Natürlich können zu den KI-Kosten noch andere Kosten kommen, aber mit einem 1 zu ~5,5 Kosten-Umsatzverhältnis ist KI günstiger, als man vielleicht vermuten würde.'''

st.write(text)
invest = st.button('Klicken Sie hier, um mehr zu erfahren!')
if invest:
    st.info(text2, icon="ℹ️")
st.caption('Quelle: [BMWK, 2019](https://www.bmwk.de/Redaktion/DE/Publikationen/Wirtschaft/einsatz-von-ki-deutsche-wirtschaft.pdf?__blob=publicationFile&v=8) (Abgerufen am 18.10.2022)')

colors = ['#434343', '#15C2FF']

if invest:
    c = alt.Chart(df_p2_melt).transform_calculate(
            key='datum.variable == "Anteil Unternehmen"'
        ).transform_joinaggregate(
            sort_key='argmax(key)', groupby=['Branche']
        ).transform_calculate(
            sort_val='datum.sort_key.Anteil'
        ).mark_bar().encode(
            column=alt.Column('Branche', header=alt.Header(orient='bottom', labelAngle=-30, labelAlign='right'), sort=alt.SortField("sort_val", order="descending")),
            x=alt.X('variable', axis=alt.Axis(ticks=False, labels=False, title=''), sort=alt.EncodingSortField(field='Anteil', order='descending')),
            y=alt.Y('Anteil', axis=alt.Axis(grid=False, tickCount=3, format='.0%'), title='Anteil am Gesamtumsatz'),
            color=alt.Color('variable', scale=alt.Scale(range=colors), legend=alt.Legend(orient='none', legendX=670, legendY=20, title=None)),
            tooltip=[alt.Tooltip('Branche'), alt.Tooltip('variable'), alt.Tooltip('Anteil', format='.2%')]
        ).configure_view(stroke=None).properties(width=50, height=200)
else:
    c = alt.Chart(df_p2_melt_empty).transform_calculate(
            key='datum.variable == "Anteil Unternehmen"'
        ).transform_joinaggregate(
            sort_key='argmax(key)', groupby=['Branche']
        ).transform_calculate(
            sort_val='datum.sort_key.Anteil'
        ).mark_bar().encode(
            column=alt.Column('Branche', header=alt.Header(orient='bottom', labelAngle=-30, labelAlign='right'), sort=alt.SortField("sort_val", order="descending")),
            x=alt.X('variable', axis=alt.Axis(ticks=False, labels=False, title=''), sort=alt.EncodingSortField(field='Anteil', order='descending')),
            y=alt.Y('Anteil', axis=alt.Axis(grid=False, tickCount=3, format='.0%'), title='Anteil am Gesamtumsatz'),
            color=alt.Color('variable', scale=alt.Scale(range=colors), legend=None),
            tooltip=[alt.Tooltip('Branche'), alt.Tooltip('Anteil', format='.1%')]
        ).configure_view(stroke=None).properties(width=70, height=200)

chart.altair_chart(c, use_container_width=True, theme=None)
st.write('')

st.markdown(f'**<p style="color:#15C2FF">Nächster Schritt:</p>**', unsafe_allow_html=True)
next = '''Aber der Einsatz von KI hat nicht nur positive Auswirkungen auf den Umsatz.
       KI-Unternehmen sind auch langlebiger. Im nächsten Schritt erfahren Sie mehr dazu!'''
st.write(next)
want_to_contribute = st.button('WEITER ZUR UNTERNEHMENSLEBENSDAUER')
if want_to_contribute:
    switch_page("unternehmenslebensdauer")
