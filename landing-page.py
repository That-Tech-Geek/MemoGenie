import streamlit as st

def main():
    # --- PAGE CONFIGURATION ---
    st.set_page_config(
        page_title="MemoGenie | The Enterprise Knowledge Engine",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- INJECT CUSTOM CSS ---
    # This is crucial for replicating the black and white, modern theme.
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
        
        /* Button Styles */
        .stButton>button {
            background-color: #ffffff;
            color: #000000;
            border: none;
            padding: 16px 32px;
            font-weight: 700;
            border-radius: 8px;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #e5e5e5;
            color: #000000;
            transform: translateY(-2px);
            border: none;
        }

        /* Feature Card Styles */
        .feature-card {
            background-color: #181818;
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #2a2a2a;
            height: 100%;
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

        /* Center Align Content */
        .center-text {
            text-align: center;
            max-width: 650px;
            margin: 0 auto;
        }
        .section-header {
             text-align: center;
             max-width: 500px;
             margin: 0 auto 4rem auto;
        }
        .section-header p {
            color: #a1a1a1;
            font-size: 1.1rem;
        }
        
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    # While a sticky header is complex, we can create a clean top bar.
    c1, c2 = st.columns([2, 5])
    with c1:
        st.markdown("<h2 style='font-size: 1.8rem; font-weight: 900;'>MemoGenie</h2>", unsafe_allow_html=True)
    with c2:
        # This is a placeholder for nav links if needed in the future
        pass
    st.markdown("---", unsafe_allow_html=True)


    # --- HERO SECTION ---
    with st.container():
        st.markdown("<div class='center-text'><h1>Unlock Your Institutional Memory.</h1></div>", unsafe_allow_html=True)
        st.markdown("<div class='center-text'><p style='font-size: 1.25rem; color: #a1a1a1;'>Your company's most valuable asset is its knowledge. But it's trapped in Slack, Notion, and meeting transcripts. MemoGenie is the AI engine that turns your scattered data into a single source of truth.</p></div>", unsafe_allow_html=True)
        
        # Center the button using columns
        _, col2, _ = st.columns([3, 2, 3])
        with col2:
            st.button("Request Enterprise Demo →")
        
        st.write(" ") # Spacer
        st.write(" ") # Spacer


    # --- PROBLEM SECTION ---
    with st.container():
        st.markdown("<div class='section-header'><h2>The High Cost of Lost Knowledge</h2><p>Every day, your team wastes hours searching for information, duplicating work, and re-learning what's already known.</p></div>", unsafe_allow_html=True)
        
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
        st.write(" ") # Spacer
        st.write(" ") # Spacer


    # --- SOLUTION SECTION ---
    with st.container():
        st.markdown("<div class='section-header'><h2>The Intelligence Layer for Your Business</h2><p>MemoGenie securely connects to your existing tools to create a searchable, intelligent knowledge base that works for you.</p></div>", unsafe_allow_html=True)

        cols = st.columns(3, gap="large")
        cards_data = [
            {"icon": "🚀", "title": "Onboard Hires in Days, Not Months", "text": "Let new team members ask MemoGenie: \"What's the history of Project X?\" and get an instant, AI-generated brief with all key decisions and documents."},
            {"icon": "💡", "title": "Surface Insights, Not Just Documents", "text": "Ask \"What are our key learnings from the Q3 customer feedback?\" and get a synthesized summary, not a list of 100 links."},
            {"icon": "🔒", "title": "Secure, Private, and Integrated", "text": "Connects to your tools with enterprise-grade security. Your data is your own, and is never used for training external models."}
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
        st.write(" ") # Spacer
        st.write(" ") # Spacer


    # --- COGNITIVE ENGINE SECTION ---
    with st.container():
        st.markdown("<div class='section-header'><h2>From Retrieval to Reasoning.</h2><p>Retrieval-Augmented Generation (RAG) is a commodity. It finds documents. Our Cognitive Engine connects disparate data points to generate novel, strategic insights your team would otherwise miss.</p></div>", unsafe_allow_html=True)

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
        st.write(" ") # Spacer
        st.write(" ") # Spacer
    

    # --- FOOTER ---
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: #a1a1a1;'><p>© 2025 MemoGenie. The Single Source of Truth for Enterprise.</p></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
