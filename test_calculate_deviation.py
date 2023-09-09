import unittest

class TestCalculateDeviation(unittest.TestCase):
    def test_deviation_calculation(self):
        y_actual = np.array([1.0, 2.0, 3.0])
        y_ideal = np.array([0.5, 2.5, 3.5])
        deviation = calculate_deviation(y_actual, y_ideal)
        self.assertAlmostEqual(deviation, 0.5, delta=1e-6)

if __name__ == '__main__':
    unittest.main()
