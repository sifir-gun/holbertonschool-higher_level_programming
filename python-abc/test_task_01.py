import unittest
from task_01_duck_typing import Circle, Rectangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=4)

    def test_rectangle_area(self):
        rectangle = Rectangle(width=4, height=7)
        self.assertEqual(rectangle.area(), 28)


if __name__ == '__main__':
    unittest.main()
