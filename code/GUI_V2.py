# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:27:39 2022

@author: Subrat Kishore Dutta
"""

import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from obj2html import obj2html
import pyvista as pv
import pandas as pd
from pyvista import examples
import time

st.set_page_config(layout="wide")

filename = examples.planefile
reader = pv.get_reader(filename)
html_string = obj2html('data.obj', html_elements_only=False)
pv.set_jupyter_backend('pythreejs')
plotter = pv.Plotter(
        border=False,
        window_size=[500,400]) 
plotter.background_color = "black"
mesh = reader.read()
plotter.add_mesh(mesh,color="grey")
model_html = "model.html"
other = plotter.export_html(model_html, backend='pythreejs')

with open(model_html,'r') as file: 
    model_obj = file.read() #reading the 3d mesh object



#functions
    
    
##  given a dummy function for the simulation which takes in all the parameters and can be used for calculations
    
def simulate(model,sheet_width,sheet_length,sheet_material,sheet_density,x_offset,y_offset,precision):
    print(model,sheet_width,sheet_length,sheet_material,sheet_density,x_offset,y_offset,precision)
    time.sleep(2)

#defining the font types
    
    ## this font is used for the paragraphs for example the section describing the project
st.markdown("""
                    <style>
                    .paragraph-font {
                            font-size:10px !important;            
                            }
                    </style>
                    """, unsafe_allow_html=True)
    
    ## this font is used for the name and single standing texts
st.markdown("""
                    <style>
                    .name-font {
                            font-size:15px !important;
                            }
                    </style>
                    """, unsafe_allow_html=True)

# sidebar contains information about the project the team for the project and can hold other information about the project
with st.sidebar:
    with st.expander('Project Quasim'):
        st.image('logo.png')       
        st.markdown('<p class="paragraph-font">The <a href="https://www.quasim-project.de/">Project Quasim</a> investigates how advantages can be developed for applications in the manufacturing industry using quantum computers (QC) in the medium and long term. The manufacturing industry is one of the central German economic sectors and at the same time requires the fulfillment of the highest quality standards in order to be competitive worldwide.</p>', unsafe_allow_html=True)
    
    with st.expander('Team'):
        st.image('name1.jpg',width=100)
        st.markdown('<p class="name-font">Superman</p>', unsafe_allow_html=True)
        P1P1,P1P2,P1P3,P1P4,P1P5,P1P6 = st.columns(6) #variable nameing convention: Person N profile N
        P1P1.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/linkedin-circled--v1.png>)](<https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py>)")
        P1P2.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/github.png>)](<https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py>)")
        P1P3.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/behance.png>)](<https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py>)")
        P1P4.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/gmail.png>)](<mailto:dummydummy4@gmail.com>)")
        
        st.image('name2.jpg',width=100)
        st.markdown('<p class="name-font" style=“text-decoration: none;” >Spider Man</p>', unsafe_allow_html=True)
        P2P1,P2P2,P2P3,P2P4,P2P5,P2P6 = st.columns(6)
        P2P1.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/linkedin-circled--v1.png>)](<https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py>)")
        P2P2.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/github.png>)](<https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py>)")
        P2P3.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/behance.png>)](<https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py>)")
        P2P4.markdown("[![Title](<https://img.icons8.com/ios-glyphs/30/000000/gmail.png>)](<mailto:dummydummy@gmail.com>)")
    with st.expander('Join Us'):
        st.markdown('<p class="name-font">name_1@dfki.de</p>', unsafe_allow_html=True)


# the following two columns holds the body of the system
col1,col2=st.columns((4.2, 1.4),gap="large")

## column1 has all the panels that shows the results obtained after simulation. it holds the 3d mesh surface to be shown, the plots, the simulation video that is been created and also the comparison table
with col1:
    st.subheader("Project Quasim")
    tab1, tab2 = st.tabs(["3D model", "plots"])
    
    with tab1:
        with st.expander("Model"):
            panel1_1=st.empty()  # this panel forms the first row of panels and occurs on the first tab hence the variable name panel1_1 following the naming convention panelN_M (N=row,M=tab)
            panel1_1.image('logo.png')
            
    with tab2:
        panel1_2=st.empty()
        panel1_2.write('not available')
    
    tab3, tab4 = st.tabs(["Thermal Sim", "Performance Measure"])
    with tab3:
        panel2_1=st.empty()
        panel2_1.write('not available')
    with tab4:
        panel2_2=st.empty()
        panel2_2.write('not available')

## columns2 is the control panel for the simulation. it takes in all the inputs from selecting models to selecting sheet properties for the simulation.
with col2:
    
    model = st.selectbox('dummy',("Select Model","FEM","MGN","GCN",'Hy GCN'),label_visibility="hidden")

    
    with st.expander("Sheet"):
        sheet_width = st.number_input('Sheet Width')
        sheet_length = st.number_input('Sheet Length')
        sheet_material = st.selectbox('Sheet Material',("Aluminium","Steel","Stainless Steel"))
        sheet_density = st.number_input('Sheet Density')
        
        
    with st.expander("Configuration"):
        x_offset = st.number_input('x offset')
        y_offset = st.number_input('y offset')
    
    with st.expander("Prediction"):
        precision = st.slider('precision', 0, 100, 10)
    if st.button('Submit'):## this bottom will the start the actual simulation on the final integrated system
        with st.spinner(''):
            simulate(model,sheet_width,sheet_length,sheet_material,sheet_density,x_offset,y_offset,precision)
            with panel1_1.container():
                st.components.v1.html(model_obj,height=400)
            panel1_2.image('plot.png')
            panel2_1.video('video1.mp4')
            
            df = pd.DataFrame(
            np.random.randn(4, 3),
            columns=('model','run time','accuracy')) ## dummy data for the table
            panel2_2.table(df)
        
    if st.button('Reset'): # hitting this will clear out all the panels but will keep the parameters fixed as it is
        panel1_1.image('logo.png')
        panel1_2.write('not available')
        panel2_1.write('not available')
        panel2_2.write('not available')