import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Physics Teacher's Web App",
    page_icon="🧑‍🏫",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About Me", "Video Links", "Documents", "Contact Me"]
)

# Define each page
def home_page():
    st.title("Welcome to My Web App!")
    st.markdown(
        """
        Hi, I'm a physics teacher passionate about education and technology. 
        Explore this web app to learn more about me, access resources, and get in touch.
        """
    )
    st.image("https://source.unsplash.com/featured/?physics,science", use_column_width=True)

def about_me_page():
    st.title("About Me")
    st.markdown(
        """
        ## Hello!
        My name is [Your Name], and I am a dedicated physics teacher who loves to integrate technology into education.
        - 🌍 Based in [Your Location].
        - 🎓 Experienced in teaching advanced physics topics.
        - 📚 Passionate about research and interactive learning.
        """
    )

def video_links_page():
    st.title("Video Links")
    st.markdown(
        """
        Here are some curated physics video links:
        - [How Gravity Works](https://www.youtube.com/watch?v=XYZ123)
        - [Understanding Quantum Mechanics](https://www.youtube.com/watch?v=XYZ456)
        - [Physics of Everyday Life](https://www.youtube.com/watch?v=XYZ789)
        """
    )

def documents_page():
    st.title("Documents")
    st.markdown("Download these useful resources:")
    st.download_button(
        label="Download Lecture Notes (PDF)",
        data=open("lecture_notes.pdf", "rb"),
        file_name="lecture_notes.pdf",
        mime="application/pdf"
    )
    st.download_button(
        label="Download Lab Manual (PDF)",
        data=open("lab_manual.pdf", "rb"),
        file_name="lab_manual.pdf",
        mime="application/pdf"
    )

def contact_me_page():
    st.title("Contact Me")
    with st.form("contact_form"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Your message has been sent!")

# Call the appropriate page function
if page == "Home":
    home_page()
elif page == "About Me":
    about_me_page()
elif page == "Video Links":
    video_links_page()
elif page == "Documents":
    documents_page()
elif page == "Contact Me":
    contact_me_page()
