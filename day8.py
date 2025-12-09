# https://adventofcode.com/2025/day/8
import math


def euclidean_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    

def part1(lines, num):
    edges = dict()
    points = dict()
    clusters = []
    cluster_points = []
    for i,circuit in enumerate(lines):
        points[i] = i
        clusters.append(1)
        cluster_points.append([i])
        for j, temp_circuit in enumerate(lines[i+1:]):
            dist = euclidean_dist(circuit, temp_circuit)
            if dist in edges.keys():
                edges[dist].append([i, j+i+1])
            else:
                edges[dist] = [[i, j+i+1]]
    
    
    for i in range(num):
        if len(edges) == 0:
            break
        min_edge_i = min(edges)
        min_edge = edges[min_edge_i]
        left = min_edge[0][0]
        right = min_edge[0][1]  
        if points[left] != points[right]:
            first_cluster = points[left]
            second_cluster = points[right]
            if clusters[first_cluster] <= clusters[second_cluster]:
                to_move = first_cluster
                to_arrive = second_cluster
            else:
                to_move = second_cluster
                to_arrive = first_cluster
            cluster_points[to_arrive] += cluster_points[to_move]
            for val in cluster_points[to_move]:
                points[val] = to_arrive
            cluster_points[to_move] = []
            clusters[to_arrive]+=clusters[to_move]
            clusters[to_move] = 0
        if len(min_edge) == 1:
            edges.pop(min_edge_i)
        else:
            edges[min_edge_i].pop(0)
    res = 1
    for size in sorted(clusters)[-3:]:
        res*=size
    return res

def part2(lines):
    edges = dict()
    points = dict()
    clusters = []
    cluster_points = []
    for i, circuit in enumerate(lines):
        points[i] = i
        clusters.append(1)
        cluster_points.append([i])
        for j, temp_circuit in enumerate(lines[i + 1:]):
            dist = euclidean_dist(circuit, temp_circuit)
            if dist in edges.keys():
                edges[dist].append([i, j + i + 1])
            else:
                edges[dist] = [[i, j + i + 1]]

    count = 0
    while len([i for i in clusters if i!=0]) >1:
        print(count)
        count+=1
        if len(edges) == 0:
            break
        min_edge_i = min(edges)
        min_edge = edges[min_edge_i]
        left = min_edge[0][0]
        right = min_edge[0][1]
        if points[left] != points[right]:
            first_cluster = points[left]
            second_cluster = points[right]
            if clusters[first_cluster] <= clusters[second_cluster]:
                to_move = first_cluster
                to_arrive = second_cluster
            else:
                to_move = second_cluster
                to_arrive = first_cluster
            cluster_points[to_arrive] += cluster_points[to_move]
            for val in cluster_points[to_move]:
                points[val] = to_arrive
            cluster_points[to_move] = []
            clusters[to_arrive] += clusters[to_move]
            clusters[to_move] = 0
        if len(min_edge) == 1:
            edges.pop(min_edge_i)
        else:
            edges[min_edge_i].pop(0)
    
    return lines[left][0]*lines[right][0]


with open("data/day8.txt") as f:
    lines = [[int(i) for i in line.split(",")] for line in f.readlines()]

print("Part 1: " + str(part1(lines, 10)))
print("Part 2: " + str(part2(lines)))