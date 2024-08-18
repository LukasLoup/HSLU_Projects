from cProfile import label
from re import X
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.graph_objects as go


df_co2_con = pd.read_excel('JupyterNotebook\Daten\Treibhausgasemissionen_nach_verbrauchergruppen.xlsx',sheet_name='Tabelle1')

color = plt.cm.Dark2(range(7))
labels = ['Energie (ohne Transport, inkl. Abfallverbrennung)',
        'Transport (ohne internationalen Flugverkehr)',
        'Industrielle Prozesse und Lösungsmittel',
        'Landwirtschaft', 
        'Abfall (ohne Abfallverbrennung)',
        'Andere (Brände, Feuerschäden)',
        'Total 1)',
        'Internationaler Flug- und Schiffsverkehr',
        'Landnutzungsänderung/Forstwirtschaft inkl. Holzprodukte']

# {kex = colum name : [label, color]}
colms = {'Energie_co2a':['Energie (ohne Transport, inkl. Abfallverbrennung)', '#000000', '--'],
        'Transport_co2a':['Transport (ohne internationalen Flugverkehr)', '#a52a2a','-'],
        'Industrielle_co2a':['Industrielle Prozesse und Lösungsmittel', '#8c92ac','-.'],
        'Landwirtschaft_co2a':['Landwirtschaft','#8db600',':'],
        'Abfall_co2a':[ 'Abfall (ohne Abfallverbrennung)','#e30022' ,''],
        'Internationaler_Flug_co2a':['Internationaler Flug- und Schiffsverkehr', '#89cff0','--'],
        'Landnutzungsänderung_co2a':['Landnutzungsänderung/Forstwirtschaft inkl. Holzprodukte', '#ff00ff','-'],
        'Total_co2a_1':['Total 1)','#ffef00','']}
        
x = df_co2_con['Jahr']



y = df_co2_con['Energie_co2a']
y_1 = df_co2_con['Transport_co2a']

df_pro = pd.DataFrame(x)

p = df_co2_con['Energie_co2a'] / df_co2_con['Total_co2a_1'] * 100

df_t = df_pro.assign(Energie_co2a_pro=p)
print(df_t)

print(type(p))
print()

fig, ax1 = plt.subplots()

for k in colms:    
    v = colms[k]
    ax1.plot(x,df_co2_con[k], color= v[1], label = v[0],ls= v[2])
    if  k not in ['Total_co2a_1','Internationaler_Flug_co2a', 'Landnutzungsänderung_co2a']:
        p = df_co2_con[k] / df_co2_con['Total_co2a_1'] * 100        
        df_pro = df_pro.assign(**{f'{k}_pro':p})

df_pro.set_index('Jahr',inplace = True)     
s = df_pro.loc[2020]
labels = s.index
values = s.values
fig_pie = go.Figure(data=[go.Pie(labels=labels,
                                 values=values,
                                 hole=.6)])

legend = ax1.legend(loc=0,bbox_to_anchor=(0.8,0.75))
                    
#ax1.add_artist(legend)
#ig_pie.show()
#plt.show()

colors_pie_pro = {}
for k in colms: 
    v = colms[k]
    colors_pie_pro[k] = v[1] 
print(colors_pie_pro.values)