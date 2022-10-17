from datetime import datetime

start_datum = datetime(2022, 8, 1)
end_datum = datetime(2022, 8, 5)
start_datum_str = start_datum.strftime("%Y-%m-%d")
end_datum_str = end_datum.strftime("%Y-%m-%d")


def format_number(number, precision=0):
    # build format string
    format_str = '{{:,.{}f}}'.format(precision)

    # make number string
    number_str = format_str.format(number)

    # replace chars
    return number_str.replace(',', 'X').replace('.', ',').replace('X', '.')


def df_format(df):
    columns = {'Klicks': 0,
               'Impressionen': 0,
               'Kosten': 2,
               'CPC': 2,
               'CTR': 2,
               'CPM': 2,
               'Umsatz': 2,
               'Transaktionen': 0
               }
    columns.keys()
    
    df_formatted = df.copy()
    matched_cols = [x for x in columns.keys() if x in df_formatted.columns]
    for col in matched_cols:
        df_formatted[col] = df_formatted[col].apply(lambda x: format_number(x, columns[col]))

    return df_formatted
