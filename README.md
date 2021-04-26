# ENPM661
## Project 3 - Implementation of A Star and Djikstra Algoirthm
#### **Contributors :**
**Alkesh Kumar Srivastava**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hari Krishna Prannoy Namala** <br />
UID -117451788&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UID -117507409 <br />
_alkesh@umd.edu_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_pnamala@umd.edu_
Project 3 aimed to introducing the implementation of search algorithms in a *Mobile Robot*. In the <img src="https://latex.codecogs.com/gif.latex?3%5E%7Brd%7D"/> phase of project 3, we intend to simulate a TurtleBot robot using A* algorithm on a differential drive constraint. To run this project you need to make sure that your system has the following libraries installed :   
* numpy	1.20.1	
* opencv-python	4.5.1.48
* pygame	2.0.1

In phase 2 we implemented A* algorithm for a mobile robot that was constrained to move only in 5 directions. In this phase, we are looking forward for a more physical implementation of our robot and therefore we will be using Gazebo simulation platform in which our mobile robot will be a TurtleBot that will explore this map:<br/>
![Input](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/image6.png)

In the root folder you will notice that there are multiple files and directories but to normally look at how A* is working in the environment shown above run`__main__.py`
As soon as you will run this program, you will be asked to input the *starting co-ordinates of the robot as well as its orientation in the environment*. Please ensure that you are entering the co-ordinates separated by commas as is shown in the image below:
![Input](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/image3.png)

As you can see from the image that the other input information that a user is required to enter are the *goal state, the left and right rpm values of the robot and the clearance of the robot.* These  informations are vital since our robot is constrained to move with differential drive. As soon as you will hit enter a window will pop-up animating the implementation of A* in the information that you provided as:

![Envrionment](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/image4.png)

At the end of the animation you will also be provided with a set of tuples that can be seen below:

![Output](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/image5.png)

What do these tuple represents? The tuples provide each and every information that our mobile robot is doing. The first three element of the tuple denotes the *x,y,<img src="https://latex.codecogs.com/gif.latex?%5Ctheta"/>* that corresponds to the new location of the robot if their left wheel rotated at *l_rpm* rotation per minuite and *r_rpm* rotation per minute in a second which is also denoted in the same tuple by *element 5* and *6*. The *4th* element is the cost of moving from previous state to the current state.
Thus, for an optimal path we are able to print the path as well as all the necessary information that our mobile robot gives us along with a visual representation of the same. 

Here are few examples of exploration that our mobile robot is successfully able to traverse and obtain an optimal path using A* algorithm.

1. From (0,0) to (5,9): <br/>
![Maze 1](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/gif_00_59.gif)
2. From (0,0) to (8,6): <br/>
![Maze 2](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/gif_00_86.gif)
3. From (0,0) to (9,9): <br/>
![Maze 3](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/gif_00_99.gif)

<br/>
For simulation in Gazebo environment there are two small caveats:<br/>
1.  You need to unzip the file <i>project3sim.zip</i> in your catkin workspace. <br/>
2.  Due to computational cost, my machine ran out of memory and it is preferred to copy and paste the path obtained from <i>__main__.py</i> to <i>example_path<i> variable in <i>c_l_control.py</i> file in <i>src</i> directory.<br/>


After you are done extracting the zip file in your catkin workspace you are required to initialize `ros` and source `setup.bash` file. In `mainlaunch.launch ` file you are also expected to manually input the initial position. The manual input is expected from the user to avoid the machine to run out of memory and have a smooth simulation.<br/>

Once initialized, launch the gazebo environment using :<br/>
`roslaunch project3sim mainlaunch.launch`<br/>
Once the gazebo environment is up and running, open a new tab in the terminal and source the `setup.bash` file again. To control the turtulebot you need to run the `c_l_control.py` file by :<br/>
`rosrun project3sim c_l_control.py`<br/>

**PLEASE MAKE SURE THE `example_path` VARIABLE IS ASSIGNED ACCORDING TO YOUR DESIRED PATH.**

Once you hit enter the simulation will start running. Here are two examples:
1. (6,8) to (9,9): <br/>
![Simulation 1](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/gif_68_99.gif)
2. (8,5) to (7,7): <br/>
![Simulation 2](https://github.com/alkesh-umd/enpm661-p3-phase3/blob/main/images/gif_85_77.gif)

You can also find the video to these here:
1. A-star implementation visualization - <a href="https://drive.google.com/drive/folders/1sbmTwOJ36AwGbg8H5j5u-pVb9FJLhlR3?usp=sharing">Click Here</a>
2. Gazebo Simulation - <a href="https://drive.google.com/drive/folders/1EhwUw2N970HGsC35S_rbuF5UhZQsSRcZ?usp=sharing">Click Here</a>


In case you encounter any difficulty please feel free to contact the creators - <br/>
***Alkesh K Srivastava*** - `{alkesh@umd.edu}`, University of Maryland, College Park <br/>
***Hari Krishna Prannoy Namala*** - `{pnamala@umd.edu}`, University of Maryland, College Park <br/>
