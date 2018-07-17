import bpy

'''Copies modifiers from parent object to all children,
    for use in array/mirror/etc visualization modifiers'''
def main(context):
    parent_ob = bpy.context.active_object
    for curr_ob in parent_ob.children:
        if curr_ob.type == 'MESH':
            context.scene.objects.active = curr_ob
            for mod in parent_ob.modifiers:
                if mod.type == 'ARRAY':
                    #if 'Array' not in context.scene.objects.active.modifiers:
                    bpy.ops.object.modifier_add(type=mod.type)
                    context.scene.objects.active.modifiers['Array'].use_relative_offset = False
                    context.scene.objects.active.modifiers["Array"].use_constant_offset = True
                    context.scene.objects.active.modifiers['Array'].constant_offset_displace = (parent_ob.dimensions[0]/2, 0.0,0.0)
                else if mod.type != 'ARRAY':
                    bpy.ops.object.modifier_add(type=mod.type)


class EasyVis(bpy.types.Operator):
    """For use in array/mirror/etc visualization modifiers"""
    bl_idname = "object.easy_vis"
    bl_label = "Copy Mods for Easy Vis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(EasyVis)


def unregister():
    bpy.utils.unregister_class(EasyVis)


if __name__ == "__main__":
    register()
