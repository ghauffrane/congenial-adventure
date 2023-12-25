from distutils import extension
from turtle import color
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_file_browser import st_file_browser


selected = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#e4dcf2", "color": "black"}, 
    }
)#edf2dc clear green

if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None
    
    
st.header('Default Options')
event = st_file_browser("/home/gofy/congenial-adventure", key='A')
st.write(event)