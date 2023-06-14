from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='Advantage_system4.1',
))

h = {}

J = {
    ('Lisa','Timo'): 3,
    ('Lisa','Anna'): 5,
    ('Lisa','Tom'): 7,
    ('Lisa', 'Onur'): 6,
    ('Timo','Anna'): 5,
    ('Timo','Tom'): 3,
    ('Timo','Onur'): 8,
    ('Anna','Tom'): 5,
    ('Anna','Onur'): 2
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
    chain_strength=15,
    annealing_time=100,
)
dwave.inspector.show(response)
print(response)
