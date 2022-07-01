import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D


def get_points_square(N):
    pos = np.zeros((N, N, 2))
    pos[:, :, 0], pos[:, :, 1] = np.meshgrid(np.arange(N), np.arange(N))
    return np.reshape(pos, (-1, 2))


N = 10
pos = get_points_square(N)


A = 0.9
angle = 35
fr = 1
k = np.array([np.cos(angle*np.pi/180), np.sin(angle*np.pi/180)])*fr
w = 2*np.pi
g = 0
rot = (angle+45)*np.pi/180

angles = np.random.normal(scale=97, size=N*N)


def f(t):
    frequency = np.sum(pos*k, axis=1)
    disp = A*np.sin(frequency-w*t)
    new_disp = np.zeros(np.shape(pos))
    new_disp[:, 0] = np.cos(rot)*disp
    new_disp[:, 1] = np.sin(rot)*disp
    return pos+new_disp


def s(t):
    frequency = np.sum(pos*k, axis=1)
    disp = A*np.sin(frequency-w*t)
    return (disp.flatten()+1)*10+1


def s_square(t):
    frequency = np.sum(pos*k, axis=1)
    disp = A*np.sin(frequency-w*t)
    return (disp.flatten()+1)*0.75+0.3


def angle_square(t):
    frequency = np.sum(pos*k, axis=1)
    disp = np.sin(frequency-w*t)
    return (disp.flatten()+1)*0.5


new_pos = f(0)
new_size = s(0)
new_size_square = s_square(0)
new_angle = angle_square(0)*angles

fig = plt.figure(figsize=(7, 7), facecolor='0.2')
ax = plt.subplot(111)
pos_flat = np.reshape(pos, (-1, 2))
pats = [patches.Rectangle(pos_flat[i]-new_size_square[i]/2, new_size_square[i], new_size_square[i], fc='w', ec='0.2')
        for i in range(len(pos_flat))]
for i, p in enumerate(pats):
    p.set_transform(Affine2D().rotate_deg_around(
        *pos_flat[i, :], new_angle[i])+ax.transData)
    ax.add_patch(p)

d = 0.4
big_frame = patches.Rectangle(
    (0-d, 0-d), N-1+2*d, N-1+2*d, fc='w', ec='0.2', zorder=0)
ax.add_patch(big_frame)
ax.set_xlim(-1.5, N+0.5)
ax.set_ylim(-1.5, N+0.5)
ax.set_axis_off()

ax_time = plt.axes([0.1, 0.05, 0.8, 0.03])
time_slider = Slider(
    ax=ax_time,
    label='t',
    valmin=0,
    valmax=10,
    valinit=0,
)


def update(val):
    new_pos = f(time_slider.val)
    p = np.reshape(new_pos, (-1, 2))
    points.set_offsets(p)
    fig.canvas.draw_idle()


def update_size(val):
    new_size = s(time_slider.val)
    points.set_sizes(new_size)
    fig.canvas.draw_idle()


def update_size_square(val):
    new_size = s_square(time_slider.val)
    new_angle = angle_square(time_slider.val)*angles
    for i, p in enumerate(pats):
        p.set_xy(pos_flat[i, :]-new_size[i]/2)
        p.set_transform(Affine2D().rotate_deg_around(
            *pos_flat[i, :], new_angle[i])+ax.transData)
        p.set_width(new_size[i])
        p.set_height(new_size[i])
    fig.canvas.draw_idle()


time_slider.on_changed(update)
plt.tight_layout()
plt.show()
