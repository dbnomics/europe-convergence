from csv import writer
import importlib

import streamlit as st
from charts import plot_gdp, plot_gdp_percap, plot_hicp, plot_lng_int_rate, plot_debt, plot_deficit
from data_loader import (
    download_gdp_data,
    download_gdp_percap,
    download_hicp_data,
    download_lng_int_rate,
    download_debt_data,
    download_deficit
)
from streamlit_option_menu import option_menu


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
                "GDP & GDP Per Capita",
                "Public Finance Sustainability",
                "Price Stability",
                "Long Term Interest Rate",
                "Sources"
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
        st.header("What is meant by convergence ?")
        st.write(
            'After its creation and multiple expansions, the European Union had to implement "convergence criteria" to ensure harmony and stability.\n'
            "Convergence, as an economic term, can be defined as the process by which economies or regions with different levels of production, wealth, debt etc. become more and more similar.\n"
            "\n"
            "**Does the European Union need convergence of its countries?**\n"
            "\n"
            "By entering the European Union, a country faces a legal obligation to join the Euro Area.\n"
            "Some countries have decided to not participate, as Denmark and Sweden have done.\n"
            "Other members, do not meet the criteria to enter the area, as Bulgaria or Romania.\n"
            "The Euro Area could be describe as a **Monetary  Union** and define as a geographic area made up of the 20 countries that have adopted the euro as their unique currency.\n"
            "The economic integration is a specific economic organization in which there are free movements of goods, people and capital that leads to the convergence of good prices, production factor prices and wages.\n"
            "A strict convergence only appeared in perfectly integrated economics.\n"
            'In many cases, the "automatic convergent" never happens due to increasing returns to scale (the more a firm produces a good the lower the average cost).\n'
            'To measure the degree of integration of a Monetary Union, looking at the "convergence" is a good indicator.\n'
            "- The absence of convergence could lead to important macroeconomic unbalances between members. Example : the sovereign debt crisis has shown the risks of wide gaps between economies.\n"
            "- In the Euro Area, the adoption of a single currency could create economic distortions if economies don't converge : some countries become more competitive leading to trade imbalances.\n"
            "- To be effective, the Monetary Policy requires that economies are similar: policies that could suit some countries be inadequate for others.\n"
            "- Finally, convergence reduces the risk of economic and financial crises\n."
        )
        st.write("**What are the Maastrich Convergence Criteria?**\n")
        st.write(
            "Convergence criteria have been decided by the European Union to ensure that a member is ready to enter the Euro Area.\n"
            "There are **four criteria of economic integration**:\n"
            "- **Price Stability**\n"
            "- **Sound and Sustainable Public Finance**\n"
            "- **Stability of Exchange Rate**\n"  # https://economy-finance.ec.europa.eu/euro/enlargement-euro-area/adoption-fixed-euro-conversion-rate/erm-ii-eus-exchange-rate-mechanism_en => only for Bulgaria and Danmark
            "- **Long Term Interest Rate**\n"
            "\n"
            "With data avalaible on DBnomics charts have been created to show the state of convergence of the members of the euro area and future members.\n"
        )
        st.subheader("**Members of the Euro Area**")
        st.write("**20 members of the European Union are members of the Euro Area**")
        st.write(
            "- Germany\n"
            "- Austria\n"
            "- Belgium\n"
            "- Cyprus\n"
            "- Croatia\n"
            "- Spain\n"
            "- Estonia\n"
            "- Finland\n"
            "- France\n"
            "- Greece\n"
            "- Ireland\n"
            "- Italy\n"
            "- Latvia\n"
            "- Lithuania\n"
            "- Luxembourg\n"
            "- Malta\n"
            "- Netherlands\n"
            "- Portugal\n"
            "- Slovakia\n"
            "- Slovenia\n"
        )
    if selected == "GDP & GDP Per Capita":
        df_gdp = download_gdp_data()
        fig1 = plot_gdp(df_gdp)
        st.plotly_chart(fig1)

        df_gdp_cap = download_gdp_percap()
        fig2 = plot_gdp_percap(df_gdp_cap)
        st.plotly_chart(fig2)

        st.subheader("Dataset GDP")
        st.write(df_gdp)


        st.subheader("Dataset GDP Per Capita")
        st.write(df_gdp_cap)

    if selected == "Public Finance Sustainability":
        st.write(":blue[**According to the Maastricht criteria, the public deficit of a European Union member state must not exceed 3% of GDP.**]")
        df_debt = download_debt_data()
        df_deficit = download_deficit()
        fig = plot_debt(df_debt)
        st.plotly_chart(fig)
        fig1 = plot_deficit(df_deficit)
        st.plotly_chart(fig1)
        st.subheader("Dataset General Governement Debt")
        st.write(df_debt)
        
        st.subheader("Dataset Deficit")
        st.write(df_deficit)

    if selected == "Price Stability":
        st.write(":blue[**Inflation rate cannot exceed by more than 1.5 percentage points that of the three best performing members.**]")
        df_hicp = download_hicp_data()
        fig = plot_hicp(df_hicp)
        st.plotly_chart(fig)
        st.subheader("Dataset")
        st.write(df_hicp)

    if selected == "Long Term Interest Rate":
        st.write(":blue[**The long-term interest rate should not exceed by more than two percentage points that of the three best-performing member states in terms of price stability.**]")
        df_lng_rt = download_lng_int_rate()
        fig = plot_lng_int_rate(df_lng_rt)
        st.plotly_chart(fig)
        st.subheader("Dataset")
        st.write(df_lng_rt)
    
    if selected == "Sources":
        st.subheader("**Data**")
        st.write(
            "- [GDP](https://db.nomics.world/WB/WDI?q=WB%2FWDI%2FA-NY.GDP.MKTP.KD&tab=list)\n"
            "- [GDP per Capita](https://db.nomics.world/WB/WDI?q=WB%2FWDI%2FA-NY.GDP.PCAP.KD&tab=list)\n"
            "- [General Government Debt](https://db.nomics.world/IMF/WEO:2024-04?q=debt&tab=list)\n"
            "- [Deficit](https://db.nomics.world/Eurostat/gov_10dd_edpt1?q=Eurostat%2Fgov_10dd_edpt1%2FA.PC_GDP.S13.B9&tab=list)\n"
            "- [HICP](https://db.nomics.world/Eurostat/prc_hicp_fp?q=Eurostat%2Fprc_hicp_fp%2FM.I15.CP00.FIN&tab=list)\n"
            "- [Long Term Interest Rate](https://db.nomics.world/Eurostat/irt_lt_mcby_q?tab=list)\n"
        )

        st.markdown("---")
        st.write("[Source Code](https://github.com/dbnomics/europe-convergence)")
        st.write("[DBnomics](https://db.nomics.world)")


if __name__ == "__main__":
    main()
