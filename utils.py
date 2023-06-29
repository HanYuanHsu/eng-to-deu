N_CHAR = 132

def char_to_index(ch):
    if ch == 'ä':
        return 128
    if ch == 'ö':
        return 129
    if ch == 'ü':
        return 130

    try:
        ind = ord(ch)
    except:
        return N_CHAR - 1 # unknown character
    else:
        return ind if (ind >= 0 and ind < N_CHAR-1) else N_CHAR - 1





