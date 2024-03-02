# Install necessary libraries
!pip install streamlit pyngrok pycaret

# Set the authtoken for ngrok
!ngrok authtoken 2d7AMT8kfUEQvnYoQ2poJrut9uD_6mMEDjgwvyFxQHXKfJRmy


# Write your Streamlit app code in a file named app.py
import streamlit as st
import pandas as pd
from pycaret.classification import *

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to perform exploratory data analysis
def perform_eda(data):
    # Conduct exploratory data analysis
    pass

# Function to train machine learning model
def train_model(data, target_variable, model_type='auto'):
    setup(data, target=target_variable, silent=True)
    best_model = compare_models()
    return best_model

def main():
    st.title('Machine Learning Web App')

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:
        data = load_data(uploaded_file)
        st.write(data.head())

        # EDA
        perform_eda(data)

        # Target variable selection
        target_variable = st.selectbox('Select Target Variable', data.columns)

        # Model training
        if st.button('Train Model'):
            best_model = train_model(data, target_variable)
            st.write('Best Model:', best_model)

if __name__ == '__main__':
    main()

# Run ngrok to create a tunnel
from pyngrok import ngrok
ngrok_tunnel = ngrok.connect(8501)

# Get the public URL of the Streamlit app
public_url = ngrok_tunnel.public_url
print("Streamlit app can be accessed at:", public_url)

# Start the Streamlit app
!streamlit run --server.port 8501 app.py

# Close the ngrok tunnel
ngrok_tunnel.close()
