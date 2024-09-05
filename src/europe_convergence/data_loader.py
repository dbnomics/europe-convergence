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


def download_gdp_data():
    gdp_data = fetch_series(
        [
            "WB/WDI/A-NY.GDP.MKTP.KD-AUS",
            "WB/WDI/A-NY.GDP.MKTP.KD-BEL",
            "WB/WDI/A-NY.GDP.MKTP.KD-DEU",
            "WB/WDI/A-NY.GDP.MKTP.KD-DNK",
            "WB/WDI/A-NY.GDP.MKTP.KD-FRA",
            "WB/WDI/A-NY.GDP.MKTP.KD-GRC",
            "WB/WDI/A-NY.GDP.MKTP.KD-IRL",
            "WB/WDI/A-NY.GDP.MKTP.KD-ITA",
            "WB/WDI/A-NY.GDP.MKTP.KD-LTU",
            "WB/WDI/A-NY.GDP.MKTP.KD-POL",
            "WB/WDI/A-NY.GDP.MKTP.KD-PRT",
            "WB/WDI/A-NY.GDP.MKTP.KD-ROU",
            "WB/WDI/A-NY.GDP.MKTP.KD-SWE",
        ],
        max_nb_series=20,
    )
    return gdp_data


def download_gdp_percap():
    gdp_percap = fetch_series(
        [
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-AUS",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-BEL",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-DEU",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-DNK",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-FRA",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-GRC",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-IRL",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-ITA",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-LTU",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-POL",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-PRT",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-ROU",
            "WB/WDI/A-NY.GDP.MKTP.KD.ZG-SWE",
        ],
        max_nb_series=20,
    )
    return gdp_percap


def download_hicp_data():
    hicp = fetch_series(
        [
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.AT",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.BE",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.DE",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.DK",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.EL",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.ES",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.FR",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.HR",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.HU",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.IE",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.LT",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.NL",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.PL",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.PT",
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.SE",
        ],
        max_nb_series=20,
    )
    return hicp
def download_lng_int_rate():
    lng_int_rt= fetch_series(
        [
            "Eurostat/irt_lt_mcby_q/Q.MCBY.AT",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.BE",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.DE",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.DK",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.EL",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.EE",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.ES",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.FI",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.FR",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.HU",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.IT",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.MT",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.NL",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.PL",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.PT",
            "Eurostat/irt_lt_mcby_q/Q.MCBY.SE",
        ],
    max_nb_series= 20
    )
    return lng_int_rt