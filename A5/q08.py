from unittest import TestCase


class TestLineIntersect(TestCase):

    def test_line_intersect_parallel(self):
        self.assertEqual(line_intersect([[0.0, 0.0], [1.0, 3.0]], [[0.0, 1.0], [1.0, 4.0]]), None)

    def test_line_intersect_coincident(self):
        self.assertEqual(line_intersect([[0.0, 0.0], [1.0, 3.0]], [[0.0, 0.0], [1.0, 3.0]]), [[0.0, 0.0], [1.0, 3.0]])

    def test_line_intersect_perpendicular(self):
        # return intersecting point
        self.assertEqual(line_intersect([[3.0, -5.0], [3.0, 15.0]], [[-5.0, 5.0], [10.0, 5.0]]), [3.0, 5.0])

    def test_line_intersect_once(self):
        # return intersecting point
        self.assertEqual(line_intersect([[-2.0, -4.0], [0.0, 2.0]], [[-2.0, -2.0], [0.0, 0.0]]), [-1.0, -1.0])
