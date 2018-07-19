import bpy

'''Copies modifiers from parent object to all children,
    for use in array/mirror/etc modifiers'''
'''Found a better solution at https://blender.stackexchange.com/questions/4878/how-to-copy-modifiers-with-attribute-values-from-active-object-to-selected-objec'''    

def main(context):
    parent_ob = bpy.context.active_object
    for curr_ob in parent_ob.children:
        if curr_ob.type == 'MESH':
            context.scene.objects.active = curr_ob
            #iterate through modifiers in parent object
            for parent_mods in parent_ob.modifiers:
                #Create the modifier
                child_mods = curr_ob.modifiers.get(parent_mods.name, None)
                if not child_mods:
                    child_mods = curr_ob.modifiers.new(parent_mods.name, parent_mods.type)
                
                #collect names of writable properties in a list
                properties = [p.identifier for p in parent_mods.bl_rna.properties if not p.is_readonly]
                
                #copy properties to active object
                for prop in properties:
                    setattr(child_mods, prop, getattr(parent_mods,prop))
        #repeat above process for any secondary children
        if curr_ob.children:
            for child in curr_ob.children:
                if child.type == 'MESH':
                    context.scene.objects.active = child
                    for parent_mods in parent_ob.modifiers:
                        #Create the modifier
                        child_mods = child.modifiers.get(parent_mods.name, None)
                        if not child_mods:
                            child_mods = child.modifiers.new(parent_mods.name, parent_mods.type)
                        
                        #collect names of writable properties in a list
                        properties = [p.identifier for p in parent_mods.bl_rna.properties if not p.is_readonly]
                        
                        #copy properties to active object
                        for prop in properties:
                            setattr(child_mods,prop,getattr(parent_mods,prop))
    context.scene.objects.active = parent_ob
                            
                    

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
