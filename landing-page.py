import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="MemoGenie - Automate Investment Memos",
    page_icon="📑",
    layout="wide",
)

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #121212;
            color: #E0E0E0;
        }
        .hero-text {
            font-size: 3rem;
            font-weight: 800;
            color: white;
            text-align: center;
        }
        .hero-sub {
            font-size: 1.25rem;
            color: #9CA3AF;
            text-align: center;
            max-width: 700px;
            margin: auto;
        }
        .btn {
            background-color: #7C3AED;
            color: white;
            font-weight: bold;
            padding: 0.8rem 2rem;
            border-radius: 9999px;
            text-decoration: none;
        }
        .btn:hover {
            background-color: #6D28D9;
        }
        .card {
            background-color: #1F2937;
            padding: 2rem;
            border-radius: 1rem;
            border: 1px solid #374151;
            color: #D1D5DB;
        }
        .card h3 {
            color: white;
            margin-bottom: 0.5rem;
        }
        .footer {
            color: #9CA3AF;
            text-align: center;
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)


# --- Navbar ---
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<h2 style='color:white;'>📑 MemoGenie</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(
        """<p style='text-align:right;'>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn" target="_blank">Get Started</a>
        </p>""", unsafe_allow_html=True
    )

st.write("---")


# --- Hero Section ---
st.markdown("<div class='hero-text'>Automate Due Diligence,<br> Accelerate Decisions.</div>", unsafe_allow_html=True)
st.markdown("<p class='hero-sub'>MemoGenie is your AI-powered co-founder, turning raw startup data into actionable, VC-grade investment memos in hours, not weeks.</p>", unsafe_allow_html=True)
st.markdown(
    """<p style='text-align:center; margin-top:2rem;'>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn" target="_blank">Start Building Memos</a>
    </p>""", unsafe_allow_html=True
)


# --- Features Section ---
st.write("## 🚀 The Engine Behind the Decisions")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <h3>Automated Memo Generation</h3>
            <p>Convert unstructured data from pitch decks and financials into a structured, comprehensive investment memo.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h3>OCR & Metadata Parsing</h3>
            <p>Seamlessly process non-downloadable decks and PDFs, extracting key insights with proprietary OCR technology.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <h3>Proprietary Valuation Model</h3>
            <p>Get a data-backed valuation using comparative multiple modeling, integrated directly into the memo.</p>
        </div>
    """, unsafe_allow_html=True)


# --- CTA Section ---
st.write("## ")
st.markdown("""
    <div style="background-color:#7C3AED; padding:2rem; border-radius:1.5rem; text-align:center;">
        <h2 style="color:white;">Ready to 10x Your Due Diligence?</h2>
        <p style="color:#E9D5FF;">Stop wasting time on manual work. Get the intel you need, faster than ever.</p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn" style="background:white; color:#7C3AED;" target="_blank">Get Access</a>
    </div>
""", unsafe_allow_html=True)


# --- Footer ---
st.markdown("<div class='footer'>&copy; 2025 MemoGenie. All rights reserved.</div>", unsafe_allow_html=True)
