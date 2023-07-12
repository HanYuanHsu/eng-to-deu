import re
N_CHAR = 135

############
# the ascii characters are mapped to their ascii indices
# ä is mapped to 128
# ö is mapped to 129
# ü is mapped to 130
# ß is mapped to 131
# <SOS> is mapped to 132
# <EOS> is mapped to 133
# the rest, unknown, is mapped to 134
############ 


def char_to_index(ch):
    if ch == 'ä':
        return 128
    if ch == 'ö':
        return 129
    if ch == 'ü':
        return 130
    if ch == 'ß':
        return 131
    if ch == '<SOS>':
        return 132
    if ch == '<EOS>':
        return 133

    try:
        ind = ord(ch)
    except:
        return N_CHAR - 1 # unknown character
    else:
        return ind if (ind >= 0 and ind < N_CHAR-1) else N_CHAR - 1

def index_to_char(ind):
    assert 0 <= ind and ind < N_CHAR

    if ind == 128:
        return 'ä'
    if ind == 129:
        return 'ö'
    if ind == 130:
        return 'ü'
    if ind == 131:
        return 'ß'
    if ind == 132:
        return '<SOS>'
    if ind == 133:
        return '<EOS>'

    if ind == N_CHAR-1:
        return '<UNK>'
    
    return chr(ind)


def partition_sentence(sentence):
    '''
    partitions the input sentence into words and punctuations.
    for example, if the input is "I am fine, and you?"
    then the output is ["I", "am", "fine", ",", "and", "you", "?"]
    '''

    # \w+: Matches one or more word characters. Word characters include alphanumeric characters (letters and digits) and underscores (_).
    #
    # [^\w\s]: Matches a single character that is not a word character or whitespace character. 
    # The caret ^ at the beginning of the character set [\w\s] negates the set, matching any character that is not in the set. 
    # This alternative matches any non-word and non-whitespace character.
    #
    #
    # There is a not-so-ideal case though.
    # "That's too risky." will become ['That', "'", 's', 'too', 'risky', '.']
    # but I want "That's"
    pattern = r'\w+|[^\w\s]'

    return re.findall(pattern, sentence)


if __name__ == '__main__':
    print(partition_sentence("I am fine, and you?"))






