import matplotlib.pyplot as plt
from grid_classes import Lattice as Lat
from plotting import Figure_Lattice as Fig

tot_num_poly = 500
angle = 35
# approx number of wavelengths in the direction
fr = 1.3

grid = Lat(tot_num_poly, "hex", 4, 3, angle, fr)
fig = Fig()

# fig.create_points(grid, slider=True)

fig.create_poly(grid, t=0.25)

plt.show()
