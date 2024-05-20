from os import listdir
import streamlit as st
import altair as alt
from pandas import read_excel

st.set_page_config(page_title='Panorama do Censo 2022')
selected = st.selectbox('Local', options=listdir('data'), index=5)

df1 = read_excel(f'data/{selected}/Crescimento Populacional.xlsx')
df2 = read_excel(f'data/{selected}/Pirâmide etária.xlsx')

df1 = df1.dropna(axis=0)
df1 = df1.dropna(axis=1)
df2 = df2.dropna(axis=0)
df2 = df2.dropna(axis=1)

df1 = df1.rename(columns={'Ano da pesquisa': 'ano', 'População(pessoas)': 'pop'})
df2 = df2.rename(columns={'Grupo de idade': 'idade', 'População feminina(pessoas)': 'fem', 'População masculina(pessoas)': 'masc'})

total = df2['fem'].sum() + df2['masc'].sum()
df2['masc_pct'] = df2['masc'] / total * 100
df2['masc_pct'] = df2['masc_pct'].map('{:,.2f} %'.format)
df2['masc_pct'] = df2['masc_pct'].str.replace('.', ',')
df2['fem_pct'] = df2['fem'] / total * 100
df2['fem_pct'] = df2['fem_pct'].map('{:,.2f} %'.format)
df2['fem_pct'] = df2['fem_pct'].str.replace('.', ',')
df2['zero'] = 0

chart1 = alt.Chart(df1, title='Crescimento populacional').mark_line(point={'size': 100}).encode(
    x=alt.X('ano').title(None).axis(grid=False),
    y=alt.Y('pop').title(None).axis(labelExpr='datum.value / 1E6 + " M"'),
    tooltip=[alt.Tooltip('ano').title('Ano da pesquisa'), alt.Tooltip('pop').title('População').format(',')],
)

chart2a = alt.Chart(df2).mark_bar(color='blue').encode(
    x=alt.X('masc').title('Homens').sort('descending'),
    y=alt.Y('idade').title(None).sort(None),
    tooltip=alt.Tooltip('masc').format(','),
)

chart2b = alt.Chart(df2).mark_bar(color='red').encode(
    x=alt.X('fem').title('Mulheres'),
    y=alt.Y('idade').title(None).sort(None).axis(None),
    tooltip=alt.Tooltip('fem').format(',')
)

chart2a_text = alt.Chart(df2).mark_text(color='white', align='right', dx=-5).encode(
    x=alt.X('zero').title('Homens').sort('descending'),
    y=alt.Y('idade').title(None).sort(None),
    text=alt.Text('masc_pct'), 
)

chart2b_text = alt.Chart(df2).mark_text(color='white', align='left', dx=5).encode(
    x=alt.X('zero').title('Mulheres'),
    y=alt.Y('idade').title(None).sort(None),
    text=alt.Text('fem_pct'), 
)

st.container(border=True).write(f'👪 :orange[População:] {total:,} :gray[pessoas]')

row1 = st.container(border=True)
row1.altair_chart(chart1, use_container_width=True)

row2 = st.container(border=True).columns(2)
row2[0].altair_chart(chart2a + chart2a_text, use_container_width=True)
row2[1].altair_chart(chart2b + chart2b_text, use_container_width=True)
