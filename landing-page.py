import streamlit as st

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="MemoGenie | The Enterprise Knowledge Engine",
    page_icon="🧞",
    layout="wide",
)

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
    <style>
    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Orbitron:wght@700;900&family=Playfair+Display:wght@700&display=swap');

    html, body, [class*="css"] {
        background: #000;
        color: #fff;
        font-family: 'Inter', sans-serif;
    }

    /* Headlines use Orbitron */
    h1, h2 {
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Sub-headlines use Playfair for contrast */
    h3 {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
    }

    /* Glow Animations */
    .glow {
        color: #fff;
        text-shadow: 0 0 12px #0ff, 0 0 24px #0ff, 0 0 36px #09f;
    }

    /* CTA button */
    .cta-button {
        display:inline-block;
        background: linear-gradient(90deg, #0ff, #09f);
        color: black;
        padding: 1rem 2.5rem;
        font-weight: 700;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 15px rgba(0,255,255,0.4);
    }
    .cta-button:hover {
        transform: scale(1.07) translateY(-3px);
        box-shadow: 0 0 25px rgba(0,255,255,0.7);
    }

    /* Flip Cards */
    .flip-card {
      background-color: transparent;
      width: 100%;
      height: 300px;
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
      padding: 24px;
      background: #111;
    }
    .flip-card-back {
      transform: rotateY(180deg);
      background: #181818;
    }

    /* Section headers */
    .section h2 {
        font-size: 2.8rem;
        font-weight: 900;
        margin-bottom: 15px;
    }
    .section p {
        color: #a1a1a1;
        max-width: 700px;
        margin: auto;
        font-size: 1.15rem;
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

# -------------------------------
# HERO
# -------------------------------
st.markdown("<h1 class='glow' style='text-align:center;font-size:4rem;'>MemoGenie</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#a1a1a1;font-size:1.3rem;'>The Enterprise Knowledge Engine</p>", unsafe_allow_html=True)

st.markdown(f"""
<div style='text-align:center;padding:80px 20px;'>
    <h2 style='font-size:3rem;font-weight:900;'>Unlock Your Institutional Memory.</h2>
    <p style='max-width:750px;margin:20px auto;color:#a1a1a1;'>
        Right now, your company’s knowledge is scattered across Slack, Notion, email threads, and meeting transcripts. 
        MemoGenie doesn’t just retrieve it — it organizes, synthesizes, and evolves it into the <b>single most valuable asset you own</b>.
    </p>
    <a href='{form_url}' target='_blank' class='cta-button'>Request Enterprise Demo →</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# FEATURES SECTION 1
# -------------------------------
st.markdown("""
<div class='section' style='text-align:center;'>
    <h2>The Hidden Costs of Lost Knowledge</h2>
    <p>Every day, your org bleeds money and momentum. Employees reinvent the wheel, key insights disappear into Slack black holes, and institutional memory evaporates with every exit interview.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <h3>⏳ Slow Onboarding</h3>
              <p>Months wasted ramping new hires.</p>
            </div>
            <div class="flip-card-back">
              <p>Instead of spending 90 days chasing docs and context, new teammates should be producing in week one.</p>
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
              <p>Projects constantly re-litigated.</p>
            </div>
            <div class="flip-card-back">
              <p>Without a living knowledge base, history repeats itself. Decisions get revisited, decks get rebuilt, and execution stalls.</p>
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
              <p>Expertise walks out the door.</p>
            </div>
            <div class="flip-card-back">
              <p>When an employee leaves, their context, insights, and mistakes go with them — weakening your org’s long-term resilience.</p>
            </div>
          </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# FEATURES SECTION 2
# -------------------------------
st.markdown("""
<div class='section' style='text-align:center;'>
    <h2>The Intelligence Layer For Your Business</h2>
    <p>MemoGenie doesn’t just <i>store</i> data. It understands it. A searchable, AI-powered knowledge graph surfaces insights before you even think to ask.</p>
</div>
""", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    st.success("🚀 **Onboard in Days, Not Months**\n\nNew hires can query MemoGenie like a senior teammate: *“What’s the history of Project X?”* and get a full strategic brief instantly.")
with col5:
    st.success("💡 **Surface Insights, Not Just Docs**\n\nAsk *“What did we learn from Q3 churn?”* and get synthesized answers — not an avalanche of links.")
with col6:
    st.success("🔒 **Enterprise-Grade Security**\n\nYour data never leaves your control. Zero data leakage, zero model training on your IP.")

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# CALL TO ACTION AGAIN
# -------------------------------
st.markdown(f"""
<div style='text-align:center;margin:60px;'>
    <a href='{form_url}' target='_blank' class='cta-button'>Book a Private Demo →</a>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("<p style='text-align:center;color:#666;padding:30px;'>&copy; 2025 MemoGenie. The Single Source of Truth for Enterprise.</p>", unsafe_allow_html=True)
