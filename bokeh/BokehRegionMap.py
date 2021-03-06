from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states
from Regions import region_dict, region_color

def BokehRegion_Map():
    '''
    This function produces a bokeh map of US states which is colored based on geographic locations. It needs to import two dictionaries from regions.py.
    :return: p (bokeh figure): the result of bokeh map coloring states by region
    '''

    state_xs = [states[code]["lons"] for code in states]
    state_ys = [states[code]["lats"] for code in states]

    #categorize states into colors
    list_of_colors=[]

    for state in states:
        flag=True
        for key, value in region_dict.items():
            if state in value:
                list_of_colors.append(region_color[key])
                flag=False
        if flag==True:
            print(state)

    p = figure(title="Bokeh Region Map", toolbar_location="left",
               plot_width=3400, plot_height=700)

    p.patches(state_xs,state_ys,
              fill_color=list_of_colors,fill_alpha=0.7,
              line_color='black',line_width=0.5)

    output_file("Bokeh_Region.html", title="GeoRegions")
    show(p)
    return p

if __name__=='__main__':
    BokehRegion_Map()