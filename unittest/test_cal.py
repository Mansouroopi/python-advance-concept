import unittest
import cal


class TestCal(unittest.TestCase):
    """docstring for TestCalculator."""

    def setUp(self):
        print('setting up testing...')

    def tearDown(self):
        print('tearing down testing....')

    def test_add(self):
        self.assertEqual(cal.add(10, 5), 15, 'success')
        self.assertEqual(cal.add(-10, -5), -15, 'success')
        self.assertEqual(cal.add(10, -5), 5, 'success')

    def test_sub(self):
        self.assertEqual(cal.sub(10, 5), 5, 'message')
        self.assertEqual(cal.sub(10, -5), 15, 'message')
        self.assertEqual(cal.sub(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(cal.multiply(10, 5), 50, 'message')
        self.assertEqual(cal.multiply(10, -5), -50, 'message')
        self.assertEqual(cal.multiply(-10, - 5), 50, 'message')
        self.assertEqual(cal.multiply(10, 0), 0, 'message')

    def test_divide(self):
        self.assertEqual(cal.divide(10, 5), 2, 'message')
        self.assertEqual(cal.divide(10, -5), -2, 'message')
        self.assertRaises(ValueError, cal.divide, 10, 0)
        with self.assertRaises(ValueError):
            cal.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
