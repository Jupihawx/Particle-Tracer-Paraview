from paraview.simple import *

from numpy import genfromtxt
my_data = genfromtxt('points_data.csv', delimiter=",")


##################### Create source #########################

#Check the existing proxies to rename it with a diffrent name for the source
i=0
name=[]

name.append("ParticleTracerGenerated"+str(i))
currentItem=FindSource(name[i])

while str(currentItem)!="None":
    i+=1
    name.append("ParticleTracerGenerated"+str(i))
    currentItem=FindSource(name[i])

name.pop() #remove last element because it does not exist

renderView1 = GetActiveViewOrCreate('RenderView')


########################################################################### Create particles ###########################################################################

for sources in name:
    particle=FindSource(sources)
    index=int(sources[-1])
    particleDisplay=GetDisplayProperties(particle, view=renderView1)
    particleDisplay.AmbientColor=[my_data[index+1][9]/255,my_data[index+1][10]/255,my_data[index+1][11]/255]
    particleDisplay.DiffuseColor=[my_data[index+1][9]/255,my_data[index+1][10]/255,my_data[index+1][11]/255]


# set scalar coloring
renderView1.Update()
UpdatePipeline()
Render()

