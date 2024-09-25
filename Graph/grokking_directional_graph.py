from collections import deque


def person_is_seller(name: str) -> bool:
    return name[-1] == "m"


def search(graph: dict, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


graph = {"you": ["Alice", "Bob", "Claire"],
         "Alice": ["Peggy"],
         "Bob": ["Peggy", "Anuj"],
         "Anuj": [],
         "Claire": ["Thom", "Jonny"],
         "Thom": [],
         "Jonny": [],
         "Peggy": []
         }

search(graph, "you")
