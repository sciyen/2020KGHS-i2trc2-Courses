import numpy as np
import matplotlib.pyplot as plt 

# Environment
left_wall = -10
right_wall = 10
ground = 0
g = -9.8 

# Pingpong initial state
initial_height = 10

def main():
    pos = [0, initial_height-1]
    vel = [1, -0.1]
    # Create random velocity of each points
    for time in range(100):
        # Clear screen 
        plt.cla()

        # Update points location
        pos[0] += vel[0] 
        pos[1] += vel[1] 

        # Side wall
        if pos[0] >= right_wall or pos[0] <= left_wall:
            vel[0] = -vel[0]

        if pos[1] <= ground:
            vel[1] = -vel[1]
            pos[1] = 0

        vel[1] = vel[1] + g * 0.1

        plt.scatter(pos[0], pos[1], color='gray')
        plt.plot([left_wall,left_wall, right_wall, right_wall], 
                 [initial_height, 0, 0, initial_height])
        plt.pause(0.1)

if __name__ == "__main__":
    main()
