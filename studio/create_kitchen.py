
import bpy
import math
from mathutils import Vector

# Reset the Blender scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# Materials
def make_material(name, color, roughness=0.7):
    material = bpy.data.materials.new(name)
    material.diffuse_color = (*color, 1)
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*color, 1)
    material.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = roughness
    return material

cream = make_material("Warm cream", (0.88, 0.72, 0.52))
wall = make_material("Soft pastel blue", (0.38, 0.65, 0.78))
wood = make_material("Honey wood", (0.42, 0.22, 0.10))
white = make_material("Cabinet ivory", (0.92, 0.88, 0.76))
red = make_material("Biscuit packet red", (0.75, 0.08, 0.06))
gold = make_material("Golden biscuit", (0.78, 0.48, 0.16))
dark = make_material("Dark details", (0.08, 0.07, 0.06))

def cube(name, location, scale, material, bevel=0.08):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)

    if bevel:
        modifier = obj.modifiers.new("Soft rounded edges", "BEVEL")
        modifier.width = bevel
        modifier.segments = 3
        obj.modifiers.new("Weighted corner normals", "WEIGHTED_NORMAL")

    return obj

# Floor and walls
cube("Kitchen floor", (0, 0, -0.15), (12, 10, 0.3), wood)
cube("Back wall", (0, 4.8, 3), (12, 0.25, 6), wall)
cube("Left wall", (-5.8, 0, 3), (0.25, 10, 6), cream)

# Kitchen cabinets
cube("Lower cabinets", (0, 2.5, 0.8), (7, 1.2, 1.6), white)
cube("Countertop", (0, 2.4, 1.7), (7.3, 1.5, 0.18), wood)

for x in [-2.8, -1.4, 0, 1.4, 2.8]:
    cube("Cabinet door", (x, 1.88, 0.85), (1.25, 0.08, 1.25), cream, 0.04)

# Upper cabinets
cube("Upper cabinet row", (0, 3.95, 4), (6.5, 1, 1.5), white)
for x in [-2.5, -1.25, 0, 1.25, 2.5]:
    cube("Upper cabinet door", (x, 3.4, 4), (1.1, 0.08, 1.3), cream, 0.04)

# Window
cube("Window frame", (-3.8, 4.55, 3), (1.8, 0.12, 2), white)
cube("Window glass", (-3.8, 4.47, 3), (1.55, 0.04, 1.75), wall, 0.01)

# Giant biscuit packet
cube("Giant biscuit packet", (1.4, 1.5, 2.15), (1.6, 0.35, 0.85), red, 0.12)

# Giant biscuit
bpy.ops.mesh.primitive_cylinder_add(
    vertices=48,
    radius=0.42,
    depth=0.16,
    location=(-1.5, 1.35, 1.95)
)
biscuit = bpy.context.object
biscuit.name = "Giant biscuit"
biscuit.data.materials.append(gold)
biscuit.rotation_euler[0] = math.radians(90)

# Small decorative details
cube("Kitchen shelf", (0, 3.9, 2.7), (3, 0.5, 0.12), wood)

# Camera
bpy.ops.object.camera_add(location=(8, -13, 8))
camera = bpy.context.object
direction = Vector((0, 2, 2.2)) - camera.location
camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
camera.data.lens = 42
bpy.context.scene.camera = camera

# Lighting
bpy.ops.object.light_add(type="AREA", location=(0, -5, 8))
light = bpy.context.object
light.data.energy = 1600
light.data.shape = "DISK"
light.data.size = 8

# Render settings
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.filepath = "/tmp/cartoon_kitchen.png"

scene.world.color = (0.25, 0.25, 0.25)

bpy.ops.render.render(write_still=True)
print("3D KITCHEN RENDER COMPLETE")
