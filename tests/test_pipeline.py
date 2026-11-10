import unittest

from ai.preprocessing import load_and_clean_data
from ai.predict import predict_pollution


class TestPollutionGuard(unittest.TestCase):

    def test_dataset_loading(self):
        X, y = load_and_clean_data()

        self.assertGreaterEqual(len(X), 5)
        self.assertEqual(len(X), len(y))

        self.assertEqual(
            list(X.columns),
            ["PM2.5", "PM10", "Temperature", "Humidity"]
        )

    def test_model_prediction(self):
        prediction = predict_pollution(
            pm25=20,
            pm10=40,
            temperature=25,
            humidity=55
        )

        self.assertIsInstance(prediction, float)
        self.assertGreaterEqual(prediction, 0)


if __name__ == "__main__":
    unittest.main()