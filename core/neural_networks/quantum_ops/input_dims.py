# Secuencia de entrada (batch, timesteps, features)
input_seq = torch.randn(1, 10, 128)  

# Predicción de 5 pasos temporales
predictions = predictor.predict_timeline(input_seq, n_steps=5)
