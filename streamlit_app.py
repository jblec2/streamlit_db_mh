import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
query = """
SELECT time, value
FROM hydro_observation
WHERE variable_id = 1
AND loc = 'Fxp6'
ORDER BY time
"""

df = conn.query(query, ttl="10m")


# Print results.
st.line_chart(df.set_index("time"))

