import math
from euler_estimator import EulerEstimator
import matplotlib.pyplot as plt

class BiologicalNeuron:

    def __init__(self, stimulus = lambda t: 0):
        self.s_t = stimulus
        self.v_0 = 0
        self.h_0 = 0.07 * (math.e**3 + 1)/((0.07 * (math.e**3 + 1))+1)
        self.n_0 = 1/(1.25*(math.e-1)+1)
        self.m_0 = 2.5/(2.5+4*(math.e**2.5 - 1))
        self.c = 1

    def a_n(self, t, x):
        return 0.01*(10-x[0])/(math.exp(0.1*(10-x[0]))-1)


    def b_n(self, t, x):
        return 0.125*math.exp(-x[0]/80)


    def a_m(self, t, x):
        return 0.1*(25-x[0])/(math.exp(0.1*(25-x[0]))-1)


    def b_m(self, t, x):
        return 4*math.exp(-x[0]/18)


    def a_h(self, t, x):
        return 0.07 * math.exp(-x[0]/20)


    def b_h(self, t, x):
        return 1/(math.exp(0.1*(30-x[0]))+1)


    def dn_dt(self, t, x):
        return self.a_n(t, x)*(1 - x[1]) - self.b_n(t, x)*x[1]


    def dm_dt(self, t, x):
        return self.a_m(t, x)*(1 - x[2]) - self.b_m(t, x)*x[2]


    def dh_dt(self, t, x):
        return self.a_h(t, x)*(1 - x[3]) - self.b_h(t, x)*x[3]

    def i_na(self, t, x):
        return self.g_na(t, x)*(x[0]-115)


    def g_na(self, t, x):
        return 120 * x[2]**3 * x[3]


    def i_k(self, t, x):
        return self.g_k(t, x)*(x[0]+12)


    def g_k(self, t, x):
        return 36 * x[1]**4


    def i_l(self, t, x):
        return self.g_l(t, x)*(x[0]-10.6)


    def g_l(self, t, x):
        return 0.3


    def dv_dt(self, t, x):
        return (self.s_t(t) - self.i_na(t, x) - self.i_k(t, x) - self.i_l(t, x))

    def plot_activity(self):
        euler = EulerEstimator(derivatives = [self.dv_dt, self.dn_dt, self.dm_dt, self.dh_dt], point = (0, (self.v_0, self.n_0, self.m_0, self.h_0)))
        plt.plot([n/2 for n in range(160)], [self.s_t(n/2) for n in range(160)])
        euler.plot([0, 80], step_size=0.02,file_name="photo.png")