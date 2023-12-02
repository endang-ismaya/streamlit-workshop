import streamlit as st

st.title("Streamlit Development")
st.header("I am Endang Ismaya")
st.subheader("Learn how to develop a streamlit app.")

st.text("this is a paragraph")

# markdown
st.markdown("## Markdown")

l1 = ["Streamlit", "Numpy", "Pandas", "Matplotlib", "Seaborn"]

for item in l1:
    st.markdown(f"- [ ] {item}")

# Latex (mathematical)
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# json
json_data = {
    "family": ["endang", "indah", "alde", "aqeela", "auza", "arsyila", "akhdan"]
}
st.json(json_data)

# code
code1 = """
def func():
    return "Hello World"

# run func()
func()
"""
st.code(code1, language="python")

# write any
st.write("## H2")
st.write("<h1>This is H1 Tag</>")

# metric
st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")
