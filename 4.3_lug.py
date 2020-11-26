import numpy as np
import matplotlib.pyplot as plt


class Lug:
    def __init__(self, w, D, t):
        self.A1 = (w - D) / 2 + D/2 * (1 - np.cos(np.pi/4))
        self.A2 = (w - D) / 2
        self.A3 = (w - D) / 2
        self.A4 = (w - D) / 2 + D/2 * (1 - np.cos(np.pi/4))
        self.D = D
        self.t = t
        self.A_av = float()
        self.A_br = float()
        self.A_t = float()

    def simplify(self, w, D, t):
        # self.A3 = self.A2
        # self.A1 = self.A2 + self.D / 2 * (1 - np.cos(np.pi/4))
        # self.A4 = self.A1
        self.A1 = (w - D) / 2 + D / 2 * (1 - np.cos(np.pi / 4))
        self.A2 = (w - D) / 2
        self.A3 = (w - D) / 2
        self.A4 = (w - D) / 2 + D / 2 * (1 - np.cos(np.pi / 4))
        self.D = D
        self.t = t
        self.A_av = 6 / (3 / (self.A1 * self.t) + 1 / (self.A2 * self.t) + 1 / (self.A3 * self.t) + 1 / (self.A4 * self.t))
        self.A_br = self.D * self.t
        self.A_t = self.t * 2 * self.A2

    def volume(self):
        L = self.D / 2 * 1.5  # 1.5 is arbitrarily chosen
        area = (self.D + 2 * self.A2) * L + 0.5 * np.pi * (self.D / 2 + self.A2) ** 2 - np.pi * (self.D / 2) ** 2
        return area * self.t

    def print_dim(self):
        print(f"A1: {round(self.A1, 3)}, A2: {round(self.A2, 3)}, A3: {round(self.A3, 3)}, A4: {round(self.A4, 3)}, D: {round(self.D, 3)}, t: {round(self.t, 3)}, ")



class Material:
    materials = []

    def __init__(self, sigma_y, density):
        self.sigma_y = sigma_y
        self.density = density
        Material.materials.append(self)

    def mass(self, volume):
        return self.density * volume


# Materials
Al_2014_T6 = Material(382000000, 2800)
Al_2024_T3 = Material(310000000, 2765)
Al_7075_T6 = Material(444500000, 2800)


def curve_transverse(x):
    """input is A_av/A_br, output is stress concentration factor"""
    y = 2.546639 + (-0.0006606586 - 2.546639)/(1 + (x/1.39298)**1.134334)  # curve fit to curve 3 Fig. D1:13
    return y


def curve_axial(x):
    """input is W/D, output is stress concentration factor"""
    y = - x / 10 + 1.1  # approximation from all the curves
    return y


F = 3338
F_a = F / 2  # axial load
F_t = F / 2  # transverse laod
F_x = 1.25 * 7 * 9.80665 * 192.5 * 0.25



Lug = Lug(0.04, 0.018, 0.01)
# Lug.simplify(0, 1, 1)


"""stress analysis"""
def failure_check():
    sigma_y_a = F_a / curve_axial((Lug.D + 2 * Lug.A2)/Lug.D) / Lug.A_t
    sigma_y_t = F_t / curve_transverse(Lug.A_av / Lug.A_br) / Lug.A_br
    L = Lug.D * 1.5
    sigma_bending = F_x * L * 6 / w / Lug.t**2
    return max(sigma_y_a, sigma_y_t, sigma_bending, sigma_bending + sigma_y_a)


"""iteration section"""
#np.array =([D, t, w, material, mass])
D1 = 0.00346
table = np.array([0, 0, 0, 0, 0])
for d in np.arange(D1, 0.06, 0.001):
    for t in np.arange(0.001, 0.01, 0.001):
        for w in np.arange(d + 0.02, 0.08, 0.005):
            for material in Material.materials:
                Lug.simplify(w, d, t)
                mass = material.density * Lug.volume() * 2  # this does not account for the back up plate
                instance = np.array([d, t, w, Material.materials.index(material), mass])
                sigma_max = failure_check()
                if material.sigma_y > sigma_max:  # maybe add a safety factor?
                    table = np.vstack((table, instance))
                else:
                    pass

print(np.array(["D1", "t1", "w", "material", "mass"]))
table = table[table[:, 4].argsort()]
print(table)
print(table.shape)


# example
def lug_get_MS(dim, mat, loads):
    """do calculations for the maximum loads with these dimensions and this material"""
    Lug.simplify(dim["w1"], dim["D1"], dim["t1"])
    stress_max = failure_check()
    ms = stress_max / mat['sigma_y'] - 1
    return ms