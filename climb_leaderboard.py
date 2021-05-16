#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def compute_rank_table(ranked):
    rank_table = []
    rank = 1
    i = 0

    while i < len(ranked):
        if i != 0:
            if not (ranked[i] == ranked[i-1]):
                rank = rank + 1
        rank_table.append(rank)
        i += 1
    return rank_table

def compute_rank_index(ranked, old_index, element):
    
    low = 0
    high = old_index
    
    if element > ranked[0]:
        return 0
    if element < ranked[len(ranked)-1]:
        return len(ranked)
    if element in ranked:
        return ranked.index(element)
    
    for value in ranked[0:old_index]:
        if element > value:
            return ranked.index(value)
    
    #while low <= high:
#
#        mid = int((low+high)/2)
#        print(low, high, mid, ranked, element)
#        
#        if low == high == mid:
#            if element < ranked[mid]:
#                return mid+1
#            else:
#                return mid
            
#        if element > ranked[mid]:
#            high = mid - 1
#        elif element < ranked[mid]:
#            low = mid + 1
 
#        print("print2")
#        print(low, high, mid, ranked, element)
    
#    return mid
    
            
    
def climbingLeaderboard(ranked, player):
    # Write your code here
    
    rank_table = compute_rank_table(ranked)
 

    player_rank = []
    old_rank = len(ranked) - 1
    for element in player:
        new_ranked = ranked + [element]
        new_ranked.sort(reverse=True)
        index_value = new_ranked.index(element)
        rank_table = compute_rank_table(new_ranked)
    #    index_value = compute_rank_index(ranked, old_rank, element)
    #    old_rank = index_value
    #    print("element index", element, index_value, rank_table)
        if index_value >= len(rank_table):
            rank_value = rank_table[len(rank_table)-1] + 1
        else:
            rank_value = rank_table[index_value]
        player_rank.append(rank_value)
        
    return player_rank
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
