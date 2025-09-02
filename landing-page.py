import streamlit as st
import time

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
        }

        h2 {
            font-size: 2.8rem !important;
        }
        
        /* Main CTA Button */
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
            color: #000000;
            transform: translateY(-2px);
            border: none;
        }

        /* Demo "Ask" Button */
        div[data-testid*="stHorizontalBlock"] .stButton>button {
             background-color: #181818;
             border: 1px solid #2a2a2a;
        }
         div[data-testid*="stHorizontalBlock"] .stButton>button:hover {
             border-color: #ffffff;
         }


        /* Feature Card Styles */
        .feature-card {
            background-color: #181818;
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #2a2a2a;
            height: 100%;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: #a1a1a1;
        }
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 0.75rem;
        }
        .feature-card p {
            color: #a1a1a1;
        }
        
        /* AI Response Box */
        .ai-response {
            background-color: #181818;
            border: 1px solid #2a2a2a;
            padding: 1.5rem;
            border-radius: 12px;
            margin-top: 1rem;
        }

        /* Center Align Content */
        .center-text {
            text-align: center;
            max-width: 650px;
            margin: 0 auto;
        }
        .section-header {
             text-align: center;
             max-width: 600px;
             margin: 0 auto 4rem auto;
        }
        .section-header p {
            color: #a1a1a1;
            font-size: 1.1rem;
        }

        /* Remove top margin from Streamlit title */
        div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
            padding-top: 0rem;
        }
        
    </style>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    with st.container():
        st.markdown("<div class='center-text'><h1>Unlock Your Institutional Memory.</h1></div>", unsafe_allow_html=True)
        st.markdown("<div class='center-text'><p style='font-size: 1.25rem; color: #a1a1a1;'>Your company's most valuable asset is its knowledge. But it's trapped in Slack, Notion, and meeting transcripts. MemoGenie is the AI engine that turns your scattered data into a single source of truth.</p></div>", unsafe_allow_html=True)
        
        _, col2, _ = st.columns([3.5, 2, 3.5])
        with col2:
            st.link_button("Request Enterprise Demo →", "#request-a-demo", use_container_width=True)
        
        st.write(" ")
        st.write(" ")


    # --- PROBLEM SECTION ---
    with st.container():
        st.markdown("<div id='the-problem' class='section-header'><h2>The High Cost of Lost Knowledge</h2><p>Every day, your team wastes hours searching for information, duplicating work, and re-learning what's already known.</p></div>", unsafe_allow_html=True)
        
        cols = st.columns(3, gap="large")
        cards_data = [
            {"icon": "⏳", "title": "Slow Onboarding", "text": "New hires take months to become productive, piecing together context from endless documents and asking repetitive questions."},
            {"icon": "🔄", "title": "Redundant Work", "text": "Decisions are re-litigated and projects are re-started because past work is impossible to find, costing you time and money."},
            {"icon": "🚪", "title": "Knowledge Drain", "text": "When an employee leaves, their expertise walks out the door. Critical knowledge is lost forever, weakening your entire organization."}
        ]
        for i, card in enumerate(cards_data):
            with cols[i]:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{card['icon']}</div>
                    <h3>{card['title']}</h3>
                    <p>{card['text']}</p>
                </div>
                """, unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")


    # --- INTERACTIVE DEMO ---
    with st.container():
        st.markdown("<div id='demo' class='section-header'><h2>See The Cognitive Engine in Action</h2><p>Ask a question. Our engine won't just find a document—it will connect the dots across your entire organization to give you a strategic answer.</p></div>", unsafe_allow_html=True)

        c1, c2 = st.columns([4, 1])
        with c1:
            user_question = st.text_input("Ask about a project, a decision, or a customer...", placeholder="e.g., What were the key learnings from the Q4 customer feedback on Project Atlas?", label_visibility="collapsed")
        with c2:
            ask_button = st.button("Ask MemoGenie", use_container_width=True)

        if ask_button and user_question:
            with st.spinner("Analyzing connections across documents, transcripts, and messages..."):
                time.sleep(2) # Simulate work
            
            st.markdown(
                """
                <div class="ai-response">
                    <h4>Synthesized Answer:</h4>
                    <p>The key learning from Q4 feedback on <strong>Project Atlas</strong> was that while users loved the new UI (praised by <strong>Alice</strong> in the product sync on Nov 12th), the data export feature was a critical failure point. This issue was first flagged by <strong>Bob</strong> from the Sales team after a call with a major client (see transcript) and is linked to the same API limitation that caused delays in the failed <strong>Project Titan</strong> last year.</p>
                    <p><strong>Recommendation:</strong> Prioritize a fix for the export feature and review the API dependency to avoid repeating past mistakes.</p>
                    <small>SOURCES: [Project Atlas - Q4 Feedback.docx], [Nov 12 - Product Sync Transcript], [Client Call - Bob.mp3]</small>
                </div>
                """, unsafe_allow_html=True
            )
        st.write(" ")
        st.write(" ")


    # --- COGNITIVE ENGINE SECTION ---
    with st.container():
        st.markdown("<div id='the-engine' class='section-header'><h2>From Retrieval to Reasoning.</h2><p>Retrieval-Augmented Generation (RAG) is a commodity. It finds documents. Our Cognitive Engine connects disparate data points to generate novel, strategic insights your team would otherwise miss.</p></div>", unsafe_allow_html=True)

        cols = st.columns(3, gap="large")
        cards_data = [
            {"icon": "🕸️", "title": "The Dynamic Knowledge Graph", "text": "We don't just index your data; we build a real-time map of it. It understands the relationships between people, projects, decisions, and outcomes."},
            {"icon": "🕵️", "title": "Proactive AI Agents", "text": "Our autonomous agents monitor the knowledge graph 24/7 to surface unseen opportunities, flag emerging risks, and identify critical patterns before a human could."},
            {"icon": "🔮", "title": "Causal & Predictive Insights", "text": "Go beyond what happened to why it happened. The engine helps you understand the second-order effects of decisions, enabling you to lead with foresight."}
        ]
        for i, card in enumerate(cards_data):
            with cols[i]:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{card['icon']}</div>
                    <h3>{card['title']}</h3>
                    <p>{card['text']}</p>
                </div>
                """, unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
    
    # --- GOOGLE FORM EMBED ---
    with st.container():
        st.markdown("<div id='request-a-demo' class='section-header'><h2>Get Started with MemoGenie</h2><p>Request a personalized demo and discover how our Cognitive Engine can unlock the institutional memory of your enterprise.</p></div>", unsafe_allow_html=True)
        
        google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?embedded=true"
        
        st.components.v1.html(
            f'<iframe src="{google_form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>',
            height=820
        )


    # --- FOOTER ---
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: #a1a1a1;'><p>© 2025 MemoGenie. The Single Source of Truth for Enterprise.</p></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

