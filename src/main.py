import streamlit as st
from initial_credentials import *
import pandas as pd
## Connect to BQ

@st.cache(allow_output_mutation=True)
def fetch_data():
    facilities = pd.read_gbq(query = 'SELECT * FROM `showvik-argolis-test-project.post_acute_medical.facilities`',project_id = project_name,dialect='standard')
    agency_nurses = pd.read_gbq(query = 'SELECT * FROM `showvik-argolis-test-project.post_acute_medical.agency_nurses`',project_id = project_name,dialect='standard')
    travel_nurses = pd.read_gbq(query = 'SELECT * FROM `showvik-argolis-test-project.post_acute_medical.travel_nurses`',project_id = project_name,dialect='standard')

    return (facilities, agency_nurses, travel_nurses)

facilities, agency_nurses, travel_nurses = fetch_data()

facilities
agency_nurses
travel_nurses