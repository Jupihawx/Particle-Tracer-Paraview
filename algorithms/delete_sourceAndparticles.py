from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()


renderView1 = GetActiveViewOrCreate('RenderView')

i=0
name="LiveProgrammableSource"+str(i)
currentItem=FindSource(name)

while str(currentItem)!="None":
    i+=1
    name="LiveProgrammableSource"+str(i)
    currentItem=FindSource(name)

options=range(i)
options=[str(i) for i in options]

user_input=""
input_message="What point do you want to delete? \n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

while user_input.lower() not in options:
    user_input = input(input_message)

print('You deleted: ' + user_input)

#chosen_one = input("What point do you want to delete?")

toBeDeletedTracer=FindSource('ParticleTracerGenerated'+str(user_input))
toBeDeletedSource=FindSource('LiveProgrammableSource'+str(user_input))
Delete(toBeDeletedTracer)
del toBeDeletedTracer
Delete(toBeDeletedSource)
del toBeDeletedSource   