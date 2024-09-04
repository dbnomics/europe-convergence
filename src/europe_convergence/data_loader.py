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
        "OECD/QNA/AUT.B1_GS1.LNBQR.Q",
        "OECD/QNA/BEL.B1_GS1.LNBQR.Q",
        "OECD/QNA/DEU.B1_GS1.LNBQR.Q",
        "OECD/QNA/DNK.B1_GS1.LNBQR.Q",
        "OECD/QNA/FRA.B1_GS1.LNBQR.Q",
        "OECD/QNA/GRC.B1_GS1.LNBQR.Q",
        "OECD/QNA/HUN.B1_GS1.LNBQR.Q",
        "OECD/QNA/IRL.B1_GS1.LNBQR.Q",
        "OECD/QNA/ITA.B1_GS1.LNBQR.Q",
        "OECD/QNA/LTU.B1_GS1.LNBQR.Q",
        "OECD/QNA/POL.B1_GS1.LNBQR.Q",
        "OECD/QNA/PRT.B1_GS1.LNBQR.Q",
        "OECD/QNA/ROU.B1_GS1.LNBQR.Q",
        "OECD/QNA/SWE.B1_GS1.LNBQR.Q",
    )
    return gdp_data
