# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 08:37:48 2023

Streamlit app for CTR

@author: AXF162
Allan Fong
allan.fong@medstar.net
"""
import streamlit as st
import pandas as pd
import numpy as np

ectr_points = 0
octr_points = 0

ectr_cat_points = 0
octr_cat_points = 0


def main():
    st.set_page_config(layout="wide",
                      page_title="CNHC Carpal Tunnel Decision Analysis Tool"
    )
    
    # ---- Custom Styling ----
    st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: Arial, Helvetica, sans-serif;
    }

    /* Slider color */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background-color: navy !important;
    }

    .stSlider [data-baseweb="slider"] > div > div {
        background-color: navy !important;
    }

    /* Header styling */
    .main-title {
        text-align: center;
        color: navy;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .sub-title {
        text-align: center;
        color: #333333;
        font-size: 1.3rem;
        margin-top: 0;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---- Logo ----
    col1, col2 = st.columns([1, 5])

    with col1:
        st.image("cnhc_logo.png", width=140)

    with col2:
        st.markdown(
            """
            <div class="main-title">
            Curtis National Hand Center Carpal Tunnel Decision Analysis Tool
            </div>
            <div class="sub-title">
            Open versus Endoscopic Carpal Tunnel Release
            </div>
            """,
            unsafe_allow_html=True
        )


                       
    st.write('Select Feature Weights (0 is not important, 5 is most important - on sliding scale)')

    w_cost = st.slider('Lower cost paid by insurance:', 0, 5, 1)
    w_pp = st.slider('Lower cost paid by patient:', 0, 5, 2)

    w_inf = st.slider('Decrease infection risk:', 0, 5, 2)
    w_tni = st.slider('Avoid non-permanent nerve injury (temporary numbness/tingling or strength decrease after surgery that improves on its own usually in 1-3 months):', 0, 5, 1)
    #w_tni = st.slider('Transient nerve injury:', 0, 5, 1)

    w_pni = st.slider('Avoid permanent nerve injury (permanent numbness/tingling or strength decrease – may require additional surgery or may never improve):', 0, 5, 3)
    #w_pni = st.slider('Permanent nerve injury :', 0, 5, 3)
    w_rr = st.slider('Avoid carpal tunnel syndrome coming back (may require additional surgery):', 0, 5, 3)
    #w_rr = st.slider('Recurrence rate:', 0, 5, 3)

    w_pain = st.slider('Minimize pain affecting your daily life for first 2 weeks after surgery:', 0, 5, 1)
    #w_pain = st.slider('Pain inference:', 0, 5, 1)
    w_uex = st.slider('Maximize hand and arm function for first 2 weeks after surgery:', 0, 5, 1)
    #w_uex = st.slider('UEX:', 0, 5, 1)
    w_vas = st.slider('Less overall pain for first 2 weeks after surgery :', 0, 5, 2)
    #w_vas = st.slider('VAS:', 0, 5, 2)

    ectr_points = w_cost*1 + w_pp*1 + w_inf*2 + w_tni*1 + w_pni*2 + w_rr*1 + w_pain*1 + w_uex*2 + w_vas*2
    octr_points = w_cost*2 + w_pp*2 + w_inf*1 + w_tni*2 + w_pni*1 + w_rr*2 + w_pain*2 + w_uex*1 + w_vas*1
    # Calculate 
    if ectr_points>octr_points:
        st.write('Based on your responses, the preferred procedure for you is: ENDOSCOPIC carpal tunnel release')
        #st.write('ECTR is a better choice by ' + str(ectr_points-octr_points) + ' points')
    elif octr_points>ectr_points:
        st.write('Based on your responses, the preferred procedure for you is: OPEN carpal tunnel release')
        #st.write('OCTR is a better choice by ' + str(octr_points-ectr_points) + ' points')
    else:
        st.write('Based on your responses, ENDOSCOPIC and OPEN are equally preferred')
        #st.write('ECTR and OCTR are the same')
        
    #### Remove second iteration to simplify (6/19/26)
    #st.write('***')
    #st.write('Select Category Weights (0 is not important, 5 is most important)')
    #wc_cost = st.slider('Cost:', 0, 5, 1)
    #wc_stc = st.slider('Short term complication:', 0, 5, 2)
    #wc_ltc = st.slider('Long term complication:', 0, 5, 2)
    #wc_stp = st.slider('Short term PRO:', 0, 5, 2)
    #ectr_cat_points = wc_cost*1 + wc_stc*2 + wc_ltc*2 + wc_stp*4
    #octr_cat_points = wc_cost*3 + wc_stc*2 + wc_ltc*2 + wc_stp*1
    #if ectr_cat_points>octr_cat_points:
    #    st.write('ECTR is a better choice by ' + str(ectr_cat_points-octr_cat_points) + ' points')
    #elif octr_cat_points>ectr_cat_points:
    #    st.write('OCTR is a better choice by ' + str(octr_cat_points-ectr_cat_points) + ' points')
    #else:
    #    st.write('ECTR and OCTR are the same')

if __name__ == "__main__":
    main()
