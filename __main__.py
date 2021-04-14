from __astar__ import a_star
print("Note: Value of \u03F4 should only be in degrees (\N{DEGREE SIGN})\n"
      "Please Enter the starting co-ordinates of the robot and its orientation as (x,y,\u03F4):")
starting_coordinates = input()
start = starting_coordinates.split(',')
start = (int(start[0]), int(start[1]), int(start[2]))
print("Please Enter the goal co-ordinates of the robot and its orientation as (goal_x,goal_y):")
goal_coordinates = input()
goal = goal_coordinates.split(',')
goal = (int(goal[0]), int(goal[1]))
print("Please Enter two angular rotation for the wheels of the bot as (rpm_1, rpm_2) in rotations per minute:")
rpm = input()
rpm = rpm.split(',')
rpm = (int(rpm[0]), int(rpm[1]))
print("Please Enter the CLEARANCE for the Robot:")
clearance = input()
clearance = int(clearance)

puzzle = [[''] * 10] * 10
# start, goal, rpm_1, rpm_2
sol = a_star(puzzle, start, (goal[0], goal[1],0), rpm[0], rpm[1])
print(sol)
