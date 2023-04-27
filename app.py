import pickle
import sys
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pkg_resources import cleanup_resources
 
# loading the trained model
pickle_in = open('model.pkl', 'rb') 
classifier = pickle.load(pickle_in)



@st.cache_data
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Temperature, Humidity, TVOC, eCO2, RawH2, RawEthanol, Pressure, PM1, PM2, NC0, NC1, NC2):   

    data = {
    'Temperature[C]':[Temperature],
    'Humidity[%]':[Humidity],
    'TVOC[ppb]':[TVOC],
    'eCO2[ppm]':[eCO2],
    'Raw H2':[RawH2],
    'Raw Ethanol':[RawEthanol],
    'Pressure[hPa]':[Pressure],
    'PM1.0':[PM1],
    'PM2.5':[PM2],
    'NC0.5':[NC0],
    'NC1.0':[NC1],
    'NC2.5':[NC2]
} 
    data = pd.DataFrame(data)
    data = pd.DataFrame(StandardScaler().fit_transform(data),columns = data.columns)    
 
    # Making predictions 
    prediction = classifier.predict(data)
     
    if prediction == 0:
        pred = 'Not Active'
    else:
        pred = 'Active'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit IoT Smoke Detection ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Temperature = st.number_input("Temperature[C]") 
    Humidity = st.number_input("Humidity[%]") 
    TVOC = st.number_input("TVOC[ppb]")
    eCO2 = st.number_input("eCO2[ppm]")
    RawH2 = st.number_input("Raw H2")
    RawEthanol = st.number_input("Raw Ethanol")
    Pressure = st.number_input("Pressure[hPa]")
    PM1 = st.number_input("PM1.0")
    PM2 = st.number_input("PM2.5")
    NC0 = st.number_input("NC0.5")
    NC1 = st.number_input("NC1.0")
    NC2 = st.number_input("NC2.5")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Temperature, Humidity, TVOC, eCO2, RawH2, RawEthanol, Pressure, PM1, PM2, NC0, NC1, NC2) 
        st.success('Alarm is {}'.format(result))
        print('Temperature[C]', Temperature)
        print('Humidity[%]', Humidity)
        print('TVOC[ppb]', TVOC)
        print('eCO2[ppm]', eCO2)
        print('Raw H2', RawH2)
        print('Raw Ethanol', RawEthanol)
        print('Pressure[hPa]', Pressure)
        print('PM1.0', PM1)
        print('PM2.5', PM2)
        print('NC0.5', NC0)
        print('NC1.0', NC1)
        print('NC2.5', NC2)
        print('Prediction: Alarm is ',result)
     
if __name__=='__main__': 
    try:
        main()
    except KeyboardInterrupt:
        cleanup_resources()
        sys.exit(0)