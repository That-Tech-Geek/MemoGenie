import streamlit as st

# Page config
st.set_page_config(
    page_title="MemoGenie | The Enterprise Knowledge Engine",
    layout="wide"
)

# Inject Google Fonts + CSS
st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">

    <style>
        :root {
            --background: #000000;
            --text-primary: #ffffff;
            --text-secondary: #a1a1a1;
            --surface: #181818;
            --primary: #ffffff; 
            --primary-hover: #e5e5e5;
            --border-color: #2a2a2a;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--background);
            color: var(--text-primary);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 24px;
        }

        h1, h2, h3 {
            font-weight: 700;
            line-height: 1.2;
        }

        .header {
            padding: 20px 0;
            border-bottom: 1px solid var(--border-color);
            position: sticky;
            top: 0;
            background-color: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            z-index: 10;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--text-primary);
            text-decoration: none;
        }

        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            margin-left: 24px;
            transition: color 0.3s ease;
            font-weight: 600;
        }

        .nav-links a:hover {
            color: var(--text-primary);
        }

        .nav-cta {
            background-color: var(--primary);
            color: var(--background);
            font-weight: 700;
            padding: 8px 16px;
            border-radius: 6px;
        }

        .nav-cta:hover {
            background-color: var(--primary-hover);
            color: var(--background) !important;
        }

        .hero {
            text-align: center;
            padding: 120px 0;
        }

        .hero h1 {
            font-size: 4.5rem;
            font-weight: 900;
            letter-spacing: -2px;
            margin-bottom: 20px;
            color: var(--text-primary);
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--text-secondary);
            max-width: 650px;
            margin: 0 auto 40px;
        }

        .cta-button {
            display: inline-block;
            background-color: var(--primary);
            color: var(--background);
            padding: 16px 32px;
            font-size: 1.1rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: 8px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }

        .cta-button:hover {
            background-color: var(--primary-hover);
            transform: translateY(-3px);
        }

        .features {
            padding: 80px 0;
            border-top: 1px solid var(--border-color);
        }

        .section-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-header h2 {
            font-size: 2.8rem;
            font-weight: 900;
        }

        .section-header p {
            font-size: 1.1rem;
            color: var(--text-secondary);
            max-width: 500px;
            margin: 10px auto 0;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
        }

        .feature-card {
            background-color: var(--surface);
            padding: 32px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            border-color: var(--text-secondary);
        }

        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 12px;
        }

        .feature-card p {
            color: var(--text-secondary);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 16px;
        }

        .footer {
            text-align: center;
            padding: 40px 0;
            margin-top: 60px;
            border-top: 1px solid var(--border-color);
            color: var(--text-secondary);
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 3rem;
            }
            .hero p {
                font-size: 1.1rem;
            }
            .nav-links a {
                display: none;
            }
            .nav-links .nav-cta {
                display: block;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject HTML structure
st.markdown(
    """
    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">MemoGenie</a>
                <div class="nav-links">
                    <a href="#solutions">Solutions</a>
                    <a href="#">Customers</a>
                    <a href="#">Pricing</a>
                    <a href="#" class="nav-cta">Request a Demo</a>
                </div>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>Unlock Your Institutional Memory.</h1>
                <p>
                    Your company's most valuable asset is its knowledge. But it's trapped in Slack, Notion, and meeting transcripts. MemoGenie is the AI engine that turns your scattered data into a single source of truth.
                </p>
                <a href="#" class="cta-button">Request Enterprise Demo &rarr;</a>
            </div>
        </section>

        <!-- Problem Section -->
        <section id="solutions" class="features">
            <div class="container">
                <div class="section-header">
                    <h2>The High Cost of Lost Knowledge</h2>
                    <p>Every day, your team wastes hours searching for information, duplicating work, and re-learning what's already known.</p>
                </div>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">⏳</div>
                        <h3>Slow Onboarding</h3>
                        <p>New hires take months to become productive, piecing together context from endless documents and asking repetitive questions.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔄</div>
                        <h3>Redundant Work</h3>
                        <p>Decisions are re-litigated and projects are re-started because past work is impossible to find, costing you time and money.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🚪</div>
                        <h3>Knowledge Drain</h3>
                        <p>When an employee leaves, their expertise walks out the door. Critical knowledge is lost forever, weakening your entire organization.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Solution Section -->
        <section id="features" class="features">
            <div class="container">
                <div class="section-header">
                    <h2>The Intelligence Layer for Your Business</h2>
                    <p>MemoGenie securely connects to your existing tools to create a searchable, intelligent knowledge base that works for you.</p>
                </div>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3>Onboard Hires in Days, Not Months</h3>
                        <p>Let new team members ask MemoGenie: "What's the history of Project X?" and get an instant, AI-generated brief with all key decisions and documents.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">💡</div>
                        <h3>Surface Insights, Not Just Documents</h3>
                        <p>Ask "What are our key learnings from the Q3 customer feedback?" and get a synthesized summary, not a list of 100 links.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔒</div>
                        <h3>Secure, Private, and Integrated</h3>
                        <p>Connects to your tools with enterprise-grade security. Your data is your own, and is never used for training external models.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Cognitive Engine Section -->
        <section class="features">
            <div class="container">
                <div class="section-header">
                    <h2>From Retrieval to Reasoning.</h2>
                    <p>Retrieval-Augmented Generation (RAG) is a commodity. It finds documents. Our Cognitive Engine connects disparate data points to generate novel, strategic insights your team would otherwise miss.</p>
                </div>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🕸️</div>
                        <h3>The Dynamic Knowledge Graph</h3>
                        <p>We don't just index your data; we build a real-time map of it. It understands the relationships between people, projects, decisions, and outcomes.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🕵️</div>
                        <h3>Proactive AI Agents</h3>
                        <p>Our autonomous agents monitor the knowledge graph 24/7 to surface unseen opportunities, flag emerging risks, and identify critical patterns before a human could.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔮</div>
                        <h3>Causal & Predictive Insights</h3>
                        <p>Go beyond what happened to why it happened. The engine helps you understand the second-order effects of decisions, enabling you to lead with foresight.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 MemoGenie. The Single Source of Truth for Enterprise.</p>
        </div>
    </footer>
    """,
    unsafe_allow_html=True
)
