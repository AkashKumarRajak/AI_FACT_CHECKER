import streamlit as st
import pandas as pd
import plotly.express as px


def render_dashboard(history):

    st.header("Analytics Dashboard")

    if len(history) == 0:

        st.warning("No analytics data available.")

        return

    # ==================================================
    # DATAFRAME
    # ==================================================

    df = pd.DataFrame(

        history,

        columns=[
            "id",
            "claim",
            "result",
            "confidence",
            "category",
            "risk",
            "source_trust"
        ]
    )

    # ==================================================
    # METRICS
    # ==================================================

    total = len(df)

    avg_confidence = round(
        df["confidence"].mean(),
        2
    )

    avg_source = round(
        df["source_trust"].mean(),
        2
    )

    top_category = (
        df["category"]
        .mode()[0]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Verifications",
            total
        )

    with col2:
        st.metric(
            "Average Confidence",
            f"{avg_confidence}%"
        )

    with col3:
        st.metric(
            "Average Source Trust",
            f"{avg_source}%"
        )

    with col4:
        st.metric(
            "Top Category",
            top_category
        )

    st.divider()

    # ==================================================
    # CONFIDENCE DISTRIBUTION
    # ==================================================

    st.subheader(
        "Confidence Score Distribution"
    )

    fig1 = px.histogram(

        df,

        x="confidence",

        color="confidence",

        nbins=10,

        color_discrete_sequence=[
            "#00F5FF",
            "#00FF85",
            "#FFD700",
            "#FF6B00",
            "#FF006E"
        ]
    )

    fig1.update_layout(

        paper_bgcolor="#040816",

        plot_bgcolor="#040816",

        font_color="white"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ==================================================
    # CATEGORY DISTRIBUTION
    # ==================================================

    st.subheader(
        "Category Distribution"
    )

    category_count = (
        df["category"]
        .value_counts()
        .reset_index()
    )

    category_count.columns = [
        "category",
        "count"
    ]

    fig2 = px.pie(

        category_count,

        names="category",

        values="count",

        hole=0.5,

        color="category",

        color_discrete_sequence=[
            "#22D3EE",
            "#00F57A",
            "#8B5CF6",
            "#FF4D6D",
            "#FACC15"
        ]
    )

    fig2.update_layout(

        paper_bgcolor="#040816",

        font_color="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ==================================================
    # RISK DISTRIBUTION
    # ==================================================

    st.subheader(
        "Risk Level Distribution"
    )

    risk_count = (
        df["risk"]
        .value_counts()
        .reset_index()
    )

    risk_count.columns = [
        "risk",
        "count"
    ]

    fig3 = px.pie(

        risk_count,

        names="risk",

        values="count",

        hole=0.5,

        color="risk",

        color_discrete_map={

            "LOW": "#00FF85",
            "MEDIUM": "#FFD700",
            "HIGH": "#FF3B30"

        }
    )

    fig3.update_layout(

        paper_bgcolor="#040816",

        font_color="white"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )