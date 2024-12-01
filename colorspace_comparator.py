import matplotlib.pyplot as plt

# Chromaticity coordinates for Rec. 601
rec601_primaries = {
    'red': (0.630, 0.340),
    'green': (0.310, 0.595),
    'blue': (0.155, 0.070)
}

# Chromaticity coordinates for Rec. 709
rec709_primaries = {
    'red': (0.640, 0.330),
    'green': (0.300, 0.600),
    'blue': (0.150, 0.060)
}

# Chromaticity coordinates from the DCI-P3
dcip3_primaries = {
    'red': (0.7347, 0.2653),
    'green': (0.14, 0.86),
    'blue': (0.1, -0.02985)
}

# Plotting the chromaticity diagram
fig, ax = plt.subplots()

# Plot Rec. 601 triangle
rec601_triangle = plt.Polygon([
    rec601_primaries['red'],
    rec601_primaries['green'],
    rec601_primaries['blue']
], fill=None, edgecolor='blue', label='Rec. 601')

# Plot Rec. 709 triangle
rec709_triangle = plt.Polygon([
    rec709_primaries['red'],
    rec709_primaries['green'],
    rec709_primaries['blue']
], fill=None, edgecolor='red', linestyle='--', label='Rec. 709')

# Plot DCI-P3 triangle
dcip3_triangle = plt.Polygon([
    dcip3_primaries['red'],
    dcip3_primaries['green'],
    dcip3_primaries['blue']
], fill=None, edgecolor='green', linestyle='-.', label='DCI-P3 Primaries')

ax.add_patch(rec601_triangle)
ax.add_patch(rec709_triangle)
ax.add_patch(dcip3_triangle)

# Annotate primary colors for Rec. 601
for primary, (x, y) in rec601_primaries.items():
    ax.plot(x, y, 'bo')
    ax.text(x, y, f'Rec. 601 {primary}', fontsize=9, ha='right')

# Annotate primary colors for Rec. 709
for primary, (x, y) in rec709_primaries.items():
    ax.plot(x, y, 'ro')
    ax.text(x, y, f'Rec. 709 {primary}', fontsize=9, ha='right')

# Annotate primary colors for DCI-P3
for primary, (x, y) in dcip3_primaries.items():
    ax.plot(x, y, 'go')
    ax.text(x, y, f'dcip3 {primary}', fontsize=9, ha='right')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Chromaticity Diagram: Rec. 601 vs Rec. 709 vs DCI-P3 Primaries')
ax.legend()

plt.grid(True)
plt.show()
