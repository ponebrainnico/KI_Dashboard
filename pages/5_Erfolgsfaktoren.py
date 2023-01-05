import streamlit as st
import streamlit.components.v1 as components
import ui.template as template
from daten.datenbank import df_p5
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI Dashboard",
    page_icon="🎖",
    layout="wide"
)

#--- UI laden ---
template.local_css()

st.markdown('<img class="center" src="https://brain.performance.one/wp-content/uploads/2019/05/Logo_P.ONE_BRAIN_weiss.png">', unsafe_allow_html=True)
st.markdown('#')

st.header('Was ist für einen erfolgreichen Einsatz nötig?')
st.write('###')

cat_order = ['stark', 'weniger stark', 'gar nicht']
df_p5_melt = pd.melt(df_p5, value_vars=cat_order, id_vars=['Faktor'])
color_scale = alt.Scale(
    domain=cat_order,
    range=['#15C2FF', '#5D666E', '#252A2F']
)

c = alt.Chart(df_p5_melt).transform_calculate(
        key='datum.variable=="stark"'
    ).transform_joinaggregate(
        sort_key='argmax(key)', groupby=['Faktor']
    ).mark_bar(size=18).encode(
        x=alt.X('sum(value)', title='Anteil', stack='normalize', axis=alt.Axis(format='.0%', tickCount=6, tickSize=15, labelPadding=8, gridDash=[2, 3])),
        y=alt.Y('Faktor',
                sort=alt.SortField('sort_key', order='descending'),
                title='Faktor',
                axis=alt.Axis(tickSize=0, labelPadding=15),
                scale=alt.Scale(paddingOuter=0.7, clamp=True)),
        color=alt.Color('variable:N', sort=cat_order, scale=color_scale, legend=alt.Legend(title='Auswirkung')),
        tooltip=[alt.Tooltip('Faktor', title='Faktor'), alt.Tooltip('variable', title='Wichtigkeit'), alt.Tooltip('value', format='.0%', title='Anteil')],
        order=alt.Order('color_variable_sort_key:Q')
    ).properties(height=420
    # ).configure(background='#252A2F', padding={"left": 100, "top": 20, "right": 20, "bottom": 20}
    ).configure_axisY(
        titleAlign='right',
        titleAngle=0,
        titleY=-20,
        titleX=-15,
        labelLimit=400
    ).configure_axisX(
        titleY=55,
        labelFlush=False
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        labelFontSize=13,
        titleFontSize=15
    )

st.altair_chart(c, use_container_width=True, theme=None)
# st.caption('Quelle: [BMWK, 2021](https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-herausforderungen.pdf?__blob=publicationFile&v=4) (Abgerufen am 18.10.2022)')

components.html('''<div style="text-align:right; color:#5D666E; font-family:'Roboto', sans-serif; font-size:0.63em">
                        Quelle: 
                        <a style="color:#007da7" href="https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-herausforderungen.pdf?__blob=publicationFile&v=4" target="_blank">
                            BMWK, 2021
                        </a>
                        (Abgerufen am 18.10.2022)
                   </div>''', height=40)

text = '''Es gibt eine große Anzahl an Faktoren, die die Wahrscheinlichkeit eines KI-Einsatzes beeinflussen.
Viele Unternehmen, die noch keine KI nutzen, geben an, dass eine bessere IT-Ausstattung und datenschutzkonforme Cloud-Angebote entscheidende Faktoren sind.
Aber auch die Verfügbarkeit von Daten und Fachkräften sind wichtig. Bei all diesen Faktoren können wir Sie unterstützen!
Unser Expertenteam berät Sie gerne, wie Sie KI gewinnbringend in Ihrem Unternehmen einsetzen können.'''
st.write(text)
st.write('')

st.markdown(f'**<p style="color:#15C2FF">Nächster Schritt:</p>**', unsafe_allow_html=True)
st.write('Haben Sie ein paar Ideen sammeln können, wie KI Ihr Unternehmen optimieren könnte? Sprechen Sie uns gerne an, damit wir Ihnen individualisierte Lösungen vorschlagen können!!')
st.button("Kontakt")
