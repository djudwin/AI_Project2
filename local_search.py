import sys
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

class Coordinates:
	x = 0
	y = 0

def get_start_coordinates():
	x_min = int((sys.argv)[2])
	y_min = int((sys.argv)[3])
	x_max = int((sys.argv)[4])
	y_max = int((sys.argv)[5])

	start_coordinates = Coordinates()
	start_coordinates.x = x_min
	start_coordinates.y = y_min
	return start_coordinates

def get_input_file():
	fo = open((sys.argv)[1], "r")
	input_file = fo.read()
	fo.close()
	return input_file

def simulated_annealing(coordinates, num_steps, x_min, x_max, y_min, y_max):
	max_value = 0
	max_value_coordinates = coordinates

	step_number = 0
	while step_number < num_steps:
		function_result = my_func(coordinates.x, coordinates.y)
		if (function_result > max_value):
			max_value = function_result
			max_value_coordinates = coordinates

		neighbor1 = Coordinates()
		if (coordinates.x + 1 <= x_max):
			neighbor1.x = coordinates.x + 1
		else:
			neighbor1.x = coordinates.x
		neighbor1.y = coordinates.y
		neighbor2 = Coordinates()
		if (coordinates.x - 1 >= x_min):
			neighbor2.x = coordinates.x - 1
		else:
			neighbor2.x = coordinates.x
		neighbor2.y = coordinates.y
		neighbor3 = Coordinates()
		neighbor3.x = coordinates.x
		if (coordinates.y + 1 <= y_max):
			neighbor3.y = coordinates.y + 1
		else:
			neighbor3.y = coordinates.y
		neighbor4 = Coordinates()
		neighbor4.x = coordinates.x
		if (coordinates.y - 1 >= y_min):
			neighbor4.y = coordinates.y - 1
		else:
			neighbor4.y = coordinates.y

		neighbor1_result = my_func(neighbor1.x, neighbor1.y)
		neighbor2_result = my_func(neighbor2.x, neighbor2.y)
		neighbor3_result = my_func(neighbor3.x, neighbor3.y)
		neighbor4_result = my_func(neighbor4.x, neighbor4.y)

		if (neighbor1_result > max_value):
			max_value = neighbor1_result
			max_value_coordinates = neighbor1
		if (neighbor2_result > max_value):
			max_value = neighbor2_result
			max_value_coordinates = neighbor2
		if (neighbor3_result > max_value):
			max_value = neighbor3_result
			max_value_coordinates = neighbor3
		if (neighbor4_result > max_value):
			max_value = neighbor4_result
			max_value_coordinates = neighbor4

		coordinates.x = random.randint(x_min, x_max)
		coordinates.y = random.randint(y_min, y_max)

		print([coordinates.x, coordinates.y])

		step_number += 1

	return max_value_coordinates

def hillclimb(coordinates, num_steps, x_min, x_max, y_min, y_max):
	max_value = 0
	max_value_coordinates = coordinates

	step_number = 0
	while step_number < num_steps:
		function_result = my_func(coordinates.x, coordinates.y)
		if (function_result > max_value):
			max_value = function_result
			max_value_coordinates = coordinates

		neighbor1 = Coordinates()
		if (coordinates.x + 1 <= x_max):
			neighbor1.x = coordinates.x + 1
		else:
			neighbor1.x = coordinates.x
		neighbor1.y = coordinates.y
		neighbor2 = Coordinates()
		if (coordinates.x - 1 >= x_min):
			neighbor2.x = coordinates.x - 1
		else:
			neighbor2.x = coordinates.x
		neighbor2.y = coordinates.y
		neighbor3 = Coordinates()
		neighbor3.x = coordinates.x
		if (coordinates.y + 1 <= y_max):
			neighbor3.y = coordinates.y + 1
		else:
			neighbor3.y = coordinates.y
		neighbor4 = Coordinates()
		neighbor4.x = coordinates.x
		if (coordinates.y - 1 >= y_min):
			neighbor4.y = coordinates.y - 1
		else:
			neighbor4.y = coordinates.y

		neighbor1_result = my_func(neighbor1.x, neighbor1.y)
		neighbor2_result = my_func(neighbor2.x, neighbor2.y)
		neighbor3_result = my_func(neighbor3.x, neighbor3.y)
		neighbor4_result = my_func(neighbor4.x, neighbor4.y)

		if (neighbor1_result > max_value):
			max_value = neighbor1_result
			max_value_coordinates = neighbor1
		if (neighbor2_result > max_value):
			max_value = neighbor2_result
			max_value_coordinates = neighbor2
		if (neighbor3_result > max_value):
			max_value = neighbor3_result
			max_value_coordinates = neighbor3
		if (neighbor4_result > max_value):
			max_value = neighbor4_result
			max_value_coordinates = neighbor4

		coordinates.x = random.randint(x_min, x_max)
		coordinates.y = random.randint(y_min, y_max)

		step_number += 1

	return max_value_coordinates

def graph(func, xmin, ymin, xmax, ymax, points=[]):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Make data.
    X = np.arange(xmin, xmax, 0.25)
    Y = np.arange(ymin, ymax, 0.25)
    X, Y = np.meshgrid(X, Y)

    Z = func(X,Y)
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, #cmap=cm.coolwarm,
    linewidth=0, antialiased=False)
    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Add a color bar which maps values to colors.
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    for i in points:
        ax.plot([i[0]], [i[1]], [i[2]], '.', color=(i[3]/1000,0,0)) 
    plt.show()

def main():

	# Get command line arguments
	input_file = get_input_file()
	start_coordinates = get_start_coordinates()
	x_min = int((sys.argv)[2])
	y_min = int((sys.argv)[3])
	x_max = int((sys.argv)[4])
	y_max = int((sys.argv)[5])

	# Put function for hill climb in global namespace
	exec(input_file, globals())

	num_steps = 2000

	max_coordinates = simulated_annealing(start_coordinates, num_steps, x_min, x_max, y_min, y_max)

	return_coordiantes = [max_coordinates.x, max_coordinates.y]

	print(return_coordiantes)

	points = [ [1, 2, 3, 0], [2, 3, 3, 1] ]

	graph(my_func, x_min, y_min, x_max, y_max, points)
 

main()
