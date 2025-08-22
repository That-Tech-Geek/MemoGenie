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
            line-height: 1.6;
        }
        h1, h2, h3 {
            font-weight: 700;
        }
        .hero-text {
            font-size: 3rem;
            font-weight: 800;
            color: white;
            text-align: center;
            margin-bottom: 1rem;
        }
        .hero-sub {
            font-size: 1.35rem;
            color: #9CA3AF;
            text-align: center;
            max-width: 750px;
            margin: 1rem auto 2rem auto;
            display: block;
        }
        .btn {
            display: inline-block;
            background-color: #7C3AED;
            color: white !important;
            font-weight: bold;
            padding: 0.9rem 2.2rem;
            border-radius: 9999px;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .btn:hover {
            background-color: #6D28D9;
            transform: translateY(-2px);
        }
        .btn-light {
            background-color: white;
            color: #7C3AED !important;
        }
        .card {
            background-color: #1F2937;
            padding: 2rem;
            border-radius: 1rem;
            border: 1px solid #374151;
            color: #D1D5DB;
            transition: all 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            text-align: center;
        }
        .card:hover {
            transform: translateY(-4px);
            border-color: #7C3AED;
        }
        .card h3 {
            color: white;
            margin-bottom: 0.75rem;
        }
        /* Fix for equal-height cards inside Streamlit columns */
        .card-container {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
        }
        .card-container > div {
            flex: 1;
            min-width: 250px;
            max-width: 350px;
        }
        .cta-section {
            background-color: #7C3AED;
            padding: 3rem 2rem;
            border-radius: 1.5rem;
            text-align: center;
            margin-top: 3rem;
        }
        .cta-section h2 {
            color: white;
            margin-bottom: 1rem;
        }
        .cta-section p {
            color: #E9D5FF;
            margin-bottom: 2rem;
        }
        .footer {
            color: #9CA3AF;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            border-top: 1px solid #2D2D2D;
        }
    </style>
""", unsafe_allow_html=True)


# --- Navbar ---
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<h2 style='color:white; margin:0;'>📑 MemoGenie</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(
        """<p style='text-align:right; margin:0;'>
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

st.markdown("""
<div class="card-container">
    <div>
        <div class="card">
            <h3>Automated Memo Generation</h3>
            <p>Turn pitch decks and financials into structured, investor-ready memos — no manual work required.</p>
        </div>
    </div>
    <div>
        <div class="card">
            <h3>OCR & Metadata Parsing</h3>
            <p>Extract key insights even from locked or image-based PDFs with built-in OCR and parsing.</p>
        </div>
    </div>
    <div>
        <div class="card">
            <h3>Proprietary Valuation Model</h3>
            <p>See data-backed valuations instantly, using comparative multiples integrated into every memo.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# --- Deep Research Section ---
st.write("## 🔍 VC Deep Research – Beyond the Memo")

st.markdown("""
    <div class="card" style="background: linear-gradient(135deg, #1F2937, #111827); padding:2.5rem; text-align:center; border: 1px solid #374151; max-width: 1000px; margin:auto;">
        <h2 style="color:white; margin-bottom:1rem;">From Memos to Market Mastery</h2>
        <p style="color:#D1D5DB; font-size:1.15rem; max-width:800px; margin:auto;">
            MemoGenie Deep Research isn’t just about writing memos — it’s about giving you <b>Gemini-level intelligence</b>.
            Go beyond pitch decks and surface numbers. Uncover hidden competitors, stress-test financial models,
            track market shifts, and map out risks before anyone else sees them.
        </p>
        <div class="card-container" style="margin-top:2rem;">
            <div>
                <div class="card">
                    <h3>📊 Smarter Valuations</h3>
                    <p>Test thousands of financial scenarios in hours, not weeks.</p>
                </div>
            </div>
            <div>
                <div class="card">
                    <h3>🕵️ Competitive Edge</h3>
                    <p>Spot hidden rivals, funding moves, and hiring shifts before the market does.</p>
                </div>
            </div>
            <div>
                <div class="card">
                    <h3>⚖️ Risk Radar</h3>
                    <p>From regulatory red flags to market timing risks — see them quantified and mapped.</p>
                </div>
            </div>
        </div>
        <p style="margin-top:2rem; color:#E9D5FF; font-size:1.05rem;">
            What used to take analysts <b>weeks</b> is now done in <b>hours</b> — with sharper insights and zero bias.
        </p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" 
           class="btn" target="_blank" style="margin-top:1.5rem;">Unlock Deep Research</a>
    </div>
""", unsafe_allow_html=True)


# --- CTA Section ---
st.markdown("""
    <div class="cta-section">
        <h2>Ready to 10x Your Due Diligence?</h2>
        <p>Stop wasting time on manual work. Get the intel you need, faster than ever.</p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn btn-light" target="_blank">Get Access</a>
    </div>
""", unsafe_allow_html=True)


# --- Footer ---
st.markdown("<div class='footer'>&copy; 2025 MemoGenie. All rights reserved.</div>", unsafe_allow_html=True)
