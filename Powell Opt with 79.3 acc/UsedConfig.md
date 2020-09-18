```python
feature_map = ZFeatureMap(feature_dim = 3, reps = 2, insert_barriers = True)
variational_circuit = RealAmplitudes(feature_dims = 3, reps = 2, entanglement = 'full')
optimizer = POWELL(maxiter = 500, tol = 0.07)
```