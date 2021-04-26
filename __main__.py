from __astar__ import a_star, a_star_explore
from Howplotcurves import plot_path
import cv2

if __name__ == "__main__":
    print("Note: Value of \u03F4 should only be in degrees (\N{DEGREE SIGN})\n"
          "Please Enter the starting co-ordinates of the robot and its orientation as (x,y,\u03F4):")
    starting_coordinates = input()
    start = starting_coordinates.split(',')
    start = (int(start[0]), int(start[1]), int(start[2]), 0, 0, 0)
    print("Please Enter the goal co-ordinates of the robot and its orientation as (goal_x,goal_y):")
    goal_coordinates = input()
    goal = goal_coordinates.split(',')
    goal = (int(goal[0]), int(goal[1]), 0, 0, 0, 0)
    print("Please Enter two angular rotation for the wheels of the bot as (rpm_1, rpm_2) in rotations per minute:")
    rpm = input()
    rpm = rpm.split(',')
    rpm = (int(rpm[0]), int(rpm[1]))
    print("Please Enter the CLEARANCE for the Robot:")
    clearance = input()
    clearance = float(clearance)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("animation.avi", fourcc, 10, (640, 480))
    puzzle = [[''] * 10] * 10
    # start, goal, rpm_1, rpm_2
    sol = a_star(puzzle, start, goal, rpm[0], rpm[1], clearance, out)
    # explored = a_star_explore(puzzle, start, (goal[0], goal[1],0), rpm[0], rpm[1])

    print("Optimal Path: \n", sol)
    plot_path(sol, out)

# print("Explored Path: \n",explored)
