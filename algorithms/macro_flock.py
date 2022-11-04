# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider, Button
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
renderView1 = GetActiveViewOrCreate('RenderView')

axSlider1= plt.axes([0.1,0.2,0.8,0.05])
slider1= Slider(axSlider1, 'Slider 1', valmin=0,valmax=100)

plt.show()

PointX, PointY, PointZ = input("Enter coordinates of point X Y Z: ").split()

#Check the existing proxies to rename it with a diffrent name
i=0
name="PointSourceGenerated"+str(i)
currentItem=FindSource(name)

while str(currentItem)!="None":
    i+=1
    name="PointSourceGenerated"+str(i)
    currentItem=FindSource(name)


view = GetActiveView()
currentTime=view.ViewTime
print(currentTime)


# create a new 'Point Source'
pointSourceGenerated = PointSource(registrationName=name)



# Properties modified on pointSource1
pointSourceGenerated.Center = [int(PointX), int(PointY), int(PointZ)]
pointSourceGenerated.NumberOfPoints = 100
pointSourceGenerated.Radius = 1.0

# UpdatePipeline(time=200.0, proxy=pointSourceGenerated) #NOT NEEDED?

# find source
# building_simplifiedstl = FindSource('building_simplified.stl') #NOT NEEDED?

# find source
#afoam = FindSource('a.foam')

tempInter = FindSource('ProgrammableFilter1')

# set active source
SetActiveSource(tempInter) #NOT NEEDED?

# toggle 3D widget visibility (only when running from the GUI)
# Hide3DWidgets(proxy=pointSourceGenerated) #NOT NEEDED?

# create a new 'ParticleTracer'
particleTracerGenerated = ParticleTracer(registrationName='ParticleTracerGenerated'+str(i), Input=tempInter,
    SeedSource=pointSourceGenerated)
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
ColorBy(particleTracerGeneratedDisplay, ('POINTS', 'ParticleAge'))


particleTracerGeneratedDisplay.RescaleTransferFunctionToDataRange(True, True)

# set active source
# Show(temporalParticlesToPathlines1_1)
UpdatePipeline()
# set active source
Show(particleTracerGenerated)

#UpdatePipeline(time=200, proxy=glyphGenerated) 
UpdatePipeline()
