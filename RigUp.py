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


def create_head_guides():
    """Creates head guide locators"""

    # Center head guides
    cn_head_guide = cmds.spaceLocator(name='cn_head_guide')[0]
    cmds.xform(cn_head_guide, ws=True, t=(0.002, 5.501, 0))

    cn_jaw_guide = cmds.spaceLocator(name='cn_jaw_guide')[0]
    cmds.xform(cn_jaw_guide, ws=True, t=(0.004, 5.201, 0.397))

    # L eye Guide
    l_eye_guide = cmds.spaceLocator(name='l_eye_guide')[0]
    cmds.xform(l_eye_guide, ws=True, t=(0.154, 5.749, 0.314))

    # R eye Guide
    r_eye_guide = cmds.spaceLocator(name='r_eye_guide')[0]
    cmds.xform(r_eye_guide, ws=True, t=(-0.149, 5.749, 0.314))


def create_neck_guides():
    """Creates neck guide locators"""

    # Neck guides
    cn_neck_01_guide = cmds.spaceLocator(name='cn_neck_01_guide')[0]
    cmds.xform(cn_neck_01_guide, ws=True, t=(0.002, 4.988, 0))

    cn_neck_02_guide = cmds.spaceLocator(name='cn_neck_02_guide')[0]
    cmds.xform(cn_neck_02_guide, ws=True, t=(0.002, 5.164, 0))

    cn_neck_03_guide = cmds.spaceLocator(name='cn_neck_03_guide')[0]
    cmds.xform(cn_neck_03_guide, ws=True, t=(0.002, 5.361, 0))


def create_torso_guides():
    """Creates torso guide locators"""
    # Torso guides
    cn_spine_01_guide = cmds.spaceLocator(name='cn_spine_01_guide')[0]
    cmds.xform(cn_spine_01_guide, ws=True, t=(0.002, 3.4, 0.041))
    
    cn_spine_02_guide = cmds.spaceLocator(name='cn_spine_02_guide')[0]
    cmds.xform(cn_spine_02_guide, ws=True, t=(0.002, 3.603, 0.041))

    cn_spine_03_guide = cmds.spaceLocator(name='cn_spine_03_guide')[0]
    cmds.xform(cn_spine_03_guide, ws=True, t=(0.002, 3.807, 0.041))

    cn_spine_04_guide = cmds.spaceLocator(name='cn_spine_04_guide')[0]
    cmds.xform(cn_spine_04_guide, ws=True, t=(0.002, 4.011, 0.041))

    cn_spine_05_guide = cmds.spaceLocator(name='cn_spine_05_guide')[0]
    cmds.xform(cn_spine_05_guide, ws=True, t=(0.002, 4.215, 0.041))

    cn_spine_06_guide = cmds.spaceLocator(name='cn_spine_06_guide')[0]
    cmds.xform(cn_spine_06_guide, ws=True, t=(0.002, 4.419, 0.041))

    cn_spine_07_guide = cmds.spaceLocator(name='cn_spine_07_guide')[0]
    cmds.xform(cn_spine_07_guide, ws=True, t=(0.002, 4.826, 0.041))

    cn_spine_08_guide = cmds.spaceLocator(name='cn_spine_08_guide')[0]
    cmds.xform(cn_spine_08_guide, ws=True, t=(0.002, 4.826, 0.041))


def create_arm_guides():
    """Creates arm guide locators"""
    # L arm guides
    l_shoulder_guide = cmds.spaceLocator(name='l_shoulder_guide')[0]
    cmds.xform(l_shoulder_guide, ws=True, t=(0.476, 4.901, -0.05))

    l_clavicle_01_guide = cmds.spaceLocator(name='l_clavicle_01_guide')[0]
    cmds.xform(l_clavicle_01_guide, ws=True, t=(0.054, 4.841, 0))

    l_clavicle_02_guide = cmds.spaceLocator(name='l_clavicle_02_guide')[0]
    cmds.xform(l_clavicle_02_guide, ws=True, t=(0.476, 4.901, -0.05))

    l_elbow_guide = cmds.spaceLocator(name='l_elbow_guide')[0]
    cmds.xform(l_elbow_guide, ws=True, t=(1.279, 4.901,  -0.049))

    l_wrist_guide = cmds.spaceLocator(name='l_wrist_guide')[0]
    cmds.xform(l_wrist_guide, ws=True, t=(2.144, 4.901,  -0.038))

    # R Arm Guides
    r_shoulder_guide = cmds.spaceLocator(name='r_shoulder_guide')[0]
    cmds.xform(r_shoulder_guide, ws=True, t=(-0.476, 4.901,  -0.05))

    r_clavicle_01_guide = cmds.spaceLocator(name='r_clavicle_01_guide')[0]
    cmds.xform(r_clavicle_01_guide, ws=True, t=(-0.049, 4.841,  0))

    r_clavicle_02_guide = cmds.spaceLocator(name='r_clavicle_02_guide')[0]
    cmds.xform(r_clavicle_02_guide, ws=True, t=(-0.476,  4.901,  -0.05))
    
    r_elbow_guide = cmds.spaceLocator(name='r_elbow_guide')[0]
    cmds.xform(r_elbow_guide, ws=True, t=(-1.279,  4.901,  -0.049))

    r_wrist_guide = cmds.spaceLocator(name='r_wrist_guide')[0]
    cmds.xform(r_wrist_guide, ws=True, t=(-2.144,  4.901, -0.038))


def create_leg_guides():
    """Creates leg guide locators"""
    # L leg guides
    l_leg_guide = cmds.spaceLocator(name='l_leg_guide')[0]
    cmds.xform(l_leg_guide, ws=True, t=(0.183,  3.404, 0.038))

    l_knee_guide = cmds.spaceLocator(name='l_knee_guide')[0]
    cmds.xform(l_knee_guide, ws=True, t=(0.183,  1.859, 0.064))

    l_ankle_guide = cmds.spaceLocator(name='l_ankle_guide')[0]
    cmds.xform(l_ankle_guide, ws=True, t=(0.183,  0.182, -0.018))

    l_foot_01_guide = cmds.spaceLocator(name='l_foot_01_guide')[0]
    cmds.xform(l_foot_01_guide, ws=True, t=(0.183,  0.182, -0.018))

    l_foot_02_guide = cmds.spaceLocator(name='l_foot_02_guide')[0]
    cmds.xform(l_foot_02_guide, ws=True, t=(0.204, 0, 0.361))

    l_foot_03_guide = cmds.spaceLocator(name='l_foot_03_guide')[0]
    cmds.xform(l_foot_03_guide, ws=True, t=(0.204, 0, 0.497))

    # R leg guides
    r_leg_guide = cmds.spaceLocator(name='r_leg_guide')[0]
    cmds.xform(r_leg_guide, ws=True, t=(-0.183,  3.404, 0.038))

    r_knee_guide = cmds.spaceLocator(name='r_knee_guide')[0]
    cmds.xform(r_knee_guide, ws=True, t=(-0.183,  1.859, 0.064))
    
    r_ankle_guide = cmds.spaceLocator(name='r_ankle_guide')[0]
    cmds.xform(r_ankle_guide, ws=True, t=(-0.183, 0.182, -0.018))

    r_foot_01_guide = cmds.spaceLocator(name='r_foot_01_guide')[0]
    cmds.xform(r_foot_01_guide, ws=True, t=(-0.183, 0.182, -0.018))
    
    r_foot_02_guide = cmds.spaceLocator(name='r_foot_02_guide')[0]
    cmds.xform(r_foot_02_guide, ws=True, t=(-0.204, 0, 0.361))

    r_foot_03_guide = cmds.spaceLocator(name='r_foot_03_guide')[0]
    cmds.xform(r_foot_03_guide, ws=True, t=(-0.204, 0, 0.497))
    
def create_hand_guides():
    """Creates hand guide locators"""

    ###################################################################################################
    # L Hand Guides
    ###################################################################################################

    # Index
    l_index_01_guide = cmds.spaceLocator(name='l_index_01_guide')[0]
    cmds.xform(l_index_01_guide, ws=True, t=(2.428, 4.913, 0.112))

    l_index_02_guide = cmds.spaceLocator(name='l_index_02_guide')[0]
    cmds.xform(l_index_02_guide, ws=True, t=(2.537,4.913, 0.134))
    
    l_index_03_guide = cmds.spaceLocator(name='l_index_03_guide')[0]
    cmds.xform(l_index_03_guide, ws=True, t=(2.669, 4.923, 0.163))

    l_index_04_guide = cmds.spaceLocator(name='l_index_04_guide')[0]
    cmds.xform(l_index_04_guide, ws=True, t=(2.778, 4.941, 0.181))

    # Ring
    l_ring_01_guide = cmds.spaceLocator(name='l_ring_01_guide')[0]
    cmds.xform(l_ring_01_guide, ws=True, t=(2.442, 4.922, -0.067))

    l_ring_02_guide = cmds.spaceLocator(name='l_ring_02_guide')[0]
    cmds.xform(l_ring_02_guide, ws=True, t=(2.562, 4.923, -0.07))
    
    l_ring_03_guide = cmds.spaceLocator(name='l_ring_03_guide')[0]
    cmds.xform(l_ring_03_guide, ws=True, t=(2.657, 4.924, -0.072))

    l_ring_04_guide = cmds.spaceLocator(name='l_ring_04_guide')[0]
    cmds.xform(l_ring_04_guide, ws=True, t=(2.807, 4.923, -0.076))

    # Middle
    l_middle_01_guide = cmds.spaceLocator(name='l_middle_01_guide')[0]
    cmds.xform(l_middle_01_guide, ws=True, t=(2.444, 4.923, 0.025))

    l_middle_02_guide = cmds.spaceLocator(name='l_middle_02_guide')[0]
    cmds.xform(l_middle_02_guide, ws=True, t=(2.567, 4.921, 0.032))

    l_middle_03_guide = cmds.spaceLocator(name='l_middle_03_guide')[0]
    cmds.xform(l_middle_03_guide, ws=True, t=(2.691, 4.927, 0.038))

    l_middle_04_guide = cmds.spaceLocator(name='l_middle_04_guide')[0]
    cmds.xform(l_middle_04_guide, ws=True, t=(2.835, 4.964, 0.047))


    # Pinky
    l_pinky_01_guide = cmds.spaceLocator(name='l_pinky_01_guide')[0]
    cmds.xform(l_pinky_01_guide, ws=True, t=(2.413, 4.91, -0.148))

    l_pinky_02_guide = cmds.spaceLocator(name='l_pinky_02_guide')[0]
    cmds.xform(l_pinky_02_guide, ws=True, t=(2.517, 4.906, -0.165))

    l_pinky_03_guide = cmds.spaceLocator(name='l_pinky_03_guide')[0]
    cmds.xform(l_pinky_03_guide, ws=True, t=(2.597, 4.904, -0.176))

    l_pinky_04_guide = cmds.spaceLocator(name='l_pinky_04_guide')[0]
    cmds.xform(l_pinky_04_guide, ws=True, t=(2.702, 4.879, -0.187))

    # Thumb
    l_thumb_01_guide = cmds.spaceLocator(name='l_thumb_01_guide')[0]
    cmds.xform(l_thumb_01_guide, ws=True, t=(2.221, 4.879, 0.092))

    l_thumb_02_guide = cmds.spaceLocator(name='l_thumb_02_guide')[0]
    cmds.xform(l_thumb_02_guide, ws=True, t=(2.27, 4.828, 0.18))

    l_thumb_03_guide = cmds.spaceLocator(name='l_thumb_03_guide')[0]
    cmds.xform(l_thumb_03_guide, ws=True, t=(2.319, 4.784, 0.254))

    l_thumb_04_guide = cmds.spaceLocator(name='l_thumb_04_guide')[0]
    cmds.xform(l_thumb_04_guide, ws=True, t=(2.376, 4.745, 0.368))

    ##################################################################################################
    # R Hand Guides
    ##################################################################################################

    # Index
    r_index_01_guide = cmds.spaceLocator(name='r_index_01_guide')[0]
    cmds.xform(r_index_01_guide, ws=True, t=(-2.428, 4.913, 0.112))

    r_index_02_guide = cmds.spaceLocator(name='r_index_02_guide')[0]
    cmds.xform(r_index_02_guide, ws=True, t=(-2.537, 4.913, 0.134))

    r_index_03_guide = cmds.spaceLocator(name='r_index_03_guide')[0]
    cmds.xform(r_index_03_guide, ws=True, t=(-2.669, 4.913, 0.134))

    r_index_04_guide = cmds.spaceLocator(name='r_index_04_guide')[0]
    cmds.xform(r_index_04_guide, ws=True, t=(-2.778, 4.941, 0.181))

    # Ring
    r_ring_01_guide = cmds.spaceLocator(name='r_ring_01_guide')[0]
    cmds.xform(r_ring_01_guide, ws=True, t=(-2.442, 4.922, -0.067))

    r_ring_02_guide = cmds.spaceLocator(name='r_ring_02_guide')[0]
    cmds.xform(r_ring_02_guide, ws=True, t=(-2.562, 4.929, -0.07))

    r_ring_03_guide = cmds.spaceLocator(name='r_ring_03_guide')[0]
    cmds.xform(r_ring_03_guide, ws=True, t=(-2.657, 4.929, -0.075))

    r_ring_04_guide = cmds.spaceLocator(name='r_ring_04_guide')[0]
    cmds.xform(r_ring_04_guide, ws=True, t=(-2.805, 4.954, -0.079))

    # Middle
    r_middle_01_guide = cmds.spaceLocator(name='r_middle_01_guide')[0]
    cmds.xform(r_middle_01_guide, ws=True, t=(-2.444, 4.923, 0.025))

    r_middle_02_guide = cmds.spaceLocator(name='r_middle_02_guide')[0]
    cmds.xform(r_middle_02_guide, ws=True, t=(-2.568, 4.921,  0.032))

    r_middle_03_guide = cmds.spaceLocator(name='r_middle_03_guide')[0]
    cmds.xform(r_middle_03_guide, ws=True, t=(-2.691, 4.927, 0.038))

    r_middle_04_guide = cmds.spaceLocator(name='r_middle_04_guide')[0]
    cmds.xform(r_middle_04_guide, ws=True, t=(-2.835, 4.964, 0.047))

    # Pinky
    r_pinky_01_guide = cmds.spaceLocator(name='r_pinky_01_guide')[0]
    cmds.xform(r_pinky_01_guide, ws=True, t=(-2.413, 4.91, -0.148))

    r_pinky_02_guide = cmds.spaceLocator(name='r_pinky_02_guide')[0]
    cmds.xform(r_pinky_02_guide, ws=True, t=(-2.517, 4.906, -0.165))

    r_pinky_03_guide = cmds.spaceLocator(name='r_pinky_03_guide')[0]
    cmds.xform(r_pinky_03_guide, ws=True, t=(-2.597, 4.904, -0.176))

    r_pinky_04_guide = cmds.spaceLocator(name='r_pinky_04_guide')[0]
    cmds.xform(r_pinky_04_guide, ws=True, t=(-2.702, 4.928, -0.187))

    # Thumb
    r_thumb_01_guide = cmds.spaceLocator(name='r_thumb_01_guide')[0]
    cmds.xform(r_thumb_01_guide, ws=True, t=(-2.221, 4.879, 0.092))

    r_thumb_02_guide = cmds.spaceLocator(name='r_thumb_02_guide')[0]
    cmds.xform(r_thumb_02_guide, ws=True, t=(-2.27, 4.828, 0.18))

    r_thumb_03_guide = cmds.spaceLocator(name='r_thumb_03_guide')[0]
    cmds.xform(r_thumb_03_guide, ws=True, t=(-2.319, 4.784, 0.254))

    r_thumb_04_guide = cmds.spaceLocator(name='r_thumb_04_guide')[0]
    cmds.xform(r_thumb_04_guide, ws=True, t=(-2.376, 4.745, 0.368))


def create_all_guides():
    """Creates all biped rig placement guides."""
    create_head_guides()
    create_neck_guides()
    create_torso_guides()
    create_arm_guides()
    create_leg_guides()
    create_hand_guides()

########################################################################################################################
# Skeleton Creation
########################################################################################################################
def create_head_joints():
    """Builds skeleton at the location of guide locators."""
    # CN Head
    cmds.select(clear=True)

    cn_head_guide_pos = cmds.xform('cn_head_guide', worldSpace=True, q=True, translation=True)

    cn_head_jnt = cmds.joint(name='cn_head_jnt', position=cn_head_guide_pos)    
    
    # L Eye
    cmds.select(clear=True)

    l_eye_guide_pos = cmds.xform('l_eye_guide', worldSpace=True, q=True, translation=True)

    l_eye_jnt = cmds.joint(name='l_eye_jnt', position=l_eye_guide_pos)    

    # R Eye
    cmds.select(clear=True)

    r_eye_guide_pos = cmds.xform('r_eye_guide', worldSpace=True, q=True, translation=True)

    r_eye_jnt = cmds.joint(name='r_eye_jnt', position=r_eye_guide_pos)  

    # CN Jaw
    cmds.select(clear=True)

    cn_jaw_guide_pos = cmds.xform('cn_jaw_guide', worldSpace=True, q=True, translation=True)

    cn_jaw_jnt = cmds.joint(name='cn_jaw_jnt', position=cn_jaw_guide_pos)    

def create_neck_joints():
    """Builds skeleton at the location of guide locators."""
    # CN Neck 01
    cmds.select(clear=True)

    cn_neck_01_guide_pos = cmds.xform('cn_neck_01_guide', worldSpace=True, q=True, translation=True)

    cn_neck_01_jnt = cmds.joint(name='cn_neck_01_jnt', position=cn_neck_01_guide_pos)    
    
    # CN Neck 02
    cmds.select(clear=True)

    cn_neck_02_guide_pos = cmds.xform('cn_neck_02_guide', worldSpace=True, q=True, translation=True)

    cn_neck_02_jnt = cmds.joint(name='cn_neck_02_jnt', position=cn_neck_02_guide_pos)    
    
    # CN Neck 03
    cmds.select(clear=True)

    cn_neck_03_guide_pos = cmds.xform('cn_neck_03_guide', worldSpace=True, q=True, translation=True)

    cn_neck_03_jnt = cmds.joint(name='cn_neck_03_jnt', position=cn_neck_03_guide_pos)        

def create_torso_joints():
    """Builds skeleton at the location of guide locators."""
    # CN Spine 01
    cmds.select(clear=True)

    cn_spine_01_guide_pos = cmds.xform('cn_spine_01_guide', worldSpace=True, q=True, translation=True)

    cn_spine_01_jnt = cmds.joint(name='cn_spine_01_jnt', position=cn_spine_01_guide_pos)    
    
    # CN Spine 02
    cmds.select(clear=True)

    cn_spine_02_guide_pos = cmds.xform('cn_spine_02_guide', worldSpace=True, q=True, translation=True)

    cn_spine_02_jnt = cmds.joint(name='cn_spine_02_jnt', position=cn_spine_02_guide_pos)    
    
    # CN Spine 03
    cmds.select(clear=True)

    cn_spine_03_guide_pos = cmds.xform('cn_spine_03_guide', worldSpace=True, q=True, translation=True)

    cn_spine_03_jnt = cmds.joint(name='cn_spine_03_jnt', position=cn_spine_03_guide_pos)    
    
    # CN Spine 04
    cmds.select(clear=True)

    cn_spine_04_guide_pos = cmds.xform('cn_spine_04_guide', worldSpace=True, q=True, translation=True)

    cn_spine_04_jnt = cmds.joint(name='cn_spine_04_jnt', position=cn_spine_04_guide_pos)    
    
    # CN Spine 05
    cmds.select(clear=True)

    cn_spine_05_guide_pos = cmds.xform('cn_spine_05_guide', worldSpace=True, q=True, translation=True)

    cn_spine_05_jnt = cmds.joint(name='cn_spine_05_jnt', position=cn_spine_05_guide_pos)        

    # CN Spine 06
    cmds.select(clear=True)

    cn_spine_06_guide_pos = cmds.xform('cn_spine_06_guide', worldSpace=True, q=True, translation=True)

    cn_spine_06_jnt = cmds.joint(name='cn_spine_06_jnt', position=cn_spine_06_guide_pos)    
    
    # CN Spine 07
    cmds.select(clear=True)

    cn_spine_07_guide_pos = cmds.xform('cn_spine_07_guide', worldSpace=True, q=True, translation=True)

    cn_spine_07_jnt = cmds.joint(name='cn_spine_07_jnt', position=cn_spine_07_guide_pos)    
    
    # CN Spine 08
    cmds.select(clear=True)

    cn_spine_08_guide_pos = cmds.xform('cn_spine_08_guide', worldSpace=True, q=True, translation=True)

    cn_spine_08_jnt = cmds.joint(name='cn_spine_08_jnt', position=cn_spine_08_guide_pos)    

def create_arm_joints():
    """Builds skeleton at the location of guide locators."""
    # R Clavicle 01
    cmds.select(clear=True)
    r_clavicle_01_guide_pos = cmds.xform('r_clavicle_01_guide', worldSpace=True, q=True, translation=True)

    r_clavicle_01_jnt = cmds.joint(name='r_clavicle_01_jnt', position=r_clavicle_01_guide_pos)
    
    # R Clavicle 02
    cmds.select(clear=True)
    r_clavicle_02_guide_pos = cmds.xform('r_clavicle_02_guide', worldSpace=True, q=True, translation=True)

    r_clavicle_02_jnt = cmds.joint(name='r_clavicle_02_jnt', position=r_clavicle_02_guide_pos)    
    
    # R Shoulder
    cmds.select(clear=True)

    r_shoulder_guide_pos = cmds.xform('r_shoulder_guide', worldSpace=True, q=True, translation=True)

    r_shoulder_jnt = cmds.joint(name='r_shoulder_jnt', position=r_shoulder_guide_pos)
    
    # R Elbow
    cmds.select(clear=True)

    r_elbow_guide_pos = cmds.xform('r_elbow_guide', worldSpace=True, q=True, translation=True)

    r_elbow_jnt = cmds.joint(name='r_elbow_jnt', position=r_elbow_guide_pos)
    
    # L Clavicle 01
    cmds.select(clear=True)
    l_clavicle_01_guide_pos = cmds.xform('l_clavicle_01_guide', worldSpace=True, q=True, translation=True)

    l_clavicle_01_jnt = cmds.joint(name='l_clavicle_01_jnt', position=l_clavicle_01_guide_pos)
    
    # L Clavicle 02
    cmds.select(clear=True)
    l_clavicle_02_guide_pos = cmds.xform('l_clavicle_02_guide', worldSpace=True, q=True, translation=True)

    l_clavicle_02_jnt = cmds.joint(name='l_clavicle_02_jnt', position=l_clavicle_02_guide_pos)
    
    # L Shoulder
    cmds.select(clear=True)

    l_shoulder_guide_pos = cmds.xform('l_shoulder_guide', worldSpace=True, q=True, translation=True)

    l_shoulder_jnt = cmds.joint(name='l_shoulder_jnt', position=l_shoulder_guide_pos)


    # L Elbow
    cmds.select(clear=True)

    l_elbow_guide_pos = cmds.xform('l_elbow_guide', worldSpace=True, q=True, translation=True)

    l_elbow_jnt = cmds.joint(name='l_elbow_jnt', position=l_elbow_guide_pos)
    
def create_leg_joints():
    """Builds skeleton at the location of guide locators."""
    # R Leg
    cmds.select(clear=True)

    r_leg_guide_pos = cmds.xform('r_leg_guide', worldSpace=True, q=True, translation=True)

    r_leg_jnt = cmds.joint(name='r_leg_jnt', position=r_leg_guide_pos)

    # R Knee
    cmds.select(clear=True)

    r_knee_guide_pos = cmds.xform('r_knee_guide', worldSpace=True, q=True, translation=True)

    r_knee_jnt = cmds.joint(name='r_knee_jnt', position=r_knee_guide_pos)
    
    # R Ankle
    cmds.select(clear=True)

    r_ankle_guide_pos = cmds.xform('r_ankle_guide', worldSpace=True, q=True, translation=True)

    r_ankle_jnt = cmds.joint(name='r_ankle_jnt', position=r_ankle_guide_pos)

    # R Foot 01
    cmds.select(clear=True)

    r_foot_01_guide_pos = cmds.xform('r_foot_01_guide', worldSpace=True, q=True, translation=True)

    r_foot_01_jnt = cmds.joint(name='r_foot_01_jnt', position=r_foot_01_guide_pos)
    

    # R Foot 02
    cmds.select(clear=True)

    r_foot_02_guide_pos = cmds.xform('r_foot_02_guide', worldSpace=True, q=True, translation=True)

    r_foot_02_jnt = cmds.joint(name='r_foot_02_jnt', position=r_foot_02_guide_pos)

    # R Foot 03
    cmds.select(clear=True)

    r_foot_03_guide_pos = cmds.xform('r_foot_03_guide', worldSpace=True, q=True, translation=True)

    r_foot_03_jnt = cmds.joint(name='r_foot_03_jnt', position=r_foot_03_guide_pos)
    
    # L Leg
    cmds.select(clear=True)

    l_leg_guide_pos = cmds.xform('l_leg_guide', worldSpace=True, q=True, translation=True)

    l_leg_jnt = cmds.joint(name='l_leg_jnt', position=l_leg_guide_pos)
        

    # L Knee
    cmds.select(clear=True)

    l_knee_guide_pos = cmds.xform('l_knee_guide', worldSpace=True, q=True, translation=True)

    l_knee_jnt = cmds.joint(name='l_knee_jnt', position=l_knee_guide_pos)


    # L Ankle
    cmds.select(clear=True)

    l_ankle_guide_pos = cmds.xform('l_ankle_guide', worldSpace=True, q=True, translation=True)

    l_ankle_jnt = cmds.joint(name='l_ankle_jnt', position=l_ankle_guide_pos)

    # L Foot 01

    cmds.select(clear=True)

    l_foot_01_guide_pos = cmds.xform('l_foot_01_guide', worldSpace=True, q=True, translation=True)

    l_foot_01_jnt = cmds.joint(name='l_foot_01_jnt', position=l_foot_01_guide_pos)

    cmds.select(clear=True)
    
    # L Foot 02 

    l_foot_02_guide_pos = cmds.xform('l_foot_02_guide', worldSpace=True, q=True, translation=True)

    l_foot_02_jnt = cmds.joint(name='l_foot_02_jnt', position=l_foot_02_guide_pos)

    cmds.select(clear=True)
    
    # L Foot 03

    l_foot_03_guide_pos = cmds.xform('l_foot_03_guide', worldSpace=True, q=True, translation=True)

    l_foot_03_jnt = cmds.joint(name='l_foot_03_jnt', position=l_foot_03_guide_pos)


def create_hand_joints():
    """Builds skeleton at the location of guide locators."""
    # R Hand Joints
    
    # R Wrist
    cmds.select(clear=True)
    r_wrist_guide_pos = cmds.xform('r_wrist_guide', worldSpace=True, q=True, translation=True)

    r_wrist_jnt = cmds.joint(name='r_wrist_jnt', position=r_wrist_guide_pos)

    cmds.select(clear=True)    

    # R Index
    cmds.select(clear=True)

    r_index_01_guide_pos = cmds.xform('r_index_01_guide', worldSpace=True, q=True, translation=True)

    r_index_01_jnt = cmds.joint(name='r_index_01_jnt', position=r_index_01_guide_pos)

    cmds.select(clear=True)

    r_index_02_guide_pos = cmds.xform('r_index_02_guide', worldSpace=True, q=True, translation=True)

    r_index_02_jnt = cmds.joint(name='r_index_02_jnt', position=r_index_02_guide_pos)

    cmds.select(clear=True)

    r_index_03_guide_pos = cmds.xform('r_index_03_guide', worldSpace=True, q=True, translation=True)

    r_index_03_jnt = cmds.joint(name='r_index_03_jnt', position=r_index_03_guide_pos)

    cmds.select(clear=True)

    r_index_04_guide_pos = cmds.xform('r_index_04_guide', worldSpace=True, q=True, translation=True)

    r_index_04_jnt = cmds.joint(name='r_index_04_jnt', position=r_index_04_guide_pos)
    
    # R Ring
    cmds.select(clear=True)

    r_ring_01_guide_pos = cmds.xform('r_ring_01_guide', worldSpace=True, q=True, translation=True)

    r_ring_01_jnt = cmds.joint(name='r_ring_01_jnt', position=r_ring_01_guide_pos)

    cmds.select(clear=True)

    r_ring_02_guide_pos = cmds.xform('r_ring_02_guide', worldSpace=True, q=True, translation=True)

    r_ring_02_jnt = cmds.joint(name='r_ring_02_jnt', position=r_ring_02_guide_pos)

    cmds.select(clear=True)

    r_ring_03_guide_pos = cmds.xform('r_ring_03_guide', worldSpace=True, q=True, translation=True)

    r_ring_03_jnt = cmds.joint(name='r_ring_03_jnt', position=r_ring_03_guide_pos)

    cmds.select(clear=True)

    r_ring_04_guide_pos = cmds.xform('r_ring_04_guide', worldSpace=True, q=True, translation=True)

    r_ring_04_jnt = cmds.joint(name='r_ring_04_jnt', position=r_ring_04_guide_pos)

    # R Thumb
    cmds.select(clear=True)

    r_thumb_01_guide_pos = cmds.xform('r_thumb_01_guide', worldSpace=True, q=True, translation=True)

    r_thumb_01_jnt = cmds.joint(name='r_thumb_01_jnt', position=r_thumb_01_guide_pos)

    cmds.select(clear=True)

    r_thumb_02_guide_pos = cmds.xform('r_thumb_02_guide', worldSpace=True, q=True, translation=True)

    r_thumb_02_jnt = cmds.joint(name='r_thumb_02_jnt', position=r_thumb_02_guide_pos)

    cmds.select(clear=True)

    r_thumb_03_guide_pos = cmds.xform('r_thumb_03_guide', worldSpace=True, q=True, translation=True)

    r_thumb_03_jnt = cmds.joint(name='r_thumb_03_jnt', position=r_thumb_03_guide_pos)

    cmds.select(clear=True)

    r_thumb_04_guide_pos = cmds.xform('r_thumb_04_guide', worldSpace=True, q=True, translation=True)

    r_thumb_04_jnt = cmds.joint(name='r_thumb_04_jnt', position=r_thumb_04_guide_pos)

    # R Pinky
    cmds.select(clear=True)

    r_pinky_01_guide_pos = cmds.xform('r_pinky_01_guide', worldSpace=True, q=True, translation=True)

    r_pinky_01_jnt = cmds.joint(name='r_pinky_01_jnt', position=r_pinky_01_guide_pos)

    cmds.select(clear=True)

    r_pinky_02_guide_pos = cmds.xform('r_pinky_02_guide', worldSpace=True, q=True, translation=True)

    r_pinky_02_jnt = cmds.joint(name='r_pinky_02_jnt', position=r_pinky_02_guide_pos)

    cmds.select(clear=True)

    r_pinky_03_guide_pos = cmds.xform('r_pinky_03_guide', worldSpace=True, q=True, translation=True)

    r_pinky_03_jnt = cmds.joint(name='r_pinky_03_jnt', position=r_pinky_03_guide_pos)

    cmds.select(clear=True)

    r_pinky_04_guide_pos = cmds.xform('r_pinky_04_guide', worldSpace=True, q=True, translation=True)

    r_pinky_04_jnt = cmds.joint(name='r_pinky_04_jnt', position=r_pinky_04_guide_pos)

    # R Middle
    cmds.select(clear=True)

    r_middle_01_guide_pos = cmds.xform('r_middle_01_guide', worldSpace=True, q=True, translation=True)

    r_middle_01_jnt = cmds.joint(name='r_middle_01_jnt', position=r_middle_01_guide_pos)

    cmds.select(clear=True)

    r_middle_02_guide_pos = cmds.xform('r_middle_02_guide', worldSpace=True, q=True, translation=True)

    r_middle_02_jnt = cmds.joint(name='r_middle_02_jnt', position=r_middle_02_guide_pos)

    cmds.select(clear=True)

    r_middle_03_guide_pos = cmds.xform('r_middle_03_guide', worldSpace=True, q=True, translation=True)

    r_middle_03_jnt = cmds.joint(name='r_middle_03_jnt', position=r_middle_03_guide_pos)

    cmds.select(clear=True)

    r_middle_04_guide_pos = cmds.xform('r_middle_04_guide', worldSpace=True, q=True, translation=True)

    r_middle_04_jnt = cmds.joint(name='r_middle_04_jnt', position=r_middle_04_guide_pos)

    # L Hand Joints
    
    # L Wrist
    cmds.select(clear=True)   
    l_wrist_guide_pos = cmds.xform('l_wrist_guide', worldSpace=True, q=True, translation=True)

    l_wrist_jnt = cmds.joint(name='l_wrist_jnt', position=l_wrist_guide_pos)

    cmds.select(clear=True)    
 
    # L Index
    cmds.select(clear=True)

    l_index_01_guide_pos = cmds.xform('l_index_01_guide', worldSpace=True, q=True, translation=True)

    l_index_01_jnt = cmds.joint(name='l_index_01_jnt', position=l_index_01_guide_pos)

    cmds.select(clear=True)

    l_index_02_guide_pos = cmds.xform('l_index_02_guide', worldSpace=True, q=True, translation=True)

    l_index_02_jnt = cmds.joint(name='l_index_02_jnt', position=l_index_02_guide_pos)

    cmds.select(clear=True)

    l_index_03_guide_pos = cmds.xform('l_index_03_guide', worldSpace=True, q=True, translation=True)

    l_index_03_jnt = cmds.joint(name='l_index_03_jnt', position=l_index_03_guide_pos)

    cmds.select(clear=True)

    l_index_04_guide_pos = cmds.xform('l_index_04_guide', worldSpace=True, q=True, translation=True)

    l_index_04_jnt = cmds.joint(name='l_index_04_jnt', position=l_index_04_guide_pos)

    # L Ring
    cmds.select(clear=True)

    l_ring_01_guide_pos = cmds.xform('l_ring_01_guide', worldSpace=True, q=True, translation=True)

    l_ring_01_jnt = cmds.joint(name='l_ring_01_jnt', position=l_ring_01_guide_pos)

    cmds.select(clear=True)

    l_ring_02_guide_pos = cmds.xform('l_ring_02_guide', worldSpace=True, q=True, translation=True)

    l_ring_02_jnt = cmds.joint(name='l_ring_02_jnt', position=l_ring_02_guide_pos)

    cmds.select(clear=True)

    l_ring_03_guide_pos = cmds.xform('l_ring_03_guide', worldSpace=True, q=True, translation=True)

    l_ring_03_jnt = cmds.joint(name='l_ring_03_jnt', position=l_ring_03_guide_pos)

    cmds.select(clear=True)

    l_ring_04_guide_pos = cmds.xform('l_ring_04_guide', worldSpace=True, q=True, translation=True)

    l_ring_04_jnt = cmds.joint(name='l_ring_04_jnt', position=l_ring_04_guide_pos)
    
    # L Middle
    cmds.select(clear=True)

    l_middle_01_guide_pos = cmds.xform('l_middle_01_guide', worldSpace=True, q=True, translation=True)

    l_middle_01_jnt = cmds.joint(name='l_middle_01_jnt', position=l_middle_01_guide_pos)

    cmds.select(clear=True)

    l_middle_02_guide_pos = cmds.xform('l_middle_02_guide', worldSpace=True, q=True, translation=True)

    l_middle_02_jnt = cmds.joint(name='l_middle_02_jnt', position=l_middle_02_guide_pos)

    cmds.select(clear=True)

    l_middle_03_guide_pos = cmds.xform('l_middle_03_guide', worldSpace=True, q=True, translation=True)

    l_middle_03_jnt = cmds.joint(name='l_middle_03_jnt', position=l_middle_03_guide_pos)

    cmds.select(clear=True)

    l_middle_04_guide_pos = cmds.xform('l_middle_04_guide', worldSpace=True, q=True, translation=True)

    l_middle_04_jnt = cmds.joint(name='l_middle_04_jnt', position=l_middle_04_guide_pos)
    
    # L Pinky
    cmds.select(clear=True)

    l_pinky_01_guide_pos = cmds.xform('l_pinky_01_guide', worldSpace=True, q=True, translation=True)

    l_pinky_01_jnt = cmds.joint(name='l_pinky_01_jnt', position=l_pinky_01_guide_pos)

    cmds.select(clear=True)

    l_pinky_02_guide_pos = cmds.xform('l_pinky_02_guide', worldSpace=True, q=True, translation=True)

    l_pinky_02_jnt = cmds.joint(name='l_pinky_02_jnt', position=l_pinky_02_guide_pos)

    cmds.select(clear=True)

    l_pinky_03_guide_pos = cmds.xform('l_pinky_03_guide', worldSpace=True, q=True, translation=True)

    l_pinky_03_jnt = cmds.joint(name='l_pinky_03_jnt', position=l_pinky_03_guide_pos)

    cmds.select(clear=True)

    l_pinky_04_guide_pos = cmds.xform('l_pinky_04_guide', worldSpace=True, q=True, translation=True)

    l_pinky_04_jnt = cmds.joint(name='l_pinky_04_jnt', position=l_pinky_04_guide_pos)

    # L Thumb
    cmds.select(clear=True)

    l_thumb_01_guide_pos = cmds.xform('l_thumb_01_guide', worldSpace=True, q=True, translation=True)

    l_thumb_01_jnt = cmds.joint(name='l_thumb_01_jnt', position=l_thumb_01_guide_pos)

    cmds.select(clear=True)

    l_thumb_02_guide_pos = cmds.xform('l_thumb_02_guide', worldSpace=True, q=True, translation=True)

    l_thumb_02_jnt = cmds.joint(name='l_thumb_02_jnt', position=l_thumb_02_guide_pos)

    cmds.select(clear=True)

    l_thumb_03_guide_pos = cmds.xform('l_thumb_03_guide', worldSpace=True, q=True, translation=True)

    l_thumb_03_jnt = cmds.joint(name='l_thumb_03_jnt', position=l_thumb_03_guide_pos)

    cmds.select(clear=True)

    l_thumb_04_guide_pos = cmds.xform('l_thumb_04_guide', worldSpace=True, q=True, translation=True)

    l_thumb_04_jnt = cmds.joint(name='l_thumb_04_jnt', position=l_thumb_04_guide_pos)

def build_skeleton():
    """Builds skeleton at the location of guide locators"""
    create_head_joints()
    create_neck_joints()
    create_torso_joints()
    create_arm_joints()
    create_leg_joints()
    create_hand_joints()
    
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
    
    # R Arm
    cmds.parent('r_elbow_jnt', 'r_shoulder_jnt')  
    
    cmds.parent('r_wrist_jnt', 'r_elbow_jnt')  
    
def parent_leg_joints():
    """Parents leg joints to create skeletal hiearchy"""
    # L Leg
    cmds.parent('l_knee_jnt', 'l_leg_jnt')  
    cmds.parent('l_ankle_jnt', 'l_knee_jnt')  
    cmds.parent('l_foot_02_jnt', 'l_foot_01_jnt')    
    cmds.parent('l_foot_03_jnt', 'l_foot_02_jnt')    
    
    # R Leg
    cmds.parent('r_knee_jnt', 'r_leg_jnt')  
    cmds.parent('r_ankle_jnt', 'r_knee_jnt')  
    cmds.parent('r_foot_02_jnt', 'r_foot_01_jnt')    
    cmds.parent('r_foot_03_jnt', 'r_foot_02_jnt') 
    cmds.parent('r_ankle_jnt', 'r_knee_jnt')  
        
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
    """Parents hand joints to create skeletal hiearchy"""
    parent_head_joints()
    
    parent_neck_joints()
    
    parent_torso_joints()
    
    parent_arm_joints()
    
    parent_leg_joints()
    
    parent_hand_joints()
    
create_all_guides()

build_skeleton()

parent_skeleton()
