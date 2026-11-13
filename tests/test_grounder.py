"""Unit tests for agent-spatial-coordinate-grounder."""
import unittest
from agent_spatial_coordinate_grounder.grounder import SpatialCoordinateGrounder, BoundingBox

class TestSpatialGrounder(unittest.TestCase):
    def setUp(self):
        self.grounder = SpatialCoordinateGrounder(1000, 1000)

    def test_center_calculation(self):
        box = BoundingBox(0.2, 0.2, 0.4, 0.4)
        pt = self.grounder.get_click_target(box)
        self.assertEqual(pt.x, 300)
        self.assertEqual(pt.y, 300)

    def test_thousand_scale_conversion(self):
        box = BoundingBox(200, 200, 400, 400)
        pt = self.grounder.get_click_target(box)
        self.assertEqual(pt.x, 300)
        self.assertEqual(pt.y, 300)

    def test_clamping(self):
        box = BoundingBox(990, 990, 1200, 1200)
        pt = self.grounder.get_click_target(box)
        self.assertEqual(pt.x, 999)
        self.assertEqual(pt.y, 999)

if __name__ == "__main__":
    unittest.main()
