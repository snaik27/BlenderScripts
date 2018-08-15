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
    if '.001' in bone.name:
        bone.name = bone.name.replace('.001','')