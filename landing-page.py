import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="MemoGenie - Automate Investment Memos",
    page_icon="📑",
    layout="wide",
)

# --- Custom CSS for Black and Gold Theme ---
st.markdown("""
    <style>
        /* Define custom variables for a consistent theme */
        :root {
            --gold: #D4AF37;
            --dark-gold: #B8A04E;
            --bg-black: #0A0A0A;
            --card-black: #1A1A1A;
            --text-gray: #E5E7EB;
        }

        /* Basic body styling */
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-black);
            color: var(--text-gray);
            line-height: 1.6;
        }

        /* Streamlit's main app container */
        .stApp {
            background-color: var(--bg-black);
            color: var(--text-gray);
        }
        
        /* Headers with a gold gradient effect */
        .hero-title {
            font-weight: 800;
            font-size: 3rem;
            background: linear-gradient(90deg, #FFD700, #B8A04E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }

        /* Sub-header text styling */
        .hero-sub {
            font-size: 1.35rem;
            color: #9CA3AF;
            text-align: center;
            max-width: 750px;
            margin: 1rem auto 2rem auto;
            display: block;
        }

        /* Gold-themed button styles */
        .btn-gold {
            display: inline-block;
            background-color: var(--gold);
            color: black !important;
            font-weight: bold;
            padding: 0.9rem 2.2rem;
            border-radius: 9999px;
            text-decoration: none;
            transition: all 0.3s ease;
            border: 2px solid transparent; /* Required for hover effect */
        }
        .btn-gold:hover {
            background-color: transparent;
            color: var(--gold) !important;
            border-color: var(--gold);
            transform: translateY(-2px);
            box-shadow: 0 0 15px var(--dark-gold), 0 0 5px var(--dark-gold);
        }

        /* Cards for feature sections */
        .card {
            background-color: var(--card-black);
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
            border-color: var(--gold);
        }
        .card h3 {
            color: var(--gold);
            margin-bottom: 0.75rem;
        }

        /* Flexbox for card layout within columns */
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

        /* CTA section styling */
        .cta-section {
            background-color: var(--gold);
            padding: 3rem 2rem;
            border-radius: 1.5rem;
            text-align: center;
            margin-top: 3rem;
        }
        .cta-section h2, .cta-section p {
            color: black;
        }
        .btn-black {
            background-color: black;
            color: white !important;
            font-weight: bold;
            padding: 1rem 2.5rem;
            border-radius: 9999px;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .btn-black:hover {
            background-color: #333;
            transform: translateY(-2px);
        }

        /* Footer styling */
        .footer {
            color: #9CA3AF;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            border-top: 1px solid #2D2D2D;
        }

        /* Style for gold-accented text */
        .text-gold {
            color: var(--gold);
        }
    </style>
""", unsafe_allow_html=True)


# --- Navbar ---
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<h2 class='text-gold' style='margin:0;'>📑 MemoGenie</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(
        """<p style='text-align:right; margin:0;'>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn-gold" target="_blank">Get Started</a>
        </p>""", unsafe_allow_html=True
    )

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


# --- Hero Section ---
st.markdown("<div class='text-center py-16 px-4'>", unsafe_allow_html=True)
st.markdown("<h1 class='hero-title text-4xl sm:text-5xl md:text-6xl tracking-tight mb-4'>Automate Due Diligence,<br class='hidden md:inline'> Accelerate Decisions.</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-sub'>MemoGenie is your AI-powered co-founder, turning raw startup data into actionable, VC-grade investment memos in hours, not weeks.</p>", unsafe_allow_html=True)
st.markdown(
    """<p style='text-align:center; margin-top:2rem;'>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn-gold" target="_blank">Start Building Memos</a>
    </p>""", unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)


# --- Features Section ---
st.markdown("<section class='py-16'>", unsafe_allow_html=True)
st.markdown("<h2 class='text-3xl sm:text-4xl font-bold text-center mb-12 text-gray-50'><span class='text-gold'>🚀</span> The Engine Behind the Decisions</h2>", unsafe_allow_html=True)

# Using columns for the cards
col_1, col_2, col_3 = st.columns(3)
with col_1:
    st.markdown(
        """<div class="card">
            <h3>Automated Memo Generation</h3>
            <p>Turn pitch decks and financials into structured, investor-ready memos — no manual work required.</p>
        </div>""", unsafe_allow_html=True
    )
with col_2:
    st.markdown(
        """<div class="card">
            <h3>OCR & Metadata Parsing</h3>
            <p>Extract key insights even from locked or image-based PDFs with built-in OCR and parsing.</p>
        </div>""", unsafe_allow_html=True
    )
with col_3:
    st.markdown(
        """<div class="card">
            <h3>Proprietary Valuation Model</h3>
            <p>See data-backed valuations instantly, using comparative multiples integrated into every memo.</p>
        </div>""", unsafe_allow_html=True
    )
st.markdown("</section>", unsafe_allow_html=True)


# --- Deep Research Section ---
st.markdown("<section class='py-16'>", unsafe_allow_html=True)
st.markdown("""
    <div class="card" style="background: var(--card-black); padding:2.5rem; text-align:center;">
        <h2 class="text-3xl sm:text-4xl font-bold mb-4 text-gold">VC Deep Research – Beyond the Memo</h2>
        <p class="text-lg text-gray-400 max-w-4xl mx-auto mb-8">
            MemoGenie Deep Research isn’t just about writing memos — it’s about giving you <b>Gemini-level intelligence</b>. Go beyond pitch decks and surface numbers. Uncover hidden competitors, stress-test financial models, track market shifts, and map out risks before anyone else sees them.
        </p>
""", unsafe_allow_html=True)

# Using columns for the inner cards
inner_col_1, inner_col_2, inner_col_3 = st.columns(3)
with inner_col_1:
    st.markdown(
        """<div class="card">
            <h3>📊 Smarter Valuations</h3>
            <p>Test thousands of financial scenarios in hours, not weeks.</p>
        </div>""", unsafe_allow_html=True
    )
with inner_col_2:
    st.markdown(
        """<div class="card">
            <h3>🕵️ Competitive Edge</h3>
            <p>Spot hidden rivals, funding moves, and hiring shifts before the market does.</p>
        </div>""", unsafe_allow_html=True
    )
with inner_col_3:
    st.markdown(
        """<div class="card">
            <h3>⚖️ Risk Radar</h3>
            <p>From regulatory red flags to market timing risks — see them quantified and mapped.</p>
        </div>""", unsafe_allow_html=True
    )
st.markdown("""
        <p class="mt-8 text-gray-500 text-lg">
            What used to take analysts <b>weeks</b> is now done in <b>hours</b> — with sharper insights and zero bias.
        </p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog"
            class="btn-gold mt-6 inline-block"
            target="_blank">Unlock Deep Research</a>
    </div>
</section>
""", unsafe_allow_html=True)


# --- CTA Section ---
st.markdown("<section class='py-16'>", unsafe_allow_html=True)
st.markdown("""
    <div class="cta-section">
        <h2>Ready to 10x Your Due Diligence?</h2>
        <p>Stop wasting time on manual work. Get the intel you need, faster than ever.</p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="btn-black" target="_blank">Get Access</a>
    </div>
""", unsafe_allow_html=True)
st.markdown("</section>", unsafe_allow_html=True)


# --- Footer ---
st.markdown("<div class='footer'>&copy; 2025 MemoGenie. All rights reserved.</div>", unsafe_allow_html=True)
