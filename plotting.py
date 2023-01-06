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

    def create_poly(self, grid, t=0, slider=False):

        self.fig = plt.figure(figsize=(6, 6), facecolor=self.mid)
        self.fig.subplots_adjust(left=0.,
                                 bottom=0.,
                                 right=1.,
                                 top=1.)
        self.ax = plt.subplot(111)

        self.grid = grid

        red_pat = np.random.random(len(grid.pos)) < 0.95
        self.fill_color = [self.white if i else self.color for i in red_pat]

        self.pats = []
        self.update_poly(t)

        d = 0.65
        big_frame = patches.RegularPolygon(
            (0, 0), grid.big_poly, grid.furth_dist+d,
            np.pi/grid.big_poly, fc=self.gray, ec=self.mid, zorder=0)
        self.ax.add_patch(big_frame)
        self.ax.set_xlim(-grid.furth_dist-2, grid.furth_dist+2)
        self.ax.set_ylim(-grid.furth_dist-2, grid.furth_dist+2)
        self.ax.set_axis_off()

        if slider:
            self.create_time_slider(self.update_poly)

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

    def update_poly(self, val):
        new_size = self.grid.size_poly(val)
        new_angle = self.grid.angle_poly(val)

        [p.remove() for p in self.pats]

        self.pats = [patches.RegularPolygon(self.grid.pos[i, :],
                                            self.grid.smal_poly,
                                            new_size[i],
                                            np.pi/self.grid.smal_poly,
                                            fc=self.fill_color[i],
                                            ec=self.gray,
                                            linewidth=1)
                     for i in range(len(self.grid.pos))]

        for i, p in enumerate(self.pats):
            p.set_transform(Affine2D().rotate_deg_around(
                *self.grid.pos[i, :], new_angle[i])+self.ax.transData)
            self.ax.add_patch(p)

        self.fig.canvas.draw_idle()

        # for i, p in enumerate(self.pats):
        #     # p.set_xy(self.grid.pos[i, :]-new_size[i]/2)
        #     p.set_transform(Affine2D().rotate_deg_around(
        #         *self.grid.pos[i, :], new_angle[i])+self.ax.transData)
        #     p.set(radius=new_size[i])

    def create_points(self, grid, slider=False):

        self.fig = plt.figure(figsize=(6, 6), facecolor=self.white)
        self.ax = plt.subplot(111)

        self.grid = grid
        sizes = grid.size_dot(0)
        displ = grid.displacement(0)

        self.points = self.ax.scatter(
            displ[:, 0], displ[:, 1], s=sizes, c=self.gray)

        self.ax.set_xlim(-grid.furth_dist-2, grid.furth_dist+2)
        self.ax.set_ylim(-grid.furth_dist-2, grid.furth_dist+2)
        self.ax.set_axis_off()

        if slider:
            self.create_time_slider(self.update_points)

    def update_points(self, val):
        new_pos = self.grid.displacement(val)
        new_size = self.grid.size_dot(val)
        self.points.set_offsets(new_pos)
        self.points.set_sizes(new_size)
        self.fig.canvas.draw_idle()
