from Graph import Graph
from Graph_Node import Graph_Node

def build_order(project_list, dependency_list):
    dependency_dict = {}
    built_dict = {}

    for pair in dependency_list:
        if pair[1] not in dependency_dict:
            dependency_dict[pair[1]] = 1
        else:
            dependency_dict[pair[1]] += 1

    order = []

    for project in project_list:
        if project not in dependency_dict:
            order.append(project)
            built_dict[project] = 1

    while len(order) < len(project_list): #repeat until all projects have been added
        temp_dict = dependency_dict.copy()

        for pair in dependency_list:
            if pair[0] in built_dict: #if the project being depended on is already built
                temp_dict[pair[1]] -= 1 #reduce the number of dependencies by 1
                if temp_dict[pair[1]] < 1: #if this causes the number of dependencies to go to zero
                    if pair[1] not in built_dict: #if the project has not yet been built
                        order.append(pair[1]) #append the depending project
                    built_dict[pair[1]] = 1 #mark project as built

    return order



p = ['a', 'b', 'c', 'd', 'e', 'f']
d = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

print(build_order(p, d))