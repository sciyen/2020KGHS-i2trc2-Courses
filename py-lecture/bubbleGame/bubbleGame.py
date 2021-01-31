import numpy as np
import matplotlib.pyplot as plt 

# Environment
center = np.array([0, 0])
left_wall = -10
right_wall = 10
height = 20
ground = 0

# Parameters
ARROW_LEN = 4
DT = 0.04        # unit in second

# Game Variables
vec_arrow = np.ones(2)

def on_mouse_move(event):
    if event.xdata is not None and event.ydata is not None:
        global vec_arrow 
        vec_arrow = np.array([event.xdata, event.ydata])
        vec_arrow = ARROW_LEN * vec_arrow / np.linalg.norm(vec_arrow)

def plot_game(ball_pos):
    # Plot walls
    x = [left_wall, left_wall, right_wall, right_wall, left_wall]
    y = [   height,         0,          0,     height,    height]
    plt.plot(x, y)
    # Plot arrow
    plt.arrow(0, 0, vec_arrow[0], vec_arrow[1], width=0.1)
    # Plot the ball
    plt.scatter(ball_pos[0], ball_pos[1], color='gray')

def ball_motion_update(pos, vel):
    # Update moition
    pos = pos + vel * DT

    # Wall collision: x-direction
    if pos[0] >= right_wall:
        pos[0] = right_wall
        vel[0] = -vel[0]
    elif pos[0] <= left_wall:
        pos[0] = left_wall
        vel[0] = -vel[0]

    # Wall collision: y-direction
    if pos[1] <= ground:
        vel[1] = -vel[1]
        pos[1] = 0
    return pos, vel

def generate_targets():
    target = []
    for y in range(height-3, height):
        for x in range(left_wall+1, right_wall):
            target.append(np.array([x, y]))
    print(target)
    return target

def plot_targets(targets):
    for t in targets:
        x = t[0]
        y = t[1]
        plt.fill([x-0.4, x+0.4, x+0.4, x-0.4], 
                 [y+0.4, y+0.4, y-0.4, y-0.4])

def check_collision(pos, targets, collision_distance=1.2):
    dis = np.linalg.norm(pos - np.array(targets), axis=1)
    min_idx = np.argmin(dis)
    if dis[min_idx] < collision_distance:
        del targets[min_idx]

def main():
    fig = plt.figure()
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
    #fig.canvas.mpl_connect('button_release_event', on_mouse_release)
    targets = generate_targets()

    for time in range(100):
        # Ball 
        pos = np.array([0, 0])      # Reset the point of the ball
        vel = 20 * vec_arrow         # Set the ball's velocity to arrow
        while pos[1] < height:
            # Clear screen 
            plt.cla()

            # Ball position update
            pos, vel = ball_motion_update(pos, vel)
            check_collision(pos, targets)

            # Plot game
            plot_game(pos)
            plot_targets(targets)
            plt.pause(DT)

if __name__ == "__main__":
    main()
