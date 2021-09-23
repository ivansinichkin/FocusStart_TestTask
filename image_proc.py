import numpy as np


def black_or_white(image):
    N, M, L = image.shape
    image2_2d = image.reshape(N * M, 3)
    unique_pixels, hist = np.unique(image2_2d, return_counts=True, axis=0)
    # убеждаемся, что по краям массива unique_pixels белые и черные пиксели
    black_exist = np.all(unique_pixels[0] == [0, 0, 0])
    white_exist = np.all(unique_pixels[-1] == [255, 255, 255])

    if black_exist and not white_exist:
        answer = 'Чёрных пикселей больше, чем белых.' \
                 ' \n Чёрных: ' + str(hist[0]) + '. Белых нет'
    if not black_exist and white_exist:
        answer = 'Белых пикселей больше, чем чёрных.' \
                 ' \n Белых: ' + str(hist[-1]) + '. Чёрных нет'
    if not black_exist and not white_exist:
        answer = 'Ни белых, ни чёрных пикселей на картинке нет.'
    if black_exist and white_exist:
        if hist[0] > hist[-1]:
            answer = 'Чёрных пикселей больше, чем белых.' \
                     ' \n Чёрных: ' + str(hist[0]) + ', белых: ' +\
                     str(hist[-1]) + '.'
        if hist[-1] > hist[0]:
            answer = 'Белых пикселей больше, чем чёрных.' \
                     ' \n Белых: ' + str(hist[-1]) + ', чёрных: ' +\
                     str(hist[0]) + '.'
        if hist[0] == hist[-1]:
            answer = 'Чёрных и белых пикселей одинаковое ' \
                     'количество. \n Чёрных: ' + str(hist[0]) +\
                     ', белых: ' + str(hist[-1]) + '.'
    return answer


def hex2rgb(hex_code):
    hex_code = str(hex_code)
    rgb = np.array([], dtype=int)
    for i in [0, 2, 4]:
        dec = int(hex_code[i: i+2], 16)
        rgb = np.append(rgb, dec)
    return np.array(rgb)


def count_hex_pixels(image, hex_code):
    N, M, L = image.shape
    image2_2d = image.reshape(N * M, 3)
    unique_pixels, hist = np.unique(image2_2d, return_counts=True, axis=0)
    rgb = hex2rgb(hex_code)
    index=0
    for i in unique_pixels:
        if np.all(i == rgb):
            answer = 'На изображении ' + str(hist[index]) +\
                     ' пикселей с hex-кодом ' + str(hex_code) + '.'
            return answer
        index += 1
    return 'На изображении нет пикселей с hex-кодом ' + str(hex_code) + '.'
