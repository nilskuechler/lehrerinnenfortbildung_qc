from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='Advantage_system4.1',
)

# Qubit 421 = Lauch
# Qubit 3302 = Sellerie
# Qubit 3347 = Erbsen
# Qubit 466 = Mais

# ISING:
# E = s421 - s421 s3302 + s421 s3347 + s466 s3302 - s466 s3347
# QUBO: (si = 2*xi - 1)
# E = 2 x421 - 4 x421 x3302 + 4 x421 x3347 + 4 x466 x3302 - 4 x466 x3347 + 1

Q = {
    (421,421): +2,
    (421,3302): -4,
    (421,3347): +4,
    (466,3302): +4,
    (466,3347): -4,
}
response = sampler.sample_qubo(
    Q, 
    num_reads=100,
)
dwave.inspector.show(response)
print(response)
