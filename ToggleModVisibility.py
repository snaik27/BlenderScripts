import bpy

def main(context):
    #Grab objects in scene that are of type 'MESH' and have a modifiers list
    objects = [ob for ob in context.scene.objects if (ob.type == 'MESH' and ob.modifiers)]

    #Grab the first object's modifier visibility status (True or False)
    parent_mod = objects[0].modifiers[0].show_viewport
    
    #Iterate through objects list and toggle all objects' modifier visibilities based on active object
    for ob in objects:
        context.scene.objects.active = ob
        for mod in context.scene.objects.active.modifiers:
            if (parent_mod):
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