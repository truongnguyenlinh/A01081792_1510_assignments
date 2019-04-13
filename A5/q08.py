from unittest import TestCase


def line_intersect(line_1: list, line_2: list):
    """Determine whether lines entered intersect, coincide, are parallel or are perpendicular.

    PRECONDITION line_1 must have length 2, elements must be 2 lists
    PRECONDITION line_2 must have length 2, elements must be 2 lists"""
    line_1_slope = (line_1[0][1] - line_1[1][1]) / (line_1[0][0] - line_1[1][0])
    line_2_slope = (line_2[0][1] - line_2[1][1]) / (line_2[0][0] - line_2[1][0])
    line_1_intercept = (line_1[0][1] - line_1_slope * line_1[0][0])
    line_2_intercept = (line_2[0][1] - line_2_slope * line_2[0][0])
    # intersect = [(line_1_slope - line_2_slope)/(line_2_intercept - line_1_intercept),
    #              line_1_slope(line_1_slope - line_2_slope)/(line_2_intercept - line_1_intercept) + line_1_intercept]

    if line_1_slope == line_2_slope and line_1_intercept != line_2_intercept:
        return None
    elif line_1_slope == line_2_slope and line_1_intercept == line_2_intercept:
        return line_1
    # else:
    #     return intersect


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
