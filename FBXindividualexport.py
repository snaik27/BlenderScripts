# Export all objects in scene individually
bl_info = {
    "name": "FBX Object exporter",
    "category": "3D View"
}

import bpy
import os

"""Automates fbx-export on per-object basis for Blender --> Unity pipeline"""

class FBX_indivExporter(bpy.types.Operator):
    """Automates importing background/reference pictures into blender"""
    bl_idname = "object.fbxexporterz" # Unique identifier for buttons and menu items to reference.
    bl_label = "Export objects as FBX"         # Display name in the interface.
    bl_options = {'REGISTER'}

    def execute(self,context): #execute() is called by blender when running the operator
        objects = context.scene.objects
        currentFolder = os.getcwd()
        currentFolder = '/'.join(currentFolder.split('\\')) #Changes backslashes to forward slashes
        for object in objects:
            bpy.ops.object.select_all(action='DESELECT')
            object.select = True
            exportName = object.data.name + '.fbx'
            bpy.ops.export_scene.fbx(filepath=currentFolder, axis_forward='-Z', axis_up='Y', use_selection=True)


        return {'FINISHED'}           # Lets Blender know the operator finished successfully.

def register():
    bpy.utils.register_class(FBX_indivExporter)


def unregister():
    bpy.utils.unregister_class(FBX_indivExporter)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
