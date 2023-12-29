import pandas as pd
import requests
from IPython.display import HTML
from IPython.display import display

def data_report(df):
    """
    Generate a summary report for a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to generate the report for.

    Returns:
        pd.DataFrame: A summary report including column names, data types,
        percentage of missing values, number of missing values, number of unique
        values, and percentage of cardinality.

    Example:
        df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        report = data_report(df)
        print(report)
    """
    # Get column names
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    # Get data types
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    # Calculate percentage of missing values
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(
        percent_missing.values, columns=["MISSINGS (%)"])

    # Get number of missing values
    num_missings = round(df.isnull().sum())
    num_missings_df = pd.DataFrame(num_missings.values, columns=["MISSINGS"])

    # Get number of unique values
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])

    # Calculate percentage of cardinality
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(
        percent_cardin.values, columns=["CARDIN (%)"])

    # Concatenate all DataFrames
    concatenado = pd.concat([cols, types, percent_missing_df,
                            num_missings_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)

    return concatenado.T


def verbose_request(url):
    """
    Realiza una solicitud GET a la URL proporcionada e imprime un mensaje basado en el código de estado HTTP.

    Args:
        url (str): La URL a la que se realiza la solicitud.

    Returns:
        requests.Response: El objeto de respuesta de la solicitud.

    Example:
        >>> response = verbose_request("https://jsonplaceholder.typicode.com/posts/1")
        Todo OK
    """
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.reason}")
    else:
        print('Request OK [200]')
        return response


def df_horizontal(dfs):
    """
    Combina múltiples DataFrames y los muestra horizontalmente en un entorno Jupyter Notebook.

    Args:
        dfs (list): Una lista de DataFrames de pandas.

    Returns:
        None

    Example:
        >>> df_horizontal([df1, df2, df3])
    """
    html = '<div style="display:flex">'
    for df in dfs:
        html += '<div style="margin-right: 32px">'
        html += df.to_html()
        html += '</div>'
    html += '</div>'
    display(HTML(html))
