import streamlit as st
from st_aggrid import AgGrid  #, GridUpdateMode
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
            "<h2 style='text-align: center; '>Kampagnenbericht Google Ads</h2>", 
            unsafe_allow_html=True)
        placeholder.write("")
        
        placeholder_date_start.write("")
        start_datum = date_start.date_input(label="Wählen Sie das Startdatum", value=constants.start_datum)
        end_datum = date_end.date_input(label="Wählen Sie das Enddatum", value=constants.end_datum)
        placeholder_date_end.write("")

        # st.write(start_datum)
        # start_datum = pd.to_datetime(start_datum)
        # end_datum = pd.to_datetime(end_datum)
        # st.write(end_datum)

    st.markdown("---")

    #--- Daten laden ---
    df_g_ads = db.google_ads(start_datum, end_datum)

    metric1, metric2, metric3, metric4, metric5 = st.columns(5)
    metric1.metric(label="Klicks", value=constants.format_number(df_g_ads['Klicks'].sum()))
    metric2.metric(label="Impressionen", value=constants.format_number(df_g_ads['Impressionen'].sum()))
    metric3.metric(label="Kosten", value=constants.format_number(df_g_ads['Kosten'].sum(), 2) + " €")
    metric4.metric(label="Transaktionen", value=constants.format_number(df_g_ads['Transaktionen'].sum()))
    metric5.metric(label="⌀ CPC", value=constants.format_number(df_g_ads['Kosten'].sum() / df_g_ads['Klicks'].sum(), 2) + " €")

    st.markdown("---")
    df_g_ads = constants.df_format(df_g_ads)
    grid_g_table = AgGrid(df_g_ads[['Kampagne', 'Klicks', 'Impressionen', 'Kosten', 'CPC', 'CPM', 'Transaktionen']], 
                            # height=auto, 
                            # gridOptions=gridoptions,
                            # update_mode=GridUpdateMode.SELECTION_CHANGED,
                            fit_columns_on_grid_load=True,
                            # theme='light',
                            # reload_data=True
                            )
