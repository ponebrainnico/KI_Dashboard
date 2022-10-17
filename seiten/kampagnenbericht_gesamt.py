import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
import ui.template as template
import daten.datenbank as db
import constants


def run_kampagnenbericht():

    #--- UI laden ---
    template.local_css()

    logo, title, placeholder = st.columns([1, 3, 1])
    placeholder_date_start, date_start, date_end, placeholder_date_end = st.columns(4)
    with st.container():
        logo.image(template.pone_logo())
        title.markdown(
            "<h2 style='text-align: center; '>Kampagnenbericht Gesamt</h2>", 
            unsafe_allow_html=True)
        placeholder.write("")
        
        placeholder_date_start.write("")
        start_datum = date_start.date_input(label="Wählen Sie das Startdatum", value=constants.start_datum, key="start_datum_session")
        end_datum = date_end.date_input(label="Wählen Sie das Enddatum", value=constants.end_datum, key="end_datum_session")
        placeholder_date_end.write("")

    st.markdown("---")

    #--- Daten laden ---
    df_g_ads_agg = db.google_ads_agg(start_datum, end_datum)
    df_m_ads_agg = db.microsoft_ads_agg(start_datum, end_datum)

    # Daten zusammenführen
    df_complete = df_g_ads_agg.append(df_m_ads_agg)

    #### DATEN ANZEIGEN
    metric1,metric2,metric3,metric4,metric5 = st.columns(5)
    metric1.metric(label="Klicks", value=constants.format_number(df_complete['Klicks'].sum(), 0))
    metric2.metric(label="Impressionen", value=constants.format_number(df_complete['Impressionen'].sum(), 0))
    metric3.metric(label="Kosten", value=str(constants.format_number(df_complete['Kosten'].sum(), 2)) + " €")
    metric4.metric(label="Transaktionen", value=constants.format_number(df_complete['Transaktionen'].sum(), 0))
    metric5.metric(label="⌀ CPC", value=str(constants.format_number(df_complete['Kosten'].sum() / df_complete['Klicks'].sum(), 2)) +" €")



    df_complete = df_complete[['Kanal', 'Klicks', 'Impressionen', 'Kosten', 'CPC', 'CPM', 'CTR', 'Transaktionen', 'Umsatz']]

    # ALTERNATIVE ZUR NORMALTEN st.table
    grid_fall_table = AgGrid(constants.df_format(df_complete), 
                            height=110, 
                            #gridOptions=gridoptions,
                            update_mode=GridUpdateMode.SELECTION_CHANGED,
                            fit_columns_on_grid_load=True,
                            #theme='light',
                            #reload_data=True
                            )

    st.markdown("---")
    st.dataframe(data=df_complete.style.format(decimal=',', precision=2).format(precision=0, subset=['Klicks', 'Impressionen', 'Transaktionen']), use_container_width=True)
