import bpy

#Mirror _L bone constraints to corresponding R bones
Armature = bpy.data.objects["bishop_armature"]
if (bpy.context.scene.objects.active != Armature):
    bpy.ops.object.select_all(action='DESELECT')
    Armature.select = True
    bpy.context.scene.objects.active = Armature
#Make target Armature active and set to Pose mode
if (Armature.mode != 'POSE'):
    bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.select_all(action='SELECT')
all_bones = bpy.context.selected_pose_bones

#Iterate through bones looking for '_L' bones
for bone in all_bones:
    bpy.ops.pose.select_all(action='DESELECT')
    if "_L" in bone.name:
        boneL = Armature.data.bones[bone.name]
        boneR = Armature.data.bones[bone.name.replace('_L','_R')]
        #select in R -> L order to copy 'to R from L'
        boneR.select = True
        boneL.select = True
        Armature.data.bones.active = boneL
        if Armature.pose.bones[boneL.name].constraints:
            bpy.ops.pose.constraints_copy()
            for con in Armature.pose.bones[boneR.name].constraints:
                if hasattr(con,'subtarget'):
                    con.subtarget = con.subtarget.replace('_L','_R')

