import streamlit as st
import streamlit.components.v1 as components
import ui.template as template
from daten.datenbank import df_p1
import altair as alt
from streamlit_extras.switch_page_button import switch_page
alt.renderers.set_embed_options(actions=False)


st.set_page_config(
    page_title="KI Dashboard",
    page_icon="🔎",
    layout='wide'
)

#--- UI laden ---
template.local_css()

st.markdown('<img class="center" src="https://brain.performance.one/wp-content/uploads/2019/05/Logo_P.ONE_BRAIN_weiss.png">', unsafe_allow_html=True)
st.markdown('#')

st.header('Wie viele Unternehmen nutzen bereits KI?')

st.markdown(f'**<p style="color:#15C2FF">Wie stehen Sie im Vergleich zu Ihren Wettbewerbern da?</p>**', unsafe_allow_html=True)
chart = st.empty()
st.write('')


def disable_op2():
    st.session_state['op2'] = False


def disable_op3():
    st.session_state['op3'] = False


b1, b2, b3, b4 = st.columns([0.2, 2.3, 1.2, 1.5])
with b2:
    # st.write('')
    option = st.selectbox('Ihre Branche:', options=list(df_p1['Branche'].sort_values()) + ['Keine Angabe'], index=11)

with b4:
    st.write('Mein Unternehmen nutzt KI:')
    option2 = st.checkbox('Ja', key='op2', on_change=disable_op3)
    option3 = st.checkbox('Nein', key='op3', on_change=disable_op2)

if option != 'Keine Angabe':
    if option2:
        st.write(f'<span style="color:#15C2FF;font-weight:bold">></span>' +
        ' Dann sind Sie ' +
        str(round((1 - df_p1[df_p1['Branche'] == option].iloc[0, 2])*100, 2)).replace('.', ',') +
        ' % Ihrer Wettbewerber voraus!', unsafe_allow_html=True)
    elif option3:
        st.write(f'<span style="color:#15C2FF;font-weight:bold">></span>' +
        ' Dann geht es Ihnen wie ' +
        str(round((1 - df_p1[df_p1['Branche'] == option].iloc[0, 2])*100, 2)).replace('.', ',') +
        ' % Ihrer Wettbewerber.', unsafe_allow_html=True)
    else:
        st.write(f'**<span style="color:#000000">.</span>**', unsafe_allow_html=True)
else:
    st.write(f'**<span style="color:#000000">.</span>**', unsafe_allow_html=True)

st.write('')
c = alt.Chart(df_p1).mark_bar(size=18).transform_calculate(
    y="split(datum.y, '/ ')"
    ).encode(
        x=alt.X('Anteil',
                axis=alt.Axis(format='.0%', tickCount=5, tickSize=15, labelPadding=8, gridDash=[2, 3]),
                scale=alt.Scale(domain=[0, 0.2])),
        y=alt.Y('Branche_kurz',
                sort=alt.EncodingSortField(field='Anteil', order='descending'),
                axis=alt.Axis(tickSize=0, labelPadding=15),
                scale=alt.Scale(paddingOuter=0.7),
                title='Branche'),
        color=alt.condition(alt.datum.Branche_kurz == option, alt.value('#15C2FF'), alt.value('#434343')),
        tooltip=[alt.Tooltip('Branche'), alt.Tooltip('Anteil', format='.1%')]
    ).configure_axisY(
        titleAlign='right',
        titleAngle=0,
        titleY=-10,
        titleX=-15
    ).configure_axisX(
        titleY=55,
        labelFlush=False
    ).configure_axis(
        labelFontSize=13,
        titleFontSize=15
    ).configure_view(
        strokeWidth=0
    ).properties(height=450)
st.altair_chart(c, use_container_width=True, theme=None)
components.html('''<div style="text-align:right; color:#5D666E; font-family:'Roboto', sans-serif; font-size:0.63em">
                        Quelle: 
                        <a style="color:#007da7" href="https://www.bmwk.de/Redaktion/DE/Publikationen/Wirtschaft/einsatz-von-ki-deutsche-wirtschaft.pdf?__blob=publicationFile&v=8" target="_blank">BMWK, 2020</a>
                         (Abgerufen am 18.10.2022)
                   </div>''', height=40)

text = '''Zwar sind sich viele Unternehmen des Potenzials von KI-Anwendungen bewusst, doch nur wenige Unternehmen nutzen bereits KI-Lösungen.
IT-Unternehmen (IKT) sind hier noch am besten aufgestellt, da KI teilweise zum Kerngeschäft gehört, aber selbst hier nutzen nur knapp 18 % KI.
In den meisten anderen Branchen liegt der Anteil sogar unter 10 % (Gesamtdurchschnitt: 5,8 %).
Der Einsatz von KI kann daher sehr gut genutzt werden, um einen Wettbewerbsvorteil zu schaffen.'''
st.write(text)
st.write('')

st.markdown(f'**<p style="color:#15C2FF">Nächster Schritt:</p>**', unsafe_allow_html=True)
next = '''Doch warum ist der Einsatz von KI sinnvoll? Im Folgenden zeigen wir Ihnen die vielen Vorteile, die durch den Einsatz von KI entstehen.
       Als erstes erfahren Sie, wie sich die Verwendung von KI auf den Unternehmenserfolg auswirkt.'''
st.write(next)
want_to_contribute = st.button('WEITER ZUM UMSATZ')
if want_to_contribute:
    switch_page("umsatz")
