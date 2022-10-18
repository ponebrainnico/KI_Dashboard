import streamlit as st
import ui.template as template
from daten.datenbank import df_p1
import altair as alt
from streamlit_extras.switch_page_button import switch_page



st.set_page_config(
    page_title="KI Dashboard",
    page_icon="📋",
)


#--- UI laden ---
template.local_css()
template.max_width()

colT1,colT2 = st.columns([2.7, 8])
with colT2:
    chart = st.empty()

b1, b2 = st.columns([1, 1])
with b1:
    option = st.selectbox('Ihre Branche', options=list(df_p1['Branche'].sort_values()) + ['Keine Angabe'], index=11)
with b2:
    option2 = st.selectbox('Nutzt Ihr Unternehmen KI?', options=['Keine Angabe', 'Ja', 'Nein'], index=0)

c = alt.Chart(df_p1).mark_bar(size=10).encode(
    x='Anteil',
    y='Branche',
    color=alt.condition(
        alt.datum.Branche == option,
        alt.value('blue'),
        alt.value('grey')
    ),
    tooltip='Anteil'
).interactive()


chart.altair_chart(c)

if option != 'Keine Angabe':
    if option2 == 'Ja':
        st.caption('Dann sind Sie ' + str(100 - df_p1[df_p1['Branche'] == option].iloc[0, 1]) + '% Ihrer Wettbewerber voraus!')
    elif option2 == 'Nein':
        st.caption('Dann geht es Ihnen wie ' + str(df_p1[df_p1['Branche'] == option].iloc[0, 1]) + '% Ihrer Wettbewerber.')

want_to_contribute = st.button("Erfahren Sie wie sich die Verwendung von KI auf den Unternehmenserfolg auswirkt!")
if want_to_contribute:
    switch_page("umsatz")

st.write('Quelle: [BMWK, 2019](https://www.bmwk.de/Redaktion/DE/Publikationen/Wirtschaft/einsatz-von-ki-deutsche-wirtschaft.pdf?__blob=publicationFile&v=8) (Abgerufen am 18.10.2022)')