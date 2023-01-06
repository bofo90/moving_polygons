import matplotlib.pyplot as plt
from grid_classes import Square_Lattice as SL
from plotting import Figure_Lattice as Fig

num_poly = 4
angle = 35
# approx number of wavelengths in the direction
fr = 1.3

grid = SL(num_poly, "hex", 4, 3, angle, fr)
fig = Fig(negative=True)

fig.create_points(grid, slider=True)

# fig.create_poly(grid, t=0.25, slider=True)

plt.show()
