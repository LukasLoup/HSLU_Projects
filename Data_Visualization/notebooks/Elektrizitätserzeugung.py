from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import false


df_el = pd.read_excel('JupyterNotebook\Daten\Elektrizitätserzeugung_in_GWh.xlsx', sheet_name='Tabelle1')

print(df_el.columns)
#'Landeserzeugung (brutto) Verbrauch der Speicherladung',
# 'Landeserzeugung (brutto) total',
# 'Nettoerzeugung '
x = df_el['Jahr']
y = ['Wasserkraftwerke ', 'Kernkraftwerke',
       'Konventionell thermische Kraft- und Fernheizkraftwerke',
       'Diverse Erneuerbare 1)', 'Nettoerzeugung '    
     ]
colors_el = ['#007fff','#008000','Red','#a52a2a','#000000']
line_stl_el=['-.',':','-.','--','-']



def nice_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]

fig, ax_el = plt.subplots(1,2,figsize=(9, 3), sharey=False)
i = 0
for k in y:
    print(k)
    ax_el[0].plot(x,df_el[k],label=k,color=colors_el[i],ls=line_stl_el[i])
    i += 1

s = df_el.iloc[-1]
print(s.values)

legend = ax_el[0].legend(loc=0,bbox_to_anchor=(0.8,0.75))
nice_axes(ax_el[0])


ax_el[1].barh([1,2,3,4,5],[5000000,6000000,7000000,8000000,900000])
plt.show()
