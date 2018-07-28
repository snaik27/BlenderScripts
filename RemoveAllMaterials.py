import bpy

'''Automates removing materials to objects'''
def main(context):
    #Grab objects in scene that are of type 'MESH' 
    objects = [ob for ob in context.scene.objects if (ob.type == 'MESH' and ob.data.materials)]
    
    #Remove all currently assigned materials
    for ob in objects:
        context.scene.objects.active= ob
        if ob.data.materials:
            ob.data.materials.clear()
            
class removeMats(bpy.types.Operator):
    """Automates adding materials to each object, using same name as object"""
    bl_idname = "object.remove_mats"
    bl_label = "Remove Materials"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(removeMats)


def unregister():
    bpy.utils.unregister_class(removeMats)


if __name__ == "__main__":
    register()
