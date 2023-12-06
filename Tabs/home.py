"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Company Work Analysis System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Analyzing company work involves assessing operations, productivity, and employee performance to optimize efficiency and outcomes. It encompasses evaluating workflows, identifying bottlenecks, and utilizing data-driven insights to streamline processes. This analysis aids in resource allocation, goal setting, and fostering a conducive work environment, ultimately enhancing the company's competitive edge and fostering growth.
        </p>
    """, unsafe_allow_html=True)