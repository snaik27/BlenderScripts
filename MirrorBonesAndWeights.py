import bpy
from bpy import ops


#ISSUES: 
#A. Must set roll to 180d for forearm_R and upperarm_R after running script
#B. Must press Set Inverse for all "child of" bone constraints after running script
#C. 
#Mirror bones from left to right side and mirror weights as well

# 1. Mirror bones from left to right side ================================================
#Mirror _L bones to corresponding RHS
Armature = bpy.data.objects["Megaman_Armature"]

if (bpy.context.scene.objects.active != Armature):
    bpy.ops.object.select_all(action='DESELECT')
    Armature.select = True
    bpy.context.scene.objects.active = Armature
    
#Make target Armature active and set to Pose mode
if (Armature.mode != 'EDIT'):
    bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.armature.select_all(action='DESELECT')

#Iterate through bones looking for '_L' bones
for bone in Armature.data.edit_bones:
    if "_L" in bone.name:
        bone.select = True
        bone.select_head = True
        bone.select_tail = True

#Symmetrize bones
bpy.ops.armature.symmetrize()

#Return armature to object mode
bpy.ops.object.mode_set(mode='OBJECT')

# 2. Mirror vertex weights from left to right side ========================================

#Get mesh object and make sure it is the active object
ob = bpy.data.objects["Megaman_Trigger_Rigged"]
if (bpy.context.view_layer.objects.active != ob):
    bpy.ops.object.select_all(action='DESELECT')
    ob.select=True
    bpy.context.scene.objects.active = ob
ob is not None and ob.type == 'MESH', "active object isn't a mesh object"


#Delete all RHS vertex groups ("_R", ".R", "_r", ".r") if they exist
for v in bpy.context.active_object.vertex_groups:
    if "_R" in v.name:
        ops.object.vertex_group_set_active(group=v.name)
        ops.object.vertex_group_remove()

#Get list of LHS vertex_groups and make sure it has at least 1 vertex group
vertexList = [v for v in bpy.context.active_object.vertex_groups if ("_L" in v.name)]
assert len(vertexList) > 0, "active mesh has no vertex groups"

#Iterate through LHS vertex group list, for each vertex group:
for v in vertexList:
    #Make new RHS vertex groups from LHS vertex groups
    #  If ends in "_L" and --has verts in it-- vertex groups act as tags to each vertex
    #  second part of above line won't be possible w/o iterating through each vertex. Still, ~10k comparisions isn't that bad I think
    #  Adding in that second part to the conditional would preempt having to delete any unnecessary vertex groups
    if "_L" in v.name:
        #Set this group to active
        ops.object.vertex_group_set_active(group=v.name)
        #If it's unlocked, make copy
        if not (v.lock_weight):
            ops.object.vertex_group_copy()
            #Lock the original
            v.lock_weight = True
            #Mirror the copy's vertices
            ops.object.vertex_group_mirror()
        

#Flip all "_L_copy" vertexgroup names to RHS
copiedGroups = [v for v in bpy.context.active_object.vertex_groups if ("_L_copy" in v.name)]
for v in copiedGroups:
    v.name = v.name.replace("_L_copy", "_R")