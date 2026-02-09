from sqlalchemy import create_engine
import streamlit as st
import pandas as pd


@st.cache_resource
def get_engine():
    return create_engine(
        "postgresql+psycopg2://jblec2:F3zhZcaV75@10.250.131.24:5432/ul_val_prj_mh_hydro_pr"
    )

engine = get_engine()



hydro_vars_mapping = {
    1: "water table depth",
    2: "discharge",
    3: "precipitation",
    4: "water content",
    5: "stream stage"}

with st.form("my_form"):
    start_date = st.date_input("Start date")
    end_date   = st.date_input("End date")
    my_variable = st.selectbox(
        "Select variable",
        options=[1,2,3,4,5],
        format_func= lambda x: hydro_vars_mapping[x])
    st.form_submit_button("Submit")


query = """
SELECT time, value
FROM hydro_observation
WHERE variable_id = %(var_id)s
AND time BETWEEN %(start)s AND %(end)s
ORDER BY time
"""

df = pd.read_sql(
    query,
    engine,
    params={
        "start": start_date,
        "end": end_date,
        "var_id": my_variable
    }
)

st.line_chart(df.set_index("time"))
# st.write(df)
