import streamlit as st
from PIL import Image
import bg_image
import common_functions

logo = Image.open(r'logo_edc.png')
picture = Image.open(r'elin.png')
title_img = Image.open(r'bck_img.png')

st.set_page_config(
    page_title="Språkvask og Korrektur",
    page_icon=":book:",
    layout="wide",
)

st.markdown("""
  <style>
      MainMenu, header, footer {visibility: hidden}
      footer::after {
        content: '©CMN-💞2022';
        visibility: visible;
        display: block;
        padding-bottom: 1px;
        top: 0px;
        text-align: center;
        font-size: 16px;
        color: #000000;
        width: 100%;
        font-family: Alegreya, serif;
      }
  </style>
  """, unsafe_allow_html=True)

# Use a background image
bg_image.set_png_as_page_bg('light-blue.png')

tab_titles_nyNorsk = ["Hovudside", "Om meg", "Kontakt"]
tab_titles_bokmaal = ["Hovedside", "Om meg", "Kontakt"]

col1, col2 = st.columns([0.15, 1.1])


with col1:
    choose_language = st.radio("vel/velg språk:", ('Nynorsk', 'Bokmål'), horizontal=False, index=0)
    with open("style/style_col1.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with col2:
    st.image(title_img, use_column_width='auto', output_format='auto')
    common_functions.site_title("Språkvask og Korrektur")

    # ----------------- BOKMÅL -----------------------

    if choose_language == 'Bokmål':
        tabs = st.tabs(tab_titles_bokmaal)
        with open("style/style_col2.css") as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        # Hovedside
        with tabs[0]:
            st.write('#')
            common_functions.subheader('Norsk – begge målformer 📖')
            st.markdown(
                '<p class="font"style="font-family:Alegreya, serif;font-size:21px;color: #000000"">Jeg tar oppdrag '
                'både på bokmål og nynorsk.</p>', unsafe_allow_html=True)
            st.write('#')
            common_functions.subheader("Teksttyper 📚")
            st.markdown("""
                    <style
                        type="text/css">
                        li { color: #000000;}
                        ul { list-style-type: '✽'; }
                    </style>
                    <ul>
                        <li>
                            <p class="font"style="font-family:Alegreya, serif;font-size:21px;color:  #000000">
                                Artikler (alle lengder) – både vitenskaplige og annet</p>
                        </li>
                        <li>
                            <p class="font"style="font-family:Alegreya, serif;font-size:21px;color:  #000000">
                                Masteroppgaver</p>
                        </li>
                        <li>
                            <p class="font"style="font-family:Alegreya, serif;font-size:21px;color:  #000000">
                                Doktorgradsavhandlinger</p>
                        </li>
                        <li>
                            <p class="font"style="font-family:Alegreya, serif;font-size:21px;color:  #000000">
                                Bøker</p>
                        </li>
                        <li>
                            <p class="font"style="font-family:Alegreya, serif;font-size:21px;color:  #000000">
                                Andre tekster</p>
                        </li>
                    </ul>
                """, unsafe_allow_html=True)
        # Om meg
        with tabs[1]:
            # st.write('#')
            st.text('')
            st.markdown(""" <style> .fontMegName {font-size:30px ; font-family: 'Alegreya, serif'; color: #000000;} 
                                                         </style> """, unsafe_allow_html=True)
            st.markdown('<p class="fontMegName">Elin D. Chelighem</p>', unsafe_allow_html=True)
            st.text('')
            st.image(picture, width=250)
            st.markdown(""" <style> .fontMeg {position: absolute; font-size:21px; font-family: 'Alegreya, serif';
                                color: #000000; margin-top: 255px;} 
                            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="fontMeg">Norsklærer med lidenskap for godt, tydelig og korrekt språk.</p>',
                        unsafe_allow_html=True)
            st.markdown(""" <style> .fontMeg1 {position: absolute; font-size:21px; font-family: 'Alegreya, serif';
                                color: #000000; margin-top: 265px;} 
                                        </style> """, unsafe_allow_html=True)
            st.text('')
            st.markdown('<p class="fontMeg1">Har språkvasket akademiske tekster siden 2005.</p>',
                        unsafe_allow_html=True)
            st.write('#')
            st.write('#')
            st.write('#')
            st.write('#')

        # Kontakt
        with tabs[2]:
            st.write('#')
            st.markdown('<p style="font-family:Alegreya, serif;font-size:21px;color: #000000">'
                        'Trenger du språkvask eller korrektur?</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family:Alegreya, serif;font-size:21px;color: #000000">'
                        'Send en e-post, så sender jeg et kostnadsoverslag.</p>', unsafe_allow_html=True)
            st.markdown('<hr style="height:2px;width:59%;border-width:10;color:blue;background-color:#69b1e3">',
                        unsafe_allow_html=True)
            common_functions.change_header_kontakt("Kontakt meg! 👉 📬 ")
            st.write('#')
            st.write('#')
            contact_form = """
            <form id="myForm" action = "https://formsubmit.co/c9ceb87d17a7a5425aa1f0ca1cb9b200"
                  method="POST" enctype="multipart/form-data">
                <input type="hidden" name="_captcha" value="true">
                <input type="text" name="Navn" placeholder="Fullt navn" required>
                <input type="email" name="E-post" placeholder="Din e-postadresse" required>
                <textarea name="Melding" placeholder="Din melding" required></textarea>
                <input type="hidden" name="_template" value="table">
                <label id="labelUpload" for="input"> Klikk eller slipp en fil for opplasting <input id="upload"
                    type="file" id="images" name="Attachment" accept=".png,.jpeg,.jpg,.doc,.docx,application/msword,
                          application/vnd.openxmlformats-officedocument.wordprocessingml.document,.pdf" placeholder="">
                </label>
                <button type="submit" value="Submit" id="sendButton" class="block btn-flip" data-back="Takk" 
                    data-front="Send">
                </button> 
            </form>
               """
            st.markdown(contact_form, unsafe_allow_html=True)

            common_functions.local_css("style/style.css")

    # ----------------- NYNORSK -----------------------

    else:
        tabs = st.tabs(tab_titles_nyNorsk)
        with open("style/style_col2.css") as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        # Hovudside
        with tabs[0]:
            st.write('#')
            common_functions.subheader('Norsk – begge målformer 📖')
            st.markdown(
                '<p class="font"style="font-family:Alegreya, serif;font-size:21px;color: #000000">Eg tek oppdrag både '
                'på bokmål og nynorsk.</p>', unsafe_allow_html=True)
            st.write('#')
            common_functions.subheader("Teksttypar 📚")
            st.markdown("""
                <style type="text/css">
                    li {color:#000000}
                    ul {list-style-type: '✽'}
                </style>
                <ul>
                    <li><p class="font"style="font-family:Alegreya, serif;font-size:21px;color: #000000">
                            Artiklar (alle lengder) – både vitskaplege og anna
                        </p>
                    </li>
                    <li><p class="font"style="font-family:Alegreya, serif;font-size:21px;color:#000000">
                            Masteroppgåver
                        </p>
                    </li>
                    <li><p class="font"style="font-family:Alegreya, serif;font-size:21px;color:#000000">
                            Doktorgradsavhandlingar
                        </p>
                    </li>
                    <li><p class="font"style="font-family:Alegreya, serif;font-size:21px;color:#000000">
                            Bøker
                        </p>
                    </li>
                    <li><p class="font"style="font-family:Alegreya, serif;font-size:21px;color:#000000">
                            Andre tekstar
                        </p>
                    </li>
                </ul>
            """, unsafe_allow_html=True)
        # Om meg
        with tabs[1]:
            st.write('#')
            st.markdown(""" <style> .fontMegName {font-size:30px ; font-family: 'Alegreya, serif'; color: #000000;} 
                                             </style> """, unsafe_allow_html=True)
            st.markdown('<p class="fontMegName">Elin D. Chelighem</p>', unsafe_allow_html=True)
            st.text('')
            st.image(picture, width=250)

            st.markdown(""" <style> .fontMeg {position: absolute; font-size:21px; font-family: 'Alegreya, serif';
                                            color: #000000; margin-top: 255px;} 
                                        </style> """, unsafe_allow_html=True)
            st.markdown('<p class="fontMeg">Norsklærar med lidenskap for godt, tydeleg og korrekt språk.</p>',
                        unsafe_allow_html=True)
            st.markdown(""" <style> .fontMeg1 {position: absolute; font-size:21px; font-family: 'Alegreya, serif';
                                            color: #000000; margin-top: 265px;} 
                                                    </style> """, unsafe_allow_html=True)
            st.text('')
            st.markdown('<p class="fontMeg1">Har språkvaska akademiske tekstar sidan 2005.</p>',
                        unsafe_allow_html=True)
            st.write('#')
            st.write('#')
            st.write('#')
            st.write('#')
        # Kontakt
        with tabs[2]:
            st.write('#')
            st.markdown('<p style="font-family:Alegreya, serif;font-size:21px;color: #000000">'
                        'Treng du språkvask eller korrektur?</p>', unsafe_allow_html=True)
            st.markdown('<p style="font-family:Alegreya, serif;font-size:21px;color: #000000">'
                        'Send ein e-post, så sender eg eit kostnadsoverslag.</p>', unsafe_allow_html=True)
            st.markdown('<hr style="height:2px;width:59%;border-width:10;color:blue;background-color:#69b1e3">',
                        unsafe_allow_html=True)
            common_functions.change_header_kontakt("Kontakt meg! 👉 📬 ")
            st.write('#')
            st.write('#')

            contact_form = """
                        <form id="myForm" action = "https://formsubmit.co/c9ceb87d17a7a5425aa1f0ca1cb9b200"
             method="POST" enctype="multipart/form-data"> <input type="hidden" name="_captcha" value="true"> <input
             type="text" name="Navn" placeholder="Fullt namn" required> <input type="email" name="E-post"
             placeholder="Di e-postadresse" required> <textarea name="Melding" placeholder="Di melding"
             required></textarea><input type="hidden" name="_template" value="table">
             <label id="labelUpload" for="input"> Klikk eller slepp ei fil for opplasting <input id="upload" type="file"
              id="images" name="Attachment" accept=".png,.jpeg,.jpg,.doc,.docx,application/msword,
              application/vnd.openxmlformats-officedocument.wordprocessingml.document,.pdf" placeholder="">
             </label>
             <button type="submit" value="Submit" id="sendButton" class="block btn-flip" data-back="Takk" 
                    data-front="Send">
             </button>  </form>
             """
            st.markdown(contact_form, unsafe_allow_html=True)

            common_functions.local_css("style/style.css")

# setting footer
st.markdown("""
  <style>
      MainMenu, header, footer {visibility: hidden}
      footer::after {
        content: '©CMN-💞2022';
        visibility: visible;
        display: block;
        padding-bottom: 1px;
        top: 0px;
        text-align: center;
        font-size: 16px;
        color: #000000;
        width: 100%;
        font-family: Alegreya, serif;
      }
  </style>
  """, unsafe_allow_html=True)
