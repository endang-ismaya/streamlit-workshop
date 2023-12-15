import streamlit as st
import pandas as pd

datamurid = r"data/csv/datamurid.csv"

st.title("Belajar Pandas")

st.markdown("###### Mengambil data 'Nama' dan 'IPA' untuk dijadikan series")
df_nama_ipa = pd.read_csv(datamurid, usecols=["Nama", "IPA"], index_col="Nama")
series_nama_ipa = df_nama_ipa.squeeze()

st.write(series_nama_ipa)
st.caption(f"Jumlah Murid: {df_nama_ipa.size}")

st.write(f"Nilai IPA: {df_nama_ipa.values}")
st.write(f"Index Nama: {df_nama_ipa.index}")

df_all = pd.read_csv(datamurid)
st.dataframe(df_all)

st.write("Inggris > 80")
dt_inggris_gt_80 = df_all[df_all["Inggris"].ge(80)]
st.dataframe(dt_inggris_gt_80)

st.divider()
st.write("Semua Mata Pelajaran Nilainya >= 80")

ipa_80 = df_all["IPA"].ge(80)
ips_80 = df_all["IPS"].ge(80)
inggris_80 = df_all["Inggris"].ge(80)
matematika_80 = df_all["Matematika"].ge(80)

df_ge80 = df_all[(ipa_80) & ~(ips_80) & (inggris_80) & (matematika_80)]
st.dataframe(df_ge80)

st.divider()
st.write("Hanya Menampilkan IPA dan IPS Saja")
df_ipas = df_all[(ipa_80) & (ips_80)]
df_ipas = df_all.loc[(ipa_80) & (ips_80), ["Nama", "IPA", "IPS"]]
st.dataframe(df_ipas)
