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
# Qubit 421 = Lauch
# Qubit 466 = Mais
# Qubit 3302 = Sellerie
# Qubit 3347 = Erbse
J = {
    (421,3302): -1,
    (421,3347): +1,
    (466,3302): +1,
    (466,3347): -1,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)

dwave.inspector.show(response)
print(response)

