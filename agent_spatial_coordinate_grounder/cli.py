"""CLI for agent-spatial-coordinate-grounder."""
import sys
import argparse
from .grounder import SpatialCoordinateGrounder, BoundingBox

def main():
    parser = argparse.ArgumentParser(description="Agent Spatial Coordinate Grounder CLI")
    parser.add_argument("--demo", action="store_true", help="Run coordinate grounding demo")
    args = parser.parse_args()

    if args.demo:
        grounder = SpatialCoordinateGrounder(screen_width=1920, screen_height=1080)
        box = BoundingBox(100, 200, 150, 400)  # Normalized 1000 scale
        coords = grounder.ground_box(box)
        pt = grounder.get_click_target(box)
        print(f"[+] Grounded box pixels: {coords}")
        print(f"[+] Optimal click point: X={pt.x}, Y={pt.y}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
