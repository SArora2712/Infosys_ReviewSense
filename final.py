# ============================
# ReviewSense – FINAL PRODUCTION VERSION
# ============================

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from wordcloud import WordCloud
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ReviewSense AI Platform",
    page_icon="📊",
    layout="wide"
)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Toggle in sidebar
st.sidebar.toggle("🌙 Dark Mode", key="dark_mode")
# ---------------- USERS (MULTI USER) ----------------
users = {
    "admin": "admin123",
    "jasleen": "ml2026",
    "user1": "pass123"
}

# ---------------- GLOBAL CSS ----------------
if st.session_state.dark_mode:

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: #e2e8f0;
    }

    .card {
        background: #1e293b;
        color: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }

    .gradient-header {
        color: white;
    }

    .stButton>button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg, #eef2f3, #dfe9f3);
    }

    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    </style>
    """, unsafe_allow_html=True)
# =====================================================
# 🏠 HOME
# =====================================================
if st.session_state.page == "home":
    st.markdown("""
<style>

/* General */
body {
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.main-title {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    color: #1f3c88;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6c757d;
    margin-bottom: 2rem;
}

/* Cards */
.card {
    background: white;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    transition: 0.3s;
    text-align:center;
}
.card:hover {
    transform: translateY(-5px);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    color: white;
    border-radius: 12px;
    padding: 0.6rem 1.5rem;
    border: none;
    font-weight: 600;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
}

/* Login Box */
.login-box {
    max-width: 400px;
    margin: auto;
    margin-top: 120px;
    padding: 2rem;
    border-radius: 20px;
    background: white;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.1);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #f7f9fc;
}

</style>
""", unsafe_allow_html=True)



# =====================================================
# 🏠 HOMEPAGE (UPDATED PROFESSIONAL VERSION)
# =====================================================
if st.session_state.page == "home":

    # HERO SECTION
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1f3c88, #4facfe);
        padding: 70px 20px;
        border-radius: 20px;
        color: white;
        text-align: center;
    ">
        <h1 style="font-size:3.8rem;">📊 ReviewSense AI Platform</h1>
        <p style="font-size:1.4rem;">
        Transform Customer Feedback into Actionable Intelligence
        </p>
        <p style="max-width:750px; margin:auto; font-size:1.05rem;">
        An end-to-end AI-powered system that analyzes customer reviews,
        extracts insights, detects sentiment patterns, and enables
        data-driven decision making through interactive dashboards.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ================= PROBLEM =================
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <h2>🚧 The Problem</h2>
        <ul>
        <li>Massive volumes of unstructured customer feedback</li>
        <li>Manual analysis is slow and inefficient</li>
        <li>Difficult to identify trends, complaints, and opportunities</li>
        <li>Lack of real-time decision support</li>
        </ul>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1556740749-887f6717d7e4",
            use_container_width=True
        )

    st.write("")

    # ================= SOLUTION =================
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <h2>💡 Our Solution</h2>
        <ul>
        <li>AI-powered sentiment analysis (real-time + batch)</li>
        <li>Keyword extraction & complaint detection</li>
        <li>Interactive dashboards for data exploration</li>
        <li>Dataset intelligence & automated insights</li>
        <li>Multi-user system for scalable usage</li>
        </ul>
        """, unsafe_allow_html=True)

    st.write("")

    # ================= KEY FEATURES =================
    st.markdown("## ✨ Key Features")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="
            padding:20px;
            border-radius:15px;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            color:white;
            text-align:center;
        ">
        💬 <b>Real-Time Feedback Analysis</b><br><br>
        Analyze individual feedback instantly with sentiment & insights
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            padding:20px;
            border-radius:15px;
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            color:white;
            text-align:center;
        ">
        📂 <b>Dataset Intelligence</b><br><br>
        Upload datasets and perform automated exploratory analysis
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            padding:20px;
            border-radius:15px;
            background: linear-gradient(135deg, #fa709a, #fee140);
            color:white;
            text-align:center;
        ">
        📊 <b>Interactive Dashboard</b><br><br>
        Visualize trends, sentiment distribution, and product insights
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="
            padding:20px;
            border-radius:15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color:white;
            text-align:center;
        ">
        🤖 <b>AI Insight Engine</b><br><br>
        Generate business insights and smart recommendations
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ================= OBJECTIVES =================
    st.markdown("""
    <div style="
        background:white;
        padding:30px;
        border-radius:15px;
        box-shadow:0 8px 25px rgba(0,0,0,0.08);
    ">
    <h2>🎯 Objectives</h2>
    <ul>
    <li>Automate analysis of large-scale customer feedback</li>
    <li>Provide real-time sentiment and emotion detection</li>
    <li>Enable data-driven business decisions</li>
    <li>Identify customer pain points and improvement areas</li>
    <li>Build an intelligent, scalable feedback analysis platform</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ================= CTA =================
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

    if st.button("🚀 Get Started"):
        st.session_state.page = "login"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
   

# =====================================================
# 🔐 LOGIN
# =====================================================

elif st.session_state.page == "login":

    st.markdown("""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        height:80vh;
    ">
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        st.markdown("""
        <div style="
            padding:30px;
            border-radius:15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            box-shadow:0 15px 40px rgba(0,0,0,0.2);
        ">
        <h3 style="color:white; text-align:center;">🔐 Login</h3>
        """, unsafe_allow_html=True)

        with st.form("login"):
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            login_btn = st.form_submit_button("Login")

        st.markdown("</div>", unsafe_allow_html=True)

        if login_btn:
            if user in users and users[user] == pwd:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.markdown("</div>", unsafe_allow_html=True)
# =====================================================
# 📊 MAIN DASHBOARD AREA
# =====================================================
elif st.session_state.page == "dashboard":

    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.session_state.page = "login"
        st.rerun()

    # ---------------- SIDEBAR NAV ----------------
    st.sidebar.title("Navigation")

    menu = st.sidebar.radio(
        "Go to",
        ["📊 Dashboard", "💬 Feedback Analyzer", "📂 Dataset Analyzer"]
    )

    st.sidebar.markdown(f"👤 Logged in as: **{st.session_state.user}**")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

    # =====================================================
    # 📊 ORIGINAL DASHBOARD (UNCHANGED)
    # =====================================================
    if menu == "📊 Dashboard":
        # ============================
# ReviewSense – Milestone 4 (Enhanced & Fixed Final)
# Interactive Customer Feedback Dashboard
        # ============================
       

        # Page configuration
        st.set_page_config(
            page_title="ReviewSense Dashboard",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded",
        )

        # Custom CSS for better look
        st.markdown(
            """
                <style>
                .main-header {
                font-size: 3rem;
                color: #1f77b4;
                text-align: center;
                margin-bottom: 2rem;
                }
                .metric-card {
                background-color: #f0f2f6;
                padding: 1.5rem;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                </style>
        """,
            unsafe_allow_html=True,
        )

        # ── Load Data
        @st.cache_data
        def load_data():
            df = pd.read_csv("Milestone2_Seniment_Results.csv")
            

            df["sentiment"] = df["sentiment"].str.lower().str.strip()
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            
            return df


        @st.cache_data
        def load_keywords():
            """Load keywords CSV, supporting both plain and marked formats."""
            
            try:
                keywords_df = pd.read_csv("Milestone3_Keyword_Insights.csv")
                if "keyword" in keywords_df.columns and "frequency" in keywords_df.columns:
                    return keywords_df
            except Exception:
                pass

            
            try:
                with open("Milestone3_Keyword_Insights.csv", "r", encoding="utf-8") as f:
                    content = f.read()
                if "=== KEYWORD FREQUENCY ===" in content:
                    keyword_part = content.split("=== KEYWORD FREQUENCY===")[1].split(
                        "=== PRODUCT SENTIMENT SUMMARY ==="
                    )[0]
                    keyword_part = keyword_part.strip().splitlines()
                    if len(keyword_part) > 1:
                        keywords_df = pd.read_csv(pd.StringIO("\n".join(keyword_part)))
                        return keywords_df
            except Exception:
                pass

            return pd.DataFrame()


        df = load_data()
        keywords_df = load_keywords()

        # ── Sidebar Filters
        st.sidebar.header("🔍 Filters")
        # Sentiment
        sentiment_options = ["positive", "negative", "neutral"]
        sentiment_display = {"positive": "Positive", "negative": "Negative", "neutral": "Neutral"}
        sentiment_filter_display = st.sidebar.multiselect(
            "Select Sentiment",
            options=[sentiment_display[s] for s in sentiment_options],
            default=[sentiment_display[s] for s in sentiment_options],
        )
        sentiment_filter = [k for k, v in sentiment_display.items() if v in sentiment_filter_display]
        # Product
        product_filter = st.sidebar.multiselect(
            "Select Product",
            options=sorted(df["product"].unique()),
            default=sorted(df["product"].unique()),
        )
        # Date range
        st.sidebar.subheader("📅 Date Range")
        # Safe defaults
        if pd.notna(df["date"].min()):
            default_start = df["date"].min().date()
        else:
            default_start = datetime(2025, 1, 1).date()
        if pd.notna(df["date"].max()):
            default_end = df["date"].max().date()
        else:
            default_end = datetime(2025, 12, 31).date()
        col1, col2 = st.sidebar.columns(2)
        start_date = col1.date_input("Start Date", value=default_start)
        end_date = col2.date_input("End Date", value=default_end)

        # ── Apply Filters
        filtered_df = df[
            (df["sentiment"].isin(sentiment_filter))
            & (df["product"].isin(product_filter))
            & (df["date"] >= pd.to_datetime(start_date))
            & (df["date"] <= pd.to_datetime(end_date))
        ].copy()  # .copy() avoids SettingWithCopyWarning later

        # ── Main Dashboard
        st.markdown(
            '<h1 class="main-header">📊 ReviewSense – Customer Feedback Dashboard</h1>',
            unsafe_allow_html=True,
        )

        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        total_reviews = len(filtered_df)
        pos_count = len(filtered_df[filtered_df["sentiment"] == "positive"])
        neg_count = len(filtered_df[filtered_df["sentiment"] == "negative"])
        neu_count = len(filtered_df[filtered_df["sentiment"] == "neutral"])
        pos_pct = (pos_count / total_reviews * 100) if total_reviews > 0 else 0
        neg_pct = (neg_count / total_reviews * 100) if total_reviews > 0 else 0
        neu_pct = (neu_count / total_reviews * 100) if total_reviews > 0 else 0
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Total Reviews", total_reviews)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Positive", f"{pos_pct:.1f}%", delta=f"{pos_count} reviews")
            st.markdown("</div>", unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Negative", f"{neg_pct:.1f}%", delta=f"{neg_count} reviews")
            st.markdown("</div>", unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Neutral", f"{neu_pct:.1f}%", delta=f"{neu_count} reviews")
            st.markdown("</div>", unsafe_allow_html=True)

        # ── Sentiment Distribution ──────────────────────────────────────────────────
        st.subheader("😊 Sentiment Distribution")
        if not filtered_df.empty:
            fig1, ax1 = plt.subplots(figsize=(8, 5))
            counts = filtered_df["sentiment"].value_counts()
            colors = {"positive": "#4CAF50", "negative": "#F44336", "neutral": "#9E9E9E"}
            bars = ax1.bar(
                [sentiment_display.get(s, s.title()) for s in counts.index],
                counts.values,
                color=[colors.get(s, "gray") for s in counts.index]
            )
            ax1.set_xlabel("Sentiment")
            ax1.set_ylabel("Number of Reviews")
            ax1.set_title("Overall Sentiment Breakdown")
            for bar in bars:
                yval = bar.get_height()
                ax1.text(
                    bar.get_x() + bar.get_width() / 2,
                    yval + 10,
                    int(yval),
                    ha="center",
                    va="bottom",
                )
            st.pyplot(fig1)
        else:
            st.info("No data matches the selected filters.")

        # ── Product Sentiment ───────────────────────────────────────────────────────
        st.subheader("📱 Product-wise Sentiment")
        if not filtered_df.empty:
            product_sent = (
                filtered_df.groupby("product")["sentiment"].value_counts().unstack(fill_value=0)
            )
            # Ensure all sentiment columns exist
            for col in sentiment_options:
                if col not in product_sent.columns:
                    product_sent[col] = 0
            product_sent["Total"] = product_sent.sum(axis=1)
            product_sent["Positive %"] = (
                product_sent.get("positive", 0) / product_sent["Total"] * 100
            ).round(1)
            product_sent = product_sent.sort_values("Positive %", ascending=False)
            # Rename columns for display
            display_cols = [sentiment_display[s] for s in sentiment_options]
            product_sent_disp = product_sent.copy()
            product_sent_disp.rename(columns=sentiment_display, inplace=True)
            st.dataframe(product_sent_disp[display_cols + ["Total", "Positive %"]].style.format(precision=1), use_container_width=True)
            # Heatmap
            fig_hm, ax_hm = plt.subplots(figsize=(10, 6))
            sns.heatmap(
                product_sent[sentiment_options],
                annot=True,
                fmt="d",
                cmap="RdYlGn",
                ax=ax_hm,
            )
            ax_hm.set_title("Product Sentiment Heatmap")
            st.pyplot(fig_hm)

            # ── Trend Over Time ─────────────────────────────────────────────────────────
            st.subheader("📈 Sentiment Trends Over Time")
        if not filtered_df.empty:
            filtered_df["month"] = filtered_df["date"].dt.to_period("M")
            trend = filtered_df.groupby(["month", "sentiment"]).size().unstack(fill_value=0)
            fig_trend, ax_trend = plt.subplots(figsize=(12, 6))
            for col in trend.columns:
                ax_trend.plot(
                    trend.index.astype(str), trend[col], marker="o", linewidth=2, label=col
                )
            ax_trend.set_xlabel("Month")
            ax_trend.set_ylabel("Number of Reviews")
            ax_trend.set_title("Monthly Sentiment Trend")
            ax_trend.legend()
            ax_trend.tick_params(axis="x", rotation=45)
            plt.tight_layout()
            st.pyplot(fig_trend)
        else:
            st.info("No date-based data available after filtering.")

        # ── Keywords ────────────────────────────────────────────────────────────────
        st.subheader("🔑 Top Keywords & Word Cloud")
        if not keywords_df.empty:
            top10 = keywords_df.head(15)
            colA, colB = st.columns([3, 2])
            with colA:
                fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
                ax_bar.barh(top10["keyword"], top10["frequency"], color="skyblue")
                ax_bar.set_xlabel("Frequency")
                ax_bar.set_title("Top Keywords")
                ax_bar.invert_yaxis()
                st.pyplot(fig_bar)
            with colB:
                if len(top10) > 0:
                    word_freq = dict(zip(keywords_df["keyword"], keywords_df["frequency"]))
                    wc = WordCloud(
                        width=400, height=400, background_color="white", min_font_size=10
                    ).generate_from_frequencies(word_freq)
                    fig_wc, ax_wc = plt.subplots(figsize=(6, 6))
                    ax_wc.imshow(wc, interpolation="bilinear")
                    ax_wc.axis("off")
                    st.pyplot(fig_wc)

        # ── Confidence Score ────────────────────────────────────────────────────────
        st.subheader("📊 Confidence Score Distribution")
        if not filtered_df.empty:
            fig_hist, ax_hist = plt.subplots(figsize=(10, 5))
            ax_hist.hist(
                filtered_df["confidence_score"],
                bins=25,
                color="cornflowerblue",
                edgecolor="black",
                alpha=0.7,
            )
            ax_hist.set_xlabel("Confidence Score (–1 to +1)")
            ax_hist.set_ylabel("Count")
            ax_hist.set_title("Sentiment Confidence Distribution")
            st.pyplot(fig_hist)

        # ── Data & Download ─────────────────────────────────────────────────────────
        with st.expander("📋 Preview Filtered Data (first 15 rows)"):
            st.dataframe(filtered_df.head(15), use_container_width=True)
        st.subheader("💾 Export Options")
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button(
                "⬇️ Download Filtered Reviews",
                filtered_df.to_csv(index=False).encode("utf-8"),
                "ReviewSense_Filtered_Reviews.csv",
                "text/csv",
                use_container_width=True,
            )
        with col_dl2:
            if not keywords_df.empty:
                st.download_button(
                    "⬇️ Download Keyword List",
                    keywords_df.to_csv(index=False).encode("utf-8"),
                    "ReviewSense_Keywords.csv",
                    "text/csv",
                    use_container_width=True,
                )
        st.success("✅ Dashboard ready! Use the sidebar to explore different views.")


    # =====================================================
    # 💬 FEEDBACK ANALYZER
    # =====================================================
    elif menu == "💬 Feedback Analyzer":

        
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding:25px;
            border-radius:15px;
            color:white;
            text-align:center;
        ">
        <h2>💬 AI Feedback Intelligence</h2>
        <p>Understand what your customer is really saying</p>
        </div>
        """, unsafe_allow_html=True)

        text = st.text_area("✍️ Enter customer feedback", height=150)

        if st.button("🚀 Analyze Feedback"):

            if text.strip() != "":
                from textblob import TextBlob
                import re

                blob = TextBlob(text)
                polarity = blob.sentiment.polarity

                sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

                # =========================
                # 🎯 SENTIMENT GAUGE STYLE
                # =========================
                st.subheader("📊 Sentiment Impact")

                progress = (polarity + 1) / 2  # scale -1 to 1 → 0 to 1

                st.progress(progress)

                st.markdown(f"""
                <div style="text-align:center; font-size:18px;">
                <b>{sentiment}</b> (Score: {polarity:.2f})
                </div>
                """, unsafe_allow_html=True)

                # =========================
                # 🎨 GRADIENT BAR VISUAL
                # =========================
                st.subheader("🎨 Sentiment Strength")

                fig, ax = plt.subplots(figsize=(6,1))

                gradient = np.linspace(0, 1, 256).reshape(1, -1)
                ax.imshow(gradient, aspect='auto', cmap='coolwarm')
                ax.set_axis_off()

                # marker position
                marker = int((polarity + 1) / 2 * 255)
                ax.plot(marker, 0, 'ko')

                st.pyplot(fig)

                # =========================
                # 🔑 WORD IMPORTANCE
                # =========================
                st.subheader("🔑 Key Drivers of Feedback")

                words = re.findall(r'\b\w+\b', text.lower())
                freq = pd.Series(words).value_counts().head(8)

                fig2, ax2 = plt.subplots()
                ax2.barh(freq.index, freq.values)
                ax2.invert_yaxis()
                st.pyplot(fig2)

                # =========================
                # ☁️ WORD CLOUD
                # =========================
                st.subheader("☁️ Feedback Focus Areas")

                wc = WordCloud(width=400, height=300, background_color="white").generate(text)

                fig3, ax3 = plt.subplots()
                ax3.imshow(wc)
                ax3.axis("off")
                st.pyplot(fig3)

                # =========================
                # 💡 AI INSIGHT
                # =========================
                st.subheader("💡 Insight Summary")

                if polarity > 0.4:
                    st.success("Strong positive feedback — user is highly satisfied.")
                elif polarity > 0:
                    st.info("Mildly positive — improvement opportunities exist.")
                elif polarity < -0.4:
                    st.error("Strong negative — urgent issue detected.")
                else:
                    st.warning("Neutral/mixed feedback — analyze deeper.")

            else:
                st.warning("Enter feedback")
    # =====================================================
    # 📂 DATASET ANALYZER + Q&A
    # =====================================================
    elif menu == "📂 Dataset Analyzer":

        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            padding:25px;
            border-radius:15px;
            color:white;
            text-align:center;
        ">
        <h2>📂 Dataset Intelligence Engine</h2>
        <p>Visualize and understand your data instantly</p>
        </div>
        """, unsafe_allow_html=True)

        file = st.file_uploader("Upload CSV Dataset", type=["csv"])

        if file:
            df = pd.read_csv(file)

            # =========================
            # 📊 DATA OVERVIEW CARDS
            # =========================
            col1, col2, col3 = st.columns(3)

            col1.metric("Rows", df.shape[0])
            col2.metric("Columns", df.shape[1])
            col3.metric("Missing", df.isnull().sum().sum())

            # =========================
            # 📈 NUMERIC DISTRIBUTIONS
            # =========================
            numeric_cols = df.select_dtypes(include=np.number).columns

            if len(numeric_cols) > 0:

                st.subheader("📊 Data Distribution")

                selected_col = st.selectbox("Choose column", numeric_cols)

                fig, ax = plt.subplots()
                sns.histplot(df[selected_col], kde=True, ax=ax)
                st.pyplot(fig)

            # =========================
            # 🔥 CORRELATION HEATMAP
            # =========================
            if len(numeric_cols) > 1:

                st.subheader("🔥 Feature Relationships")

                fig2, ax2 = plt.subplots()
                sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax2)
                st.pyplot(fig2)

            # =========================
            # 📊 CATEGORY ANALYSIS
            # =========================
            cat_cols = df.select_dtypes(include="object").columns

            if len(cat_cols) > 0:

                st.subheader("📊 Category Insights")

                selected_cat = st.selectbox("Choose category column", cat_cols)

                counts = df[selected_cat].value_counts().head(10)

                st.bar_chart(counts)

            # =========================
            # 💬 SENTIMENT IF EXISTS
            # =========================
            if "review" in df.columns:

                from textblob import TextBlob

                df["sentiment"] = df["review"].apply(
                    lambda x: TextBlob(str(x)).sentiment.polarity
                )

                st.subheader("😊 Sentiment Landscape")

                fig3, ax3 = plt.subplots()
                sns.histplot(df["sentiment"], bins=20, kde=True, ax=ax3)
                st.pyplot(fig3)

                # trend
                st.subheader("📈 Sentiment Spread")

                st.line_chart(df["sentiment"])
