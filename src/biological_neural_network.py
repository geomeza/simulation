from biological_neuron import BiologicalNeuron
from euler_estimator import EulerEstimator
import matplotlib.pyplot as plt

class BiologicalNeuralNetwork:

    def __init__(self, neurons, synapses):
        self.neurons = neurons
        self.synapses = synapses

    def get_derivatives(self):
        derivatives = []
        for i, n in enumerate(self.neurons):
            senders_to_synapse = [x for x,y in self.synapses if y == i]
            derivatives.append(lambda t, x, i=i, n=n, s = senders_to_synapse: n.dv_dt(t, x[i*4:(i+1)*4]) + sum([x[p*4] for p in s if x[p*4] > 50])/n.c)
            derivatives.append(lambda t, x, i=i, n=n: n.dn_dt(t, x[i*4:(i+1)*4]))
            derivatives.append(lambda t, x, i=i, n=n: n.dm_dt(t, x[i*4:(i+1)*4]))
            derivatives.append(lambda t, x, i=i, n=n: n.dh_dt(t, x[i*4:(i+1)*4]))
        return derivatives

        

    def get_starting_point(self):
        point = [0, []]
        for neuron in self.neurons:
            point[1].append(neuron.v_0)
            point[1].append(neuron.n_0)
            point[1].append(neuron.m_0)
            point[1].append(neuron.h_0)
        return point
