import hashlib
from io import BytesIO

from django.conf import settings
from django.core.files import File
from PIL import Image, ImageDraw

EXTENSION = getattr(settings, 'AVATAR_EXTENSION', 'png')
DIMENSION = getattr(settings, 'AVATAR_DIMENSION', 256)
# number of squares per rows and columns
# over 15 the patern will start repeating itself
SQUARE_NUMBER = getattr(settings, 'AVATAR_SQUARE_NUMBER', 12)
BACKGROUND_COLOR = getattr(settings, 'AVATAR_BACKGROUND_COLOR', '#f2f2f2')
MARGIN = getattr(settings, 'AVATAR_MARGIN', 8)

TOTAL_WIDTH = DIMENSION
TOTAL_HEIGHT = DIMENSION
ROWS = SQUARE_NUMBER
COLS = SQUARE_NUMBER


def avatar_generator(username: str):
    """
    This will generate an image based on the hash of the username
    """

    canvas = Image.new('RGB', (TOTAL_WIDTH, TOTAL_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(canvas)

    h = hashlib.md5(username.encode('utf-8')).hexdigest()
    bin_hash = bin(int(h, 16))[2:].zfill(8)

    # create matrix
    matrix = [[False for col in range(COLS)] for row in range(ROWS)]

    half_cols = int(COLS / 2)
    for row in range(1, ROWS + 1):
        for col in range(1, half_cols + 1):
            # fill matrix with `True` if the bit is `1`
            if bin_hash[(row * col) % len(bin_hash)] == '1':
                matrix[row - 1][col - 1] = True
                # to create the vertical symetry
                matrix[row - 1][COLS - col] = True

    # generate pale color
    r = (int(h[:2], 16) % 69) + 114
    g = (int(h[2:4], 16) % 42) + 114
    b = (int(h[4:6], 16) % 100) + 114
    fg_color = (r, g, b)

    # color the image from the matrix
    block_width = (TOTAL_WIDTH - (MARGIN * 2)) / COLS
    block_height = (TOTAL_HEIGHT - (MARGIN * 2)) / ROWS

    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col]:
                draw.rectangle(
                    (
                        MARGIN + col * block_width,  # x1
                        MARGIN + row * block_height,  # y1
                        MARGIN + (col + 1) * block_width - 1,  # x2
                        MARGIN + (row + 1) * block_height - 1,  # y2
                    ),
                    fill=fg_color,
                )

    # create the file
    stream = BytesIO()
    canvas.save(stream, EXTENSION)

    avatar_name = '{}.{}'.format(username, EXTENSION)
    avatar = File(stream, name=avatar_name)

    return avatar
