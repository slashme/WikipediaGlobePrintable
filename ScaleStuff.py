import bpy

#Grab all objects called Shell*
shells = [obj for obj in bpy.data.objects if obj.name.startswith("Shell")]

#From http://blender.stackexchange.com/questions/2638/run-an-edit-mode-operator-on-every-object-in-the-scene
#Iterate through all objects, going into and out of edit mode
for obj in shells:
     bpy.context.scene.objects.active = obj
     #Go into edit mode:
     bpy.ops.object.mode_set(mode='EDIT', toggle=False)
     #Reveal all hidden vertices, edges and faces:
     bpy.ops.mesh.reveal()
     #Deselect all vertices:
     bpy.ops.mesh.select_all(action='DESELECT')
     #Go out of edit mode:
     bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
