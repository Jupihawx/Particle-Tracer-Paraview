import numpy as np

from numpy import genfromtxt
my_data = genfromtxt('points_data.csv', delimiter=',')

""" print(my_data[1][1])
 """

center_points=(my_data[1][0],my_data[1][1],my_data[1][2])  # to be modified by slider
num_points=int(my_data[1][3]) # to be modified by slider
radius_points= int(my_data[1][4]) # to be modified by slider


points = vtk.vtkPoints()
points.SetNumberOfPoints(num_points)
for i in range(num_points):
    generated_point_x=center_points[0]+np.random.normal(0,1,)*radius_points
    generated_point_y=center_points[1]+np.random.normal(0,1,)*radius_points
    generated_point_z=center_points[2]+np.random.normal(0,1,)*radius_points
    generated_point=(generated_point_x,generated_point_y,generated_point_z)

    points.SetPoint(i,generated_point)

output.SetPoints(points)

