from configuration import return_path, offsets_determination, move_possible
from priority_queue import PriorityQueue
from Cost import cost
import math, cv2


def heuristic(a, b):
    # Euclidean Distance
    x1, y1, theta1 = a
    x2, y2, theta2, lrpm1, rrpm1 = b
    return abs(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def cv2_viz(visited_nodes, path, clearance):
    canvas = cv2.imread("Map.png")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    name = str(path[0]) + 'to' + str(path[-1]) + '.avi'
    print(name)
    out = cv2.VideoWriter(name, fourcc, 10, (canvas.shape[1], canvas.shape[0]))
    out.write(canvas)
    i = 0
    while True:
        cv2.arrowedLine(canvas, (int(visited_nodes[i][0]), 300 - int(visited_nodes[i][1])),
                        (int(visited_nodes[i + 1][0]), 300 - int(visited_nodes[i + 1][1])), (255, 0, 0), 1, cv2.LINE_AA)
        canvas = cv2.putText(canvas, "Robot Cearance : " + str(clearance) + " units", (50, 50), cv2.FONT_HERSHEY_PLAIN,
                             1, (0, 0, 255), 2)
        out.write(canvas)
        i += 1
        if i == (len(visited_nodes) - 1):
            break
        cv2.imshow("Solution", canvas)
        cv2.waitKey(1)
    i = 0
    while True:
        cv2.arrowedLine(canvas, (int(path[i][0]), 300 - int(path[i][1])),
                        (int(path[i + 1][0]), 300 - int(path[i + 1][1])), (0, 0, 255), 1,
                        cv2.LINE_AA)
        out.write(canvas)
        i += 1
        if i == (len(path) - 1):
            break
        cv2.imshow("Solution", canvas)
        cv2.waitKey(1)


def a_star(maze, start, goal, rpm_1, rpm_2):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}
    while not pq.is_empty():
        current_cell = pq.get()
        if ((current_cell[0] - goal[0]) ** 2) + ((current_cell[1] - goal[1]) ** 2) - 1 <= 0:
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
            if 0 <= (current_cell[2] + theta_offset) < 360:
                neighbour = (
                current_cell[0] + row_offset, current_cell[1] + col_offset, current_cell[2] + theta_offset, left_rpm,
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
                current_cell[0] + row_offset, current_cell[1] + col_offset, current_cell[2] + theta_offset, left_rpm,
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
                explored_list.append(neighbour)

    return None
