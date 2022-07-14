import numpy as np


class Square_Lattice:
    def __init__(self, N, angle, fr) -> None:
        self.N = N
        self.dir = angle*np.pi/180
        self.fr = fr*2*np.pi/N

        self.create_lattice_points()
        self.k = np.array([np.cos(self.dir), np.sin(self.dir)])*self.fr
        self.rot_angles = np.random.uniform(-70, 70, size=len(self.pos))

    def create_lattice_points(self):
        pos = np.zeros((self.N, self.N, 2))
        pos[:, :, 0], pos[:, :, 1] = np.meshgrid(
            np.arange(self.N), np.arange(self.N))
        self.pos = np.reshape(pos, (-1, 2))

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
        return self.get_wave(t, 0.3, 1.1)

    def angle_square(self, t):
        return self.get_wave(t, 0, 1)*self.rot_angles
