import numpy as np


class Square_Lattice:
    def __init__(self, N, angle, fr) -> None:
        self.num_edges = 4
        self.N = N
        self.dir = angle*np.pi/180

        self.create_lattice_points()
        self.rot_angles = np.random.uniform(-70, 70, size=len(self.pos))
        self.fr = fr*2*np.pi/(np.max(self.pos)-np.min(self.pos))
        self.k = np.array([np.cos(self.dir), np.sin(self.dir)])*self.fr

    def create_lattice_points(self):
        pos = np.zeros((self.N, self.N, 2)).astype(float)
        pos[:, :, 0], pos[:, :, 1] = np.meshgrid(
            np.arange(self.N), np.arange(self.N))
        self.pos = np.reshape(pos, (-1, 2))
        self.pos -= (self.N-1)/2

        self.furth_dist = np.max(np.sqrt(np.sum(self.pos**2, axis=1)))

    def sin_wave(self, t):
        x = np.sum(self.pos*self.k, axis=1)
        y = np.sin(x-2*np.pi*t)
        return y

    def get_wave(self, t, min, max):
        return (self.sin_wave(t)+1)*(max-min)/2+min

    def displacement(self, t):
        y = self.get_wave(t, -0.5, 0.5)
        new_disp = np.zeros(np.shape(self.pos))
        rot = self.dir+np.pi/4
        new_disp[:, 0] = np.cos(rot)*y
        new_disp[:, 1] = np.sin(rot)*y
        return self.pos+new_disp

    def size_dot(self, t):
        return self.get_wave(t, 2, 7)

    def size_square(self, t):
        return self.get_wave(t, 0.2, 0.8)

    def angle_square(self, t):
        return self.get_wave(t, 0, 1)*self.rot_angles


class Hex_Lattice:
    def __init__(self, N, angle, fr) -> None:
        self.num_edges = 6
        self.N = N
        self.dir = angle*np.pi/180

        self.create_lattice_points()
        self.rot_angles = np.random.uniform(-70, 70, size=len(self.pos))
        self.fr = fr*2*np.pi/(np.max(self.pos)-np.min(self.pos))
        self.k = np.array([np.cos(self.dir), np.sin(self.dir)])*self.fr

    def create_lattice_points(self):

        latt_pos = []
        deltas = [[1, 0, -1], [0, 1, -1], [-1, 1, 0],
                  [-1, 0, 1], [0, -1, 1], [1, -1, 0]]
        for r in range(self.N):
            x = 0
            y = -r
            z = +r
            latt_pos.append([x, y, z])
            for j in range(6):
                if j == 5:
                    num_of_hexas_in_edge = r-1
                else:
                    num_of_hexas_in_edge = r
                for i in range(num_of_hexas_in_edge):
                    x = x+deltas[j][0]
                    y = y+deltas[j][1]
                    z = z+deltas[j][2]
                    latt_pos.append([x, y, z])

        latt_pos = np.array(latt_pos)

        y = 3/2 * latt_pos[:, 2] * 0.6
        x = np.sqrt(3) * (latt_pos[:, 2]/2 + latt_pos[:, 1]) * 0.6
        self.pos = np.append([x], [y], axis=0).T

        self.furth_dist = np.max(np.sqrt(np.sum(self.pos**2, axis=1)))

    def sin_wave(self, t):
        x = np.sum(self.pos*self.k, axis=1)
        y = np.sin(x-2*np.pi*t)
        return y

    def get_wave(self, t, min, max):
        return (self.sin_wave(t)+1)*(max-min)/2+min

    def displacement(self, t):
        y = self.get_wave(t, -0.5, 0.5)
        new_disp = np.zeros(np.shape(self.pos))
        rot = self.dir+np.pi/4
        new_disp[:, 0] = np.cos(rot)*y
        new_disp[:, 1] = np.sin(rot)*y
        return self.pos+new_disp

    def size_dot(self, t):
        return self.get_wave(t, 2, 7)

    def size_square(self, t):
        return self.get_wave(t, 0.2, 0.8)

    def angle_square(self, t):
        return self.get_wave(t, 0, 1)*self.rot_angles


class Tri_Lattice:
    def __init__(self, N, angle, fr) -> None:
        self.num_edges = 3
        self.N = N
        self.dir = angle*np.pi/180

        self.create_lattice_points()
        self.rot_angles = np.random.uniform(-70, 70, size=len(self.pos))
        self.fr = fr*2*np.pi/(np.max(self.pos)-np.min(self.pos))
        self.k = np.array([np.cos(self.dir), np.sin(self.dir)])*self.fr

    def create_lattice_points(self):

        pos = []
        drift_x = 0
        drift_y = 0
        for i in reversed(range(self.N)):
            print(i)
            for j in range(i+1):
                print(j)
                pos.append([drift_x+j, drift_y])
            drift_y -= np.sqrt(3)/2
            drift_x += 0.5

        self.pos = np.array(pos)
        center = np.mean(self.pos, axis=0)
        self.pos[:, 0] = self.pos[:, 0] - center[0]
        self.pos[:, 1] = self.pos[:, 1] - center[1]

        self.furth_dist = np.max(np.sqrt(np.sum(self.pos**2, axis=1)))

    def sin_wave(self, t):
        x = np.sum(self.pos*self.k, axis=1)
        y = np.sin(x-2*np.pi*t)
        return y

    def get_wave(self, t, min, max):
        return (self.sin_wave(t)+1)*(max-min)/2+min

    def displacement(self, t):
        y = self.get_wave(t, -0.5, 0.5)
        new_disp = np.zeros(np.shape(self.pos))
        rot = self.dir+np.pi/4
        new_disp[:, 0] = np.cos(rot)*y
        new_disp[:, 1] = np.sin(rot)*y
        return self.pos+new_disp

    def size_dot(self, t):
        return self.get_wave(t, 2, 7)

    def size_square(self, t):
        return self.get_wave(t, 0.2, 0.8)

    def angle_square(self, t):
        return self.get_wave(t, 0, 1)*self.rot_angles
