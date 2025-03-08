import streamlit as st 
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Simulated Data
if "lessons" not in st.session_state:
    st.session_state["lessons"] = pd.DataFrame({
        "Lesson": [],
        "Teacher": [],
        "Date": [],
        "Students": []
    })

if "users" not in st.session_state:
    st.session_state["users"] = {}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "theme" not in st.session_state:
    st.session_state["theme"] = "Light"  # Default theme

# Apply Theme
def apply_theme():
    if st.session_state["theme"] == "Dark":
        dark_css = """
            <style>
                body {background-color: #121212; color: white;}
                .stApp {background-color: #121212;}
                .css-1d391kg {color: white;} /* Titles */
                .css-2trqyj {color: white;} /* Text */
            </style>
        """
        st.markdown(dark_css, unsafe_allow_html=True)

apply_theme()

# Landing Page
if not st.session_state["authenticated"]:
    st.title("📚 Lesson Management System")
    st.subheader("Effortless Lesson Planning & Student Management")
    st.write("Manage your lessons efficiently with scheduling, analytics, and easy user management.")

    st.markdown("""
    ### Key Features:
    - 📅 **Schedule and Manage Lessons**
    
        here you shedule and manage your lessons directly with scheduling, analytics, and easy user management. You can also manage your lessons with scheduling, analytics, and easy user management
        
    - 📊 **Authentication (Sign Up & Sign In)**
    
        here you can sign up and sign in to your account to manage your lessons directly with scheduling, analytics, and easy user management. You can also manage your lessons with scheduling, analytics, and easy user management
        
    - 📊 **View Student Participation Analytics**
    
        here you can view student participation analytics directly with scheduling, analytics, and easy user management. You can also manage your lessons with scheduling, analytics, and easy user management
    
    - 👨‍🏫 **Lesson Management**
    
        The Lessons page lets users view all scheduled lessons in a table, showing the lesson name, teacher, date, and number of students. Users can add a new lesson by entering the lesson name, teacher’s name, date, and student count, then clicking "Add Lesson" to save it. They can also delete any lesson they no longer need.
    
    - 🔐 **Dashboard**
    
        After signing in, users land on the Dashboard, which presents key statistics through visual charts:

        A bar graph showing the number of students per lesson.
        Summarized insights on student participation.
        If no lessons exist, a message prompts users to add new lessons.
    
    """)
    
    st.markdown("---")
    

    menu = st.radio("Choose an option:", ["Sign Up", "Sign In"], horizontal=True)

    # st.markdown("---")
    
    if menu == "Sign Up":
        st.subheader("Create an Account")
        new_user = st.text_input("Username", placeholder="Enter your username")
        new_password = st.text_input("Password", type="password", placeholder="Enter a secure password")
        if st.button("Sign Up", use_container_width=True):
            if new_user and new_password:
                st.session_state["users"][new_user] = new_password
                st.success("✅ Account created successfully! You can now sign in.")
            else:
                st.error("⚠️ Please fill all fields.")

    elif menu == "Sign In":
        st.subheader("Login to Your Account")
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        if st.button("Sign In", use_container_width=True):
            if username in st.session_state["users"] and st.session_state["users"][username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success(f"✅ Welcome, {username}!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")
else:
    # Sidebar Navigation
    with st.sidebar:
        st.title(f"Welcome {st.session_state['username']}")
        selected = option_menu(
            menu_title="Lesson Management", 
            options=["Dashboard", "Lessons", "Analytics", "Settings"],
            icons=["house", "book", "bar-chart", "gear"],
            menu_icon="cast",
            default_index=0
        )
        if st.button("Sign Out", use_container_width=True):
            st.session_state["authenticated"] = False
            st.rerun()

    # Dashboard Page
    if selected == "Dashboard":
        st.title("📊 Lesson Management Dashboard")
        if not st.session_state["lessons"].empty:
            fig = px.bar(st.session_state["lessons"], x="Lesson", y="Students", color="Lesson", title="Students per Lesson")
            st.plotly_chart(fig)
        else:
            st.write("No data available. Add a lesson to see analytics.")

    # Lessons Page
    elif selected == "Lessons":
        st.title("📚 Lesson Schedule")
        if not st.session_state["lessons"].empty:
            st.dataframe(st.session_state["lessons"])
        else:
            st.write("No lessons available. Add a new lesson.")

        new_lesson = st.text_input("Add New Lesson")
        new_teacher = st.text_input("Teacher Name")
        new_date = st.date_input("Lesson Date")
        new_students = st.number_input("Number of Students", min_value=1, step=1)

        if st.button("Add Lesson", use_container_width=True):
            if new_lesson and new_teacher and new_date:
                new_entry = pd.DataFrame({
                    "Lesson": [new_lesson],
                    "Teacher": [new_teacher],
                    "Date": [new_date.strftime('%Y-%m-%d')],
                    "Students": [new_students]
                })
                st.session_state["lessons"] = pd.concat([st.session_state["lessons"], new_entry], ignore_index=True)
                st.success(f"✅ Lesson '{new_lesson}' added!")
                st.rerun()
            else:
                st.error("⚠️ Please fill all fields before adding a lesson.")

        st.subheader("Delete a Lesson")
        if not st.session_state["lessons"].empty:
            lesson_to_delete = st.selectbox("Select Lesson to Delete", st.session_state["lessons"]["Lesson"])
            if st.button("Delete Lesson", use_container_width=True):
                st.session_state["lessons"] = st.session_state["lessons"][st.session_state["lessons"]["Lesson"] != lesson_to_delete]
                st.success(f"✅ Lesson '{lesson_to_delete}' deleted!")
                st.rerun()
        else:
            st.write("No lessons available to delete.")

    # Analytics Page
    elif selected == "Analytics":
        st.title("📈 Lesson Analytics")
        if not st.session_state["lessons"].empty:
            avg_students = st.session_state["lessons"]["Students"].mean()
            st.metric(label="Average Students per Lesson", value=f"{avg_students:.1f}")
            fig2 = px.pie(st.session_state["lessons"], names="Lesson", values="Students", title="Student Distribution per Lesson")
            st.plotly_chart(fig2)
        else:
            st.write("No data available for analytics. Add lessons to see insights.")

    # Settings Page
    elif selected == "Settings":
        st.title("⚙ Settings")
        theme = st.selectbox("Choose Theme", ["Light", "Dark"], index=0 if st.session_state["theme"] == "Light" else 1)

        if st.button("Apply Theme", use_container_width=True):
            st.session_state["theme"] = theme
            st.success(f"✅ Theme set to {theme}. Refreshing...")
            st.rerun()
