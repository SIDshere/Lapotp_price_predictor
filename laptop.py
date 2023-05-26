


import streamlit as st
import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('changed.csv')
st.title('Laptop Price Predictor')

model = pickle.load(open("lpd.pkl", "rb"))

st.markdown( "## All the fields are mandatory.")
st.subheader('Laptop Details:')

company = st.selectbox("Company", options=df["Brand"].unique())

def company_laptop(company):
    if company == "ASUS":
        return 2
    elif company == "Lenovo":
        return 8
    elif company == "HP":
        return 6
    elif company =="Primebook":
        return 11
    elif company =="DELL":
        return 4
    elif company =="MSI":
        return 10
    elif company =="acer":
        return 15
    elif company =="Infinix":
        return 7
    elif company =="realme":
        return 16
    elif company =="SAMSUNG":
        return 13
    elif company =="GIGABYTE":
        return 5
    elif company =="ALIENWARE":
        return 0
    elif company =="MICROSOFT":
        return 9
    elif company =="APPLE":
        return 1
    elif company =="RedmiBook":
        return 12
    elif company =="Vaio":
        return 14
    elif company =="Avita":
        return 3  



company_of_laptop = company_laptop(company)


processor_name = st.selectbox("Name of the Processor",options=df["p_brand"].unique())


def pro_name(processor_name):
    if processor_name == "Intel":
        return 1
    elif processor_name == "AMD":
        return 0
    elif processor_name == "MediaTek":
        return 2

name_of_the_processor = pro_name(processor_name)


processor_type = st.selectbox("Type of the Processor(CPU)",options=df["processor_type"].unique())


def pro_type(processor_type):
    if processor_type  == "i5":
        return 9
    elif processor_type == "i3":
        return 8
    elif processor_type == "MT":
        return 2
    elif processor_type == "i7":
        return 10
    elif processor_type == "Ryzen 5":
        return 5
    elif processor_type == "Ryzen 7":
        return 6
    elif processor_type == "i9":
        return 11
    elif processor_type == "Ryzen 3":
        return 4
    elif processor_type == "Celeron":
        return 1
    elif processor_type == "Ryzen 9":
        return 7
    elif processor_type == "Athlon":
        return 0
    elif processor_type == "Pentium":
        return 3
   
type_of_the_processor = pro_type(processor_type)

generation = st.number_input('Generation', step=1, min_value=2)

ram_in_gb = st.number_input('RAM in GB', step=4, min_value=4)

core_version = st.radio('Cores', options=[0, 2,3,4,5,7,9])
ratings = st.radio('Ratings', options=[4.1,4.4,4.2,4.3,3.9,4.0,4.5,3.8,4.8,5.0,4.7,4.6,4.9 ,3.7,3.6,3.0,2.8,3.5,1.0,1.7,1.6 ])
operating_system_type = st.selectbox("Operating System",options=df["OS"].unique())


def os_type(operating_system_type):
    if operating_system_type  == "Windows":
        return 6
    elif operating_system_type == "Prime":
        return 5
    elif operating_system_type == "Chrome":
        return 0
    elif operating_system_type == "DOS":
        return 1
    elif operating_system_type == "Linux":
        return 2
    elif operating_system_type == "Mac":
        return 3
    elif operating_system_type == "OS":
        return 4
    
type_of_os = os_type(operating_system_type)

diskdrive_type = st.selectbox("Disk Drive",options=df["disk_drive"].unique())


def disk_type(diskdrive_type):
    if diskdrive_type  == "SSD":
        return 3
    elif diskdrive_type == "Not available":
        return 2
    elif diskdrive_type  == "Both":
        return 0
    elif diskdrive_type  == "HDD":
        return 1
type_of_diskdrive = disk_type(diskdrive_type)

size_in_inches = st.selectbox('Size of the laptop in Inches', options=df["display"].unique())

graphic_card = st.radio("Graphic Card (0-No,1-Yes)", options=[0, 1])
touchscreen  = st.radio("Touchscreen (0-No,1-Yes)", options=[0, 1])

features=[ratings,ram_in_gb,core_version,generation,company_of_laptop,size_in_inches,type_of_diskdrive,name_of_the_processor,type_of_the_processor,type_of_os,graphic_card,touchscreen]
final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(final_features)
    st.balloons()
    #st.success(f'Your predicted price of the laptop is {round(prediction[0],3)}')
    st.success(f'Your predicted price of the laptop is {prediction[0]}')


