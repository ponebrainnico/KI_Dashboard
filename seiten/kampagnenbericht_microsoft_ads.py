import streamlit as st
# from st_aggrid import AgGrid, GridUpdateMode
# from st_aggrid.grid_options_builder import GridOptionsBuilder
import ui.template as template
import daten.datenbank as db
import constants


def run_kampagnenbericht():
    #--- UI laden ---
    template.local_css()
    template.max_width()

    logo, title, placeholder = st.columns([1, 3, 1])
    placeholder_date_start, date_start, date_end, placeholder_date_end = st.columns(4)
    with st.container():
        logo.image(template.pone_logo())
        title.markdown(
            "<h2 style='text-align: center; '>Kampagnenbericht Microsoft Ads</h2>", 
            unsafe_allow_html=True)
        placeholder.write("")
        
        placeholder_date_start.write("")
        start_datum = date_start.date_input(label="Wählen Sie das Startdatum", value=constants.start_datum, key="date_start_msad")
        end_datum = date_end.date_input(label="Wählen Sie das Enddatum", value=constants.end_datum, key="date_end_msad")
        placeholder_date_end.write("")

    #--- Daten laden ---
    df_m_ads = db.microsoft_ads(start_datum, end_datum)
    
    st.markdown("---")

    metric1, metric2, metric3, metric4, metric5 = st.columns(5)
    metric1.metric(label="Klicks", value=constants.format_number(df_m_ads['Klicks'].sum()))
    metric2.metric(label="Impressionen", value=constants.format_number(df_m_ads['Impressionen'].sum()))
    metric3.metric(label="Kosten", value=constants.format_number(df_m_ads['Kosten'].sum(), 2) + " €")
    metric4.metric(label="Transaktionen", value=constants.format_number(df_m_ads['Transaktionen'].sum()))
    metric5.metric(label="⌀ CPC", value=constants.format_number(df_m_ads['Kosten'].sum() / df_m_ads['Klicks'].sum(), 2) + " €")

    st.markdown("---")

    # Dataframe in Eurpäische Zahlenformat bringen
    df_m_ads = df_m_ads.style.format(precision=0, thousands='.', subset=['Klicks', 'Impressionen', 'Transaktionen'])\
                             .format('{:.2%}', decimal=',', subset=['CTR'])\
                             .format('{:.2f} €', decimal=',', thousands='.', subset=['CPC', 'Kosten', 'Umsatz', 'CPM'])
    st.dataframe(data=df_m_ads, height=500, use_container_width=True)
    # grid_fall_table = AgGrid(df_m_ads_filtered, 
    #                          height=500, 
    #                          # gridOptions=gridoptions,
    #                          update_mode=GridUpdateMode.SELECTION_CHANGED,
    #                          fit_columns_on_grid_load=True,
    #                          # theme='light',
    #                          # reload_data=True
    #                         )
