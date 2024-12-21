
# Function to generate finder pattern coordinates for a QR Code (Version 3)
def generate_finder_pattern_coordinates():
    coordinates = {
        "top_left": [],
        "top_right": [],
        "bottom_left": []
    }

    # Top-Left Finder Pattern
    for row in range(7):
        for col in range(7):
            coordinates["top_left"].append((row, col))

    # Top-Right Finder Pattern
    for row in range(7):
        for col in range(22, 29):  # Offset for top-right position
            coordinates["top_right"].append((row, col))

    # Bottom-Left Finder Pattern
    for row in range(22, 29):  # Offset for bottom-left position
        for col in range(7):
            coordinates["bottom_left"].append((row, col))

    return coordinates

# Function to add finder patterns to the QR matrix
def add_finder_patterns(QR):
    coordinates = generate_finder_pattern_coordinates()

    # Define black (8) and white (4) modules
    white = ('\N{white large square}')
    black = ('\N{black large square}')

    # Top-Left Finder Pattern
    for row, col in coordinates["top_left"]:
        if row in [0, 6] or col in [0, 6]:  # Outer black square
            QR[row][col] = black
        elif 1 <= row <= 5 and 1 <= col <= 5:  # Inner white square
            QR[row][col] = white
        if 2 <= row <= 4  and 2 <= col <= 4 :  # Center black module
            QR[row][col] = black

    # Top-Right Finder Pattern
    for row, col in coordinates["top_right"]:
        if row in [0, 6] or col in [22, 28]:  # Outer black square
            QR[row][col] = black
        elif 1 <= row <= 5 and 23 <= col <= 27:  # Inner white square
            QR[row][col] = white
        if 2 <= row <=4  and 24 <= col <=26:  # Center black module
            QR[row][col] = black

    # Bottom-Left Finder Pattern
    for row, col in coordinates["bottom_left"]:
        if row in [22, 28] or col in [0, 6]:  # Outer black square
            QR[row][col] = black
        elif 23 <= row <= 27 and 1 <= col <= 5:  # Inner white square
            QR[row][col] = white
        if 24 <= row <=26 and 2 <= col <= 4:  # Center black module
            QR[row][col] = black

    return QR

# Initialize a blank 29x29 QR matrix
QR = [[('\N{white large square}') for i in range(29)] for _ in range(29)]

# Add finder patterns to the matrix
QR = add_finder_patterns(QR)

# Print the QR matrix
for row in QR:
    print(row, end='\n')

