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
            "<h2 style='text-align: center; color: black;'>Kampagnenbericht Keywords</h2>", 
            unsafe_allow_html=True)
        placeholder.write("")
        
        placeholder_date_start.write("")
        start_datum = date_start.date_input(label="Wählen Sie das Startdatum", value=constants.start_datum, key="date_start_kw")
        end_datum = date_end.date_input(label="Wählen Sie das Enddatum", value=constants.end_datum, key="date_end_kw")
        placeholder_date_end.write("")

    st.markdown("---")


    #--- Daten laden ---
    df_keywords = db.google_ads_keywords(start_datum, end_datum)

    st.dataframe(data=df_keywords.sort_values('Klicks', ascending=False).style.format(precision=0, thousands='.', subset=['Klicks', 'Impressionen']).format('{:,.2%}', decimal=',', subset=['CTR', 'Anteil_moegliche_Impressionen', 'Impressionen_top']),
        height=500, use_container_width=True)
        
    # grid_fall_table = AgGrid(df_m_ads_filtered, 
    #                          height=500, 
    #                          # gridOptions=gridoptions,
    #                          update_mode=GridUpdateMode.SELECTION_CHANGED,
    #                          fit_columns_on_grid_load=True,
    #                          # theme='light',
    #                          # reload_data=True
    #                         )
