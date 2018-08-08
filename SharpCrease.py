import bpy
import bmesh

#For all selected objects, script conditionally marks sharp edges if that edge is creased (greater than 50% crease)
# and creases edges if that edge (to 100% crease) is marked sharp

#Script uses bmesh so you don't have to keep switching in and out of Edit mode (takes longer)

#Grab selected objects in context
objects = [ob for ob in bpy.context.selected_objects]

for ob in objects:
    #set first ob active and grab its data
    bpy.context.scene.objects.active = ob
    me = bpy.context.object.data
    bm = bmesh.new()   # create temp bmesh
    bm.from_mesh(me)   # fill it in from a Mesh

    # grab creased edges
    cr = bm.edges.layers.crease.verify()

    #show edge creases in case you're in editmode for the one object you've selected already
    me.show_edge_crease = True
    
    #Main__ part of script
    for e in bm.edges:
        #mark sharp all edge-creased edges
        if (e[cr] > 0.5):
            e.smooth = False
        #edge-crease all sharp edges
        if (e.smooth == False):
            e[cr]= 1.0

    # Finish up, write the bmesh back to the mesh
    bm.to_mesh(me)
    bm.free()  # free and prevent further access