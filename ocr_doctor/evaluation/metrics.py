def normalize(text: str) -> str:
    # we collapse all whitespace into single spaces
    return " ".join(text.split())


def edit_distance(a, b) -> int:
    # minimum insertions, deletions and substitutions.
    rows = len(a) + 1
    cols = len(b) + 1
    table = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        table[i][0] = i

    for j in range(cols):
        table[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(
                    table[i - 1][j],
                    table[i][j - 1],
                    table[i - 1][j - 1],
                )
    return table[-1][-1]


def cer(reference: str, hypothesis: str) -> float:
    # we calculate the character error rate
    reference = normalize(reference)
    hypothesis = normalize(hypothesis)

    if not reference:
        return 0.0 if not hypothesis else 1.0
    return edit_distance(reference, hypothesis) / len(reference)


def wer(reference: str, hypothesis: str) -> float:
    # we calculate the word error rate
    reference_words = normalize(reference).split()
    hypothesis_words = normalize(hypothesis).split()

    if not reference_words:
        return 0.0 if not hypothesis_words else 1.0
    return edit_distance(reference_words, hypothesis_words) / len(reference_words)
