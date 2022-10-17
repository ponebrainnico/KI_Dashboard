import pandas as pd
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('daten/Pone_datawarehouse_.json')
project_id = "datawarehouse-271615"
customer= 'Lamm' ###### TODO: HIER ZUGRIFF AUF EINGABEMASKE


def google_ads(start_datum, end_datum):
    # Für Seite 1
    sql_g_ads = """
    SELECT
        campaign as Kampagne,
        SUM(clicks) as Klicks,
        SUM(conversions) as Transaktionen,
        ROUND(SUM(cost),2) as Kosten,
        (SUM(cost) / SUM(clicks)) as CPC,
        ROUND(AVG(average_cpc),2) as CPC_avg,
        ROUND(AVG(average_cpm),2) as CPM_avg,
        (SUM(cost) / SUM(impressions))*1000 as CPM,
        SUM(impressions) as Impressionen,
    FROM `datawarehouse-271615.PerformanceOne.BO_{2}_Ads_Kampagnen`
    WHERE day >= '{0}' AND day <= '{1}'
    GROUP BY campaign
    """.format(start_datum, end_datum, customer)
    df_g_ads = pd.read_gbq(sql_g_ads, project_id=project_id, dialect='standard', credentials=credentials)
    return df_g_ads

def google_ads_agg(start_datum, end_datum):
    # Für Seite 2
    sql_g_ads_agg = """
    SELECT
        SUM(clicks) as Klicks,
        SUM(conversions) as Transaktionen,
        ROUND(SUM(cost),2) as Kosten,
        (SUM(cost) / SUM(clicks)) as CPC,
        ROUND(AVG(average_cpc),2) as CPC_avg,
        (SUM(cost) / SUM(impressions))*1000 as CPM,
        ROUND(AVG(average_cpm),2) as CPM_avg,
        (SUM(clicks) / sum(impressions))*100 as CTR,
        SUM(impressions) as Impressionen,
        'Google Ads' as Kanal
    FROM `datawarehouse-271615.PerformanceOne.BO_{2}_Ads_Kampagnen`
    WHERE day >= '{0}' AND day <= '{1}'
    """.format(start_datum, end_datum, customer)
    df_g_ads_agg = pd.read_gbq(sql_g_ads_agg, project_id=project_id, dialect='standard', credentials=credentials)
    
    return df_g_ads_agg


def google_ads_keywords(start_datum, end_datum):
    # Für Seite 4
    sql_g_ads = """
    SELECT
        campaign as Kampagne,
        ad_group_criterion_keyword_text AS Keyword,
        SUM(clicks) AS Klicks,
        SUM(impressions) AS Impressionen,
        (SUM(clicks) / NULLIF(SUM(impressions), 0)) AS CTR,
        (SUM(CAST(search_impr_share AS FLOAT64) * impressions) / NULLIF(SUM(impressions), 0)) AS Anteil_moegliche_Impressionen,
        (SUM(CAST(search_top_impression_share AS FLOAT64) * impressions) / NULLIF(SUM(impressions), 0)) AS Impressionen_top
    FROM `datawarehouse-271615.PerformanceOne.BO_{2}_Ads_Keywords`
    WHERE day >= '{0}' AND day <= '{1}'
    GROUP BY campaign, ad_group_criterion_keyword_text
    """.format(start_datum, end_datum, customer)
    df_g_ads = pd.read_gbq(sql_g_ads, project_id=project_id, dialect='standard')
    return df_g_ads


def microsoft_ads_agg(start_datum, end_datum):
    # Microsoft Ads ### Achtung: cpm berechnen
    # Für Seite 1
    sql_m_ads_agg = """
    SELECT 
        SUM(clicks) as Klicks,
        SUM(impressions) as Impressionen,
        ROUND(SUM(costs),2) as Kosten,
        (SUM(clicks) / sum(impressions))*100 as CTR,
        ROUND(AVG(averagecpc),2) as CPC_avg,
        SUM(conversion_value) as Transaktionen,
        ROUND(SUM(allrevenue),2) as Umsatz,
        (SUM(costs) / SUM(clicks)) as CPC,
        (SUM(costs) / SUM(impressions))*1000 as CPM,
        'Microsoft Ads' as Kanal
    FROM `datawarehouse-271615.PerformanceOne.BO_{2}_MicrosoftAds_Kampagnen`
    WHERE timeperiod >= '{0}' AND timeperiod <= '{1}'
    """.format(start_datum, end_datum, customer)
    df_m_ads_agg = pd.read_gbq(sql_m_ads_agg, project_id=project_id, dialect='standard', credentials=credentials)
    return df_m_ads_agg


def microsoft_ads(start_datum, end_datum):
    # Für Seite 3
    sql_m_ads = """
    SELECT
        campaign as Kampagne,
        SUM(clicks) as Klicks,
        SUM(impressions) as Impressionen,
        SUM(costs) as Kosten,
        SUM(conversions_post_click) as Transaktionen,
        SUM(conversion_value) as Umsatz,
        SUM(costs) / SUM(clicks) as CPC,
        (SUM(costs) / SUM(impressions))*1000 as CPM,
        (SUM(clicks) / SUM(impressions)) as CTR
    FROM `datawarehouse-271615.PerformanceOne.BO_{2}_MicrosoftAds_Kampagnen`
    WHERE timeperiod >= '{0}' AND timeperiod <= '{1}'
    GROUP BY campaign
    """.format(start_datum, end_datum, customer)
    df_m_ads = pd.read_gbq(sql_m_ads, project_id=project_id, dialect='standard')
    return df_m_ads
