from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thommy'] = []
graph['jonny'] = []

def person_is_seller(name):
    return len(name) > 5


def serch(name):
    serch_queue = deque()
    serch_queue += graph[name]
    searched = []  # Массив для отслеживания уже проверенных людей
    while serch_queue:
        person = serch_queue.popleft()
        if person in searched:
            continue
        elif person_is_seller(person):
            print('{} is a mango seller!'.format(person.title()))
            return True
        else:
            serch_queue += graph[person]
            serch_queue.append(person)
    return False

serch('you')
