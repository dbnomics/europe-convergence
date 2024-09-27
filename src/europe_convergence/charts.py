from matplotlib.figure import figaspect
import pandas as pd
import plotly.express as px


def plot_gdp(df_gdp):
    df_gdp = df_gdp.rename(columns={"original_period": "Years"})
    fig = px.line(
        df_gdp,
        x="Years",
        y="value",
        color="Geopolitical entity (reporting)",
        title="Evolution of Gross Domestic Production",
        labels={
            "Years": "Years",
            "value": "GDP",
            "Geopolitical entity (reporting)": "European Union Countries",
        },
        custom_data=["Years", "value", "Geopolitical entity (reporting)"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "GDP: %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=700,
    )
    return fig


def plot_gdp_percap(df_gdp_percap):
    df_gdp_percap = df_gdp_percap.rename(columns={"original_period": "Years"})
    fig = px.line(
        df_gdp_percap,
        x="Years",
        y="value",
        color="Geopolitical entity (reporting)",
        title="Evolution of Gross Domestic Production per Capita",
        labels={
            "Years": "Years",
            "value": "GDP per capita",
            "Geopolitical entity (reporting)": "European Union Countries",
        },
        custom_data=["Years", "value", "Geopolitical entity (reporting)"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "GDP per capita: %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    return fig


def plot_hicp(df_hicp):
    df_hicp["original_period"] = pd.to_datetime(df_hicp["original_period"], errors="coerce")
    df_hicp["original_period"] = df_hicp["original_period"].dt.strftime("%Y-%m")
    df_hicp = df_hicp.rename(
        columns={
            "original_period": "Date",
            "Geopolitical entity (reporting)": "Country",
        }
    )
    fig = px.line(
        df_hicp,
        x="Date",
        y="original_value",
        color="Country",
        title="Evolution of harmonised index of consumer prices (HICP)",
        labels={
            "Date": "Years",
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
        title="Evolution of Long term interest rate - convergence criterion",
        labels={
            "Date": "Years",
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

def plot_debt(df_debt):
    df_debt = df_debt.rename(
        columns={
            "original_value" : "Debt",
            "Geopolitical entity (reporting)" : "Country"

    }
    )
    fig = px.line(
        df_debt,
        x="original_period",
        y="Debt",
        color="Country",
        title="General government gross debt - Percent of GDP",
        labels={
            "original_period": "Years",
            "Debt": "General government gross debt",
            "Country": "European Union Countries",
        },
        custom_data=["original_period", "Debt", "Country"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "General government gross debt (% of GDP): %{customdata[1]}",
            ]
        )
    )
    fig.update_layout(
        height=800,
    )
    
    return fig

def plot_deficit(df_deficit):
    df_deficit["original_period"] = pd.to_datetime(df_deficit["original_period"], errors="coerce")
    df_deficit["original_period"] = df_deficit["original_period"].dt.strftime("%Y")
    df_deficit = df_deficit.rename(
        columns={
            "original_period": "Date",
            "Geopolitical entity (reporting)": "Country",
        }
    )
    fig = px.line(
        df_deficit,
        x="Date",
        y="original_value",
        color="Country",
        title="Percentage of gross domestic product (GDP) – General government – Net lending (+) /net borrowing (-)",
        labels={
            "Date": "Years",
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
    