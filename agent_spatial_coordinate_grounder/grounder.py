"""Translates normalized vision model coordinates to absolute screen pixels."""
from typing import Dict, List, Optional, Tuple, Any

class ScreenPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_tuple(self) -> Tuple[int, int]:
        return self.x, self.y

class BoundingBox:
    def __init__(self, ymin: float, xmin: float, ymax: float, xmax: float):
        # Coordinates in 0.0 - 1.0 or 0 - 1000 scale
        if ymax > 1.0 or xmax > 1.0:
            self.ymin = ymin / 1000.0
            self.xmin = xmin / 1000.0
            self.ymax = ymax / 1000.0
            self.xmax = xmax / 1000.0
        else:
            self.ymin = ymin
            self.xmin = xmin
            self.ymax = ymax
            self.xmax = xmax

class SpatialCoordinateGrounder:
    """Grounds normalized bounding boxes into exact hardware screen coordinates."""

    def __init__(self, screen_width: int = 1920, screen_height: int = 1080, dpi_scale: float = 1.0):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.dpi_scale = dpi_scale

    def ground_box(self, box: BoundingBox) -> Tuple[int, int, int, int]:
        left = int(box.xmin * self.screen_width * self.dpi_scale)
        top = int(box.ymin * self.screen_height * self.dpi_scale)
        right = int(box.xmax * self.screen_width * self.dpi_scale)
        bottom = int(box.ymax * self.screen_height * self.dpi_scale)
        return left, top, right, bottom

    def get_click_target(self, box: BoundingBox, margin_ratio: float = 0.5) -> ScreenPoint:
        left, top, right, bottom = self.ground_box(box)
        center_x = left + int((right - left) * margin_ratio)
        center_y = top + int((bottom - top) * margin_ratio)

        # Clamping to screen boundaries
        clamped_x = max(0, min(int(self.screen_width * self.dpi_scale) - 1, center_x))
        clamped_y = max(0, min(int(self.screen_height * self.dpi_scale) - 1, center_y))
        return ScreenPoint(clamped_x, clamped_y)
