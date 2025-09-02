import streamlit as st

# Page config
st.set_page_config(
    page_title="MemoGenie | The Enterprise Knowledge Engine",
    page_icon="🧞",
    layout="wide",
)

# Inject custom CSS + animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background: #000;
        color: #fff;
    }

    /* Glow Animations */
    .glow {
        color: #fff;
        text-shadow: 0 0 10px #fff, 0 0 20px #999, 0 0 30px #666;
    }
    .cta-button {
        display:inline-block;
        background: white;
        color: black;
        padding: 1rem 2rem;
        font-weight: 700;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.3s ease-in-out;
    }
    .cta-button:hover {
        background: #e5e5e5;
        transform: scale(1.05) translateY(-3px);
    }

    /* Flip Card Container */
    .flip-card {
      background-color: transparent;
      width: 100%;
      height: 260px;
      perspective: 1000px;
    }
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.8s;
      transform-style: preserve-3d;
    }
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }
    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      border: 1px solid #2a2a2a;
      border-radius: 12px;
      padding: 20px;
      background: #181818;
    }
    .flip-card-back {
      transform: rotateY(180deg);
      background: #111;
    }

    /* Section headers */
    .section h2 {
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 10px;
    }
    .section p {
        color: #a1a1a1;
        max-width: 600px;
        margin: auto;
    }

    hr {
        border: none;
        border-top: 1px solid #2a2a2a;
        margin: 3rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Google Form link
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog"

# HEADER
st.markdown("<h1 class='glow' style='text-align:center;font-size:4rem;'>MemoGenie</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#a1a1a1;'>The Enterprise Knowledge Engine</p>", unsafe_allow_html=True)

# HERO
st.markdown(f"""
<div style='text-align:center;padding:80px 20px;'>
    <h1 style='font-size:3rem;font-weight:900;'>Unlock Your Institutional Memory.</h1>
    <p style='max-width:650px;margin:20px auto;color:#a1a1a1;'>
        Your company’s most valuable asset is its knowledge. MemoGenie transforms scattered Slack, Notion, and meeting data into a single source of truth.
    </p>
    <a href='{form_url}' target='_blank' class='cta-button'>Request Enterprise Demo →</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# FEATURE SECTIONS with Flip Cards
st.markdown("""
<div class='section' style='text-align:center;'>
    <h2>The High Cost of Lost Knowledge</h2>
    <p>Every day, your team wastes hours searching for info, duplicating work, and re-learning what’s already known.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <h3>⏳ Slow Onboarding</h3>
              <p>New hires take months to ramp.</p>
            </div>
            <div class="flip-card-back">
              <p>They struggle piecing together endless docs and repetitive Q&A.</p>
            </div>
          </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <h3>🔄 Redundant Work</h3>
              <p>Projects get restarted.</p>
            </div>
            <div class="flip-card-back">
              <p>Past work is buried, costing you time and money.</p>
            </div>
          </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <h3>🚪 Knowledge Drain</h3>
              <p>Employees leave, knowledge leaves.</p>
            </div>
            <div class="flip-card-back">
              <p>Critical expertise evaporates, weakening the org.</p>
            </div>
          </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# FUTURISTIC SECTION
st.markdown("""
<div class='section' style='text-align:center;'>
    <h2>The Intelligence Layer for Your Business</h2>
    <p>MemoGenie connects your tools to create a searchable, intelligent knowledge base that works for you.</p>
</div>
""", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    st.info("🚀 **Onboard in Days, Not Months**\n\nAsk MemoGenie for instant project histories.")
with col5:
    st.info("💡 **Surface Insights, Not Just Docs**\n\nSynthesized summaries, not link dumps.")
with col6:
    st.info("🔒 **Enterprise-Grade Security**\n\nYour data stays yours. Period.")

st.markdown("<hr>", unsafe_allow_html=True)

# DEMO BUTTON AGAIN
st.markdown(f"""
<div style='text-align:center;margin:40px;'>
    <a href='{form_url}' target='_blank' class='cta-button'>Request a Demo →</a>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("<p style='text-align:center;color:#666;padding:30px;'>&copy; 2025 MemoGenie. The Single Source of Truth for Enterprise.</p>", unsafe_allow_html=True)
