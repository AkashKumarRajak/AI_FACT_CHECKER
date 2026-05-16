import streamlit as st
from services.tavily_service import search_claim
from services.openrouter_service import verify_claim

from utils.confidence import calculate_confidence
from utils.category import detect_category
from utils.risk_score import calculate_risk_score
from utils.credibility import calculate_source_trust

from database.db import (
    init_db,
    save_result,
    get_history,
    delete_history
)

from dashboard.analytics import render_dashboard


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Fact Verification & Intelligence Platform",
    layout="wide"
)

init_db()


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #040816;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #1f2230;
}

h1, h2, h3 {
    color: white;
}

.stButton>button {
    background: linear-gradient(
        90deg,
        #00C6FF,
        #0072FF
    );

    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 24px;
    font-weight: bold;
}

.stButton>button:hover {
    transform: scale(1.03);
    transition: 0.2s;
}

/* DELETE BUTTON */

button[kind="secondary"] {
    background: #1f2937 !important;
    color: #9ca3af !important;
    border: 1px solid #374151 !important;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #9ca3af;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("AI Fact Checker")

    st.info(
        "AI-powered misinformation detection and verification platform."
    )

    st.divider()

    st.subheader("Features")

    st.markdown("""
    - AI Verification
    - Live Evidence
    - Trust Analysis
    - Analytics Dashboard
    - Fake News Risk Detection
    """)

    st.divider()

    st.subheader("Trending Claims")

    st.markdown("""
    - AI replacing jobs
    - Bitcoin market crash
    - Climate change debate
    - US election claims
    """)


# ==================================================
# TITLE
# ==================================================

st.title("AI Fact Verification & Intelligence Platform")

st.markdown("""
AI-powered claim verification using:

- Live web evidence
- AI reasoning
- Confidence scoring
- Source credibility analysis
- Verification analytics
- Fake news risk scoring
""")


# ==================================================
# TABS
# ==================================================

tab1, tab2 = st.tabs([
    "Verification",
    "Analytics Dashboard"
])


# ==================================================
# TAB 1
# ==================================================

with tab1:

    claim = st.text_area(
    "Enter a claim to verify",
    value=st.session_state.get(
        "claim_input",
        ""
    ),
    height=150
)

    verify_button = st.button(
        "Verify Claim"
    )

    if verify_button and claim:

        with st.spinner("Searching evidence..."):
            evidence = search_claim(claim)

        with st.spinner("AI analyzing claim..."):
            result = verify_claim(
                claim,
                evidence
            )

        with st.spinner("Calculating confidence..."):
            confidence = calculate_confidence(
                claim,
                evidence,
                result
            )

        risk = calculate_risk_score(claim)

        category = detect_category(claim)

        source_score = calculate_source_trust(
            [
                src.get("url", "")
                for src in evidence
            ]
        )

        # SAVE

        save_result(
            claim,
            result,
            confidence,
            category,
            risk,
            source_score
        )

        st.success("Verification Complete")

        # METRICS

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Confidence Score",
                f"{confidence}%"
            )

        with col2:
            st.metric(
                "Category",
                category
            )

        with col3:

            if risk.upper() == "HIGH":
                st.error(f"Misinformation Risk: {risk}")

            elif risk.upper() == "MEDIUM":
                st.warning(f"Misinformation Risk: {risk}")

            else:
                st.success(f"Misinformation Risk: {risk}")

        with col4:
            st.metric(
                "Source Trust",
                f"{source_score}%"
            )

        st.divider()

        # RESULT

        st.subheader("AI Verification Result")

        if "true" in result.lower():
            st.success(result)

        elif "false" in result.lower():
            st.error(result)

        else:
            st.warning(result)

        st.divider()

        # SOURCES

        st.subheader("Evidence Sources")

        for item in evidence:

            title = item.get(
                "title",
                "Source"
            )

            content = item.get(
                "content",
                ""
            )

            url = item.get(
                "url",
                ""
            )

            with st.expander(title):

                st.write(content)

                st.markdown(
                    f"[Open Source]({url})"
                )

    # ==================================================
    # HISTORY
    # ==================================================

    st.divider()

history = get_history()

st.subheader("Recent Verifications")

for row in history:

    id_ = row[0]
    old_claim = row[1]
    confidence_old = row[3]
    category_old = row[4]

    col1, col2 = st.columns([10, 1])
    
    # ==========================================
    # CLAIM BUTTON
    # ==========================================

    with col1:

        if st.button(
            old_claim,
            key=f"claim_{id_}"
        ):

            st.session_state["claim_input"] = old_claim

            st.rerun()

        st.caption(
            f"Confidence: {confidence_old}% | Category: {category_old}"
        )

    # ==========================================
    # DELETE BUTTON
    # ==========================================

    with col2:

        if st.button(
            "🗑",
            key=f"delete_{id_}"
        ):

            delete_history(id_)

            st.success("Deleted successfully")

            st.rerun()

    st.divider()


# ==================================================
# TAB 2
# ==================================================

with tab2:

    history = get_history()

    render_dashboard(history)


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
© 2025 Akash Kumar Rajak. AI Fact Verification & Intelligence Platform. All Rights Reserved.
</div>
""", unsafe_allow_html=True)

