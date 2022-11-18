import streamlit as st
import ui.template as template
from daten.datenbank import df_p1
import altair as alt
from streamlit_extras.switch_page_button import switch_page
alt.renderers.set_embed_options(actions=False)


st.set_page_config(
    page_title="KI Dashboard",
    page_icon="🔎",
)


#--- UI laden ---
template.local_css()
template.max_width()



st.header('Wie viele Unternehmen nutzen bereits KI?')
st.write('Wie stehen Sie im Vergleich zu Ihren Wettbewerbern da?')
chart = st.empty()



b1, b2, b3 = st.columns([2, 2, 1])
with b1:
    option2 = st.checkbox('Mein Unternehmen nutzt KI.')
with b2:
    # option2 = st.selectbox('Nutzt Ihr Unternehmen KI?', options=['Keine Angabe', 'Ja', 'Nein'], index=0)
    option = st.selectbox('Ihre Branche', options=list(df_p1['Branche'].sort_values()) + ['Keine Angabe'], index=11)

if option != 'Keine Angabe':
    if option2:
        st.write('Dann sind Sie ' + str(round((1 - df_p1[df_p1['Branche'] == option].iloc[0, 1])*100, 2)) + '% Ihrer Wettbewerber voraus!')
    elif not option2:
        st.write('Dann geht es Ihnen wie ' + str(round((1 - df_p1[df_p1['Branche'] == option].iloc[0, 1])*100, 2)) + '% Ihrer Wettbewerber.')
else:
    st.write('#')

c = alt.Chart(df_p1).mark_bar().encode(
        x=alt.X('Anteil', axis=alt.Axis(format='.0%', grid=False, tickCount=6)),
        y=alt.Y('Branche', sort=alt.EncodingSortField(field='Anteil', order='descending')),
        color=alt.condition(alt.datum.Branche == option, alt.value('#15C2FF'), alt.value('#434343')),
        tooltip=alt.Tooltip('Anteil', format='.1%')
    ).properties(width=800, height=250)
st.altair_chart(c)

text = '''Zwar ist KI in aller Munde, doch nur wenige Unternehmen nutzen bereits KI-Lösungen.
IT-Unternehmen (IKT) sind hier noch am besten aufgestellt(, da KI teilweise zum Kerngeschäft gehört), aber selbst hier nutzen nur knapp 18% KI.
In den meisten anderen Branchen liegt der Anteil sogar unter 10% (Gesamtdurchschnitt: 5,8%). Der Einsatz von KI kann daher sehr gut genutzt werden, um einen Wettbewerbsvorteil zu schaffen.'''
st.write(text)
st.caption('Quelle: [BMWK, 2019](https://www.bmwk.de/Redaktion/DE/Publikationen/Wirtschaft/einsatz-von-ki-deutsche-wirtschaft.pdf?__blob=publicationFile&v=8) (Abgerufen am 18.10.2022)')
st.write('#')

st.write('Nächster Schritt:')
st.write("Erfahren Sie wie sich die Verwendung von KI auf den Unternehmenserfolg auswirkt!")
want_to_contribute = st.button('WEITER ZUM UMSATZ')
if want_to_contribute:
    switch_page("umsatz")
