import streamlit as st
import streamlit.components.v1 as components


# Background color and text color of a header/subheader
def subheader(url):
    # background-color:#a8def7;
    st.markdown(f'<p style="color:#000000;font-size:24px;font-family:Alegreya, serif '
                f';border-radius:2%;font-weight:bold;width:100%;">{url}</p>',
                unsafe_allow_html=True)


def site_title(name):
    components.html(f"""<div id="title" style='font-size:40px;padding-top:45px;padding-left:70px;color:#000000;
                            font-family:Alegreya, serif;'> <b>{name}</b> 
                         </div>
    """)


def change_header_kontakt(url):
    st.markdown(f'<p style="font-family:Alegreya, serif;font-size:30px;color: #000000;border-radius:2%;">{url}</p>',
                unsafe_allow_html=True)


# Use Local CSS File
def local_css(file_name):
    with open(file_name) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
