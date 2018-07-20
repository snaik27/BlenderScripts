import bpy

'''Automates adding material to objects to work with Substance Painter'''
def main(context):
    #Grab objects in scene that are of type 'MESH' and has no materials linked to it
    objects = [ob for ob in context.scene.objects if (ob.type == 'MESH' and not ob.data.materials)]
    
    #Assign new material to object with same name as object
    for ob in objects:
        context.scene.objects.active= ob
        if not ob.data.materials:
            mat = bpy.data.materials.new(name=ob.name)
            ob.data.materials.append(mat)

class addSubstanceMat(bpy.types.Operator):
    """Automates adding materials to each object, using same name as object"""
    bl_idname = "object.add_sub_material"
    bl_label = "Add Substance Material"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(addSubstanceMat)


def unregister():
    bpy.utils.unregister_class(addSubstanceMat)


if __name__ == "__main__":
    register()
