from paraview.simple import *

liveProgrammableSource1 = LiveProgrammableSource(registrationName='LiveProgrammableSource1')
liveProgrammableSource1.Script = ''
liveProgrammableSource1.ScriptRequestInformation = ''
liveProgrammableSource1.PythonPath = ''
liveProgrammableSource1.ScriptCheckNeedsUpdate = ''

afoam = FindSource('a.foam')
liveProgrammableSource1.Script = """import numpy as np

from numpy import genfromtxt
my_data = genfromtxt(\'points_data.csv\', delimiter=\',\')

\"\"\" print(my_data[1][1])
 \"\"\"

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

"""
liveProgrammableSource1.ScriptRequestInformation = ''
liveProgrammableSource1.PythonPath = ''
liveProgrammableSource1.ScriptCheckNeedsUpdate = """import csv
r = csv.reader(open('./points_data.csv')) # Here your csv file
lines = list(r)

if int(lines[1][5]):
  lines[1][5]=0
  writer = csv.writer(open('./points_data.csv', 'w'))
  writer.writerows(lines)
  self.SetNeedsUpdate(True)
"""
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
liveProgrammableSource1Display = Show(liveProgrammableSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
liveProgrammableSource1Display.Representation = 'Surface'
liveProgrammableSource1Display.ColorArrayName = [None, '']
liveProgrammableSource1Display.SelectTCoordArray = 'None'
liveProgrammableSource1Display.SelectNormalArray = 'None'
liveProgrammableSource1Display.SelectTangentArray = 'None'
liveProgrammableSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
liveProgrammableSource1Display.SelectOrientationVectors = 'None'
liveProgrammableSource1Display.ScaleFactor = 1.5563205718994142
liveProgrammableSource1Display.SelectScaleArray = 'None'
liveProgrammableSource1Display.GlyphType = 'Arrow'
liveProgrammableSource1Display.GlyphTableIndexArray = 'None'
liveProgrammableSource1Display.GaussianRadius = 0.07781602859497071
liveProgrammableSource1Display.SetScaleArray = [None, '']
liveProgrammableSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
liveProgrammableSource1Display.OpacityArray = [None, '']
liveProgrammableSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
liveProgrammableSource1Display.DataAxesGrid = 'GridAxesRepresentation'
liveProgrammableSource1Display.PolarAxes = 'PolarAxesRepresentation'
liveProgrammableSource1Display.SelectInputVectors = [None, '']
liveProgrammableSource1Display.WriteLog = ''

renderView1.Update()
