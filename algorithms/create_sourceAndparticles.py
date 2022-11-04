from paraview.simple import *


##################### Create source #########################

#Check the existing proxies to rename it with a diffrent name for the source
i=0
name="LiveProgrammableSource"+str(i)
currentItem=FindSource(name)

while str(currentItem)!="None":
    i+=1
    name="LiveProgrammableSource"+str(i)
    currentItem=FindSource(name)


liveProgrammableSource1 = LiveProgrammableSource(registrationName=name)




script="""import numpy as np

from numpy import genfromtxt
my_data = genfromtxt(\'points_data.csv\', delimiter=\',\')


center_points=(my_data[{0}][0],my_data[{0}][1],my_data[{0}][2])  # to be modified by slider
num_points=int(my_data[{0}][3]) # to be modified by slider
radius_points= int(my_data[{0}][4]) # to be modified by slider


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

script_update= """import csv
r = csv.reader(open('./points_data.csv')) # Here your csv file
lines = list(r)

if int(lines[{0}][5]):
  lines[{0}][5]=0
  writer = csv.writer(open('./points_data.csv', 'w'))
  writer.writerows(lines)
  self.SetNeedsUpdate(True)
"""

liveProgrammableSource1.Script = script.format(i+1) # replace the value above to the right one for the particle we are working on. i+1 because line 0 is the name of the data in the csv

liveProgrammableSource1.ScriptRequestInformation = ''
liveProgrammableSource1.PythonPath = ''
liveProgrammableSource1.ScriptCheckNeedsUpdate = script_update.format(i+1)

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


########################################################################### Create particles ###########################################################################


name="PointSourceGenerated"+str(i)


FieldSource = FindSource('ProgrammableFilter1')
particleSource = FindSource('LiveProgrammableSource'+str(i))

# set active source
SetActiveSource(FieldSource) #NOT NEEDED?


# create a new 'ParticleTracer'
particleTracerGenerated = ParticleTracer(registrationName='ParticleTracerGenerated'+str(i), Input=FieldSource,
    SeedSource=particleSource)
particleTracerGenerated.SelectInputVectors = ['POINTS', 'U_noise']

UpdatePipeline()
# Properties modified on particleTracer1
particleTracerGenerated.StaticSeeds = 1
# particleTracerGenerated.StaticMesh = 1
particleTracerGenerated.MeshOverTime = "Static"
particleTracerGenerated.ComputeVorticity = 0
particleTracerGenerated.ForceReinjectionEveryNSteps = 1

particleTracerGeneratedDisplay = GetDisplayProperties(particleTracerGenerated, view=renderView1)

# set scalar coloring
UpdatePipeline()
#ColorBy(particleTracerGeneratedDisplay, ('POINTS', 'ParticleAge'))

colors=[[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1]] # A MODIFIER POUR UN TRUC NICER

particleTracerGeneratedDisplay.AmbientColor = colors[i]
particleTracerGeneratedDisplay.DiffuseColor = colors[i]


#particleTracerGeneratedDisplay.RescaleTransferFunctionToDataRange(True, True)

# set active source
# Show(temporalParticlesToPathlines1_1)
UpdatePipeline()
# set active source
Show(particleTracerGenerated)

#UpdatePipeline(time=200, proxy=glyphGenerated) 
UpdatePipeline()
