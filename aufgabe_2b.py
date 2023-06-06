from dwave.system import DWaveSampler
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='Advantage_system4.1',
))

h = {}

J = {
    (0,4): -1, (0,5): +1, (0,6): -1, (0,7): +1,
    (1,4): +1, (1,5): -1, (1,7): -1,
    (2,5): +1, (2,6): -1, (2,7): -1,
    (3,4): +1, (3,5): -1, (3,6): -1, (3,7): +1,

    (4,12): +1, (6,14): +1, (7,15): -1,

    # Ersetzen Sie hier "0" durch die korrekten Werte der Koppler
    (8,12): 0, (8,13): 0, (8,14): 0, (8,15): 0,
    (9,12): 0, (9,13): 0, (9,14): 0, (9,15): 0,
    (10,13): 0, (10,14): 0, (10,15): 0,
    (11,12): 0, (11,13): 0, (11,14): 0, (11,15): 0,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=1000,
)
dwave.inspector.show(response)
