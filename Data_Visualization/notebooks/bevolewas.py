import plotly.express as px
import pandas as pd



df_b = pd.read_excel('JupyterNotebook\Daten\Bevölkerungswachstum.xlsx', sheet_name='Tabelle1',)

fig = px.bar(df_b,x='Jahr', y='Ständige Wohnbevölkerung',
            color='CO2',color_continuous_scale=[(0, "red"), (0.5, "green"), (1, "blue")],
            hover_name="Jahr")

fig.show()