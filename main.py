# All/w2-幾何藝術-Alhambra/
# pat-5
#
# 2024-05-22
# 2025-02-21
#
# https://www.aramcoworld.com/Articles/January-2022/Art-of-Islamic-Patterns-Alicatado
# 要執行本程式, 請按上方run▶
#
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
# 載入繪圖模組 pyplot, 重新命名為 plt
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
    numsegments = 1440
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
    ax.plot(xs, ys, color=MYcolor, alpha=1.0, linewidth=LINEWIDTH, solid_capstyle='round', zorder=ZORDER)
    return
#
def motif_fill(LS, color, ZORDER, Alpha) :
    #
    xs, ys = LS.xy
    ax.fill(xs, ys, alpha=Alpha, closed=True, edgecolor=None, facecolor=color, fill=True, zorder=ZORDER)
    return
#
# --------------------------------------------------------
#
# set initial value
r0  = 5
cxy = (0,0)
dx = 4.3301270189221945
dy = 2.5
cxy = (dx, dy)
m = 8.660254037844387
n = 7.5
#
# 開啟互動視窗
fig = plt.figure(figsize=(6, 6), num="interactive window")
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
## ---------------------------------------------------------------
#
print('running ...')
r0  = 5
cxy = (0,0)
dx = 4.3301270189221945
dy = 2.5
cxy = (dx, dy)
#
circle_1 = shapely_Arc(cxy, r0, 0, 360)
# motif_line(circle_1, 'blue', 10, 1.0)
#
p1 = (dx+r0*np.cos( 3*np.pi/6), dy+r0*np.sin( 3*np.pi/6))
p2 = (dx+r0*np.cos( 7*np.pi/6), dy+r0*np.sin( 7*np.pi/6))
p3 = (dx+r0*np.cos(11*np.pi/6), dy+r0*np.sin(11*np.pi/6))
#
tri_xy = [p1,p2,p3,p1]
tri    = LineString(tri_xy)
edge_1 = LineString([p3,p1])
edge_2 = affinity.rotate(edge_1, 1*60, p2)
edge_3 = affinity.rotate(edge_1, 2*60, p2)
edge_4 = affinity.rotate(edge_1, 3*60, p2)
edge_5 = affinity.rotate(edge_1, 4*60, p2)
edge_6 = affinity.rotate(edge_1, 5*60, p2)
#
edge_1_xy = list(edge_1.coords)
edge_2_xy = list(edge_2.coords)
edge_3_xy = list(edge_3.coords)
edge_4_xy = list(edge_4.coords)
edge_5_xy = list(edge_5.coords)
edge_6_xy = list(edge_6.coords)
#
hex_xy = edge_1_xy + edge_2_xy + edge_3_xy + edge_4_xy + edge_5_xy + edge_6_xy
hex = LineString(hex_xy)
#
down_cxy = (dx+0, p2[1])
circle_2 = shapely_Arc(down_cxy, 0.15, 0, 360)
motif_fill(circle_2, 'red', 20, 1.0)
#
line_p2_p3 = LineString([p2, p3])
line_1 = affinity.rotate(line_p2_p3,  30, p2)
line_2 = affinity.rotate(line_p2_p3, -30, down_cxy)
# motif_line(line_1, 'black', 10, 0.6)
# motif_line(line_2, 'black', 10, 0.6)
#
its_1 = line_1.intersection(line_2)
its_1_xy = (its_1.x, its_1.y)
circle_3 = shapely_Arc(its_1_xy, 0.15, 0, 360)
motif_fill(circle_3, 'blue', 20, 1.0)
#
pp2 = Point(p2)
#
r1 = its_1.distance(pp2)
arc_1 = shapely_Arc(its_1_xy, r1, 210, 330)
arc_2 = affinity.rotate(arc_1, 180, down_cxy)
motif_line(arc_1, 'gray', 10, 1.0)
motif_line(arc_2, 'purple', 10, 1.0)
#
arc_1_list = list(arc_1.coords)
arc_2_list = list(reversed(list(arc_2.coords)))
arc_A_xy = arc_1_list + arc_2_list
arc_A = LineString(arc_A_xy)
arc_B = affinity.rotate(arc_A, 120, (dx,dy))
arc_C = affinity.rotate(arc_A, 240, (dx,dy))
#
motif_line(arc_A, 'red',  10, 1.0)
motif_line(arc_B, 'cyan', 10, 1.0)
motif_line(arc_C, 'magenta', 10, 1.0)
#
plt.savefig("./png/fig-05.png",format="png",dpi=150)
#
arc_A_xy = list(arc_A.coords)
arc_B_xy = list(arc_B.coords)
arc_C_xy = list(arc_C.coords)
fan_xy = arc_A_xy + arc_B_xy + arc_C_xy
fan_A = LineString(fan_xy)
motif_fill(fan_A, 'magenta', 10, 0.7)
#
plt.savefig("./png/fig-06A.png",format="png",dpi=150)
#
motif_line(fan_A, 'blue', 10, 1.0)
#
plt.savefig("./png/fig-06B.png",format="png",dpi=150)
#
fan_B = affinity.rotate(fan_A, 2*60, (0,0))
fan_C = affinity.rotate(fan_A, 4*60, (0,0))
motif_fill(fan_B, 'magenta', 10, 0.7)
motif_fill(fan_C, 'magenta', 10, 0.7)
#
motif_line(hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-07.png",format="png",dpi=150)
#
tx = 1.5*m
ty = 1.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-08A.png",format="png",dpi=150)
#
tx = 0.0*m
ty = 2.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-08B.png",format="png",dpi=150)
#
tx =-1.5*m
ty = 1.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-08C.png",format="png",dpi=150)
#
tx =-1.5*m
ty =-1.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-08D.png",format="png",dpi=150)
#
tx = 0.0*m
ty =-2.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-08E.png",format="png",dpi=150)
#
tx = 1.5*m
ty =-1.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-08F.png",format="png",dpi=150)
#
tx = 3*m
ty = 0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-09A.png",format="png",dpi=150)
#
tx = 1.5*m
ty = 3.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-09B.png",format="png",dpi=150)
#
tx =-1.5*m
ty = 3.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-09C.png",format="png",dpi=150)
#
tx =-3*m
ty = 0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-09D.png",format="png",dpi=150)
#
tx =-1.5*m
ty =-3.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-09E.png",format="png",dpi=150)
#
tx = 1.5*m
ty =-3.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-09F.png",format="png",dpi=150)
#
tx = 3.0*m
ty = 2.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-10A.png",format="png",dpi=150)
#
tx =-3.0*m
ty = 2.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-10B.png",format="png",dpi=150)
#
tx =-3.0*m
ty =-2.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-10C.png",format="png",dpi=150)
#
tx = 3.0*m
ty =-2.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-10D.png",format="png",dpi=150)
#
tx = 0.0*m
ty = 4.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-11A.png",format="png",dpi=150)
#
tx = 3.0*m
ty = 4.0*n
#
t_fan_A = affinity.translate(fan_A, tx, ty)
t_fan_B = affinity.translate(fan_B, tx, ty)
t_fan_C = affinity.translate(fan_C, tx, ty)
motif_fill(t_fan_A, 'magenta', 10, 0.7)  
motif_fill(t_fan_B, 'magenta', 10, 0.7)  
motif_fill(t_fan_C, 'magenta', 10, 0.7)  
#
t_hex = affinity.translate(hex, tx, ty)
motif_line(t_hex, "green", 10, 0.6)
#
plt.savefig("./png/fig-11B.png",format="png",dpi=150)
#
print('done')
print('view output tab ...')
print('Press Stop to exit')
plt.show()