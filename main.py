# All/00-template
# Template-for-Python-with-TkAgg-VNC
#
# 2026-02-06
# 用於繪製圖形的 Python 模板

"""
Total disk used on this machine: about 36 GB out of 74 GB available
The 36 GB total includes everything: 
    your project files, 
    installed packages, 
    the system environment,
    language toolchains. 

Your actual project files are only a small portion of that. 
Most of the space is taken up by the underlying system and installed tools/packages.

This project is currently using 166 MB of disk storage.
Your actual code and libraries are only about 11 MB total.

What        Size        What it is
----------------------------------------------------------
.cache      154 MB      Temporary files created by your tools/packages (like pip/uv cache)
.git        2.4 MB      Version history of your project
.pythonlibs     11 MB   Installed Python libraries your code depends on
Your code 
+ config        ~100 KB Your actual project files

So 154 MB (93%) of the space is just cached files that your package manager stores to speed things up. 

The cache is harmless -- it just helps things install faster if you ever update packages.
"""
#
# 要執行本程式, 請按上方run▶
#
import shutil
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
#
from shapely import affinity
from shapely.geometry  import LineString, Point
#
from platform import python_version
print('the python version is',python_version())
print('')
#
# /home/runner/workspace/
total, used, free = shutil.disk_usage("/home")
print("/home directory...")
print('< disk usage >')
print("Total: %d GiB" % (total // (2**30)))
print(" Used: %d GiB" % (used  // (2**30)))
print(" Free: %d GiB" % (free  // (2**30)))
#
# ---------------------------------------------
#
def set_graphic_area(width,height) :

    cm2inch = 1/2.54    # inch per cm
    #
    # define graphic area
    #
    left_margin = 1.0   # cm
    right_margin = 1.0  # cm
    #
    figure_width  = width  # cm , from xmin to xmax
    figure_height = height # cm , from ymin to ymax
    #
    top_margin = 1.0    # cm
    bottom_margin = 1.0 # cm
    #
    box_width = left_margin + figure_width + right_margin   # cm
    box_height = top_margin + figure_height + bottom_margin # cm
    #
    top_value    = 1.0 - top_margin / box_height
    bottom_value = bottom_margin / box_height
    left_value   = left_margin / box_width
    right_value  = 1.0 - right_margin / box_width
    #
    return (box_width*cm2inch,box_height*cm2inch,top_value,bottom_value,left_value,right_value,width)
    #
# end of def
#
# Define the arc
# center position is cxy = (cx, cy)
# start_angle, end_angle is in degrees
#
def shapely_Arc(cxy, r, start_angle, end_angle) :
    #
    numsegments = 720
    # The coordinates of the arc
    theta = np.radians(np.linspace(start_angle, end_angle, numsegments))
    x = cxy[0] + r * np.cos(theta)
    y = cxy[1] + r * np.sin(theta)
    Arc = LineString(np.column_stack([x, y]))
    return Arc
    #
# end of def
#
def motif_line(LS, MYcolor, ZORDER, LINEWIDTH) :
    #
    xs, ys = LS.xy
    ax.plot(xs, ys, 
            color=MYcolor, 
            alpha=1.0, 
            linewidth=LINEWIDTH, 
            solid_capstyle='round', 
            zorder=ZORDER)
    return
# end def
#
def motif_fill(LS, color, ZORDER, Alpha) :
    #
    xs, ys = LS.xy
    ax.fill(xs, ys, 
            alpha=Alpha, 
            closed=True, 
            edgecolor=None, 
            facecolor=color, 
            fill=True, 
            zorder=ZORDER)
    return
# end def
#
# --------------------------------------------------------
#
# set initial value
#
r0 = 12
tup7 = set_graphic_area(r0, r0)  
plt.ion()
fig = plt.figure(figsize=(tup7[0], tup7[1])) # 呼叫 pyplot.figure(), 建立一個圖表物件, 並成為目前圖表物件
ax = fig.add_subplot(1,1,1)   # 圖表的繪圖區域被分為1個子圖, 1 row, 1 column, plot to index 1
fig.subplots_adjust(
                top    = tup7[2] ,
                bottom = tup7[3] ,
                left   = tup7[4] ,
                right  = tup7[5] ,
                )
#
plt.xlim(-tup7[6]/2, tup7[6]/2)    # 設定X軸的顯示範圍, from xmin to xmax
plt.ylim(-tup7[6]/2, tup7[6]/2)    # 設定Y軸的顯示範圍, from ymin to ymax
#
x_values = [-6,-4,-2,0,2,4,6]
y_values = [-6,-4,-2,0,2,4,6]
ax.set_xticks(x_values)
ax.set_yticks(y_values)
plt.tick_params(labelsize=10)
#
# plt.grid(color='green', linewidth=0.4)
plt.grid(True)
# ax.set_axis_off() # will turn off grid line
ax.set_axis_on()    # will turn on grid line
#
# get current axes, set X,Y same ratio & scale  
plt.gca().set_aspect('equal', adjustable='box') 
#
plt.savefig('./png/graphic.png', dpi=150)
#
plt.show()
#
print(' ')
print('done')
print('view VNC tab ...')
print('Press Stop to exit')
#
plt.show()