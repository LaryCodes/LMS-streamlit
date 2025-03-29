import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.markdown("""
    <style>
        /* Modern Dark Theme with Professional Aesthetics */
        :root {
            --primary-color: #6e48aa;
            --secondary-color: #1e96fc;
            --background-color: #121212;
            --card-bg: #1e1e1e;
            --text-color: #f5f5f5;
            --accent-color: #00d4ff;
            --danger-color: #ff5252;
            --success-color: #4caf50;
            --border-radius: 12px;
        }

        /* Global Reset and Typography */
        .stApp {
            background: linear-gradient(135deg, #121212 0%, #1e1e2f 100%);
            color: var(--text-color);
            font-family: 'Poppins', 'Inter', sans-serif;
        }
        
        /* Header Styling */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem;
            letter-spacing: -0.5px;
        }
        
        /* Card Components with Glass Morphism */
        .card {
            background: rgba(30, 30, 46, 0.85);
            backdrop-filter: blur(10px);
            border-radius: var(--border-radius);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 25px;
            margin-bottom: 24px;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        
        /* Action Buttons - Updated with dark blue-black gradient */
        .stButton>button {
            background: linear-gradient(135deg, #0d324d, #1a1a2e) !important;
            color: white !important;
            border: none !important;
            border-radius: var(--border-radius) !important;
            padding: 12px 24px !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
        }
        .stButton>button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 7px 15px rgba(0, 0, 0, 0.3) !important;
            background: linear-gradient(135deg, #164e73, #1e1e42) !important;
        }
        .stButton>button:active {
            transform: translateY(1px) !important;
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.2) !important;
        }
        
        /* Primary action buttons - Slightly brighter blue accent */
        .stButton>button[data-baseweb="button"][kind="primary"] {
            background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
            box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Secondary/Delete buttons - Dark style */
        div[data-testid="stButton"] button[kind="secondary"] {
            background: linear-gradient(135deg, #243B55, #141E30) !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 15px rgba(20, 30, 48, 0.3) !important;
        }
        
        /* Remove any custom button styles that were added inline */
        div[data-testid="stButton"] button[kind="secondary"]:last-child {
            background: linear-gradient(135deg, #243B55, #141E30) !important;
        }
        
        /* Add Lesson button */
        form > div[data-testid="stButton"] > button {
            background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
            height: 60px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            letter-spacing: 1px !important;
        }
        
        /* Global text and label colors */
        .stApp {
            background: linear-gradient(135deg, #121212 0%, #1e1e2f 100%);
            color: var(--text-color);
            font-family: 'Poppins', 'Inter', sans-serif;
        }
        
        /* Make all form labels white and visible - expanded selectors */
        label, 
        .stTextInput label, 
        .stNumberInput label, 
        .stDateInput label, 
        .stSelectbox label,
        p[data-baseweb="typo-paragraphsmall"],
        [data-testid="stForm"] label,
        div[data-baseweb="form-control-label"],
        div[data-baseweb="form-control-label"] label,
        .stNumberInput span {
            color: white !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            margin-bottom: 8px !important;
            opacity: 1 !important;
            text-shadow: 0px 0px 2px rgba(0,0,0,0.4) !important;
        }
        
        /* Extra specificity for number input elements */
        [data-testid="stNumberInput"] label,
        [data-testid="stNumberInput"] span[data-baseweb="block"],
        [data-testid="stNumberInput"] div[data-baseweb="block"] {
            color: white !important;
            opacity: 1 !important;
        }
        
        /* Fix for streamlit label container */
        div.st-emotion-cache-16idsys p,
        div.st-emotion-cache-16idsys {
            color: white !important;
            font-weight: 500 !important;
            opacity: 1 !important;
        }
        
        /* Input Fields - Consistent white background with black text */
        .stTextInput>div>div>input, 
        .stNumberInput>div>div>input, 
        .stDateInput>div>div>div>input, 
        .stSelectbox>div>div>div,
        .stMultiselect>div>div>div {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: var(--border-radius);
            color: #000000 !important;
            padding: 12px 16px;
            height: 45px;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        
        /* Ensure placeholder text is visible */
        .stTextInput>div>div>input::placeholder,
        .stNumberInput>div>div>input::placeholder,
        .stDateInput input::placeholder {
            color: rgba(0, 0, 0, 0.5) !important;
        }
        
        /* Ensure selectbox text and options are visible */
        .stSelectbox > div > div > div {
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #000000 !important;
            min-height: 45px !important;
            display: flex !important;
            align-items: center !important;
            padding-left: 15px !important;
        }
        
        /* Dropdown menu styling */
        div[data-baseweb="popover"] div[data-baseweb="menu"] {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border: 1px solid rgba(0, 0, 0, 0.1) !important;
        }
        
        div[data-baseweb="popover"] div[data-baseweb="menu"] ul li {
            color: #000000 !important;
        }
        
        div[data-baseweb="popover"] div[data-baseweb="menu"] ul li:hover {
            background-color: rgba(110, 72, 170, 0.1) !important;
        }
        
        /* Date input specific styling */
        .stDateInput input, .stDateInput div[data-baseweb="input"] {
            color: #000000 !important;
            background-color: rgba(255, 255, 255, 0.9) !important;
        }
        
        /* Date picker calendar styling */
        div[data-baseweb="calendar"] {
            background-color: white !important;
            border: 1px solid rgba(0, 0, 0, 0.1) !important;
        }
        
        div[data-baseweb="calendar"] button, div[data-baseweb="calendar"] div {
            color: #000000 !important;
        }
        
        /* Number input fields */
        .stNumberInput p, .stNumberInput span {
            color: #000000 !important;
        }
        .stNumberInput button {
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #000000 !important;
        }
        
        /* Focus states for input fields */
        .stTextInput>div>div>input:focus, 
        .stNumberInput>div>div>input:focus,
        .stDateInput>div>div>div>input:focus,
        .stSelectbox>div>div>div:focus,
        .stMultiselect>div>div>div:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 0 2px rgba(0, 212, 255, 0.3);
            background-color: white !important;
        }
        
        /* Authentication inputs */
        /* Make login/signup form inputs especially visible */
        [data-testid="stForm"] .stTextInput>div>div>input, 
        [data-testid="stForm"] .stTextInput input[type="text"],
        [data-testid="stForm"] .stTextInput input[type="password"] {
            background-color: white !important;
            color: #000000 !important;
            border: 1px solid rgba(0, 0, 0, 0.2);
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: rgba(30, 30, 46, 0.3);
            padding: 10px;
            border-radius: 12px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            border-radius: 8px !important;
            color: white !important;
            background-color: rgba(255, 255, 255, 0.1) !important;
            transition: all 0.3s ease;
            border: none !important;
            padding: 0 25px !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(255, 255, 255, 0.15) !important;
            transform: translateY(-2px);
        }
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
            color: white !important;
            box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3) !important;
            transform: translateY(-3px);
            font-weight: 700 !important;
        }
        
        /* Custom styling for auth section */
        .auth-section {
            background: rgba(20, 20, 35, 0.7);
            border-radius: 16px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            padding: 30px;
            position: relative;
        }
        
        /* Animated background for sign-in/sign-up */
        .auth-bg-animation {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                45deg, 
                rgba(30, 60, 114, 0.1) 0%, 
                rgba(42, 82, 152, 0.1) 25%, 
                rgba(64, 91, 168, 0.1) 50%, 
                rgba(30, 96, 145, 0.1) 75%, 
                rgba(20, 30, 48, 0.1) 100%
            );
            background-size: 400% 400%;
            animation: gradientAnim 15s ease infinite;
            z-index: -1;
        }
        
        @keyframes gradientAnim {
            0% { background-position: 0% 50% }
            50% { background-position: 100% 50% }
            100% { background-position: 0% 50% }
        }
        
        /* DataFrames and Tables */
        .stDataFrame {
            border-radius: var(--border-radius);
            overflow: hidden;
        }
        .stDataFrame > div {
            border-radius: var(--border-radius);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .stDataFrame th {
            background-color: rgba(30, 30, 46, 0.9);
            color: var(--accent-color);
            font-weight: 600;
            padding: 12px 16px;
        }
        .stDataFrame td {
            background-color: rgba(30, 30, 46, 0.6);
            color: var(--text-color);
            padding: 10px 16px;
        }
        
        /* Charts and Visualizations */
        .js-plotly-plot {
            border-radius: var(--border-radius);
            background: rgba(30, 30, 46, 0.6);
            padding: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        /* Radio Buttons */
        .stRadio > div {
            background-color: rgba(30, 30, 46, 0.6);
            border-radius: var(--border-radius);
            padding: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .stRadio label {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            padding: 8px 16px;
            margin: 5px;
            transition: all 0.2s ease;
        }
        .stRadio label:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        /* Metrics */
        .stMetric {
            background: rgba(30, 30, 46, 0.8);
            border-radius: var(--border-radius);
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 20px;
        }
        .stMetric label {
            color: var(--accent-color);
            font-weight: 600;
        }
        
        /* Make metric values white and larger */
        .stMetric [data-testid="stMetricValue"] {
            color: white !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.2) !important;
        }
        
        /* Make metric labels white */
        .stMetric [data-testid="stMetricLabel"] {
            color: white !important;
            font-size: 1rem !important;
            font-weight: 500 !important;
            opacity: 0.9 !important;
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] > div {
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 1rem;
        }
        
        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(30, 30, 46, 0.4);
            border-radius: 5px;
        }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            border-radius: 5px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, var(--secondary-color), var(--primary-color));
        }
        
        /* Option Menu Styling */
        .nav-link {
            margin: 0.2rem 0;
            border-radius: 6px !important;
            text-align: left;
            font-weight: 500;
            transition: all 0.2s ease;
        }
        .nav-link:hover {
            background-color: rgba(110, 72, 170, 0.2) !important;
        }
        .nav-link-selected {
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color)) !important;
            color: white !important;
            font-weight: 600 !important;
        }
        
        /* Success and Error Messages */
        .stAlert {
            border-radius: var(--border-radius);
            padding: 10px 16px;
        }
        .element-container div[data-baseweb="notification"] {
            border-radius: var(--border-radius);
            margin-bottom: 1rem;
        }
        
        /* Status elements */
        .success {
            color: var(--success-color);
            font-weight: 600;
        }
        .error {
            color: var(--danger-color);
            font-weight: 600;
        }
        
        /* Form layout improvements */
        .form-row {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        
        /* Improved spacing and alignment */
        .stApp > header {
            background-color: transparent;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }
        
        /* Custom styling for tabs only */
        div[data-testid="stHorizontalBlock"] > div[data-baseweb="tab-list"] {
            gap: 0;
            background-color: rgba(30, 30, 46, 0.3);
            padding: 8px;
            border-radius: 12px;
            display: flex;
            width: fit-content;
            margin: 0 auto 20px auto;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        div[data-baseweb="tab"] {
            border-radius: 8px !important;
            padding: 10px 30px !important;
            margin: 0 5px;
            transition: all 0.3s ease-in-out;
            font-weight: 600 !important;
            letter-spacing: 0.5px;
            border: none !important;
            background: rgba(30, 30, 46, 0.7) !important;
        }
        
        div[data-baseweb="tab"]:hover {
            background: rgba(30, 60, 114, 0.5) !important;
            transform: translateY(-2px);
        }
        
        div[data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
            box-shadow: 0 5px 15px rgba(30, 60, 114, 0.4);
            transform: translateY(-3px);
        }
    </style>
""", unsafe_allow_html=True)

def get_chart_theme():
    return {
        "template": "plotly_dark",
        "color_discrete_sequence": px.colors.sequential.Plasma,
        "background_color": "rgba(30, 30, 46, 0.0)",
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"color": "#f5f5f5"}
    }


if "lessons" not in st.session_state:
    st.session_state["lessons"] = pd.DataFrame({
        "Lesson": [], "Teacher": [], "Date": [], "Students": []
    })

if "users" not in st.session_state:
    st.session_state["users"] = {}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("📚 Professional Lesson Management System")
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Streamline Your Teaching Workflow")
    st.write("Our powerful platform helps educators manage lessons, track student progress, and analyze teaching performance - all in one place.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 📅 Lesson Planning")
        st.write("Efficiently schedule and organize your teaching calendar")
    with col2:
        st.markdown("#### 📊 Analytics")
        st.write("Gain insights with detailed visualizations and reports")
    with col3:
        st.markdown("#### 👨‍🏫 Resource Management")
        st.write("Keep track of teachers, students and class resources")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    /* Custom styling for tabs only */
    div[data-testid="stHorizontalBlock"] > div[data-baseweb="tab-list"] {
        gap: 0;
        background-color: rgba(30, 30, 46, 0.3);
        padding: 8px;
        border-radius: 12px;
        display: flex;
        width: fit-content;
        margin: 0 auto 20px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    div[data-baseweb="tab"] {
        border-radius: 8px !important;
        padding: 10px 30px !important;
        margin: 0 5px;
        transition: all 0.3s ease-in-out;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        border: none !important;
        background: rgba(30, 30, 46, 0.7) !important;
    }
    
    div[data-baseweb="tab"]:hover {
        background: rgba(30, 60, 114, 0.5) !important;
        transform: translateY(-2px);
    }
    
    div[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
        box-shadow: 0 5px 15px rgba(30, 60, 114, 0.4);
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        username = st.text_input("Username", placeholder="Enter your username", key="login_username")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
        col1, col2 = st.columns([3, 1])
        with col1:
            login_btn = st.button("Sign In", use_container_width=True)
        
        if login_btn:
            if username in st.session_state["users"] and st.session_state["users"][username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success(f"✅ Welcome, {username}!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")
    
    with tab2:
        new_user = st.text_input("Username", placeholder="Choose a username", key="signup_username")
        new_password = st.text_input("Password", type="password", placeholder="Create a secure password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password", key="confirm_password")
        
        signup_btn = st.button("Create Account", use_container_width=True)
        if signup_btn:
            if new_user and new_password and new_password == confirm_password:
                if new_user in st.session_state["users"]:
                    st.error("⚠️ Username already exists.")
                else:
                    st.session_state["users"][new_user] = new_password
                    st.success("✅ Account created successfully! You can now sign in.")
            elif new_password != confirm_password:
                st.error("⚠️ Passwords do not match.")
            else:
                st.error("⚠️ Please fill all fields.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state['username']}")
        st.markdown("---")
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Lessons", "Analytics", "Settings"],
            icons=["house", "book", "bar-chart", "gear"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0", "background-color": "transparent"},
                "icon": {"font-size": "16px", "margin-right": "8px"},
                "nav-link": {"font-size": "15px", "text-align": "left", "margin": "4px 0", 
                           "padding": "10px 15px", "--hover-color": "rgba(110, 72, 170, 0.2)"},
                "nav-link-selected": {"background": "linear-gradient(90deg, #6e48aa, #1e96fc)"},
            }
        )
        
        st.markdown("---")
        if st.button("Sign Out", use_container_width=True):
            st.session_state["authenticated"] = False
            st.rerun()

    if selected == "Dashboard":
        st.title("📊 Interactive Dashboard")
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            lesson_count = len(st.session_state["lessons"]) if not st.session_state["lessons"].empty else 0
            st.metric("Total Lessons", f"{lesson_count}")
        with col2:
            total_students = st.session_state["lessons"]["Students"].sum() if not st.session_state["lessons"].empty else 0
            st.metric("Total Students", f"{total_students}")
        with col3:
            avg_students = st.session_state["lessons"]["Students"].mean() if not st.session_state["lessons"].empty else 0
            st.metric("Avg. Students/Lesson", f"{avg_students:.1f}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Lesson Attendance Overview")
        if not st.session_state["lessons"].empty:
            fig = px.bar(st.session_state["lessons"], x="Lesson", y="Students", color="Lesson",
                         title="Students per Lesson")
            
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#f5f5f5"},
                margin=dict(l=20, r=20, t=50, b=20),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("📌 No lesson data available yet. Add lessons to see insights here.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Recent Lessons")
        if not st.session_state["lessons"].empty:

            recent = st.session_state["lessons"].sort_values("Date", ascending=False).head(5)
            st.dataframe(recent, use_container_width=True, height=250)
        else:
            st.info("📌 No lessons scheduled. Add your first lesson to get started.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif selected == "Lessons":
        st.title("📚 Lesson Management")
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Create New Lesson")
        
        col1, col2 = st.columns(2)
        with col1:
            new_lesson = st.text_input("Lesson Title", placeholder="e.g. Python Fundamentals")
            new_teacher = st.text_input("Teacher", placeholder="Teacher Name")
        with col2:
            new_date = st.date_input("Lesson Date")

            st.markdown('<p style="color: white; font-weight: 500; margin-bottom: 8px; font-size: 14px;">Number of Students</p>', unsafe_allow_html=True)
            new_students = st.number_input("", min_value=1, step=1, label_visibility="collapsed")
        
        if st.button("Add Lesson", use_container_width=True):
            if new_lesson and new_teacher and new_date:
                new_entry = pd.DataFrame({
                    "Lesson": [new_lesson], "Teacher": [new_teacher],
                    "Date": [new_date.strftime('%Y-%m-%d')], "Students": [new_students]
                })
                st.session_state["lessons"] = pd.concat([st.session_state["lessons"], new_entry], ignore_index=True)
                st.success(f"✅ Lesson '{new_lesson}' successfully added!")
                st.rerun()
            else:
                st.error("⚠️ Please fill all required fields.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Current Lessons")
        
        if not st.session_state["lessons"].empty:

            sorted_lessons = st.session_state["lessons"].sort_values("Date")
            st.dataframe(sorted_lessons, use_container_width=True)
            
            st.markdown("#### Manage Lessons")
            
            delete_lesson = st.selectbox(
                "Select Lesson to Delete",
                st.session_state["lessons"]["Lesson"],
                key="delete_lesson_select"
            )
            
            st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
            
            st.markdown("""
            <style>
                div[data-testid="stButton"] button[kind="secondary"]:last-child {
                    background: linear-gradient(135deg, #243B55, #141E30) !important;
                    font-weight: 700;
                    letter-spacing: 1px;
                    color: white;
                }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("DELETE SELECTED LESSON", use_container_width=True, 
                        key="delete_lesson_btn", type="secondary"):
                st.session_state["lessons"] = st.session_state["lessons"][st.session_state["lessons"]["Lesson"] != delete_lesson]
                st.success(f"✅ Lesson '{delete_lesson}' deleted successfully!")
                st.rerun()
        else:
            st.info("📌 No lessons available. Create your first lesson above.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif selected == "Analytics":
        st.title("📈 Performance Analytics")
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if not st.session_state["lessons"].empty:
            st.subheader("Student Distribution by Lesson")
            fig = px.pie(st.session_state["lessons"], names="Lesson", values="Students",
                      color_discrete_sequence=px.colors.sequential.Plasma)
            
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#f5f5f5"},
                margin=dict(l=20, r=20, t=40, b=20),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("📌 No data available for analytics. Add lessons to see insights.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if not st.session_state["lessons"].empty:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Teacher Performance")
            
            teacher_stats = st.session_state["lessons"].groupby("Teacher").agg({
                "Lesson": "count",
                "Students": ["sum", "mean"]
            }).reset_index()
            
            teacher_stats.columns = ["Teacher", "Lessons Taught", "Total Students", "Avg Students/Lesson"]
            teacher_stats["Avg Students/Lesson"] = teacher_stats["Avg Students/Lesson"].round(1)
            
            st.dataframe(teacher_stats, use_container_width=True)
            
            fig = px.bar(teacher_stats, x="Teacher", y="Avg Students/Lesson", color="Teacher",
                      title="Average Class Size by Teacher",
                      color_discrete_sequence=px.colors.sequential.Plasma)
            
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#f5f5f5"},
                margin=dict(l=20, r=20, t=50, b=20),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if not st.session_state["lessons"].empty:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Attendance Trends")
            
            df_trend = st.session_state["lessons"].copy()
            df_trend["Date"] = pd.to_datetime(df_trend["Date"])
            df_trend = df_trend.sort_values("Date")
            
            fig = px.line(df_trend, x="Date", y="Students", markers=True,
                       title="Student Attendance Over Time",
                       color_discrete_sequence=px.colors.sequential.Plasma)
            
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#f5f5f5"},
                margin=dict(l=20, r=20, t=50, b=20),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    elif selected == "Settings":
        st.title("⚙ System Settings")
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Account Settings")
        
        current_user = st.session_state["username"]
        st.write(f"Currently logged in as: **{current_user}**")
        
        if st.button("Change Password", use_container_width=True):
            st.session_state["show_password_change"] = True
        
        if st.session_state.get("show_password_change", False):
            current_password = st.text_input("Current Password", type="password")
            new_password = st.text_input("New Password", type="password")
            confirm_new_password = st.text_input("Confirm New Password", type="password")
            
            if st.button("Update Password", use_container_width=True):
                if st.session_state["users"][current_user] == current_password:
                    if new_password == confirm_new_password:
                        st.session_state["users"][current_user] = new_password
                        st.success("✅ Password updated successfully!")
                        st.session_state["show_password_change"] = False
                    else:
                        st.error("⚠️ New passwords do not match.")
                else:
                    st.error("⚠️ Current password is incorrect.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Data Management")
        
        if st.button("Export Lesson Data", use_container_width=True):
            if not st.session_state["lessons"].empty:
                csv = st.session_state["lessons"].to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="lesson_data.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            else:
                st.warning("⚠️ No data available to export.")
        
        st.markdown("#### Reset System")
        st.warning("⚠️ Caution: The following actions cannot be undone.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Reset Lesson Data", use_container_width=True):
                st.session_state["lessons"] = pd.DataFrame({
                    "Lesson": [], "Teacher": [], "Date": [], "Students": []
                })
                st.success("✅ All lesson data has been reset.")
        with col2:
            if st.button("Reset All Data", use_container_width=True):
                st.session_state["lessons"] = pd.DataFrame({
                    "Lesson": [], "Teacher": [], "Date": [], "Students": []
                })
                st.session_state["users"] = {}
                st.session_state["authenticated"] = False
                st.success("✅ System completely reset. You will be logged out.")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
