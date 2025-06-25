# Detección de anomalías (valores > 0.7)
anomaly_scores = torch.tensor([0.2, 0.8, 0.4, 0.9])
corrected = predictor.stabilize_timeline(anomaly_scores)
