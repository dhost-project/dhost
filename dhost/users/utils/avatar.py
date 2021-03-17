import hashlib
from io import BytesIO

from django.conf import settings
from django.core.files import File
from PIL import Image, ImageDraw

AVATAR_EXTENSION = getattr(settings, 'AVATAR_EXTENSION', 'PNG')
AVATAR_DIMENSION = getattr(settings, 'AVATAR_DIMENSION', 256)
# number of squares per rows and columns
AVATAR_SQUARE_NUMBER = getattr(settings, 'AVATAR_SQUARE_NUMBER', 12)
AVATAR_BACKGROUND_COLOR = getattr(
    settings,
    'AVATAR_BACKGROUND_COLOR',
    '#f2f2f2',
)


def avatar_generator(username: str):
    extension = AVATAR_EXTENSION
    total_width = AVATAR_DIMENSION
    total_height = AVATAR_DIMENSION
    # over 15 the patern will start repeating itself
    rows = AVATAR_SQUARE_NUMBER
    cols = AVATAR_SQUARE_NUMBER
    background_color = AVATAR_BACKGROUND_COLOR

    canvas = Image.new('RGB', (total_width, total_height), background_color)
    draw = ImageDraw.Draw(canvas)

    h = hashlib.md5(username.encode('utf-8')).hexdigest()

    bin_hash = bin(int(h, 16))[2:].zfill(8)

    # create matrix
    matrix = [[False for col in range(cols)] for row in range(rows)]

    half_cols = int(cols / 2)
    for row in range(1, rows + 1):
        for col in range(1, half_cols + 1):
            # fill matrix with `True` if the bit is `1`
            if bin_hash[(row * col) % len(bin_hash)] == '1':
                matrix[row - 1][col - 1] = True
                # to create the vertical symetry
                matrix[row - 1][cols - col] = True

    # generate pale color
    r = (int(h[:2], 16) % 70) + 114
    g = (int(h[2:4], 16) % 43) + 114
    b = (int(h[4:6], 16) % 100) + 114
    fg_color = (r, g, b)

    # color the image
    block_width = total_width / cols
    block_height = total_height / rows

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]:
                draw.rectangle(
                    (
                        col * block_width,  # x1
                        row * block_height,  # y1
                        (col + 1) * block_width - 1,  # x2
                        (row + 1) * block_height - 1  # y2
                    ),
                    fill=fg_color
                )

    stream = BytesIO()
    canvas.save(stream, extension)

    avatar_name = '{}.{}'.format(username, extension.lower())

    avatar = File(stream, name=avatar_name)

    return avatar
