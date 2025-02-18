# All/ep-PBL/
# Py-template-2024-12-10
# 2024-12-10
# 
# Minbar Burhan al-Din,Jerusalem
# python 3.8.2
# run on https://replit
# run on ubuntu 22.04 LTS
#
# 要執行本程式, 請按上方 run▶
#
import numpy as np
import matplotlib.pyplot as plt         # 載入繪圖模組 pyplot, 重新命名為 plt
#
from shapely import affinity
from shapely.geometry import LineString, Point
#
# -------------------------------------------------
#
def set_graphic_area(width,height) :

    cm2inch = 1/2.54    # inch per cm
    #
    # define graphic area
    #
    left_margin = 1.2   # cm
    right_margin = 1.2  # cm
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
def shapely_Arc(cxy, r, start_angle, end_angle) :

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
    xs,ys = LS.xy
    ax.plot(xs, ys, color=MYcolor, alpha=1.0, linewidth=LINEWIDTH, solid_capstyle='round', zorder=ZORDER)
    return
#
def motif_fill(LS, color, ZORDER, Alpha) :
    #
    xs,ys = LS.xy
    ax.fill(xs, ys, alpha=Alpha, closed=True, edgecolor=None, facecolor=color, fill=True, zorder=ZORDER)
    return
#
def polygon_line(poly, MYcolor, ZORDER, LINEWIDTH) :
    #
    xs, ys = poly.exterior.coords.xy
    ax.plot(xs, ys, color=MYcolor, alpha=1.0, linewidth=LINEWIDTH, solid_capstyle='round', zorder=ZORDER)
    return
#
# ---------------------------------------------------
#
print('main running ...')
#
tup7 = set_graphic_area(12,12)  
fig = plt.figure(figsize=(tup7[0], tup7[1])) # 呼叫 pyplot.figure(), 建立一個圖表物件, 並成為目前圖表物件
ax = fig.add_subplot(1,1,1)   # 圖表的繪圖區域被分為1個子圖, 1 row, 1 column, plot to index 1
fig.subplots_adjust(
                top    = tup7[2] ,
                bottom = tup7[3] ,
                left   = tup7[4] ,
                right  = tup7[5] ,
                )
#
# r = 20/np.cos(np.pi/3)
# print(r)
r = 40
dx = r*np.cos(np.pi/3)/2
dy = r*np.sin(np.pi/3)/2
print(dx)
print(dy)
#
cxy = (0,0) # ()元組
plt.xlim(-dx-0.5, dx+0.5)    # 設定X軸的顯示範圍, from xmin to xmax
plt.ylim(-dy-0.5, dy+0.5)    # 設定Y軸的顯示範圍, from ymin to ymax
# 
x_values = [-10,0,10]
y_values = [-17.32,0,17.32]
ax.set_xticks(x_values)
ax.set_yticks(y_values)
plt.tick_params(labelsize=10)
#
plt.grid(True)
# get current axes, set X,Y same ratio & scale  
plt.gca().set_aspect('equal', adjustable='box') 
#
# ax.set_axis_off()   # will turn off grid line
ax.set_axis_on()  # will turn on grid line
#
rectangle_xy = [(-dx,-dy),(dx,-dy),(dx,dy),(-dx,dy),(-dx,-dy)]
rectangle = LineString(rectangle_xy)
motif_fill(rectangle, "lightblue", 10, 0.3)
#
vline_right = LineString([( dx,-dy), ( dx,dy)])
line_60 = LineString([(-dx,-dy), (dx,dy)])
motif_line(line_60, 'red', 10, 0.7)
#
top_line = LineString([(-dx,dy), (dx,dy)])
#
line_75 = affinity.rotate(line_60, 15, (-dx,-dy))
line_75_end = line_75.intersection(top_line)
line_75_end_xy = (line_75_end.x, line_75_end.y)
line_75 = LineString([(-dx,-dy), line_75_end_xy])
motif_line(line_75, 'green', 10, 0.7)
#
line_45 = affinity.rotate(line_60, -15, (-dx,-dy))
line_45_end = line_45.intersection(vline_right)
line_45_end_xy = (line_45_end.x, line_45_end.y)
print(line_45_end_xy)
line_45 = LineString([(-dx,-dy), line_45_end_xy])
motif_line(line_45, 'green', 10, 0.7)
#
line_30 = affinity.rotate(line_60, -30, (-dx,-dy))
its_right_1 = line_30.intersection(vline_right)
its_right_1_xy = ( dx, its_right_1.y)
line_30 = LineString([(-dx,-dy), its_right_1_xy])
motif_line(line_30, 'green', 10, 0.7)
#
r1 = 10
cir_1 = shapely_Arc(cxy, r1, 0, 360)
#
motif_line(cir_1, 'blue', 10, 1.5)
#
plt.savefig("./png/01.png",format="png",dpi=300)
#
print('done')
plt.show()