def vote(votes):
    votes_count = {x: 0 for x in set(votes)}
    for v in votes:
        votes_count[v] += 1

    max_vote = 0
    max_vote_count = 0

    for k, v in votes_count.items():
        if v > max_vote_count:
            max_vote = k
            max_vote_count = v

    return max_vote

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))
