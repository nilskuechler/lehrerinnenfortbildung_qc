from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='Advantage_system4.1',
)

# Programmierung der bias hi
h = {
    421: 0,
    3302: 0,
}

# Programmierung der Koppler Jij
J = {
    (421,3302): +1,  # Beispiel
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)

dwave.inspector.show(response)
