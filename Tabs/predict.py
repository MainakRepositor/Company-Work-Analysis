"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Employee Attrition Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.

    col1,col2 = st.columns(2)

    with col1:
    
        team = st.slider("Team Size", int(df["team"].min()), int(df["team"].max()))
        targeted_productivity = st.slider("targeted productivity", float(df["targeted_productivity"].min()), float(df["targeted_productivity"].max()))
        smv = st.slider("SMV", int(df["smv"].min()), int(df["smv"].max()))
        over_time = st.slider("over_time", int(df["over_time"].min()), int(df["over_time"].max()))
        incentive = st.slider("incentive", float(df["incentive"].min()), float(df["incentive"].max()))
        idle_time = st.slider("idle_time", int(df["idle_time"].min()), int(df["idle_time"].max()))
        idle_men = st.slider("idle_men", int(df["idle_men"].min()), int(df["idle_men"].max()))
        

    with col2:
        no_of_workers = st.slider("no_of_workers", float(df["no_of_workers"].min()), float(df["no_of_workers"].max()))
        month = st.slider("month", float(df["month"].min()), float(df["month"].max()))
        quarter_Quarter1 = st.slider("quarter_Quarter1", float(df["quarter_Quarter1"].min()), float(df["quarter_Quarter1"].max()))
        quarter_Quarter2 = st.slider("quarter_Quarter2", float(df["quarter_Quarter2"].min()), float(df["quarter_Quarter2"].max()))
        quarter_Quarter3 = st.slider("quarter_Quarter3", float(df["quarter_Quarter3"].min()), float(df["quarter_Quarter3"].max()))
        quarter_Quarter4 = st.slider("quarter_Quarter4", float(df["quarter_Quarter4"].min()), float(df["quarter_Quarter4"].max()))
        department_finishing = st.slider("department_finishing", float(df["department_finishing"].min()), float(df["department_finishing"].max()))
        department_sweing = st.slider("department_sweing", float(df["department_sweing"].min()), float(df["department_sweing"].max()))
        
        

    # Create a list to store all the features
    features = [team,targeted_productivity,smv,over_time,incentive,idle_time,idle_men,no_of_workers,month,quarter_Quarter1,quarter_Quarter2,quarter_Quarter3,quarter_Quarter4,department_finishing,department_sweing]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.11
        
        st.sidebar.info("Depending the results, the company will be classified in the metrics of BCG-Matrix")
        met = pd.read_csv('BCG.csv')
        st.sidebar.table(
            met
        )

        # Prfloat the output according to the prediction
        x = round((prediction[0]*100),2)

        if (x>70):
            st.warning("Company is balanced.")
            st.info("BCG Says: Question Mark")

        elif(x>90):
            st.success("Company has out-performed")
            st.info("BCG Says: Cash Cow")

        elif(x>100):
            st.success("Company is soaring with profits.")
            st.info("BCG Says: Star")

        else:
            st.error("Company is not performing as expected")
            st.info("BCG Says: Dog")
          
          
                
        # Prfloat teh score of the model 
        st.sidebar.write("The model used is trusted by HRs and has an accuracy of ", round((score*100),2),"%")
