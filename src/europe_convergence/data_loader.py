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
            "WB/WDI/A-NY.GDP.PCAP.KD-AUS",
            "WB/WDI/A-NY.GDP.PCAP.KD-BEL",
            "WB/WDI/A-NY.GDP.PCAP.KD-DEU",
            "WB/WDI/A-NY.GDP.PCAP.KD-DNK",
            "WB/WDI/A-NY.GDP.PCAP.KD-FRA",
            "WB/WDI/A-NY.GDP.PCAP.KD-GRC",
            "WB/WDI/A-NY.GDP.PCAP.KD-IRL",
            "WB/WDI/A-NY.GDP.PCAP.KD-ITA",
            "WB/WDI/A-NY.GDP.PCAP.KD-LTU",
            "WB/WDI/A-NY.GDP.PCAP.KD-POL",
            "WB/WDI/A-NY.GDP.PCAP.KD-PRT",
            "WB/WDI/A-NY.GDP.PCAP.KD-ROU",
            "WB/WDI/A-NY.GDP.PCAP.KD-SWE",
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
            "Eurostat/prc_hicp_fp/M.I15.CP00.FIN.RO",
        ],
        max_nb_series=20,
    )
    return hicp


def download_lng_int_rate():
    lng_int_rt = fetch_series(
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
        max_nb_series=20,
    )
    return lng_int_rt


def download_debt_data():
    debt = fetch_series(
        [
            "IMF/WEO:2024-04/AUS.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/BEL.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/DEU.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/DNK.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/FRA.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/GRC.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/IRL.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/ITA.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/LTU.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/POL.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/PRT.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/ROU.GGXWDG_NGDP.pcent_gdp",
            "IMF/WEO:2024-04/SWE.GGXWDG_NGDP.pcent_gdp",
        ]
    )
    return debt


def download_deficit():
    deficit = fetch_series(
        [
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.AT",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.BE",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.DE",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.DK",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.EL",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.EE",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.ES",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.FI",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.FR",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.HU",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.IT",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.MT",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.NL",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.PL",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.PT",
            "Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.B9.SE",
        ]
    )
    return deficit
