import streamlit as st
import time

# --- MOCK DATA ---
# Refactored to use triple-quoted f-strings for robust multi-line HTML
DEMO_RESPONSES = {
    "What were the key learnings from the Q4 customer feedback on Project Atlas?": {
        "answer": f"""
            The key learning from Q4 feedback on <strong>Project Atlas</strong> was a strong dichotomy:
            <ul>
                <li>Users loved the new UI, praised for its speed and intuitiveness (praised by <strong>Alice</strong> in the product sync on Nov 12th).</li>
                <li>However, the data export feature was a critical failure point for power users, representing a significant churn risk.</li>
            </ul>
            This export issue was first flagged by <strong>Bob</strong> from Sales after a call with a major client and is linked to the 
            same API limitation that caused delays in the failed <strong>Project Titan</strong> last year.
        """,
        "recommendation": "Prioritize a fix for the export feature and form a task force to evaluate the core API dependency to avoid repeating past mistakes.",
        "sources": ["[Project Atlas - Q4 Feedback.docx]", "[Nov 12 - Product Sync Transcript]", "[Client Call - Bob.mp3]"]
    },
    "Summarize the competitive landscape for our new 'Genie' feature.": {
        "answer": f"""
            The competitive landscape for 'Genie' is dominated by three players:
            <ul>
                <li><strong>Competitor A:</strong> Strong in the enterprise market but their product is known to be slow and bloated.</li>
                <li><strong>Competitor B:</strong> A fast-moving startup that recently raised a Series B. Their feature set is limited but they have strong user love.</li>
                <li><strong>Internal Project 'Phoenix':</strong> A now-defunct internal tool from two years ago that attempted a similar goal. 
                The post-mortem (authored by <strong>Carol</strong>) cited a lack of data integration as the primary reason for failure.</li>
            </ul>
            MemoGenie's advantage is our ability to integrate deeply with existing tools, 
            directly addressing the failure point of our own past attempts.
        """,
        "recommendation": "Focus marketing on the speed and seamless integration of MemoGenie compared to Competitor A, and highlight our broader feature set than Competitor B.",
        "sources": ["[Market Analysis Q3.pptx]", "[Competitor B - Series B Press Release]", "[Project Phoenix Post-Mortem.pdf]"]
    }
}

def main():
    # --- PAGE CONFIGURATION ---
    st.set_page_config(
        page_title="MemoGenie | The Enterprise Knowledge Engine",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- INJECT CUSTOM CSS ---
    st.markdown("""
    <style>
        /* General Styles */
        body {
            color: #ffffff;
            background-color: #000000;
        }
        .stApp {
             background-color: #000000;
        }
        
        /* Remove Streamlit Header/Footer */
        header, footer {
            visibility: hidden;
        }

        /* Text Styles */
        h1, h2 {
            font-weight: 900 !important;
        }
        
        h1 {
            font-size: 4.5rem !important;
            letter-spacing: -2px !important;
            line-height: 1.1 !important;
        }

        h2 {
            font-size: 3rem !important;
            letter-spacing: -1px !important;
        }
        
        /* --- Navigation Bar --- */
        .nav-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 1rem 2rem;
            background-color: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            z-index: 999;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #2a2a2a;
        }
        .nav-logo {
            font-size: 1.8rem;
            font-weight: 900;
            color: #ffffff;
            text-decoration: none;
        }
        .nav-links a {
            color: #a1a1a1;
            text-decoration: none;
            margin-left: 2rem;
            font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #ffffff;
        }
        .nav-cta {
            background-color: #ffffff;
            color: #000000 !important;
            padding: 0.5rem 1rem;
            border-radius: 8px;
        }

        /* --- Main CTA Button --- */
        .stButton>a>button {
            background-color: #ffffff;
            color: #000000;
            border: none;
            padding: 16px 32px;
            font-weight: 700;
            border-radius: 8px;
            transition: all 0.2s ease-in-out;
        }
        .stButton>a>button:hover {
            background-color: #e5e5e5;
            transform: translateY(-2px);
        }
        
        /* Feature & UI Card Styles */
        .card {
            background-color: #181818;
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #2a2a2a;
            height: 100%;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            border-color: #a1a1a1;
        }
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        /* Center Align Content */
        .section-header {
             text-align: center;
             max-width: 700px;
             margin: 0 auto 4rem auto;
        }
        .section-header p {
            color: #a1a1a1;
            font-size: 1.2rem;
        }

        /* Section dividers */
        .section {
            padding-top: 8rem;
            padding-bottom: 8rem;
        }
        .section-divider {
            border-bottom: 1px solid #2a2a2a;
        }
        
        /* --- Cadence UI Container --- */
        .cadence-container {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 1.5rem;
            font-family: 'Inter', sans-serif;
            color: #000000;
        }
        
        .cadence-container h5, .cadence-container strong {
             color: #000000;
        }
        .cadence-container hr {
            border-color: #dddddd;
        }

        .cadence-container .engagement-card {
            background-color: #f0f0f0;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #dddddd;
            margin-bottom: 1rem;
            color: #333333;
        }
        
        .cadence-container .engagement-card .status {
            font-weight: 700;
        }
        .cadence-container .engagement-card .status-at-risk { color: #ff4b4b; }
        .cadence-container .engagement-card .status-on-track { color: #3dd56d; }
        .cadence-container .engagement-card .status-awaiting { color: #f0b429; }
        
        .cadence-container .button-row {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        .cadence-container .cadence-button {
            flex-grow: 1;
            background-color: #e9ecef;
            color: #000000;
            border: 1px solid #ced4da;
            padding: 0.75rem 1rem;
            font-weight: 700;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s;
            text-align: center;
        }
        .cadence-container .cadence-button:hover {
            background-color: #dee2e6;
        }
        .cadence-container .advance-button {
            background-color: #000000;
            color: #ffffff;
            border: 1px solid #000000;
        }
        .cadence-container .advance-button:hover {
            background-color: #333333;
        }
        
        .footer-text {
            text-align: center;
            color: #a1a1a1; 
            padding: 2rem 0;
        }

    </style>
    """, unsafe_allow_html=True)

    # --- CUSTOM NAVIGATION BAR ---
    st.markdown("""
        <div class="nav-container">
            <a href="#top" class="nav-logo">MemoGenie</a>
            <div class="nav-links">
                <a href="#how-it-works">How It Works</a>
                <a href="#cadence">Cadence</a>
                <a href="#the-engine">The Engine</a>
                <a href="#request-a-demo" class="nav-cta">Request a Demo</a>
            </div>
        </div>
    """, unsafe_allow_html=True)


    # --- HERO SECTION ---
    with st.container():
        st.markdown("<div id='top' style='padding-top: 8rem'></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'><h1>Unlock Your Institutional Memory.</h1><p>Your company's most valuable asset is its knowledge. But it's trapped in Slack, Notion, and meeting transcripts. MemoGenie is the AI engine that turns your scattered data into a single source of truth.</p></div>", unsafe_allow_html=True)
        
        _, col2, _ = st.columns([3.5, 2, 3.5])
        with col2:
            st.link_button("Request Enterprise Demo →", "#request-a-demo", use_container_width=True)
    
    # --- SOCIAL PROOF ---
    with st.container():
        st.write(" ")
        st.write(" ")
        st.markdown("<p style='text-align: center; color: #a1a1a1;'>TRUSTED BY THE WORLD'S MOST INNOVATIVE COMPANIES</p>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: 600; color: #555555; letter-spacing: 0.5rem;'>LOGO LOGO LOGO LOGO</h3>", unsafe_allow_html=True)
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # --- HOW IT WORKS ---
    with st.container():
        st.markdown("<div id='how-it-works' class='section'></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'><h2>Connect. Reason. Act.</h2><p>In three simple steps, MemoGenie transforms your disparate data into a proactive, intelligent advantage.</p></div>", unsafe_allow_html=True)
        
        cols = st.columns(3, gap="large")
        cards_data = [
            {"icon": "🔌", "title": "1. Connect Your Tools", "text": "With one click, securely link MemoGenie to your existing knowledge sources: Slack, Notion, Google Drive, and more. Our system begins indexing immediately."},
            {"icon": "🕸️", "title": "2. Build The Knowledge Graph", "text": "Our engine maps the hidden relationships between people, projects, and decisions, creating a dynamic, real-time model of your organization's brain."},
            {"icon": "💡", "title": "3. Get Proactive Insights", "text": "Don't just search, ask. MemoGenie delivers synthesized answers, surfaces hidden risks, and provides the strategic foresight you need to win."}
        ]
        for i, card in enumerate(cards_data):
            with cols[i]:
                st.markdown(f"""
                <div class="card">
                    <div class="card-icon">{card['icon']}</div>
                    <h3>{card['title']}</h3>
                    <p>{card['text']}</p>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # --- CADENCE SECTION ---
    with st.container():
        st.markdown("<div id='cadence' class='section'></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'><h2>From Insight to Action: Introducing Cadence</h2><p>Cadence is the killer app powered by the MemoGenie engine. It's your calendar's Chief of Staff, using institutional knowledge to automate follow-ups, eliminate scheduling-hell, and ensure no opportunity is ever dropped.</p></div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1,1], gap="large")

        with col1:
            st.subheader("Stop Chasing. Start Closing.")
            st.write("""
            For sales teams, VCs, and recruiters, momentum is everything. Cadence monitors your pipeline of conversations and turns your MemoGenie knowledge graph into action.
            - **AI-Powered Playbooks:** It knows your firm's process and suggests the next best action for every engagement.
            - **Automated Follow-ups:** It sends the right message at the right time, so your team can focus on conversations, not logistics.
            - **The "Magic Wand":** The `Advance All` button executes every overdue automated task in one click, clearing your team's plate for high-value work.
            """)
        
        with col2:
            cadence_html = """
            <div class="cadence-container">
                <h5><strong>Momentum Score: <span class="status-at-risk">8 Engagements Stalled</span></strong></h5>
                <hr>
                
                <div class="engagement-card">
                    <strong>Jane Doe @ Acme Corp</strong> - Close Seed Investment<br>
                    <span class="status status-at-risk">🚨 AT RISK (NO CONTACT IN 10 DAYS)</span><br>
                    <small><strong>Next Step:</strong> AUTOMATED: Follow-up #3 sends in 4 hours.</small>
                </div>

                <div class="engagement-card">
                    <strong>John Smith @ Innovate Inc</strong> - Schedule Demo<br>
                    <span class="status status-awaiting">⏳ AWAITING REPLY (DAY 2)</span><br>
                    <small><strong>Next Step:</strong> ACTION: Record personalized video about their competitor.</small>
                </div>

                <div class="engagement-card">
                    <strong>Sam Wilson @ Future Tech</strong> - Term Sheet Negotiation<br>
                    <span class="status status-on-track">✅ MEETING SCHEDULED (TOMORROW)</span><br>
                    <small><strong>Next Step:</strong> AI is generating pre-meeting brief.</small>
                </div>

                <div class="button-row">
                    <button class="cadence-button">＋ New Engagement</button>
                    <button class="cadence-button">My Day</button>
                    <button class="cadence-button advance-button">🚀 Advance All</button>
                </div>
            </div>
            """
            st.components.v1.html(cadence_html, height=480)

        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # --- THE MEMOGENIE ADVANTAGE (ENGINE) ---
    with st.container():
        st.markdown("<div id='the-engine' class='section'></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'><h2>From Retrieval to Reasoning.</h2><p>This isn't just another RAG pipeline. Our Cognitive Engine connects disparate data points to generate novel, strategic insights your team would otherwise miss.</p></div>", unsafe_allow_html=True)

        cols = st.columns(3, gap="large")
        cards_data = [
            {"icon": "🚀", "title": "90% Faster Onboarding", "text": "Give new hires a co-pilot that can answer any question about your company's history, projects, and processes instantly."},
            {"icon": "🔄", "title": "Reduce Redundant Work by 15%", "text": "Our proactive agents surface existing work and past decisions before your team starts a new project from scratch."},
            {"icon": "🔮", "title": "Lead with Foresight", "text": "Go beyond what happened to why it happened. Understand the second-order effects of decisions and mitigate risks before they emerge."}
        ]
        for i, card in enumerate(cards_data):
            with cols[i]:
                st.markdown(f"""
                <div class="card">
                    <div class="card-icon">{card['icon']}</div>
                    <h3>{card['title']}</h3>
                    <p>{card['text']}</p>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    
    # --- GOOGLE FORM EMBED ---
    with st.container():
        st.markdown("<div id='request-a-demo' class='section'></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'><h2>Get Started with MemoGenie</h2><p>Request a personalized demo and discover how our Cognitive Engine and Cadence application can unlock the institutional memory of your enterprise.</p></div>", unsafe_allow_html=True)
        
        google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?embedded=true"
        
        st.components.v1.html(
            f'<iframe src="{google_form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>',
            height=820
        )

    # --- FOOTER ---
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<div class='footer-text'><p>© 2025 MemoGenie. The Single Source of Truth for Enterprise.</p></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
