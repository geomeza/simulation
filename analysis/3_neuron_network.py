import sys
sys.path.append('src')
from biological_neuron import BiologicalNeuron
from biological_neural_network import BiologicalNeuralNetwork
from euler_estimator import EulerEstimator
import matplotlib.pyplot as plt

def electrode_voltage(t):
        if t > 10 and t < 11:
            return 150
        elif t > 20 and t < 21:
            return 150
        elif t > 30 and t < 40:
            return 150
        elif t > 50 and t < 51:
            return 150
        elif t > 53 and t < 54:
            return 150
        elif t > 56 and t < 57:
            return 150
        elif t > 59 and t < 60:
            return 150
        elif t > 62 and t < 63:
            return 150
        elif t > 65 and t < 66:
            return 150
        return 0
neuron_0 = BiologicalNeuron(stimulus=electrode_voltage)
neuron_1 = BiologicalNeuron()
neuron_2 = BiologicalNeuron()
neurons = [neuron_0, neuron_1, neuron_2]
synapses = [(0, 1), (1, 2)]
network = BiologicalNeuralNetwork(neurons, synapses)
euler = EulerEstimator(
    derivatives=network.get_derivatives(),
    point=network.get_starting_point()
)
plt.plot([n/2 for n in range(160)], [electrode_voltage(n/2)
                                        for n in range(160)])
euler.plot([0, 80], step_size=0.001,file_name="neural_network.png")