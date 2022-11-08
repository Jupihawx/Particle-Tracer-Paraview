from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()


renderView1 = GetActiveViewOrCreate('RenderView')

name="LiveProgrammableSource{0}"
currentItem=FindSource(name)


#chosen_one = input("What point do you want to delete?")

toBeDeletedTracer=FindSource('ParticleTracerGenerated{0}')
toBeDeletedSource=FindSource("LiveProgrammableSource{0}")
Delete(toBeDeletedTracer)
del toBeDeletedTracer
Delete(toBeDeletedSource)
del toBeDeletedSource   

renderView1.Update()
Render()
