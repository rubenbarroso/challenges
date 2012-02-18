# coding=utf-8
"""
From http://programmingpraxis.com/2011/12/16/majority-voting/

In an election, the winner is required to have the majority of the votes. For instance, with the set
of votes {A A A C C B B C C C B C C}, the winner is C with 7 of 13 votes. Some elections have no
winner; with the set of votes {A B C A B C A}, A gets a plurality of the votes but not a majority,
so there is no winner. You can think of voting as a political election, or as redundant hardware in
a critical system where a failure of one component must not lead to failure of the overall system.

Your task is to write a function that determines the winner of a vote, or indicates that no candidate
reached a majority.
"""

def counts(votes):
    """ Count the votes into a distribution """
    counts = {}

    def vote_for(v):
        counts[v] = counts.get(v, 0) + 1

        # update counts

    map(vote_for, votes)
    return counts

# Test
election_first_round = counts(['A', 'A', 'A', 'C', 'C', 'B', 'B', 'C', 'C', 'C', 'B', 'C', 'C'])
print election_first_round
election_second_round = counts(['A', 'B', 'C', 'A', 'B', 'C', 'A'])
print election_second_round

# Output
# {'A': 3, 'C': 7, 'B': 3}

def winner(counts):
    """ Elect the winner (if any) """
    winner = "No winner"
    total_count = sum(counts.itervalues())
    for who, count in counts.iteritems():
        if count > (total_count / 2):
            winner = who
    return winner

# Test
print winner(election_first_round)
print winner(election_second_round)

# Output
# C
# No winner
