# All/template/
# template-TkAgg-VNC
#
# 2026-02-06
# This project use 166 MB of disk storage.
#
# 要執行本程式, 請按上方run▶
#
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
#
# ---------------------------------------------
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
m = 8.660254037844387
n = 7.5
#
# 開啟互動視窗
fig = plt.figure(figsize=(6, 6), num="graphic window")
ax = fig.add_subplot(1, 1, 1)
ax.set_axis_on()
#
plt.xlim(-3*m,3*m) # 設定X軸的顯示範圍, from xmin to xmax
plt.ylim(-20,20) # 設定Y軸的顯示範圍, from ymin to ymax
#
xvalues = [-3*m,-2*m,-1*m,0,1*m,2*m,3*m]
yvalues = [-3*n,-2*n,-1*n,0,1*n,2*n,3*n]
plt.xticks(xvalues, ['-3m','-2m','-1m','0','1m','2m','3m'])
plt.yticks(yvalues, ['-3n','-2n','-1n','0','1n','2n','3n'])
plt.tick_params(labelsize=11)
plt.grid(color='gray', linewidth=0.4)
ax.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
#
print(' ')
print('done')
print('view output tab ...')
print('Press Stop to exit')
#
plt.show()