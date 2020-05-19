# challange available here: https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
# Code snippit at the end is my playing with creating a sorted list as the elements are inserted -- neither my official nor the proper solution

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return "{} {}".format(self.name, self.score)

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.name < b.name:
            return -1
        elif a.name > b.name:
            return 1
        return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


'''

# Inserting each new element into the (eventually-sorted) list in appropriate position

sorted_players.append(list_players[0])
for p in list_players[1:]:
    new_player = p

    s = 0
    while s <= len(sorted_players):

        if s == len(sorted_players):
            sorted_players.append(new_player)
            break
        
        elif Player.comparator(new_player, sorted_players[s]) == -1:
            sorted_players.insert(s, new_player)
            break
        
        s += 1
'''