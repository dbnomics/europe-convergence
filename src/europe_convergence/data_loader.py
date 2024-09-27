from dbnomics import fetch_series

"""
Useful data to measure and plot convergence : choisir 10-15 pays 
PIB
price stability / inflation
long term interest rate convergence
public finance : healthy and viable
Autriche,Belgique,Allemagne,Danemark, France,Greece,Hongrie,Ireland,Italie,Lituanie,Pologne,Portugal,Roumanie,
Suède
"""

# list of european_country members
eu_countries = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "European Union - 27 countries (from 2020)",
    "Euro area – 20 countries (from 2023)"
]


def download_gdp_data():
    gdp = fetch_series(provider_code= "Eurostat", dataset_code= "tec00001", series_code="A.B1GQ.CP_EUR_HAB")
    df_gdp= gdp[gdp["Geopolitical entity (reporting)"].isin(eu_countries)]
    return df_gdp


def download_gdp_percap():
    gdp_percap = fetch_series(provider_code= "Eurostat", dataset_code= "tipsna40", series_code="A.CLV15_EUR_HAB.B1GQ")
    df_gdp_percap = gdp_percap[gdp_percap["Geopolitical entity (reporting)"].isin(eu_countries)]
    return df_gdp_percap


def download_hicp_data():
    hicp = fetch_series(
        provider_code="Eurostat",
        dataset_code="prc_hicp_fp",
        series_code="M.I15.CP00.FIN",
        max_nb_series=200,
    )

    df_hicp = hicp[hicp["Geopolitical entity (reporting)"].isin(eu_countries)]
    return df_hicp

def download_lng_int_rate():
    lng_int_rt = fetch_series(provider_code= "Eurostat", dataset_code="irt_lt_mcby_q", series_code="Q.MCBY.",
    max_nb_series=200)
    df_lng_int_rt = lng_int_rt[lng_int_rt["Geopolitical entity (reporting)"].isin(eu_countries)]
    return df_lng_int_rt


def download_debt_data():
    debt = fetch_series(provider_code= "Eurostat", dataset_code= "gov_10q_ggdebt", series_code="Q.GD.S13.PC_GDP")
    df_debt = debt[debt["Geopolitical entity (reporting)"].isin(eu_countries)]
    return df_debt


def download_deficit():
    deficit = fetch_series(provider_code= "Eurostat", dataset_code= "gov_10dd_edpt1", series_code="A.PC_GDP.S13.B9")
    df_deficit = deficit[deficit["Geopolitical entity (reporting)"].isin(eu_countries)]
    return df_deficit
