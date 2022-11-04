# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
renderView1 = GetActiveViewOrCreate('RenderView')


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


tempInter = FindSource('ProgrammableFilter1')
particleSource = FindSource('LiveProgrammableSource1')

# set active source
SetActiveSource(tempInter) #NOT NEEDED?

# toggle 3D widget visibility (only when running from the GUI)
# Hide3DWidgets(proxy=pointSourceGenerated) #NOT NEEDED?

# create a new 'ParticleTracer'
particleTracerGenerated = ParticleTracer(registrationName='ParticleTracerGenerated'+str(i), Input=tempInter,
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
ColorBy(particleTracerGeneratedDisplay, ('POINTS', 'ParticleAge'))


particleTracerGeneratedDisplay.RescaleTransferFunctionToDataRange(True, True)

# set active source
# Show(temporalParticlesToPathlines1_1)
UpdatePipeline()
# set active source
Show(particleTracerGenerated)

#UpdatePipeline(time=200, proxy=glyphGenerated) 
UpdatePipeline()
