import bpy

'''Copies modifiers from parent object to all children,
    for use in array/mirror/etc modifiers'''
'''Found a better solution at https://blender.stackexchange.com/questions/4878/how-to-copy-modifiers-with-attribute-values-from-active-object-to-selected-objec'''    

def main(context):
    parent_ob = bpy.context.active_object
    for curr_ob in parent_ob.children:
        if curr_ob.type == 'MESH':
            context.scene.objects.active = curr_ob
            for parent_mods in parent_ob.modifiers:
                child_mods = curr_ob.modifiers.get(parent_mods.name, None)
                if not child_mods:
                    child_mods = curr_ob.modifiers.new(parent_mods.name, parent_mods.type)
                    
                properties = [p.identifier for p in parent_mods.bl_rna.properties if not p.is_readonly]
                
                for prop in properties:
                    setattr(child_mods, prop, getattr(parent_mods,prop))     

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
