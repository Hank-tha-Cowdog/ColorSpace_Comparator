# ColorSpace_Comparator
A Python visualization tool for comparing color space primaries using CIE chromaticity diagrams.

![colorspace_comparator](https://github.com/user-attachments/assets/884afed8-2990-425f-badc-0779fb9f7d5a)

## Features
- Visual comparison of different color space gamuts
- Currently supports Rec.601, Rec.709, and custom color space plotting
- Interactive matplotlib-based visualization
- CIE xy chromaticity coordinate plotting
- Color-coded gamut triangles for easy comparison

## Technical Details
- Plots precise chromaticity coordinates for standard color spaces
- Supports custom primary input for comparison
- Generates annotated diagrams with primary point labeling
- Grid overlay for precise coordinate reading
- Polygon-based gamut boundary visualization

## Dependencies
- Python 3.7 or higher
- matplotlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/color-space-comparator.git
cd color-space-comparator
```

2. Install required dependency:
```bash
pip install matplotlib
```

## Usage
1. Run the script:
```bash
python color_space_comparator.py
```

2. To compare different color spaces, modify the `dcip3_primaries` dictionary with your custom chromaticity coordinates:
```python
dcip3_primaries = {
    'red': (x, y),
    'green': (x, y),
    'blue': (x, y)
}
```

## Output
- Generates a plot showing the gamut triangles of:
  - Rec.601 (solid blue line)
  - Rec.709 (dashed red line)
  - Custom color space (dash-dot green line)
- Primary points are marked and labeled
- CIE xy coordinates displayed on axes
