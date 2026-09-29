""" RigUp by Melodi """
""" Copyright 2026 """

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
from maya import OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial
import sys
import os


########################################################################################################################
# Guide Creation
########################################################################################################################
character_rig_guides = {
    "head": {
        "cn_head_guide": (0.002, 5.501, 0),
        "cn_jaw_guide": (0.004, 5.201, 0.397),
        "l_eye_guide": (0.154, 5.749, 0.314),
        "r_eye_guide": (-0.149, 5.749, 0.314),
    },

    "neck": {
        "cn_neck_01_guide": (0.002, 4.988, 0),
        "cn_neck_02_guide": (0.002, 5.164, 0),
        "cn_neck_03_guide": (0.002, 5.361, 0),
    },

    "torso": {
        "cn_spine_01_guide": (0.002, 3.4, 0.041),
        "cn_spine_02_guide": (0.002, 3.603, 0.041),
        "cn_spine_03_guide": (0.002, 3.807, 0.041),
        "cn_spine_04_guide": (0.002, 4.011, 0.041),
        "cn_spine_05_guide": (0.002, 4.215, 0.041),
        "cn_spine_06_guide": (0.002, 4.419, 0.041),
        "cn_spine_07_guide": (0.002, 4.650, 0.041),
        "cn_spine_08_guide": (0.002, 4.826, 0.041),
    },

    "arms": {
        "l_shoulder_guide": (0.476, 4.901, -0.05),
        "l_clavicle_01_guide": (0.054, 4.841, 0),
        "l_clavicle_02_guide": (0.476, 4.901, -0.05),
        "l_elbow_guide": (1.279, 4.901,  -0.049),
        "l_wrist_guide": (2.144, 4.901,  -0.038),

        "r_shoulder_guide": (-0.476, 4.901,  -0.05),
        "r_clavicle_01_guide": (-0.054, 4.841,  0),
        "r_clavicle_02_guide": (-0.476,  4.901,  -0.05),
        "r_elbow_guide": (-1.279,  4.901,  -0.049),
        "r_wrist_guide": (-2.144,  4.901, -0.038),
    },

    "legs": {
        "l_leg_guide": (0.183, 3.404, 0.038),
        "l_knee_guide": (0.183, 1.859, 0.064),
        "l_ankle_guide": (0.183, 0.182, -0.018),
        "l_foot_01_guide": (0.183, 0.182, -0.018),
        "l_foot_02_guide": (0.204, 0, 0.361),
        "l_foot_03_guide": (0.204, 0, 0.497),

        "r_leg_guide": (-0.183, 3.404, 0.038),
        "r_knee_guide": (-0.183, 1.859, 0.064),
        "r_ankle_guide": (-0.183, 0.182, -0.018),
        "r_foot_01_guide": (-0.183, 0.182, -0.018),
        "r_foot_02_guide": (-0.204, 0, 0.361),
        "r_foot_03_guide": (-0.204, 0, 0.497),
    },

    "hands": {
        "l_index_01_guide": (2.428, 4.913, 0.112),
        "l_index_02_guide": (2.537,4.913, 0.134),
        "l_index_03_guide": (2.669, 4.923, 0.163),
        "l_index_04_guide": (2.778, 4.941, 0.181),
        "l_ring_01_guide": (2.442, 4.922, -0.067),
        "l_ring_02_guide": (2.562, 4.923, -0.07),
        "l_ring_03_guide": (2.657, 4.924, -0.072),
        "l_ring_04_guide": (2.807, 4.923, -0.076),
        "l_middle_01_guide": (2.444, 4.923, 0.025),
        "l_middle_02_guide": (2.567, 4.921, 0.032),
        "l_middle_03_guide": (2.691, 4.927, 0.038),
        "l_middle_04_guide": (2.835, 4.964, 0.047),
        "l_pinky_01_guide": (2.413, 4.91, -0.148),
        "l_pinky_02_guide": (2.517, 4.906, -0.165),
        "l_pinky_03_guide": (2.597, 4.904, -0.176),
        "l_pinky_04_guide": (2.702, 4.879, -0.187),
        "l_thumb_01_guide": (2.221, 4.879, 0.092),
        "l_thumb_02_guide": (2.27, 4.828, 0.18),
        "l_thumb_03_guide": (2.319, 4.784, 0.254),
        "l_thumb_04_guide": (2.376, 4.745, 0.368),

        "r_index_01_guide": (-2.428, 4.913, 0.112),
        "r_index_02_guide": (-2.537, 4.913, 0.134),
        "r_index_03_guide": (-2.669, 4.923, 0.163),
        "r_index_04_guide": (-2.778, 4.941, 0.181),
        "r_ring_01_guide": (-2.442, 4.922, -0.067),
        "r_ring_02_guide": (-2.562, 4.923, -0.07),
        "r_ring_03_guide": (-2.657, 4.924, -0.072),
        "r_ring_04_guide": (-2.807, 4.923, -0.076),
        "r_middle_01_guide": (-2.444, 4.923, 0.025),
        "r_middle_02_guide": (-2.567, 4.921, 0.032),
        "r_middle_03_guide": (-2.691, 4.927, 0.038),
        "r_middle_04_guide": (-2.835, 4.964, 0.047),
        "r_pinky_01_guide": (-2.413, 4.91, -0.148),
        "r_pinky_02_guide": (-2.517, 4.906, -0.165),
        "r_pinky_03_guide": (-2.597, 4.904, -0.176),
        "r_pinky_04_guide": (-2.702, 4.879, -0.187),
        "r_thumb_01_guide": (-2.221, 4.879, 0.092),
        "r_thumb_02_guide": (-2.27, 4.828, 0.18),
        "r_thumb_03_guide": (-2.319, 4.784, 0.254),
        "r_thumb_04_guide": (-2.376, 4.745, 0.368),
    }
}

def create_guides():
    for section, guides in character_rig_guides.items():
        
         for guide_name, position in guides.items():
             
             locator = cmds.spaceLocator(name=guide_name)[0]
             
             cmds.xform(    
             locator,
             worldSpace=True,
             translation=position
             )
             
def create_joints():
    for section, guides in character_rig_guides.items():
        
        for guide_name in guides:
            
            joint_name = guide_name.replace("_guide", "_jnt")
    
            position = cmds.xform(
            guide_name,
            q=True,
            ws=True,
            t=True    
            )
        
            cmds.select(clear=True)
        
            cmds.joint(
            name=joint_name,
            position=position
            )

def parent_head_joints():
    """Parents head joints to create skeletal hiearchy"""
    # L
    cmds.parent('l_eye_jnt', 'cn_head_jnt')
    
    # R
    cmds.parent('r_eye_jnt', 'cn_head_jnt')
    
    # CN Jaw
    cmds.parent('cn_jaw_jnt', 'cn_head_jnt')
    
def parent_neck_joints():
    """Parents head joints to create skeletal hiearchy"""
    # CN Neck
    cmds.parent('cn_head_jnt', 'cn_neck_03_jnt')
    
    cmds.parent('cn_neck_03_jnt', 'cn_neck_02_jnt')
    
    cmds.parent('cn_neck_02_jnt', 'cn_neck_01_jnt')
    
def parent_torso_joints():
    """Parents torso joints to create skeletal hiearchy"""
    # CN Spine
    cmds.parent('cn_spine_02_jnt', 'cn_spine_01_jnt')
    
    cmds.parent('cn_spine_03_jnt', 'cn_spine_02_jnt')
    
    cmds.parent('cn_spine_04_jnt', 'cn_spine_03_jnt')
    
    cmds.parent('cn_spine_05_jnt', 'cn_spine_04_jnt')
    
    cmds.parent('cn_spine_06_jnt', 'cn_spine_05_jnt')
    
    cmds.parent('cn_spine_07_jnt', 'cn_spine_06_jnt')
    
    cmds.parent('cn_spine_08_jnt', 'cn_spine_07_jnt')
    
    #L Clavicle
    cmds.parent('l_clavicle_02_jnt', 'l_clavicle_01_jnt')    
    
    #R Clavicle
    cmds.parent('r_clavicle_02_jnt', 'r_clavicle_01_jnt')  
    
def parent_arm_joints():
    """Parents arm joints to create skeletal hiearchy"""
    # L Arm
    cmds.parent('l_elbow_jnt', 'l_shoulder_jnt')  
    
    cmds.parent('l_wrist_jnt', 'l_elbow_jnt')
    
    cmds.parent('l_shoulder_jnt', 'l_clavicle_02_jnt')   
    
    # R Arm
    cmds.parent('r_elbow_jnt', 'r_shoulder_jnt')  
    
    cmds.parent('r_wrist_jnt', 'r_elbow_jnt') 
    
    cmds.parent('r_shoulder_jnt', 'r_clavicle_02_jnt')   
    
def parent_leg_joints():
    """Parents leg joints to create skeletal hiearchy"""
    # L Leg
    cmds.parent('l_knee_jnt', 'l_leg_jnt')  
    cmds.parent('l_ankle_jnt', 'l_knee_jnt')  
    cmds.parent('l_foot_02_jnt', 'l_foot_01_jnt')    
    cmds.parent('l_foot_03_jnt', 'l_foot_02_jnt')  
      
    cmds.parent('l_foot_01_jnt', 'l_ankle_jnt')  
    
    # R Leg
    cmds.parent('r_knee_jnt', 'r_leg_jnt')  
    cmds.parent('r_ankle_jnt', 'r_knee_jnt')  
    cmds.parent('r_foot_02_jnt', 'r_foot_01_jnt')    
    cmds.parent('r_foot_03_jnt', 'r_foot_02_jnt')  
    
    cmds.parent('r_foot_01_jnt', 'r_ankle_jnt')  
        
def parent_hand_joints():
    """Parents leg joints to create skeletal hiearchy"""
    #L Hand
    cmds.parent('l_thumb_01_jnt', 'l_wrist_jnt')  
    cmds.parent('l_thumb_02_jnt', 'l_thumb_01_jnt')  
    cmds.parent('l_thumb_03_jnt', 'l_thumb_02_jnt')  
    cmds.parent('l_thumb_04_jnt', 'l_thumb_03_jnt') 
    
    cmds.parent('l_index_01_jnt', 'l_wrist_jnt')  
    cmds.parent('l_index_02_jnt', 'l_index_01_jnt')  
    cmds.parent('l_index_03_jnt', 'l_index_02_jnt')  
    cmds.parent('l_index_04_jnt', 'l_index_03_jnt') 
    
    cmds.parent('l_middle_01_jnt', 'l_wrist_jnt')  
    cmds.parent('l_middle_02_jnt', 'l_middle_01_jnt')  
    cmds.parent('l_middle_03_jnt', 'l_middle_02_jnt')  
    cmds.parent('l_middle_04_jnt', 'l_middle_03_jnt') 
    
    cmds.parent('l_ring_01_jnt', 'l_wrist_jnt')  
    cmds.parent('l_ring_02_jnt', 'l_ring_01_jnt')  
    cmds.parent('l_ring_03_jnt', 'l_ring_02_jnt')  
    cmds.parent('l_ring_04_jnt', 'l_ring_03_jnt') 
    
    cmds.parent('l_pinky_01_jnt', 'l_wrist_jnt')  
    cmds.parent('l_pinky_02_jnt', 'l_pinky_01_jnt')  
    cmds.parent('l_pinky_03_jnt', 'l_pinky_02_jnt')  
    cmds.parent('l_pinky_04_jnt', 'l_pinky_03_jnt')     
    
    #R Hand
    cmds.parent('r_thumb_01_jnt', 'r_wrist_jnt')  
    cmds.parent('r_thumb_02_jnt', 'r_thumb_01_jnt')  
    cmds.parent('r_thumb_03_jnt', 'r_thumb_02_jnt')  
    cmds.parent('r_thumb_04_jnt', 'r_thumb_03_jnt') 
    
    cmds.parent('r_index_01_jnt', 'r_wrist_jnt')  
    cmds.parent('r_index_02_jnt', 'r_index_01_jnt')  
    cmds.parent('r_index_03_jnt', 'r_index_02_jnt')  
    cmds.parent('r_index_04_jnt', 'r_index_03_jnt') 
    
    cmds.parent('r_middle_01_jnt', 'r_wrist_jnt')  
    cmds.parent('r_middle_02_jnt', 'r_middle_01_jnt')  
    cmds.parent('r_middle_03_jnt', 'r_middle_02_jnt')  
    cmds.parent('r_middle_04_jnt', 'r_middle_03_jnt') 
    
    cmds.parent('r_ring_01_jnt', 'r_wrist_jnt')  
    cmds.parent('r_ring_02_jnt', 'r_ring_01_jnt')  
    cmds.parent('r_ring_03_jnt', 'r_ring_02_jnt')  
    cmds.parent('r_ring_04_jnt', 'r_ring_03_jnt') 
    
    cmds.parent('r_pinky_01_jnt', 'r_wrist_jnt')  
    cmds.parent('r_pinky_02_jnt', 'r_pinky_01_jnt')  
    cmds.parent('r_pinky_03_jnt', 'r_pinky_02_jnt')  
    cmds.parent('r_pinky_04_jnt', 'r_pinky_03_jnt')     
    
def parent_skeleton():
    """Parents joints to create skeletal hiearchy"""
    parent_head_joints()

    parent_neck_joints()

    parent_torso_joints()

    parent_arm_joints()

    parent_leg_joints()

    parent_hand_joints()    

def orient_neck_01_jnt():
    cmds.joint('cn_neck_01_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_cn_spine_01_jnt():
    cmds.joint('cn_spine_01_jnt', e=True, oj='xzy', sao='zup', ch=True)    

def orient_r_clavicle_01_jnt():
    cmds.joint('r_clavicle_01_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_r_shoulder_jnt():
    cmds.joint('r_shoulder_jnt', e=True, oj='xzy', sao='zup', ch=True)
       
def orient_l_thumb_01_jnt():
    cmds.joint('l_thumb_01_jnt', e=True, oj='xyz', sao='zup', ch=True)    
    
def orient_l_index_01_jnt():
    cmds.joint('l_index_01_jnt', e=True, oj='xzy', sao='zup', ch=True)  
    
def orient_l_middle_01_jnt():
    cmds.joint('l_middle_01_jnt', e=True, oj='xzy', sao='zup', ch=True)  
    
def orient_l_ring_01_jnt():
    cmds.joint('l_ring_01_jnt', e=True, oj='xzy', sao='zup', ch=True)  
    
def orient_l_pinky_01_jnt():
    cmds.joint('l_pinky_01_jnt', e=True, oj='xzy', sao='zup', ch=True)  
    
def orient_l_wrist_jnt():
    cmds.joint('l_wrist_jnt', e=True, oj='none', sao='zup', ch=False)   
    
def orient_l_clavicle_01_jnt():
    cmds.joint('l_clavicle_01_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_l_shoulder_jnt():
    cmds.joint('l_shoulder_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_l_eye_jnt():
    cmds.joint('l_eye_jnt', e=True, oj='none', sao='zup', ch=False)
    
def orient_r_eye_jnt():
    cmds.joint('r_eye_jnt', e=True, oj='none', sao='zup', ch=False)
    
def orient_r_leg_jnt():
    cmds.joint('r_leg_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_cn_jaw_jnt():
    cmds.joint('cn_jaw_jnt', e=True, oj='none', sao='zup', ch=False)
    
def orient_r_foot_01_jnt():
    cmds.joint('r_foot_01_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_l_leg_jnt():
    cmds.joint('l_leg_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def orient_l_foot_01_jnt():
    cmds.joint('l_foot_01_jnt', e=True, oj='xzy', sao='zup', ch=True)
    
def oriented_joints():
    """Orient joints to create oriented joint hiearchy"""
    orient_neck_01_jnt()
    
    orient_l_eye_jnt()
    
    orient_r_eye_jnt()
    
    orient_cn_jaw_jnt()
    
    orient_cn_spine_01_jnt()
    
    orient_r_clavicle_01_jnt()
    
    orient_r_shoulder_jnt()
    
    orient_l_clavicle_01_jnt()
    
    orient_l_shoulder_jnt()
    
    orient_r_leg_jnt()
    
    orient_r_foot_01_jnt()
    
    orient_l_leg_jnt()
    
    orient_l_foot_01_jnt()
    
    orient_l_wrist_jnt() 
    
    orient_l_thumb_01_jnt() 
    
    orient_l_index_01_jnt() 
    
    orient_l_middle_01_jnt() 
    
    orient_l_ring_01_jnt() 
    
    orient_l_pinky_01_jnt() 
    

def create_rig_hierarchy():
    '''Creates rig hiearchy'''
    cmds.group(em=True, name='Character_Rig')

    cmds.group(em=True, name='Geo_GRP')

    cmds.group(em=True, name='Skeleton_GRP')

    cmds.group(em=True, name='Ctrl_GRP')
    
    cmds.group(em=True, name='Misc_GRP')
    
    cmds.group(em=True, name='Guides_GRP')

    cmds.parent('Geo_GRP', 'Character_Rig')
    
    cmds.parent('Skeleton_GRP', 'Character_Rig')
    
    cmds.parent('Ctrl_GRP', 'Character_Rig')
    
    cmds.parent('Misc_GRP', 'Character_Rig')
    
    cmds.parent('Guides_GRP', 'Misc_GRP')
    
    cmds.parent('cn_spine_01_jnt', 'Skeleton_GRP')
    
    cmds.parent('l_leg_jnt', 'Skeleton_GRP')
    
    cmds.parent('r_leg_jnt', 'Skeleton_GRP')
    
    cmds.parent('l_clavicle_01_jnt', 'Skeleton_GRP')
    
    cmds.parent('r_clavicle_01_jnt', 'Skeleton_GRP')
    
    cmds.parent('cn_neck_01_jnt', 'Skeleton_GRP')
    
    for section in character_rig_guides:
        for guide_name in character_rig_guides[section]:
            if guide_name.endswith("_guide"):
                cmds.parent(guide_name, 'Guides_GRP')
        
create_guides()

build_skeleton()

parent_skeleton()

oriented_joints()

create_rig_hierarchy()
