from itertools import count
import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    result_arr = []

    new_set = sorted(set(ranked), reverse = True)
    print(new_set)

    count_rank = 0

    for i in player:
        for h in new_set:
            if h > i:
                count_rank = count_rank + 1
            else:
                break
        result_arr.append(count_rank + 1)
        count_rank = 0
    
    return result_arr

    
if __name__ == '__main__':
    ranked_count = int(input("\nEnter the number of players on the leader-board: ").strip())
    ranked = list(map(int, input("\nEnter the leader-board scores in decreasing order: ").rstrip().split()))

    player_count = int(input("\nEnter the number games the NEW player plays: ").strip())
    player = list(map(int, input("\nEnter the NEW player's scores: ").rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)

    
