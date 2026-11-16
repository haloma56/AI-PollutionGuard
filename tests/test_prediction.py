from ai.predict import predict_pollution

result = predict_pollution(
    pm25=35,
    pm10=60,
    temperature=25,
    humidity=50
)
assert result is not None
print("Predicted CO:", result)