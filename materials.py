#I have no idea whether this script is useful anymore.

#Grab all objects called Shell*
shells = [obj for obj in bpy.data.objects if obj.name.startswith("Shell")]

#Grab the material called 'Material'
mat = bpy.data.materials.get("Material")

#Iterate through all objects, scaling all vertices in LetterInner:
for obj in shells:
    obj.data.materials.append(mat)
    bpy.context.scene.objects.active = obj
    bpy.ops.object.vertex_group_set_active(group='LetterInner')
    obj.active_material_index = 1
    bpy.ops.object.editmode_toggle()  #Go in edit mode
    bpy.ops.mesh.select_all(action='DESELECT') #Deselect all the vertices
    bpy.ops.object.vertex_group_select() #Select the vertices of the vertex group
    bpy.ops.object.material_slot_assign(1) #QAssign the material on the selected vertices
    bpy.ops.object.editmode_toggle()  #Return in object mode
