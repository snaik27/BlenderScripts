import bpy


def main(context):
    objects = context.scene.objects
    for ob in objects:
        if ob.type == 'MESH':
            context.scene.objects.active = ob
            for mod in context.scene.objects.active.modifiers:
                if (mod.show_viewport):
                    mod.show_viewport = False
                else:
                    mod.show_viewport = True
                
class ToggleModVis(bpy.types.Operator):
    """Toggles all objects' modifiers to be visible/invisible"""
    bl_idname = "object.toggle_mod_vis"
    bl_label = "Toggle All Objects' Modifier Visibility"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ToggleModVis)


def unregister():
    bpy.utils.unregister_class(ToggleModVis)


if __name__ == "__main__":
    register()