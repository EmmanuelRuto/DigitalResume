from pathlib import Path

import streamlit as st
from PIL import Image


# Path settings
current_dir = Path.cwd()
css_file = current_dir /"styles" / "main.css"
resume_file  = current_dir /"assets" /"Resume.pdf"
profile_pic = current_dir /"assets" / "IMG_9380.jpg"


# General Settings


PAGE_TITLE = "Resume | Emmanuel Ruto"
PAGE_ICON = "random"
NAME = "Emmanuel Ruto"
DESCRIPTION = """
Student ITS Consultant,     REGIONAL MUNICIPALITY OF WATERLOO
"""
EMAIL = "1emmanuelruto@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/emmanuel-ruto/",
    "Instagram": "https://www.instagram.com/manu.ruto/",
    "Twitter": "https://twitter.com/red_cave0",
}    


st.set_page_config(page_title = PAGE_TITLE,page_icon = PAGE_ICON)

st.title("Hey,")


#Load CSS,PDF and Profile Picture
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html = True)

with open(resume_file,"rb") as pdf_file:
    PDFFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# Hero section

col1, col2 = st.columns(2,gap = "small")
with col1:
    st.image(profile_pic,width =200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " 📄 Download Resume",
        data = PDFFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",

    )
    st.write("📭",EMAIL)




# Add social media links

st.write("#")

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")




st.write("#")
st.subheader("Experience and  Qualifications")
st.write(
    """
- ✔ Experience with fixing computers
- ✔ Processing mail using an electrinic tracking system 
- ✔ Experience in a warehouse environment.
    """
)




# Skills
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👨🏾‍💻  Programming: Python , VBA
-  📊 Data Visualization : MS Excel
- 🫙  Databases: Ms Access
    """
)
# Add work history

st.write("#")
st.write ("💻, Student ITS Consultant  | Regional Municipality Of Waterloo")
st.write("Jun.2023 - Present")
st.write(
    """
- ✔ Assisted with computer replacement, asset tracking and recording and installation of computers
- ✔ Updated and terminated users from the active directory
- ✔ Handled service request tickets effectively
    """
)

st.write("#")
st.write("📨, Mail and Distribution Support Assistant  |  Wilfrid Laurier University")
st.write("May.2023  - Jun.2023")
st.write(
    """
- ✔ Assisted with direct mailings, stuffing and sealing envelopes and labelling parcels
- ✔ Helped with sorting incoming and outgoing mail
- ✔ Scanned and processed materials in the electronic tracking system

    """
)

st.write("#")
st.write("🏭, Warehouse Associate    | Mondelez International")
st.write("Apr.2022 - Aug.2022")
st.write(
    """
- ✔ Organized products in warehouses in a timely manner, found and stored items in their correct places
- ✔ Packed products efficiently to improve delivery time and product flow across teams, showing initiative
- ✔ Ensured that the inventory was efficiently managed and well-maintained by following proper procedures

    """
)


