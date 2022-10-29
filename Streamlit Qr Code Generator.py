import streamlit as st
import numpy as np
import os

import qrcode
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=14)

from PIL import Image

def load_image(img):
    im = Image.open(img)
    return im

def main():
    menu = ["Home","DecodeQR","About"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

        with st.form(key='myqr_form'):
            raw_text = st.text_area("Text Here")
            submit_button = st.form_submit_button("Generate")

        If submit_button:

            col1,col2 =  st.beta_columns(2)

            with col1:
                qr.add_data(raw_text)

                qr.make(fit=True)
                img = qr.make_image(fill_color='black',back_color='white')

                img_filename = 'generate_image_{}.png'
                path_for_images = os.path.join('image_folder',img_filename)
                img.save(path_for_images)

                final_img = load_image(path_for_images)
                st.image(final_img)

            with col2:
                st.info("Orininal Text")
                st.write(raw_text)

    elif choice == "DecodeQR":
        st.subheader("Decode QR")

    else:
        st.subheader("About")

if __name__ == '__main__'
    main()
