from matplotlib.figure import figaspect
import pandas as pd
import plotly.express as px


def plot_gdp(gdp_data):
    gdp_data["original_period"] = pd.to_datetime(
        gdp_data["original_period"], errors="coerce"
    )
    gdp_data["original_period"] = gdp_data["original_period"].dt.strftime("%Y")
    gdp_data = gdp_data.rename(columns={"original_period": "Year"})
    fig = px.line(
        gdp_data,
        x="Year",
        y="value",
        color="country (label)",
        title="Evolution of Gross Domestic Production",
        labels={
            "Year": "Year",
            "value": "GDP",
            "country (label)": "European Union Countries",
        },
        custom_data=["Year", "value", "country (label)"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Year: %{customdata[0]}",
                "GDP: %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=700,
    )
    return fig


def plot_gdp_percap(gdp_percap):
    gdp_percap["original_period"] = pd.to_datetime(
        gdp_percap["original_period"], errors="coerce"
    )
    gdp_percap["original_period"] = gdp_percap["original_period"].dt.strftime("%Y")
    gdp_percap = gdp_percap.rename(columns={"original_period": "Year"})
    fig = px.line(
        gdp_percap,
        x="Year",
        y="value",
        color="country (label)",
        title="Evolution of Gross Domestic Production per Capita",
        labels={
            "Year": "Year",
            "value": "GDP per capita",
            "country (label)": "European Union Countries",
        },
        custom_data=["Year", "value", "country (label)"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Year: %{customdata[0]}",
                "GDP per capita: %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    return fig


def plot_hicp(hicp):
    hicp["original_period"] = pd.to_datetime(hicp["original_period"], errors="coerce")
    hicp["original_period"] = hicp["original_period"].dt.strftime("%Y-%m")
    hicp = hicp.rename(
        columns={
            "original_period": "Date",
            "Geopolitical entity (reporting)": "Country",
        }
    )
    fig = px.line(
        hicp,
        x="Date",
        y="original_value",
        color="Country",
        title="Evolution of harmonised index of consumer prices (HICP) per European Union Countries",
        labels={
            "Date": "Date",
            "original_value": "HICP (Index, 2015=100)",
            "Country": "European Union Countries",
        },
        custom_data=["Date", "original_value", "Country"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "HICP (Index, 2015=100): %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    return fig

def plot_lng_int_rate(lng_int_rt):
    lng_int_rt["original_period"] = pd.to_datetime(lng_int_rt["original_period"], errors="coerce")
    lng_int_rt["original_period"] = lng_int_rt["original_period"].dt.strftime("%Y-%m")
    lng_int_rt = lng_int_rt.rename(
        columns={
            "original_period": "Date",
            "Geopolitical entity (reporting)": "Country",
        }
    )
    fig = px.line(
        lng_int_rt,
        x="Date",
        y="original_value",
        color="Country",
        title="Evolution of harmonised index of consumer prices (HICP) per European Union Countries",
        labels={
            "Date": "Date",
            "original_value": "Long term interest rate - convergence criterion",
            "Country": "European Union Countries",
        },
        custom_data=["Date", "original_value", "Country"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "Long Term Interest Rate: %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    
    return fig

def plot_debt(debt):
    debt["original_periode"] = pd.to_datetime(debt["original_period"], errors= "coerce")
    debt = debt.rename(
        columns={
            "original_value" : "Debt",
            "WEO Country" : "Country"

    }
    )
    fig = px.line(
        debt,
        x="original_period",
        y="Debt",
        color="Country",
        title="General government gross debt - Percent of GDP",
        labels={
            "original_period": "Year",
            "Debt": "General government gross debt",
            "Country": "European Union Countries",
        },
        custom_data=["original_period", "Debt", "Country"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Year: %{customdata[0]}",
                "General government gross debt (% of GDP): %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    
    return fig

def plot_deficit(deficit):
    deficit["original_period"] = pd.to_datetime(deficit["original_period"], errors="coerce")
    deficit["original_period"] = deficit["original_period"].dt.strftime("%Y")
    deficit = deficit.rename(
        columns={
            "original_period": "Date",
            "Geopolitical entity (reporting)": "Country",
        }
    )
    fig = px.line(
        deficit,
        x="Date",
        y="original_value",
        color="Country",
        title="Percentage of gross domestic product (GDP) – General government – Net lending (+) /net borrowing (-)",
        labels={
            "Date": "Date",
            "original_value": "General Government - Net lending - Net Borrowin (% of GDP)",
            "Country": "European Union Countries",
        },
        custom_data=["Date", "original_value", "Country"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "General Government - Net lending - Net Borrowin (% of GDP): %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    return fig
    