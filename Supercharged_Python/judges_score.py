# Enter Scores and compute result
# Supercharged Python, page 22 and 74

score_list = []

def main():
    while True:
        s = input('Enter score: ')
        if not s:
            break
        score_list.append(float(s))

    print(score_list)
    print('Final Score: %s' % evaluate_scores(score_list))


def evaluate_scores(scores):
    scores.remove(max(scores))
    scores.remove(min(scores))
    return sum(scores) / len(scores)


if __name__ == '__main__':
    main()
