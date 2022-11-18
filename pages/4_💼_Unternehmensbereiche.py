import streamlit as st
import ui.template as template
from daten.datenbank import df_p4
import altair as alt
from streamlit_extras.switch_page_button import switch_page


#--- UI laden ---
template.local_css()
template.max_width()

st.title('Wo kann KI überall eingesetzt werden?')
c = alt.Chart(df_p4).mark_bar().encode(
        x=alt.X('Anteil', axis=alt.Axis(format='.0%', grid=False)),
        y=alt.Y('Unternehmensbereich', sort=alt.EncodingSortField(field='Anteil', order='descending'), title=None),
        tooltip=alt.Tooltip('Anteil', format='.0%')
    ).configure_mark(color='#15C2FF').properties(width=800, height=250).configure_axis(labelLimit=400)

st.altair_chart(c)

text = '''KI kann in fast allen Unternehmensbereichen eingesetzt werden.
Vor allem das Marketing ist ein belieber Einsatzort aber selbst in der Personalabteilung und im Controlling gibt es Einsatzmöglichkeiten.'''

st.write(text)
st.caption('Quelle: [Bitkom, 2021](https://www.bitkom.org/sites/default/files/2021-04/bitkom-charts-kunstliche-intelligenz-21-04-2021_final.pdf) (Abgerufen am 18.10.2022)')
st.write('#')

st.write('Nächster Schritt:')
st.write('Was ist nötig, um KI erfolgreich einzusetzen?')
want_to_contribute = st.button("WEITER ZU DEN ERFOLGSFAKTOREN")
if want_to_contribute:
    switch_page("erfolgsfaktoren")
