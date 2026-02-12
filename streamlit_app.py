import socket
import streamlit as st
st.write(st.secrets["connections"]["postgresql"])
try:
    ip = socket.gethostbyname(st.secrets["connections"]["postgresql"]["host"])
    st.write("Resolved IP:", ip)
except Exception as e:
    st.error(f"DNS resolution failed: {e}")
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

