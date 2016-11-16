#Script to deselect edges marked as sharp
#From http://blender.stackexchange.com/questions/41351/is-there-a-way-to-select-edges-marked-as-sharp-via-python and http://blender.stackexchange.com/questions/1412/efficient-way-to-get-selected-vertices-via-python-without-iterating-over-the-en

import bpy
import bmesh

obj = bpy.context.edit_object
me = obj.data

bm = bmesh.from_edit_mesh(me)
SelectedEdges = [e for e in bm.edges if e.select]
for e in SelectedEdges:
    if not e.smooth:
        e.select = False

bmesh.update_edit_mesh(me, False)
