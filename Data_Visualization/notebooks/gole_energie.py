
import numpy as np


def prognose_reg(x,reg_x,reg_y):
    y_prognose= []
    slope, intercept = intercept_slope_reg(reg_x,reg_y)
    for i in x:
        p = intercept + float(slope)*i
        y_prognose.append(round(p,3))
    return y_prognose

def plot(ax,x,y):
    for i in y:
        if len(i) != 5:
            raise ValueError(f'y sind nicht alle werte gegeben [[data], coler, label,ls , lw ]: {i}')
        y_plot = i[0]
        coler = i[1]
        label = i[2]
        ls = i[3]
        lw = i[4]
        ax.plot( x,
                y_plot,
                color= coler,
                label = label,
                ls = ls,
                lw = lw)

def ckeck_gole(x,y,titel,xlabel,ylabel,gole,range_gole,ymin,ymax,subplots_adjust=0.2,figsize=(9,6),ticks= 2,ncol=2):
    '''gole= ([[gole1,coler,label,ls,lw],[[golen,coler,label,ls,lw]])
        y = [[data],coler, label,ls,lw ]'''
    fig_x,fig_y = figsize
    s_gole, e_gole = range_gole 
    x_gole = [x for x in range(s_gole,e_gole)]
    x = np.array(x)

    fig, ax = plt.subplots(figsize=(fig_x, fig_y))
    plot(ax,x,y)
    for g in gole:
        g[0]= np.ones(len(x_gole))* g[0]        
  
    plot(ax,x_gole,gole)
    reg_x = np.array(x_gole).reshape((-1.1))
    reg_y = y[0]
    y_prog = prognose_reg(x,reg_x,reg_y)
    ax.plot(x_gole,y_prog,
                 color= 'red',
                 label = 'Regressionsgerade',
                 ls= '-.')

    ax.set_title(titel)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    legend = ax.legend(loc='lower left',bbox_to_anchor=(0,0),bbox_transform=fig.transFigure, fancybox=True, shadow=True, ncol=ncol)
    plt.subplots_adjust(bottom=subplots_adjust)
    plt.xticks([x for x in range(s_gole,e_gole,ticks)])
    plt.ylim(top=ymax)
    plt.ylim(bottom=ymin)
    nice_axes(ax)


