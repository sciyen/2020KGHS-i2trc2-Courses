import numpy as np
import matplotlib.pyplot as plt 

def main():
    # Create random points
    points = 100 * (np.random.rand(20, 2)-0.5)

    # Create random velocity of each points
    velocity = 1 * (np.random.rand(20, 2)-0.5)
    for time in range(100):
        # Clear screen 
        plt.cla()

        # Plot all points
        plt.scatter(points[:, 0], points[:, 1], color='gray')

        # Calculate distance
        for i in range(20):
            for j in range(i+1, 20):
                vector = points[i] - points[j]
                distance = vector[0]**2 + vector[1]**2
                distance = np.clip(distance, 0, 1500) / 1500
                plt.plot([points[i, 0], points[j, 0]], 
                         [points[i, 1], points[j, 1]], color='gray', alpha=1-distance)

        # Update points location
        points += velocity
        plt.pause(0.001)

if __name__ == "__main__":
    main()
