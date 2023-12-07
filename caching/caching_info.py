"""
st.cache_data

Cache computation that returns data:
- DataFrame from CSV
- Make a Calculation
- Query an API
- Anything that returns serializable object (st, int, float, DataFrame
    Array, List, etc)
"""


"""
st.cache_resource

Cache resources that should be available globally accross users, sessions and reruns

Usually limited to:
- ML Models
- Database Connections

"""
