import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D
from grid_classes import Square_Lattice as SL
from plotting import Figure_Lattice as Fig

N = 10
angle = 35
# approx number of wavelengths in the direction
fr = 1.3

grid = SL(N, angle, fr)
fig = Fig()

# fig.create_square_points(grid)
# fig.create_time_slider(fig.update_point_pos_size)

fig.create_square_squares(grid, t=0.25)


plt.tight_layout()
plt.show()
