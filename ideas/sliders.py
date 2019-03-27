"""
we're making a sine wave slider app

to run it
bokeh serve sliders.py

then go to
http://localhost:5006/sliders
in my browser.
"""

import numpy as np

#return the current document for the current default state
from bokeh.io import curdoc

# helps place the grid layout
from bokeh.layouts import row, column

# helps with arranging everything into some kind of graph data structure
# i think this is back end stuff for plotting but who knows/cares
from bokeh.models import ColumnDataSource

from bokeh.models.widgets import Slider,TextInput
from bokeh.plotting import figure

# set up data
N = 500
L = 11
startBound = 0
endBound = 2*np.pi
x = np.linspace(startBound,endBound,N)
y = 5*5*5*5*5*(1 - np.exp(x))

# prepping my plot for animation stuff
source = ColumnDataSource(data=dict(x=x,y=y))

# set up plot
plot = figure(plot_height=800,plot_width=800, title="First Order Response",
            tools="crosshair,pan,reset,save,wheel_zoom",
            x_range=[startBound, endBound],y_range=[0,5])

plot.line('x','y', source=source, line_width=3, line_alpha=0.6)

# set up widgets
text = TextInput(title="Title", value = "Dirichlet Function")
offset = Slider(title="Offset",value=0.0, start=-5.0,end=5.0,step=0.1)
amplitude = Slider(title="Amplitude", value=1.0, start=-5.0, end=5.0,step=0.1)
phase = Slider(title="Phase", value=0.0, start=0.0, end=2*np.pi)
freq = Slider(title="Frequency", value=1.0, start=0.1, end=5.1, step=0.1)

# set up callbacks (what are callbacks)
# basically it looks like every time you re adjust the slider, you have to change
# what data is in there
def update_title(attrname,old,new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # get current slider values
    a = amplitude.value
    b = offset.value
    w = phase.value
    k = freq.value

    # generate the new curve
    x = np.linspace(0,2*np.pi,N)
    y = a*(1-np.exp(-k*x))
    source.data = dict(x=x,y=y) # probably you extend it for 3d data

for w in [offset,amplitude,phase,freq]:
    w.on_change('value', update_data)

# set up layouts and add to document
inputs = column(text,offset,amplitude,phase,freq)
curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "First Order Response"
