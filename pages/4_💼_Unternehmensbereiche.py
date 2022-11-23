import streamlit as st
import ui.template as template
from daten.datenbank import df_p4
import altair as alt
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI Dashboard",
    page_icon="💼",
    layout="wide"
)

#--- UI laden ---
template.local_css()
# template.max_width()

st.header('Wo kann KI überall eingesetzt werden?')
c = alt.Chart(df_p4).mark_bar().encode(
        x=alt.X('Anteil', axis=alt.Axis(format='.0%', grid=False)),
        y=alt.Y('Unternehmensbereich', sort=alt.EncodingSortField(field='Anteil', order='descending'), title=None),
        tooltip=alt.Tooltip('Anteil', format='.0%')
    ).configure_mark(color='#15C2FF').properties(width=800, height=250).configure_axis(labelLimit=400)

st.altair_chart(c, use_container_width=True)

text = '''KI wird in fast allen Unternehmensbereichen eingesetzt werden.
Vor allem Marketing, Produktion und Kundendienst sind beliebe Einsatzorte.
Aber selbst in der Personalabteilung und im Controlling wird KI bereits eingesetzt, wenn auch wesentlich seltener.'''

st.write(text)
st.caption('Quelle: [Bitkom, 2021](https://www.bitkom.org/sites/default/files/2021-04/bitkom-charts-kunstliche-intelligenz-21-04-2021_final.pdf) (Abgerufen am 18.10.2022)')
# st.write('###')

st.markdown(f'**<p style="color:#15C2FF">Nächster Schritt:</p>**', unsafe_allow_html=True)
next = '''KI hat viele Vorteile und kann fast überall eingesetzt werden. Wieso setzen dann bis jetzt so wenige Unternehmen KI ein?
Diese Frage beantworten wir im nächsten Schritt, indem wir zeigen was nötig ist, um KI erfolgreich einzusetzen.'''
st.write(next)
want_to_contribute = st.button("WEITER ZU DEN ERFOLGSFAKTOREN")
if want_to_contribute:
    switch_page("erfolgsfaktoren")
