from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
Field = FindSource("Field")

ReplaceReaderFileName(Field, ['/home/boris/OpenFOAM/boris-v2206/run/windAroundBuildings/Fields/foamtest/{0}/{0}.foam'], 'FileName')

newField=FindSource("{0}.cgns")
RenameSource("Field",newField)