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



st.subheader('Wie viele Unternehmen nutzen bereits KI?')
chart = st.empty()

b1, b2 = st.columns([1, 1])
with b1:
    option = st.selectbox('Ihre Branche', options=list(df_p1['Branche'].sort_values()) + ['Keine Angabe'], index=11)
with b2:
    option2 = st.selectbox('Nutzt Ihr Unternehmen KI?', options=['Keine Angabe', 'Ja', 'Nein'], index=0)

c = alt.Chart(df_p1).mark_bar().encode(
        x=alt.X('Anteil', axis=alt.Axis(format='.0%', grid=False, tickCount=6)),
        y=alt.Y('Branche', sort=alt.EncodingSortField(field='Anteil', order='descending')),
        color=alt.condition(alt.datum.Branche == option, alt.value('#15C2FF'), alt.value('grey')),
        tooltip=alt.Tooltip('Anteil', format='.1%')
    ).properties(width=800, height=250)


chart.altair_chart(c)

if option != 'Keine Angabe' and option2 != 'Keine Angabe':
    if option2 == 'Ja':
        st.write('Dann sind Sie ' + str(round((1 - df_p1[df_p1['Branche'] == option].iloc[0, 1])*100, 2)) + '% Ihrer Wettbewerber voraus!')
    elif option2 == 'Nein':
        st.write('Dann geht es Ihnen wie ' + str(round((1 - df_p1[df_p1['Branche'] == option].iloc[0, 1])*100, 2)) + '% Ihrer Wettbewerber.')
else:
    st.write('Wie stehen Sie im vergleich zu Ihren Wettbewerbern da?')

want_to_contribute = st.button("Erfahren Sie wie sich die Verwendung von KI auf den Unternehmenserfolg auswirkt!")
if want_to_contribute:
    switch_page("umsatz")

st.write('Quelle: [BMWK, 2019](https://www.bmwk.de/Redaktion/DE/Publikationen/Wirtschaft/einsatz-von-ki-deutsche-wirtschaft.pdf?__blob=publicationFile&v=8) (Abgerufen am 18.10.2022)')