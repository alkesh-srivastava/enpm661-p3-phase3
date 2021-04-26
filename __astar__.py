import cv2
import math
import matplotlib.pyplot as plt

from Cost import cost
from configuration import return_path, offsets_determination, move_possible
from priority_queue import PriorityQueue
from Howplotcurves import plot_curve


def heuristic(a, b):
    # Euclidean Distance
    x1, y1, _, _, _, _ = a
    x2, y2, _, _, _, _ = b
    return abs(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def a_star(maze, start, goal, rpm_1, rpm_2, clearence, out):
    a = True
    fig, ax = plt.subplots()
    plt.grid()

    ax.set_aspect('equal')

    plt.xlim(-1, 10)
    plt.ylim(-1, 10)

    circle_1 = plt.Circle((2, 2), 1, color='black')
    circle_1c = plt.Circle((2, 2), 1 + clearence, color='red')
    circle_2 = plt.Circle((2, 8), 1, color='black')
    circle_2c = plt.Circle((2, 8), 1 + clearence, color='red')
    circle_g = plt.Circle(goal, 0.25, color='green')
    rect_1 = plt.Rectangle((0.25, 4.25), 1.5, 1.5, color='black')
    rect_1c = plt.Rectangle((0.25 - clearence, 4.25 - clearence), 1.5 + (2 * clearence), 1.5 + (2 * clearence),
                            color='red')
    rect_2 = plt.Rectangle((3.75, 4.25), 2.5, 1.5, color='black')
    rect_2c = plt.Rectangle((3.75 - clearence, 4.25 - clearence), 2.5 + (2 * clearence), 1.5 + (2 * clearence),
                            color='red')
    rect_3 = plt.Rectangle((7.25, 2), 1.5, 2, color='black')
    rect_3c = plt.Rectangle((7.25 - clearence, 2 - clearence), 1.5 + (2 * clearence), 2 + (2 * clearence), color='red')

    plots_list = [circle_g, circle_1c, circle_1, circle_2c, circle_2, rect_1c, rect_1, rect_2c, rect_2, rect_3c, rect_3]
    for plot in plots_list:
        ax.add_patch(plot)
    plt.title('Plotted Map', fontsize=10)
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}
    while not pq.is_empty():
        current_cell = pq.get()
        if ((current_cell[0] - goal[0]) ** 2) + ((current_cell[1] - goal[1]) ** 2) - 0.0625 <= 0:
            return return_path(predecessors, start, current_cell)
        for direction in [
            offsets_determination(0, rpm_1, current_cell[2]),
            offsets_determination(rpm_1, 0, current_cell[2]),
            offsets_determination(rpm_1, rpm_1, current_cell[2]),
            offsets_determination(0, rpm_2, current_cell[2]),
            offsets_determination(rpm_2, 0, current_cell[2]),
            offsets_determination(rpm_2, rpm_2, current_cell[2]),
            offsets_determination(rpm_1, rpm_2, current_cell[2]),
            offsets_determination(rpm_2, rpm_1, current_cell[2])
        ]:
            row_offset, col_offset, theta_offset, left_rpm, right_rpm = direction
            if current_cell[2] > 360:
                neighbour = cost(current_cell[0], current_cell[1], current_cell[2] - 360, left_rpm, right_rpm)
            elif current_cell[2] == 360:
                neighbour = cost(current_cell[0], current_cell[1], 0, left_rpm, right_rpm)
            elif current_cell[2] < 0:
                neighbour = cost(current_cell[0], current_cell[1], current_cell[2] + 360, left_rpm, right_rpm)
            else:
                neighbour = cost(current_cell[0], current_cell[1], current_cell[2], left_rpm, right_rpm)
            # Xi,Yi,Thetai,UL,UR
            if move_possible(maze, neighbour, clearence) and neighbour not in g_values:
                # delta_cost = math.sqrt((direction[0]**2) + (direction[1]**2))
                # _, _, _, delta_cost = cost(current_cell[0], current_cell[1], current_cell[2], left_rpm, right_rpm)
                if 0 <= (current_cell[2]) < 360:
                    a = plot_curve(current_cell[0], current_cell[1], current_cell[2], left_rpm, right_rpm, clearence)
                elif current_cell[2] > 360:
                    a = plot_curve(current_cell[0], current_cell[1], current_cell[2] - 360, left_rpm, right_rpm,
                                   clearence)
                elif current_cell[2] == 360:
                    a = plot_curve(current_cell[0], current_cell[1], 0, left_rpm, right_rpm, clearence)
                elif current_cell[2] < 0:
                    a = plot_curve(current_cell[0], current_cell[1], current_cell[2] + 360, left_rpm, right_rpm,
                                   clearence)
                if not a:
                    continue
                new_cost = g_values[current_cell] + neighbour[3]
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
                # print("Visited Node:", current_cell)
                img = cv2.imread('load.png')
                out.write(img)
                cv2.imshow('...', img)
                cv2.waitKey(1)

    return None


# A -star co-ordinate of the next


# Explored :
def a_star_explore(maze, start, goal, rpm_1, rpm_2):
    explored_list = list()

    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}
    while not pq.is_empty():
        current_cell = pq.get()
        if ((current_cell[0] - goal[0]) ** 2) + ((current_cell[1] - goal[1]) ** 2) - 1 <= 0:
            return explored_list
        for direction in [
            offsets_determination(0, rpm_1, current_cell[2]),
            offsets_determination(rpm_1, 0, current_cell[2]),
            offsets_determination(rpm_1, rpm_1, current_cell[2]),
            offsets_determination(0, rpm_2, current_cell[2]),
            offsets_determination(rpm_2, 0, current_cell[2]),
            offsets_determination(rpm_2, rpm_2, current_cell[2]),
            offsets_determination(rpm_1, rpm_2, current_cell[2]),
            offsets_determination(rpm_2, rpm_1, current_cell[2])
        ]:
            row_offset, col_offset, theta_offset, left_rpm, right_rpm = direction
            if 0 <= (current_cell[2] + theta_offset) < 360:
                neighbour = (
                    current_cell[0] + row_offset, current_cell[1] + col_offset, current_cell[2] + theta_offset,
                    left_rpm,
                    right_rpm)
            elif current_cell[2] + theta_offset > 360:
                neighbour = (
                    current_cell[0] + row_offset, current_cell[1] + col_offset, (current_cell[2] + theta_offset) - 360,
                    left_rpm, right_rpm)
            elif current_cell[2] + theta_offset == 360:
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset, 0)
            elif (current_cell[2] + theta_offset) < 0:
                neighbour = (
                    current_cell[0] + row_offset, current_cell[1] + col_offset, 360 + (current_cell[2] + theta_offset),
                    left_rpm, right_rpm)
            # Xi,Yi,Thetai,UL,UR
            if move_possible(maze, neighbour) and neighbour not in g_values:
                # delta_cost = math.sqrt((direction[0]**2) + (direction[1]**2))
                _, _, _, delta_cost = cost(current_cell[0], current_cell[1], current_cell[2], left_rpm, right_rpm)
                new_cost = g_values[current_cell] + delta_cost
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
                print("Visited Node:", current_cell)
                explored_list.append(neighbour)

    return None
