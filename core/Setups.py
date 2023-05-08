"""
Author: <Anthony Sychev> (hello at dm211 dot com | a.sychev at jfranc dot studio) 
Buy me a coffe: https://www.buymeacoffee.com/twooneone
setups.py (c) 2023 
Created:  2023-01-23 18:36:13 
Desc: Body, Hands and Face setups + bones
"""

import bpy
import logging
import traceback

bone_translate = {
    'clavicle_l' : {
        'bone_name': 'clavicle_l',
        'rigify_name': 'shoulder.L',
        'unreal_name': 'clavicle_l',
        'copy_location': '11 right shoulder',
        'stretch_to': '12 left shoulder',
    }
}

body_names = [
    "00 nose",
    "01 left eye (inner)",
    "02 left eye",
    "03 left eye (outer)",
    "04 right eye (inner)",
    "05 right eye",
    "06 right eye (outer)",
    "07 left ear",
    "08 right ear",
    "09 mouth (left)",
    "10 mouth (right)",
    "11 left shoulder",
    "12 right shoulder",
    "13 left elbow",
    "14 right elbow",
    "15 left wrist",
    "16 right wrist",
    "17 left pinky",
    "18 right pinky",
    "19 left index",
    "20 right index",
    "21 left thumb",
    "22 right thumb",
    "23 left hip",
    "24 right hip",
    "25 left knee",
    "26 right knee",
    "27 left ankle",
    "28 right ankle",
    "29 left heel",
    "30 right heel",
    "31 left foot index",
    "32 right foot index",
]

def do_assign(left, leftKey, centerKey, right, rightKey = None):
    success = True
    try:
        if (rightKey == None):
            left[leftKey].constraints[centerKey].target = right
        else:
            left[leftKey].constraints[centerKey].target = right[rightKey]
    except Exception as exception:
        success = False
        logging.error(traceback.format_exc())
    return success

def body_setup():
    """ Setup tracking boxes for body tracking """

    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            for space in area.spaces: 
                if space.type == 'VIEW_3D':
                    space.shading.color_type = 'OBJECT'

    scene_objects = [n for n in bpy.context.scene.objects.keys()]
    # setup = "Pose" in scene_objects
    setup = "'GEO-vincent_body'" in scene_objects

    if not setup:
        bpy.ops.object.add(radius=0.1, type='EMPTY')
        pose = bpy.context.active_object
        pose.name = "Pose"
        pose.scale = (-1,1,1)

    # pose = bpy.context.scene.objects["Pose"]
    pose = bpy.context.scene.objects["RIG-Vincent"]
    body = bpy.data.objects['GEO-vincent_body']

    # bpy.ops.object.add(radius=0.1, type='EMPTY')
    # body = bpy.context.active_object
    # body.name = "Body"
    # body.parent = pose

    for k in range(33):
        bpy.ops.mesh.primitive_cube_add()
        box = bpy.context.active_object
        box.name = body_names[k]
        box.scale = [0.003, 0.003, 0.003]
        box.location = [0,0,0]
        box.parent = body
        box.color = (0,255,0,255)

    # body = bpy.context.scene.objects["Body"]
    body = bpy.context.scene.objects["GEO-vincent_body"]
    return body

def hands_setup():
    """ Setup tracking boxes for hand tracking """

    scene_objects = [n for n in bpy.context.scene.objects.keys()]
    # setup = "Pose" in scene_objects
    setup = "RIG-Vincent" in scene_objects

    if not setup:
        bpy.ops.object.add(radius=0.1, type='EMPTY')
        pose = bpy.context.active_object
        pose.name = "Pose"
        pose.scale = (-1,1,1)

    # pose = bpy.context.scene.objects["Pose"]
    pose = bpy.context.scene.objects["RIG-Vincent"]

    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            for space in area.spaces: 
                if space.type == 'VIEW_3D':
                    space.shading.color_type = 'OBJECT'

    if "Hand Left" not in scene_objects:
        bpy.ops.object.add(radius=0.1, type='EMPTY')
        hand_left = bpy.context.active_object
        hand_left.name = "Hand Left"
        hand_left.parent = pose

        for k in range(21):
            bpy.ops.mesh.primitive_cube_add()
            box = bpy.context.active_object
            box.name = str(k).zfill(2) + "Hand Left"
            box.scale = (0.005, 0.005, 0.005)
            box.parent = hand_left
            box.color = (0,0,255,255)

    if "Hand Right" not in scene_objects:
        bpy.ops.object.add(radius=0.1, type='EMPTY')
        hand_right = bpy.context.active_object
        hand_right.name = "Hand Right"
        hand_right.parent = pose

        for k in range(21):
            bpy.ops.mesh.primitive_cube_add()
            box = bpy.context.active_object
            box.name = str(k).zfill(2) + "Hand Right"
            box.scale = (0.005, 0.005, 0.005)
            box.parent = hand_right
            box.color = (255,0,0,255)    

    hand_left = bpy.context.scene.objects["Hand Left"]
    hand_right = bpy.context.scene.objects["Hand Right"]
    pose.scale = (-1,1,1)
    return hand_left, hand_right

def face_setup():
    """ Setup tracking boxes for face tracking """

    scene_objects = [n for n in bpy.context.scene.objects.keys()]
    # setup = "Pose" in scene_objects
    setup = "RIG-Vincent" in scene_objects

    if not setup:
        bpy.ops.object.add(radius=0.1, type='EMPTY')
        pose = bpy.context.active_object
        pose.name = "Pose"
        pose.scale = (-1,1,1)

    # pose = bpy.context.scene.objects["Pose"]
    pose = bpy.context.scene.objects["RIG-Vincent"]

    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            for space in area.spaces: 
                if space.type == 'VIEW_3D':
                    space.shading.color_type = 'OBJECT'

    if "Face" not in scene_objects:
        bpy.ops.object.add(radius=0.1, type='EMPTY')
        face = bpy.context.active_object
        face.name = "Face"
        face.parent = pose

        for k in range(468):
            bpy.ops.mesh.primitive_cube_add()
            box = bpy.context.active_object
            box.name = str(k).zfill(3) + "Face"
            box.scale = (0.002, 0.002, 0.002)
            box.parent = face
            box.color = (255,0,255,255)

    face = bpy.context.scene.objects["Face"]
    pose.scale = (-1,1,1)
    return face

def body_delete():
    """ Deletes all objects associated with body capture """
    scene_objects = [n for n in bpy.context.scene.objects.keys()]
    # pose = bpy.context.scene.objects["Pose"]
    pose = bpy.context.scene.objects["RIG-Vincent"]

    # if "Body" in scene_objects:
    #     for c in bpy.context.scene.objects["Body"].children:
    #         if not len(bpy.context.scene.objects["Body"].children) == 0:
    #             bpy.data.objects[c.name].select_set(True)
    #             bpy.ops.object.delete()
    #     bpy.data.objects["Body"].select_set(True)
    #     bpy.ops.object.delete()

    if "GEO-vincent_body" in scene_objects:
        for c in bpy.context.scene.objects["GEO-vincent_body"].children:
            if not len(bpy.context.scene.objects["GEO-vincent_body"].children) == 0:
                bpy.data.objects[c.name].select_set(True)
                bpy.ops.object.delete()
        bpy.data.objects["GEO-vincent_body"].select_set(True)
        bpy.ops.object.delete()

def face_delete():
    """ Deletes all objects associated with face capture """
    scene_objects = [n for n in bpy.context.scene.objects.keys()]
    # pose = bpy.context.scene.objects["Pose"]
    pose = bpy.context.scene.objects["RIG-Vincent"]

    if "Face" in scene_objects:
        for c in  bpy.context.scene.objects["Face"].children:
            if not len(bpy.context.scene.objects["Face"].children) == 0:
                bpy.data.objects[c.name].select_set(True)
                bpy.ops.object.delete()
        bpy.data.objects["Face"].select_set(True)
        bpy.ops.object.delete()

def hands_delete():
    """ Deletes all objects associated with hands capture """
    scene_objects = [n for n in bpy.context.scene.objects.keys()]
    # pose = bpy.context.scene.objects["Pose"]
    pose = bpy.context.scene.objects["RIG-Vincent"]
    if "Hand Left" in scene_objects:
        for c in  bpy.context.scene.objects["Hand Left"].children:
            if not len(bpy.context.scene.objects["Hand Left"].children) == 0:
                bpy.data.objects[c.name].select_set(True)
                bpy.ops.object.delete()
        bpy.data.objects["Hand Left"].select_set(True)
        bpy.ops.object.delete()

    if "Hand Right" in scene_objects:
        for c in  bpy.context.scene.objects["Hand Right"].children:
            if not len(bpy.context.scene.objects["Hand Right"].children) == 0:
                bpy.data.objects[c.name].select_set(True)
                bpy.ops.object.delete()
        bpy.data.objects["Hand Right"].select_set(True)
        bpy.ops.object.delete()
