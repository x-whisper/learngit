import sys
from collections import deque

graph = {}
graph["you"] = ["alice", "eric", "claire", "peggy"]
graph["eric"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["avril", "eminem"]
graph["anuj"] = []
graph["peggy"] = ["you"]
graph["avril"] = ["tim"]
graph["eminem"] = []

def person_is_seller(person):
    return person[-1] == 'm'

search_queue = deque()
searched = []
search_queue += graph["you"]
while search_queue:
    person = search_queue.popleft()
    if person not in searched:
        if person_is_seller(person):
            print(person + " is a mango seller!")
            sys.exit()
        else:
            search_queue += graph[person]
            searched.append(person)
print("There's no mongo seller in your firends!")