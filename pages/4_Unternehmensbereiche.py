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
st.markdown('<img class="center" src="https://brain.performance.one/wp-content/uploads/2019/05/Logo_P.ONE_BRAIN_weiss.png">', unsafe_allow_html=True)
st.markdown('#')

st.header('Wo kann KI überall eingesetzt werden?')
st.write('###')

c = alt.Chart(df_p4).mark_bar(size=18).transform_calculate(
        y="split(datum.y, '/')"
    ).encode(
        x=alt.X('Anteil', axis=alt.Axis(format='.0%', tickCount=4, tickSize=15, labelPadding=8, gridDash=[2, 3])),
        y=alt.Y('y',
                sort=alt.EncodingSortField(field='Anteil', order='descending'),
                title=['Unternehmens-', 'bereich'],
                axis=alt.Axis(tickSize=0, labelPadding=15),
                scale=alt.Scale(paddingOuter=0.7)),
        tooltip=alt.Tooltip('Anteil', format='.0%')
    ).configure_mark(color='#15C2FF'
    ).properties(height=550
    ).configure_axis(
        labelLimit=400,
        labelFontSize=13,
        titleFontSize=15
    ).configure_axisY(
        titleAlign='right',
        titleAngle=0,
        titleY=-30,
        titleX=-15
    ).configure_axisX(
        titleY=55,
        labelFlush=False
    ).configure_view(
        strokeWidth=0
    )

st.altair_chart(c, use_container_width=True, theme=None)

text = '''KI wird in fast allen Unternehmensbereichen eingesetzt.
Vor allem Marketing, Produktion und Kundendienst sind beliebte Einsatzorte.
Aber selbst in der Personalabteilung und im Controlling wird KI bereits eingesetzt, wenn auch wesentlich seltener.'''

st.write(text)
st.caption('Quelle: [Bitkom, 2021](https://www.bitkom.org/sites/default/files/2021-04/bitkom-charts-kunstliche-intelligenz-21-04-2021_final.pdf) (Abgerufen am 18.10.2022)')
st.write('###')

st.markdown(f'**<p style="color:#15C2FF">Nächster Schritt:</p>**', unsafe_allow_html=True)
next = '''KI hat viele Vorteile und kann fast überall eingesetzt werden. Wieso setzen dann bis jetzt so wenige Unternehmen KI ein?
Diese Frage beantworten wir im nächsten Schritt, indem wir zeigen, was nötig ist, um KI erfolgreich einzusetzen.'''
st.write(next)
want_to_contribute = st.button("WEITER ZU DEN ERFOLGSFAKTOREN")
if want_to_contribute:
    switch_page("erfolgsfaktoren")
