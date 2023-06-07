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
    ('Eva','Emily'): -1, ('Eva','Ben'): +1, ('Eva','Sara'): -1, ('Eva','Jill'): +1,
    ('Luis','Emily'): +1, ('Luis','Ben'): -1, ('Luis','Sara'): +1, ('Luis','Jill'): +1,
    ('Jan','Ben'): -1, ('Jan','Sara'): +1, ('Jan','Jill'): -1,
    ('Nils','Emily'): -1, ('Nils','Ben'): +1, ('Nils','Sara'): -1, ('Nils','Jill'): +1,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=1000,
)
dwave.inspector.show(response)
print(response)
