import streamlit as st
import pandas as pd
import plotly.express as px

#----------------------
# PAGE CONFIGURATION
#----------------------
st.set_page_config(
    page_title="GHG Dashboard",
    page_icon="🌍",
    layout="wide"
)

#------------------
# LOAD DATA
#-------------------

@st.cache_data
def load_data():
    files = {
        "Features":"data/ghg_features.csv",
        "Forecast":"data/forecast_test.csv",
        "Comparison":"data/comparison_table.csv",
        "Scenario Projection":"data/scenario_projections.csv",
        "Scenario Summary":"data/scenario_impact_summary.csv"
    }
    for name,path in files.items():
        if not os.path.exists(path):
            st.error(f"Missing file : {path}")
            return None

    df_features = pd.read_csv(files["Features"])
    forecast_test = pd.read_csv(files["Forecast"])
    comparison_table = pd.read_csv(files["Comparison"])
    scenario_projections = pd.read_csv(files["Scenario Projection"])
    scenario_impact_summary = pd.read_csv(files["Scenario Summary"])

    return (
        df_features,forecast_test,comparison_table,scenario_projections,scenario_impact_summary
    )
data = load_data()
if data is None:
    st.stop()
(
    df_features,
    forecast_test,
    comparison_table,
    scenario_projections,
    scenario_impact_summary
) = data

# -----------------------------
# SIDEBAR
#-------------------------------

st.sidebar.title("Climate Change")
st.sidebar.subheader("Trend Analysis & Forecasting")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select a Page",
    [
        "Overview",
        "Historical Trends",
        "Country Profile",
        "Machine Learning Models",
        "ETS Forecast",
        "Scenario Analysis",
        "Data Explorer"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **Project**
    Climate Change Trend Analysis and Forecasting
    **Internship**
    IDEAS TIH Summer Internship 2026
""")

# --------------------------------
# OVERVIEW PAGE
# ----------------------------------

if page == "Overview":

    st.title("Climate Change Trend Analysis and Forecasting")

    st.markdown("""
    Welcome to the **Climate Change Trend Analysis and Forecasting Dashboard**.
    This project analyzes historical greenhouse gas (GHG) emissions,
    builds baseline machine learning models, forecasts future CO₂ emissions,
    and evaluates different climate policy scenarios.
    The dashboard is based on the work completed during the
    **IDEAS TIH Summer Internship 2026**.
""")

    st.markdown("---")
    
    # KEY METRICS---------------------------
    
    total_countries = df_features["country"].nunique()
    start_year = int(df_features["year"].min())
    end_year = int(df_features["year"].max())
    latest_data = df_features[
        df_features["year"] == end_year
    ]
    total_co2 = latest_data["co2"].sum()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Countries",
            total_countries
        )
    with col2:
        st.metric(
            "Years Covered",
            f"{start_year}-{end_year}"
        )
    with col3:
        st.metric(
            "Latest Year",
            end_year
        )
    with col4:
        st.metric(
            "Total CO₂ (Latest Year)",
            f"{total_co2:,.0f}"
        )
    st.markdown("---")
    
    # DATASET PREVIEW-----------------
    
    st.subheader("Dataset Preview")
    st.dataframe(
        df_features.head(10),
        use_container_width=True
    )
    st.markdown("---")

    # SUMMARY---------------
    st.subheader("Dataset Summary")
    summary = pd.DataFrame({

        "Metric":[
            "Total Records",
            "Countries",
            "First Year",
            "Last Year"
        ],
        "Value":[
            len(df_features),
            total_countries,
            start_year,
            end_year
        ]
    })
    st.table(summary)


# ---------------------------------
# HISTORICAL TRENDS
# ---------------------------------

elif page == "Historical Trends":

    st.title("Historical CO₂ Emission Trends")

    st.markdown("""
    Compare historical CO₂ emissions for one or more countries
    using interactive visualizations.
""")

    countries = sorted(
        df_features["country"].unique()
    )
    selected_countries = st.multiselect(
        "Select Countries",
        countries,
        default=[
            "India",
            "China",
            "United States",
            "Australia",
            "Brazil",
            "Germany",
            "Japan",
            "Russia",
            "South Africa",
            "United Kingdom"
        ]
    )
    if len(selected_countries) == 0:
        st.warning("Please select at least one country")
        st.stop()
    filtered = df_features[
        df_features["country"].isin(
            selected_countries
        )
    ]
   
    # CO2 TREND---------------

    st.subheader("Historical CO₂ Emissions")
    fig = px.line(
        filtered,
        x="year",
        y="co2",
        color="country",
        markers=True,
        title="Historical CO₂ Emissions"
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="CO₂ Emissions (Mt)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # CO2 PER CAPITA------------------------
   
    st.subheader("CO₂ Per Capita")

    fig2 = px.line(
        filtered,
        x="year",
        y="co2_per_capita",
        color="country",
        markers=True,
        title="CO₂ Per Capita"
    )
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # 5 YEAR ROLLING MEAN-------------------

    st.subheader("5-Year Rolling Mean")

    rolling = filtered.dropna(
        subset=["co2_5yr_rolling_mean"]
    )
    fig3 = px.line(
        rolling,
        x="year",
        y="co2_5yr_rolling_mean",
        color="country",
        markers=True,
        title="5-Year Rolling Mean"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
    
    # YEAR OVER YEAR CHANGE--------------------    

    st.subheader("Year-over-Year CO₂ Percentage Change")
    yoy = filtered.dropna(
        subset=["co2_yoy_pct_change"]
    )
    fig4 = px.bar(
        yoy,
        x="year",
        y="co2_yoy_pct_change",
        color="country",
        barmode="group",
        title="Annual CO₂ Percentage Change"
    )

    fig4.update_layout(
        xaxis_title="Year",
        yaxis_title="YOY Change (%)"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # DATA TABLE-------------------------

    st.subheader("Filtered Dataset")
    st.dataframe(filtered,use_container_width=True)


# ----------------------------------
# COUNTRY PROFILE
# ----------------------------------

elif page == "Country Profile":

    st.title("Country Profile")

    st.markdown("""
    Explore detailed historical CO₂ emission statistics for an individual country.
""")

    country = st.selectbox(
        "Select a Country",
        sorted(df_features["country"].unique())
    )

    country_df = (
        df_features[
            df_features["country"] == country
        ]
        .sort_values("year")
    )
    latest = country_df.iloc[-1]

    # METRICS---------------------------

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Latest Year",
            int(latest["year"])
        )
    with col2:
        st.metric(
            "CO₂",
            f"{latest['co2']:.2f}"
        )
    with col3:
        st.metric(
            "CO₂ Per Capita",
            f"{latest['co2_per_capita']:.2f}"
        )
    with col4:
        if pd.notna(latest["ghg_intensity"]):
            st.metric(
                "GHG Intensity",
                f"{latest['ghg_intensity']:.2f}"
            )
        else:
            st.metric(
                "GHG Intensity",
                "N/A"
            )

    st.markdown("---")

    # CO2 TREND----------------------------

    st.subheader("Historical CO₂ Emissions")
    fig = px.line(
        country_df,
        x="year",
        y="co2",
        markers=True,
        title=f"{country} CO₂ Emissions"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # CO2 PER CAPITA----------------------------

    st.subheader("CO₂ Per Capita")
    fig2 = px.line(
        country_df,
        x="year",
        y="co2_per_capita",
        markers=True,
        title=f"{country} CO₂ Per Capita"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ROLLING MEAN----------------------

    rolling = country_df.dropna(
        subset=["co2_5yr_rolling_mean"]
    )
    st.subheader("5-Year Rolling Mean")
    fig3 = px.line(
        rolling,
        x="year",
        y="co2_5yr_rolling_mean",
        markers=True,
        title="5-Year Rolling Mean"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # YOY CHANGE---------------------

    yoy = country_df.dropna(
        subset=["co2_yoy_pct_change"]
    )
    st.subheader("Year-over-Year Change")
    fig4 = px.bar(
        yoy,
        x="year",
        y="co2_yoy_pct_change",
        title="Annual CO₂ Percentage Change"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # SUMMARY STATISTICS----------------------

    st.subheader("Summary Statistics")
    st.dataframe(
        country_df[
            [
                "co2",
                "co2_per_capita",
                "co2_5yr_rolling_mean",
                "co2_yoy_pct_change"
            ]
        ].describe(),
        use_container_width=True
    )

    # COUNTRY DATA--------------------------

    st.subheader("Country Dataset")
    st.dataframe(
        country_df,
        use_container_width=True
    )



# -------------------------------
# MACHINE LEARNING MODELS
# -------------------------------

elif page == "Machine Learning Models":

    st.title("Machine Learning Model Comparison")

    st.markdown("""
    This section compares the prediction performance of the baseline machine learning models developed in Week 3.
""")

    st.subheader("Performance Comparison Table")
    st.dataframe(
        comparison_table,
        use_container_width=True
    )
    st.markdown("---")
    country = st.selectbox(
        "Select Country",
        sorted(comparison_table["Country"].unique())
    )
    result = comparison_table[
        comparison_table["Country"] == country
    ]
    if result.empty:
        st.warning("No data available")
        st.stop()
    st.subheader(f"Model Performance : {country}")

    # MAE----------------------------

    mae = pd.DataFrame({
        "Model":[
            "Baseline",
            "Linear Regression",
            "Random Forest"
        ],
        "MAE":[
            result["Baseline MAE"].values[0],
            result["LR_MAE"].values[0],
            result["RF_MAE"].values[0]
        ]
    })
    fig1 = px.bar(
        mae,
        x="Model",
        y="MAE",
        color="Model",
        title="Mean Absolute Error"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # RMSE-----------------------

    rmse = pd.DataFrame({
        "Model":[
            "Baseline",
            "Linear Regression",
            "Random Forest"
        ],
        "RMSE":[
            result["Baseline RMSE"].values[0],
            result["LR_RMSE"].values[0],
            result["RF_RMSE"].values[0]
        ]
    })

    fig2 = px.bar(
        rmse,
        x="Model",
        y="RMSE",
        color="Model",
        title="Root Mean Squared Error"
    )
    st.plotly_chart(
        fig2,
        use_container_width=True
    )
    st.markdown("---")
    st.subheader("Country Performance")
    st.dataframe(
        result,
        use_container_width=True
    )


# ---------------------------------------------------
# ETS FORECAST PAGE
# ---------------------------------------------------

elif page == "ETS Forecast":

    st.title("ETS(A,Ad,N) Time-Series Forecast")
    
    st.markdown("""
    This page displays the future **CO₂ emission forecasts**
    generated using the **ETS(A,Ad,N) Exponential Smoothing model**.

    Forecast Horizon:
    - **2024 – 2043**
""")

    country = st.selectbox(
        "Select Country",
        sorted(forecast_test["country"].unique())
    )
    forecast_country = forecast_test[
        forecast_test["country"] == country
    ]
    historical = df_features[
        df_features["country"] == country
    ]
    fig = px.line(
        historical,
        x="year",
        y="co2",
        title=f"{country} Historical CO₂ Emissions"
    )
    
    fig.add_scatter(
        x=forecast_country["Year"],
        y=forecast_country["Forecast_CO2"],
        mode="lines+markers",
        name="ETS Forecast"
    )

    fig.add_scatter(
        x=forecast_country["Year"],
        y=forecast_country["Lower_95CI"],
        mode="lines",
        line=dict(width=0),
        showlegend=False
    )

    fig.add_scatter(
        x=forecast_country["Year"],
        y=forecast_country["Upper_95CI"],
        mode="lines",
        fill="tonexty",
        line=dict(width=0),
        name="95% Confidence Interval"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.subheader("Forecast Table")
    st.dataframe(
        forecast_country,
        use_container_width=True
    )


# ----------------------------------------------------------
# SCENARIO ANALYSIS PAGE
# ----------------------------------------------------------

elif page == "Scenario Analysis":

    st.title("Climate Policy Scenario Analysis")

    st.markdown("""
    Three future policy scenarios are compared:
    - Business As Usual (BAU)
    - Moderate Mitigation (2% annual reduction)
    - Aggressive Mitigation (5% annual reduction)
""")

    country = st.selectbox(
        "Select Country",
        sorted(scenario_projections["Country"].unique())
    )

    country_projection = scenario_projections[
        scenario_projections["Country"] == country
    ]

    fig = px.line(
        country_projection,
        x="Year",
        y="CO2_Projected",
        color="Scenario",
        markers=True,
        title=f"{country} Scenario Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Scenario Projection Data")
    st.dataframe(
        country_projection,
        use_container_width=True
    )
    st.subheader("Cumulative CO₂ Emissions (2025–2040)")
    summary = scenario_impact_summary[
        scenario_impact_summary["Country"] == country
    ]

    fig2 = px.bar(
        summary,
        x="Scenario",
        y="Cumulative_CO2",
        color="Scenario",
        title=f"{country} Cumulative Emissions"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.subheader("Global Scenario Comparison")

    global_projection = (
        scenario_projections
        .groupby(["Year", "Scenario"])["CO2_Projected"]
        .sum()
        .reset_index()
    )

    fig3 = px.line(
        global_projection,
        x="Year",
        y="CO2_Projected",
        color="Scenario",
        markers=True,
        title="Global CO₂ Projection"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


# -----------------------------------------------------
# DATA EXPLORER PAGE
# ----------------------------------------------------

elif page == "Data Explorer":

    st.title("Data Explorer")

    st.markdown("""
    Explore the engineered greenhouse gas dataset used throughout this project.
    You can:
    - View the complete dataset
    - Filter data by country
    - Select specific columns
    - Inspect summary statistics
""")
   
    # Country Selection--------------------------------------

    countries = sorted(df_features["country"].unique())
    selected_country = st.selectbox(
        "Select Country",
        ["All Countries"] + countries
    )
    if selected_country == "All Countries":
        filtered = df_features.copy()
    else:
        filtered = df_features[
            df_features["country"] == selected_country
        ]
        
    # Column Selection---------------------------------

    selected_columns = st.multiselect(
        "Select Columns",
        filtered.columns.tolist(),
        default=[
            "country",
            "year",
            "co2",
            "co2_per_capita"
        ]
    )
    if len(selected_columns) > 0:
        st.subheader("Dataset Preview")
        st.dataframe(
            filtered[selected_columns],
            use_container_width=True
        )
    st.subheader("Dataset Summary")
    st.write(f"Rows : {filtered.shape[0]}")
    st.write(f"Columns : {filtered.shape[1]}")
    st.subheader("Summary Statistics")
    st.dataframe(
        filtered.describe(include="all"),
        use_container_width=True
    )  

    st.success("Thank you for exploring this dashboard! 🌍")
