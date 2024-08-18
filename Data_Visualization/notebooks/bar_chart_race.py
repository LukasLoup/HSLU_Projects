import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



df = pd.read_excel('JupyterNotebook\Daten\Endenergieverbrauch_nach_Energieträger_TJ.xlsx', sheet_name='Tabelle1',
                    usecols=['Jahr','Brennstoffe', 'Treibstoffe', 'Elektrizität', 'Gas','Kohle',
                    'Holz und Holzkohle', 'übrige Energieträger'])

df.set_index('Jahr',inplace = True)

colors = plt.cm.Dark2(range(7))

print(colors)

#print(df)

s = df.loc[1990]


#print(s)


def nice_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]
    
def prepare_data(df, steps=5):
    df = df.reset_index()
    df.index = df.index * steps
    last_idx = df.index[-1] + 1
    df_expanded = df.reindex(range(last_idx))
    df_expanded['Jahr'] = df_expanded['Jahr'].fillna(method='ffill') #ffill
    df_expanded = df_expanded.set_index('Jahr')
    df_rank_expanded = df_expanded.rank(axis=1, method='first')
    df_expanded = df_expanded.interpolate()
    df_rank_expanded = df_rank_expanded.interpolate()
    return df_expanded, df_rank_expanded


def init():
    ax.clear()
    nice_axes(ax)
    ax.set_ylim(.2, 6.8)
    

def valuelabel():
    rects = ax.patches    
    # For each bar: Place a label
    for rect in rects:
        # Get X and Y placement of label from rect.
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2
        # Number of points between bar and label. 
        space = 5
        # Vertical alignment for positive values
        ha = 'left'
        # If value of bar is negative: Place label left of bar
        if x_value < 0:
            # Invert space to place label to the left
            space *= -1
            # Horizontally align label at right
            ha = 'right'

        # Use X value as label and format number with one decimal place
        label = "{:.1f}  *10e3TJ".format(x_value)

        # Create annotation
        plt.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(space, 0),          # Horizontally shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            va='center',                # Vertically center label
            ha=ha)                      # Horizontally align label differently for
                                        # positive and negative values.

def update(i):
    ax.clear()
    nice_axes(ax)
    for bar in ax.containers:
        bar.remove()
    y = df_rank_expanded.iloc[i]
    width = df_expanded.iloc[i]
    ax.barh(y=y, width=width, color=colors, tick_label=labels)
    date_str = f'{int(df_expanded.index[i])}'
    ax.set_title(f'Endenergieverbrauch nach Energieträger im Jahr {date_str}', fontsize='smaller')
    ax.set_xlabel('Endenergieverbrauch in 1000 Terajoules')
    valuelabel()
    ax.text(1, 0.4, int(df_expanded.index[i]), transform=ax.transAxes,color='#777777', size=46, ha='right',weight=800)
    #plt.subplot()



df_expanded, df_rank_expanded = prepare_data(df)
labels = df_expanded.columns


fig = plt.figure(figsize=(10, 3), dpi=144)
ax = fig.add_subplot()


anim = FuncAnimation(fig=fig, func=update, init_func=init(), frames=len(df_expanded), 
                     interval=100, repeat=False)

plt.show()