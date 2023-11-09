import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/f710d6ae-0889-4a98-83e1-e78955a40ae9/9OXL10TIFG.json")
lottie_contact = load_lottieurl("https://lottie.host/aa077b30-8f74-4984-ba62-00baa7aca08e/iGuyb5fKYx.json")
image = Image.open("hello.png")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

st.write("##")
st.subheader("Hey Guys :wave:")
st.title("My Portfolio Website")
st.write("""
Hello and thank you for visiting! I'm excited to introduce you to my portfolio,\n
where I showcase my skills and passion for web development and cybersecurity.

""")

st.write("[Read More](https://instagram.com/iqlip7)")

st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Projects','Contact'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation= "horizontal"
    )

if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Hey, I am Iqlip A.K.A Shubham")
            st.title("Undergrad at PIET")
        with col2:
            st.lottie(lottie_coder)
    st.write("---")

    with st.container():
        col3 , col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
            - PIET
                - Bachelor of Computer Application
            - Mt.olivet
                - Commerce
                - Grade : 82%
            - GSBV
                - Xth
                - Grade: 72%
            """)
        with col4:
            st.subheader("""
            Skills
            - HTML
            - CSS
            - Javascript
            - Mysql
            - Python
            - C
            - Bash
            - Networking
            - Linux (Kali/Ubuntu/Parrot)
            - Git/Github
            """)

if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5,col6 = st.columns({1,2})
        with col5:
            st.image(image)
        with col6:
            st.write("##")
            st.write("##")
            st.subheader("Automated Linux Hardening GUI Tool")
            st.write("""
            In today's digital landscape, cybersecurity is of paramount importance.\n 
            Protecting your Linux-based systems from potential threats and vulnerabilities is a critical task.\n
            To simplify and streamline the process of fortifying your Linux environment,\n
            we present the Linux Hardening GUI Tool—a user-friendly,\n 
            automated solution for enhancing the security of your Linux systems.
            """)
            st.markdown("[Visit Github](https://github.com/iqlipx)")

if selected == "Contact":
    st.header(":mailbox: Get in touch!")
    st.write("##")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/demohtb07@gmail.com" method="POST">
     <input type="hidden" name="_next" value="https://yourdomain.co/thanks.html">
     <input type="text" name="name" required placeholder="Enter your name">
     <input type="email" name="email" required placeholder="Enter your email">
    <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
     </form>
    """
    left_col , right_col = st.columns({2,1})
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact,height=350)
        local_css("styles.css")
