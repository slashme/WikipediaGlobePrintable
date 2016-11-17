import bpy

#Grab all objects called Shell*
shells = [obj for obj in bpy.data.objects if obj.name.startswith("Shell")]

#From http://blender.stackexchange.com/questions/2638/run-an-edit-mode-operator-on-every-object-in-the-scene
#Iterate through all objects, going into and out of edit mode
for obj in shells:
     bpy.context.scene.objects.active = obj
     bpy.ops.object.mode_set(mode='EDIT', toggle=False)
     bpy.ops.mesh.reveal()
     bpy.ops.mesh.select_all(action='DESELECT')
     bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
