from copy import deepcopy


def main():
    global n, answer, rotation_list , answer_list
    answer = None
    rotation_list = []
    answer_list = []
    with open("graph.txt", "r") as file:
        n = int(file.readline())
        graph = [0 for _ in range(n)]
        for i in range(n):
            line = file.readline().replace("0", "").strip()
            graph[i] = line.split(" ")

        for i in range(n):
            if not graph[i][0]:
                graph[i].remove("")


    check_triples(graph)
    print(f"------------ANSWER------------")
    print(f"started_graph : {graph}")
    for i in range(len(rotation_list)):
        print("")
        print(f"rotation : {rotation_list[i]}")
        print(f"graph_after_rotation : {answer_list[i]}")

    print("")
    print(f"answer : {answer}")
    #print(check_triples(answer))
    #print(f"------------ANSWER------------")
    #print(answer)


def check_triples(graph: list):
    global answer, rotation_list, answer_list
    is_threshold_graph = True
    graph_copy = None
    for i in range(n):
        first_point = i+1
        for second_point in graph[first_point-1]:
            third_points = give_not_connected_vertices(graph, int(second_point))
            for third_point in third_points:
                if is_three_points_are_different(first_point,second_point,third_point):
                    print("------------ITERATION--------------")
                    print(f"first_point : {first_point}")
                    print(f"second_point : {second_point}")
                    print(f"third_point : {third_point}")
                    print(f"power_of_vertex(graph,first_point) : {power_of_vertex(graph,first_point)}")
                    print(f"power_of_vertex(graph,third_point) : {power_of_vertex(graph,third_point)}")
                    if power_of_vertex(graph,int(first_point)) <= power_of_vertex(graph,int(third_point)):
                        print(f"graph : {graph}")
                        is_threshold_graph = False
                        graph_copy = deepcopy(graph)
                        increasing_rotation(graph_copy,int(first_point),int(second_point),int(third_point))
                        rotation_list.append([int(first_point),int(second_point),int(third_point)])
                        answer_list.append(graph_copy)
                        print(f"graph_copy : {graph_copy}")
                        break
            if not is_threshold_graph:
                break
        if not is_threshold_graph:
            break
    if not is_threshold_graph:
        check_triples(graph_copy)
    else:
        print(f"is_threshold_graph : {is_threshold_graph}")
        answer = graph





def give_not_connected_vertices(graph: list, vertex : int) -> list:
    connected_vertices = fill_the_set()
    for elem in graph[vertex-1]:
        connected_vertices.remove(elem)
    connected_vertices.remove(str(vertex))
    return sorted(list(connected_vertices))


def fill_the_set():
    returning_set = set()
    for i in range(n):
        returning_set.add(str(i+1))
    return returning_set

def power_of_vertex(graph, vertex : int):
    return len(graph[int(vertex)-1])

def is_three_points_are_different(first:int,second:int,third:int) -> bool:
    return (first != second) and (first != third) and (second != third)

def increasing_rotation(graph:list,first:int,second:int,third:int):
    graph[first-1].remove(str(second))
    graph[second - 1].remove(str(first))
    graph[second - 1].append(str(third))
    graph[third -1].append(str(second))


if __name__ == "__main__":
    main()