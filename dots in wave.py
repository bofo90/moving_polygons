import matplotlib.pyplot as plt
from grid_classes import Square_Lattice as SL
from grid_classes import Hex_Lattice as HL
from plotting import Figure_Lattice as Fig

N = 20
angle = 35
# approx number of wavelengths in the direction
fr = 1.3

grid = SL(N, angle, fr)
fig = Fig()

# fig.create_square_points(grid)
# fig.create_time_slider(fig.update_point_pos_size)

fig.create_square_squares(grid, t=0.25)


# plt.show()


N = 5
angle = 35
# approx number of wavelengths in the direction
fr = 1.3

grid = HL(N, angle, fr)
fig = Fig()

# fig.create_square_points(grid)
# fig.create_time_slider(fig.update_point_pos_size)

fig.create_square_squares(grid, t=0.25)


plt.show()
