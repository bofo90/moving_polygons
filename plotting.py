import matplotlib.patches as patches
from matplotlib.transforms import Affine2D
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

import numpy as np


class Figure_Lattice:

    def __init__(self, negative=False) -> None:
        self.color = "#ED6D3C"  # "#D9B800"
        self.mid = "#E6E1D6"  # "#868179"
        if negative:
            self.gray = "#E6E1D6"
            self.white = "#252422"
        else:
            self.gray = "#252422"
            self.white = "#E6E1D6"

    def create_square_squares(self, grid, t=0, slider=False):

        self.fig = plt.figure(figsize=(7, 7), facecolor=self.mid)
        self.ax = plt.subplot(111)

        self.grid = grid
        sizes = grid.size_square(t)
        angles = grid.angle_square(t)

        red_pat = np.random.random(len(grid.pos)) < 0.95
        # edge_color = [self.gray if i else self.color for i in red_pat]
        fill_color = [self.white if i else self.color for i in red_pat]

        # red_pat = np.random.randint(len(grid.pos), size=2)
        # edge_color = [
        #     self.gray if i not in red_pat else self.color for i in range(len(grid.pos))]
        # fill_color = [
        #     self.white if i not in red_pat else self.color for i in range(len(grid.pos))]

        self.pats = [patches.RegularPolygon(grid.pos[i, :],
                                            4, sizes[i], np.pi/4,
                                            fc=fill_color[i],
                                            ec=self.gray,
                                            linewidth=1)
                     for i in range(len(grid.pos))]

        for i, p in enumerate(self.pats):
            p.set_transform(Affine2D().rotate_deg_around(
                *grid.pos[i, :], angles[i])+self.ax.transData)
            self.ax.add_patch(p)

        d = 0.65
        big_frame = patches.RegularPolygon(
            (0, 0), 4, grid.furth_dist+d, np.pi/4, fc=self.gray, ec=self.mid, zorder=0)
        self.ax.add_patch(big_frame)
        self.ax.set_xlim(-grid.N/2-1.5, grid.N/2+1.5)
        self.ax.set_ylim(-grid.N/2-1.5, grid.N/2+1.5)
        self.ax.set_axis_off()

        if slider:
            self.create_time_slider(self.update_squares_size_rot)

    def create_time_slider(self, func):
        ax_time = plt.axes([0.1, 0.05, 0.8, 0.03])
        self.time_slider = Slider(
            ax=ax_time,
            label='t',
            valmin=0,
            valmax=10,
            valinit=0,
        )
        self.time_slider.on_changed(func)

    def update_squares_size_rot(self, val):
        new_size = self.grid.size_square(val)
        new_angle = self.grid.angle_square(val)
        for i, p in enumerate(self.pats):
            p.set_xy(self.grid.pos[i, :]-new_size[i]/2)
            p.set_transform(Affine2D().rotate_deg_around(
                *self.grid.pos[i, :], new_angle[i])+self.ax.transData)
            p.set_width(new_size[i])
            p.set_height(new_size[i])
        self.fig.canvas.draw_idle()

    def create_square_points(self, grid):

        self.fig = plt.figure(figsize=(7, 7), facecolor=self.mid)
        self.ax = plt.subplot(111)

        self.grid = grid
        sizes = grid.size_dot(0)
        displ = grid.displacement(0)

        self.points = self.ax.scatter(
            displ[:, 0], displ[:, 1], s=sizes, c=self.white)

        d = 0
        big_frame = patches.Rectangle(
            (0-d, 0-d), grid.N-1+2*d, grid.N-1+2*d, fc=self.white, ec=self.mid, zorder=0)
        self.ax.add_patch(big_frame)
        self.ax.set_xlim(-1.5, grid.N+0.5)
        self.ax.set_ylim(-1.5, grid.N+0.5)
        self.ax.set_axis_off()

    def update_point_pos_size(self, val):
        new_pos = self.grid.displacement(val)
        new_size = self.grid.size_dot(val)
        self.points.set_offsets(new_pos)
        self.points.set_sizes(new_size)
        self.fig.canvas.draw_idle()
