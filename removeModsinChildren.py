import bpy

'''Removes modifiers from children MESH objects'''
def main(context):
    parent_ob = bpy.context.active_object
    for curr_ob in parent_ob.children:
        if curr_ob.type == 'MESH':
            curr_ob.modifiers.clear()
            if curr_ob.children:
                for child in curr_ob.children:
                    if child.type == 'MESH':
                        child.modifiers.clear()



class RemoveChildMods(bpy.types.Operator):
    """For use in array/mirror/etc visualization modifiers"""
    bl_idname = "object.remove_mods_children"
    bl_label = "Remove children mods"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RemoveChildMods)


def unregister():
    bpy.utils.unregister_class(RemoveChildMods)


if __name__ == "__main__":
    register()
