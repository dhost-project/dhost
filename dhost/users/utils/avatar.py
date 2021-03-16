import hashlib
from io import BytesIO

from django.core.files import File
from PIL import Image, ImageDraw


def avatar_generator(username: str):
    extension = 'PNG'
    total_width = 256
    total_height = 256
    # over 15 the patern will start repeating itself
    rows = 12
    cols = 12
    background_color = '#f1f1f1'

    canvas = Image.new('RGB', (total_width, total_height), background_color)
    draw = ImageDraw.Draw(canvas)

    h = hashlib.md5(username.encode('utf-8')).hexdigest()

    bin_hash = bin(int(h, 16))[2:].zfill(8)

    # create matrix
    matrix = [[False for col in range(cols)] for row in range(rows)]

    half_cols = int(cols / 2)
    for row in range(rows):
        for col in range(half_cols):
            # fill matrix with `True` if the bit is `1`
            if bin_hash[(row * col) % len(bin_hash)] == '1':
                matrix[row][col] = True
                # to create the vertical symetry
                matrix[row][cols - col - 1] = True

    # generate pale color
    r = (int(h[:2], 16) % 128) + 127
    g = (int(h[2:4], 16) % 128) + 127
    b = (int(h[4:6], 16) % 128) + 127
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
