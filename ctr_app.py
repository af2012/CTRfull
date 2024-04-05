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
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

path = 'C:/Users/axf162/MedStar Health/MHRI-Human Factors - Personal Files/Allan Fong/CODE/PYTHON_SCRIPTS/1_EHR/Curtis_Hand/'

#data = pd.read_excel(path+'CTR_RESULTS_02.xlsx', sheet_name='features')

ectr_points = 0
octr_points = 0

ectr_cat_points = 0
octr_cat_points = 0


def main():
    st.set_page_config(layout="wide")
    st.write('Select Feature Weights (0 is not important, 5 is most important)')

    w_cost = st.slider('Total cost:', 0, 5, 1)
    w_pp = st.slider('Patient out of pocket:', 0, 5, 2)

    w_inf = st.slider('Infection:', 0, 5, 2)
    w_tni = st.slider('Transient nerve injury:', 0, 5, 1)

    w_pni = st.slider('Permanent nerve injury :', 0, 5, 3)
    w_rr = st.slider('Recurrence rate:', 0, 5, 3)

    w_pain = st.slider('Pain inference:', 0, 5, 1)
    w_uex = st.slider('UEX:', 0, 5, 1)
    w_vas = st.slider('VAS:', 0, 5, 2)
    
    ectr_points = w_cost*1 + w_pp*1 + w_inf*2 + w_tni*1 + w_pni*2 + w_rr*1 + w_pain*2 + w_uex*2 + w_vas*2
    octr_points = w_cost*2 + w_pp*2 + w_inf*1 + w_tni*2 + w_pni*1 + w_rr*2 + w_pain*1 + w_uex*1 + w_vas*1
    # Calculate 
    if ectr_points>octr_points:
        st.write('ECTR is a better choice by ' + str(ectr_points-octr_points) + ' points')
    elif octr_points>ectr_points:
        st.write('OCTR is a better choice by ' + str(octr_points-ectr_points) + ' points')
    else:
        st.write('ECTR and OCTR are the same')
        

    st.write('***')
    st.write('Select Category Weights (0 is not important, 5 is most important)')

    wc_cost = st.slider('Cost:', 0, 5, 1)
    wc_stc = st.slider('Short term complication:', 0, 5, 2)
    wc_ltc = st.slider('Long term complication:', 0, 5, 2)
    wc_stp = st.slider('Short term PRO:', 0, 5, 2)
    
    ectr_cat_points = wc_cost*1 + wc_stc*2 + wc_ltc*2 + wc_stp*4
    octr_cat_points = wc_cost*3 + wc_stc*2 + wc_ltc*2 + wc_stp*1
    if ectr_cat_points>octr_cat_points:
        st.write('ECTR is a better choice by ' + str(ectr_cat_points-octr_cat_points) + ' points')
    elif octr_cat_points>ectr_cat_points:
        st.write('OCTR is a better choice by ' + str(octr_cat_points-ectr_cat_points) + ' points')
    else:
        st.write('ECTR and OCTR are the same')

if __name__ == "__main__":
    main()
