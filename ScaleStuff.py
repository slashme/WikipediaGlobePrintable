#Scaling factors - 0 is no change; 1 is the center of the ball; 0.045 takes the letters to about the thickness of the original shell.
letterscale=0.015
shellscale=0.045

#Grab all objects called Shell*
shells = [obj for obj in bpy.data.objects if obj.name.startswith("Shell")]

#Iterate through all objects, scaling all vertices in LetterInner:
for obj in shells:
    for v in obj.data.vertices:
        for vertGroup in v.groups:
            if vertGroup.group == obj.vertex_groups['LetterInner'].index:
                v.co = v.co.lerp((0,0,0),letterscale)
            if vertGroup.group == obj.vertex_groups['BI'].index or \
                    vertGroup.group == obj.vertex_groups['BE'].index:
                v.co = v.co.lerp((0,0,0),shellscale)
