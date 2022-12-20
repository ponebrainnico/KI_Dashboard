import streamlit as st
import ui.template as template
from daten.datenbank import df_p3
import altair as alt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI Dashboard",
    page_icon="⏳",
    layout="wide"
)

# UI laden
template.local_css()
# template.max_width()
st.markdown('<img class="center" src="https://brain.performance.one/wp-content/uploads/2019/05/Logo_P.ONE_BRAIN_weiss.png">', unsafe_allow_html=True)
st.markdown('#')

st.header('KI-Unternehmen haben eine längere Lebensdauer!')
st.write('###')
cat_order = ['aktiv', 'vermutlich stillgelegt', 'geschlossen']
df_p3_melt = pd.melt(df_p3, value_vars=cat_order, id_vars=['Unternehmen'])
color_scale = alt.Scale(
    domain=cat_order,
    range=['#15C2FF', '#2E75FD', '#252A2F']
)

c = alt.Chart(df_p3_melt).mark_bar(size=22).encode(
        x=alt.X('sum(value)', title='Anteil', stack='normalize', axis=alt.Axis(format='.0%', grid=True, tickCount=6, tickSize=15, labelPadding=8)),
        y=alt.Y('Unternehmen', sort=alt.SortField('sum(value)', order='descending'), title='Unternehmenstyp', axis=alt.Axis(tickSize=0, labelPadding=15)),
        color=alt.Color('variable:N', sort=cat_order, scale=color_scale, title='Status'),
        order=alt.Order('color:Q'),
        tooltip=[alt.Tooltip('variable', title='Status'), alt.Tooltip('value', title='Anteil', format='.0%')]
    ).configure_axisY(
        titleAlign='left',
        titleAngle=0,
        titleY=-20,
        titleX=-130
    ).configure_axisX(
        titleY=50
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        labelFontSize=13,
        titleFontSize=15
    ).properties(height=320)

# text = alt.Chart(df_p3_melt).mark_text(
#             align='right', color='white', dx=-2.5
#        ).encode(
#             x=alt.X('value', stack='normalize'),
#             y=alt.Y('Unternehmen'),
#             detail='variable',
#             order='cat_order:O',
#             text=alt.Text('value:Q', format='.0%')
# )

st.altair_chart(c, use_container_width=True)

text = '''Der Einsatz von KI zeigt auch positive Auswirkungen auf weitere Faktoren:
So haben Start-ups, die KI nutzen, eine wesentlich höhere Überlebensrate als der Gesamtdurchschnitt von 45 %.'''
st.write(text)
st.caption('Quelle: [BMWK, 2021](https://www.de.digital/DIGITAL/Redaktion/DE/Digitalisierungsindex/Publikationen/publikation-download-ki-startups.pdf?__blob=publicationFile&v=3) (Abgerufen am 18.10.2022)')
st.write('###')

st.markdown(f'**<p style="color:#15C2FF">Nächster Schritt:</p>**', unsafe_allow_html=True)
next = '''Bis jetzt haben wir nur gezeigt, warum sich der Einsatz von KI lohnt. Im Folgenden zeigen wir Ihnen, wo KI überall eingesetzt wird.'''
st.write(next)
want_to_contribute = st.button("WEITER ZU DEN UNTERNEHMENSBEREICHEN")
if want_to_contribute:
    switch_page("unternehmensbereiche")
