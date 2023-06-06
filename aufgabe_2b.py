from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='Advantage_system4.1',
))

h = {}

J = {
    ('Anna','Lisa'): -1, ('Anna','Timo'): +1, ('Anna','Lynn'): -1, ('Anna','Jonas'): +1,
    ('Tom','Lisa'): +1, ('Tom','Timo'): -1, ('Tom','Jonas'): -1,
    ('Pia','Timo'): +1, ('Pia','Lynn'): -1, ('Pia','Jonas'): -1,
    ('Leon','Lisa'): +1, ('Leon','Timo'): -1, ('Leon','Lynn'): -1, ('Leon','Jonas'): +1,

    ('Lisa','Emily'): +1, ('Lynn','Sara'): +1, ('Jonas','Jill'): -1,

    # Ersetzen Sie hier "0" durch die korrekten Werte der Koppler
    ('Eva','Emily'): 0, ('Eva','Ben'): 0, ('Eva','Sara'): 0, ('Eva','Jill'): 0,
    ('Luis','Emily'): 0, ('Luis','Ben'): 0, ('Luis','Sara'): 0, ('Luis','Jill'): 0,
    ('Jan','Ben'): 0, ('Jan','Sara'): 0, ('Jan','Jill'): 0,
    ('Nils','Emily'): 0, ('Nils','Ben'): 0, ('Nils','Sara'): 0, ('Nils','Jill'): 0,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=1000,
)
dwave.inspector.show(response)
print(response)
