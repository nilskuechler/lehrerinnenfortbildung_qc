from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='Advantage_system4.1',
)

h = {
}

# Programmieren Sie hier die Werte der 
# Koppler wie in Aufgabe 1a in der Form
# (qubit1, qubit2): Kopplerwert,
J = {

}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)

dwave.inspector.show(response)
