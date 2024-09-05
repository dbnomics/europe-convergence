import importlib

import streamlit as st
from charts import plot_gdp, plot_gdp_percap, plot_hicp, plot_lng_int_rate
from data_loader import download_gdp_data, download_gdp_percap, download_hicp_data, download_lng_int_rate
from streamlit_option_menu import option_menu

from europe_convergence.charts import plot_gdp_percap

# Pas forcémement nécessaire de faire un truc exprès pour les graphiques : ils vont être relativement simples
# Faire une page de présentation
# Faire des pages pour chaque critère de convergence
# => Voir comment télécharger les données pour maximiser l'efficacité : pas trop de transformation


def main() -> None:
    package_dir = importlib.resources.files("europe_convergence")
    st.set_page_config(
        page_title="Convergence of the European Union Countries",
        page_icon=str(package_dir / "images/favicon.png"),
    )
    st.image(str(package_dir / "images/dbnomics.svg"), width=300)
    st.title(":blue[A Convergence of the European Union Countries ?]")

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(str(package_dir / "assets/styles.css"))
    st.markdown(
        """
        <style>
        hr {
            height: 1px;
            border: none;
            color: #333;
            background-color: #333;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=[
                "Explanations",
                "GDP",
                "GDP Per Capita",
                "Price Stability",
                "Long Term Interest Rate",
                "Sources",
            ],
            icons=[
                "book",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "search",
            ],
            menu_icon=":",
            default_index=0,
        )

    if selected == "Explanations":
        st.markdown("In progress...")

    if selected == "GDP":
        df_gdp = download_gdp_data()
        fig = plot_gdp(df_gdp)
        st.plotly_chart(fig)
        st.subheader("Data Set")
        st.write(df_gdp)

    if selected == "GDP Per Capita":
        df_gdp_cap = download_gdp_percap()
        fig = plot_gdp_percap(df_gdp_cap)
        st.plotly_chart(fig)
        st.subheader("Data Set")
        st.write(df_gdp_cap)

    if selected == "Price Stability":
        df_hicp = download_hicp_data()
        fig = plot_hicp(df_hicp)
        st.plotly_chart(fig)
        st.subheader("Data Set")
        st.write(df_hicp)
    
    if selected == "Long Term Interest Rate":
        df_lng_rt = download_lng_int_rate()
        fig = plot_lng_int_rate(df_lng_rt)
        st.plotly_chart(fig)
        st.subheader("Data Set")
        st.write(df_lng_rt)

if __name__ == "__main__":
    main()
