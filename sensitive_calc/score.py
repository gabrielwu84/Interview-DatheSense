import re
score_card = {
    'secret': 10,
    'dathena': 7,
    'internal': 5,
    'external': 3,
    'public': 1
}
# algorithm for calculating sensitivity score
def sensitivity(blob):
    score = 0
    # add further delimiters here when discovered
    words = re.split(' |\n',blob.lower())
    for w in words:
        if w in score_card:
            score += score_card[w]
        pass
    return score
