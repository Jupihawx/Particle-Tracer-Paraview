# trace generated using paraview version 5.11.0-RC2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

currentItem=FindSource("TemporalInterpolator1")

if str(currentItem)!="None": # Do nothing if already applied
    pass

else:
    # find source
    afoam = FindSource('Field')
    renderView1 = GetActiveViewOrCreate('RenderView')

    # create a new 'Temporal Interpolator'
    temporalInterpolator1 = TemporalInterpolator(registrationName='TemporalInterpolator1', Input=afoam)

    # Properties modified on temporalInterpolator1
    temporalInterpolator1.ResampleFactor = 100


    # create a new 'Programmable Filter'
    programmableFilter1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=temporalInterpolator1)
    programmableFilter1.Script = ''
    programmableFilter1.RequestInformationScript = ''
    programmableFilter1.RequestUpdateExtentScript = ''
    programmableFilter1.PythonPath = ''

    # Properties modified on programmableFilter1
    programmableFilter1.Script = """import numpy as np
from numpy import genfromtxt
my_data = genfromtxt('points_data.csv', delimiter=',')

input0=inputs[0]
# t = inputs[0].GetInformation().Get(vtk.vtkDataObject.DATA_TIME_STEP())
dt=0.99 #Find a way to automate?
diffCoeff=my_data[1][6]
data=input0.PointData["U"] / 1.0
treated=data.Arrays[0]
noise=np.sqrt(2*diffCoeff/dt)*np.random.normal(0,1,(data.Arrays[0].shape[0],data.Arrays[0].shape[1]))

treated_data=data+noise 

#Ux=treated[:,0]
#Uy=treated[:,1]
#Uz=treated[:,2]

#Ux=Ux+np.random.normal(0,1)
#Uy=Uy+np.random.normal(0,1)
#Uz=Uz+np.random.normal(0,1)


output.PointData.append(treated_data,"U_noise")"""
    programmableFilter1.RequestInformationScript = ''
    programmableFilter1.RequestUpdateExtentScript = ''
    programmableFilter1.PythonPath = ''

    Hide(afoam, renderView1)
    Hide(programmableFilter1, renderView1)
    Hide(temporalInterpolator1, renderView1)


    # update the view to ensure updated data information
    renderView1.Update()
