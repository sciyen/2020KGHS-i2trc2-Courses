import matplotlib.pyplot as plt 

# Environment
left_wall = -10
right_wall = 10
ground = 0
g = -9.8 
dt = 0.1

bar_len = 5
# Pingpong initial state
initial_height = 10

pos = [0, initial_height-1]
vel = [1, -0.1]
bar_pos = [0, 0]

def on_key(event):
    if event.xdata is not None:
        bar_pos[0] = event.xdata
        if bar_pos[0] <= left_wall + bar_len / 2:
            bar_pos[0] = left_wall + bar_len / 2
        elif bar_pos[0] >= right_wall - bar_len / 2:
            bar_pos[0] = right_wall - bar_len / 2

def main():
    fig = plt.figure()
    fig.canvas.mpl_connect('motion_notify_event', on_key)
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

        if pos[1] <= ground and pos[0]>=bar_pos[0]-bar_len/2 and pos[0]<=bar_pos[0]+bar_len/2:
            vel[1] = -vel[1]
            pos[1] = 0
        if pos[1] < 0:
            break

        vel[1] = vel[1] + g * dt 

        plt.scatter(pos[0], pos[1], color='gray')
        plt.plot(x=[left_wall,left_wall, right_wall, right_wall], 
                 y=[initial_height, 0, 0, initial_height])
        plt.plot(x=[bar_pos[0]-bar_len/2, 
                    bar_pos[0]+bar_len/2],
                 y=[0, 0],
                 linewidth=5,
                 color='red')
        plt.pause(dt)

if __name__ == "__main__":
    main()
