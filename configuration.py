import math

t = 0
RADIUS = 0.038
LENGTH = 0.354
dt = 0.1


def offsets_determination(left_rpm, right_rpm, theta):
    theta += (RADIUS / LENGTH) * (right_rpm - left_rpm)
    delta_x = (RADIUS / 2) * (right_rpm + left_rpm) * math.cos(theta)
    delta_y = (RADIUS / 2) * (right_rpm + left_rpm) * math.sin(theta)
    return (delta_x, delta_y, theta, left_rpm, right_rpm)


def obstacle(x, y):  # This function definition inspects whether a coordinate point x
    # and y lie on the obstacle or not
    inside_circle1 = False
    inside_circle2 = False
    inside_C1 = False
    inside_C2 = False
    inside_C3 = False
    clearance = 0

    if ((x - 2) ** 2 + (y - 2) ** 2) <= ((1 + clearance) ** 2):
        inside_circle1 = True
    if ((x - 2) ** 2 + (y - 8) ** 2) <= ((1 + clearance) ** 2):
        inside_circle2 = True

    if 0.25 - clearance < x < 1.75 + clearance and 4.25 - clearance < y < 5.75 + clearance:
        inside_C1 = True

    if 3.75 - clearance < x < 6.25 and 4.25 - clearance < y < 5.75 + clearance:
        inside_C2 = True

    if 7.25 - clearance < x < 8.75 + clearance and 2 - clearance < y < 4 + clearance:
        inside_C3 = True

    if inside_circle1 or inside_circle2 or inside_C1 or inside_C2 or inside_C3:
        return True
    else:
        return False


# I defined this function with the intent to store every move
# in a list, but I guess they will never be used

def move_possible(maze, pos):
    i, j, k, l, m = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_cols and 0 <= j < num_rows and not (obstacle(i, j))


def return_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    print("There is no point of running this file.")
