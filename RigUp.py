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
    cn_head_guide = cmds.spaceLocator(p=(0.002, 5.501, 0))
    cmds.rename('locator1', 'cn_head_guide')[0]

    cn_jaw_guide = cmds.spaceLocator(p=(0.004, 5.201, 0.397))
    cmds.rename('locator1', 'cn_jaw_guide')[0]

    # L eye Guide
    l_eye_guide = cmds.spaceLocator(p=(0.154, 5.749, 0.314))
    cmds.rename('locator1', 'l_eye_guide')[0]

    # R eye Guide
    r_eye_guide = cmds.spaceLocator(p=(-0.149, 5.749, 0.314))
    cmds.rename('locator1', 'r_eye_guide')[0]


def create_neck_guides():
    """Creates neck guide locators"""

    # Neck guides
    cn_neck_01_guide = cmds.spaceLocator(p=(0, 4.988, 0))
    cmds.rename('locator1', 'cn_neck_01_guide')[0]

    cn_neck_02_guide = cmds.spaceLocator(p=(0.002, 5.164, 0))
    cmds.rename('locator1', 'cn_neck_02_guide')[0]

    cn_neck_03_guide = cmds.spaceLocator(p=(0.002, 5.361, 0))
    cmds.rename('locator1', 'cn_neck_03_guide')[0]


def create_torso_guides():
    """Creates torso guide locators"""
    # Torso guides
    cn_spine_01_guide = cmds.spaceLocator(p=(0.002, 3.4, 0.041))
    cmds.rename('locator1', 'cn_spine_01_guide')[0]

    cn_spine_02_guide = cmds.spaceLocator(p=(0.002, 3.603, 0.041))
    cmds.rename('locator1', 'cn_spine_02_guide')[0]

    cn_spine_03_guide = cmds.spaceLocator(p=(0.002, 3.807, 0.041))
    cmds.rename('locator1', 'cn_spine_03_guide')[0]

    cn_spine_04_guide = cmds.spaceLocator(p=(0.002, 4.011, 0.041))
    cmds.rename('locator1', 'cn_spine_04_guide')[0]

    cn_spine_05_guide = cmds.spaceLocator(p=(0.002, 4.215, 0.041))
    cmds.rename('locator1', 'cn_spine_05_guide')[0]

    cn_spine_06_guide = cmds.spaceLocator(p=(0.002, 4.419, 0.041))
    cmds.rename('locator1', 'cn_spine_06_guide')[0]

    cn_spine_07_guide = cmds.spaceLocator(p=(0.002, 4.622, 0.041))
    cmds.rename('locator1', 'cn_spine_07_guide')[0]

    cn_spine_08_guide = cmds.spaceLocator(p=(0.002, 4.826, 0.041))
    cmds.rename('locator1', 'cn_spine_08_guide')[0]


def create_arm_guides():
    """Creates arm guide locators"""
    # L arm guides
    l_shoulder_guide = cmds.spaceLocator(p=(0.476, 4.901, -0.05))
    cmds.rename('locator1', 'l_shoulder_guide')[0]

    l_clavicle_01_guide = cmds.spaceLocator(p=(0.054, 4.841, 0))
    cmds.rename('locator1', 'l_clavicle_01_guide')[0]

    l_clavicle_02_guide = cmds.spaceLocator(p=(0.476, 4.901, -0.05))
    cmds.rename('locator1', 'l_clavicle_02_guide')[0]

    l_elbow_guide = cmds.spaceLocator(p=(1.279, 4.901, -0.049))
    cmds.rename('locator1', 'l_elbow_guide')[0]

    l_wrist_guide = cmds.spaceLocator(p=(2.144, 4.901, -0.038))
    cmds.rename('locator1', 'l_wrist_guide')[0]

    # R Arm Guides
    r_shoulder_guide = cmds.spaceLocator(p=(-0.476, 4.901, -0.05))
    cmds.rename('locator1', 'r_shoulder_guide')[0]

    r_clavicle_01_guide = cmds.spaceLocator(p=(-0.049, 4.841, 0))
    cmds.rename('locator1', 'r_clavicle_01_guide')[0]

    r_clavicle_02_guide = cmds.spaceLocator(p=(-0.476, 4.901, -0.05))
    cmds.rename('locator1', 'r_clavicle_02_guide')[0]

    r_shoulder_guide = cmds.spaceLocator(p=(-0.476, 4.901, -0.05))
    cmds.rename('locator1', 'r_shoulder_guide')[0]

    r_elbow_guide = cmds.spaceLocator(p=(-1.279, 4.901, -0.049))
    cmds.rename('locator1', 'r_elbow_guide')[0]

    r_wrist_guide = cmds.spaceLocator(p=(-2.144, 4.901, -0.038))
    cmds.rename('locator1', 'r_wrist_guide')[0]


def create_leg_guides():
    """Creates leg guide locators"""
    # L leg guides
    l_leg_guide = cmds.spaceLocator(p=(0.183, 3.404, 0.038))
    cmds.rename('locator1', 'l_leg_guide')[0]

    l_knee_guide = cmds.spaceLocator(p=(0.183, 1.859, 0.064))
    cmds.rename('locator1', 'l_knee_guide')[0]

    l_ankle_guide = cmds.spaceLocator(p=(0.183, 0.182, -0.018))
    cmds.rename('locator1', 'l_ankle_guide')[0]

    l_foot_01_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'l_foot_01_guide')[0]

    l_foot_02_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'l_foot_02_guide')[0]

    l_foot_03_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'l_foot_03_guide')[0]

    # R leg guides
    r_leg_guide = cmds.spaceLocator(p=(-0.183, 3.404, 0.038))
    cmds.rename('locator1', 'r_leg_guide')[0]

    r_knee_guide = cmds.spaceLocator(p=(-0.183, 1.859, 0.064))
    cmds.rename('locator1', 'r_knee_guide')[0]

    r_ankle_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'r_ankle_guide')[0]

    r_foot_01_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'r_foot_01_guide')[0]

    r_foot_02_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'r_foot_02_guide')[0]

    r_foot_03_guide = cmds.spaceLocator(p=(-0.183, 0.182, -0.018))
    cmds.rename('locator1', 'r_foot_03_guide')[0]

def create_hand_guides():
    """Creates hand guide locators"""

    ###################################################################################################
    # L Hand Guides
    ###################################################################################################

    # Index
    l_index_finger_01_guide = cmds.spaceLocator(p=(2.428, 4.913, 0.112))
    cmds.rename('locator1', 'l_index_finger_01_guide')[0]

    l_index_finger_02_guide = cmds.spaceLocator(p=(2.537, 4.913, 0.134))
    cmds.rename('locator1', 'l_index_finger_02_guide')[0]

    l_index_finger_03_guide = cmds.spaceLocator(p=(2.669, 4.923, 0.163))
    cmds.rename('locator1', 'l_index_finger_03_guide')[0]

    l_index_finger_04_guide = cmds.spaceLocator(p=(2.778, 4.941, 0.181))
    cmds.rename('locator1', 'l_index_finger_04_guide')[0]

    # Ring
    l_ring_finger_01_guide = cmds.spaceLocator(p=(2.442, 4.922, -0.067))
    cmds.rename('locator1', 'l_ring_finger_01_guide')[0]

    l_ring_finger_02_guide = cmds.spaceLocator(p=(2.562, 4.929, -0.07))
    cmds.rename('locator1', 'l_ring_finger_02_guide')[0]

    l_ring_finger_03_guide = cmds.spaceLocator(p=(2.657, 4.934, -0.072))
    cmds.rename('locator1', 'l_ring_finger_03_guide')[0]

    l_ring_finger_04_guide = cmds.spaceLocator(p=(2.807, 4.943, -0.076))
    cmds.rename('locator1', 'l_ring_finger_04_guide')[0]

    # Middle
    l_middle_finger_01_guide = cmds.spaceLocator(p=(2.444, 4.923, 0.025))
    cmds.rename('locator1', 'l_middle_finger_01_guide')[0]

    l_middle_finger_02_guide = cmds.spaceLocator(p=(2.567, 4.921, 0.032))
    cmds.rename('locator1', 'l_middle_finger_02_guide')[0]

    l_middle_finger_03_guide = cmds.spaceLocator(p=(2.691, 4.927, 0.038))
    cmds.rename('locator1', 'l_middle_finger_03_guide')[0]

    l_middle_finger_04_guide = cmds.spaceLocator(p=(2.835, 4.964, 0.047))
    cmds.rename('locator1', 'l_middle_finger_04_guide')[0]

    # Pinky
    l_pinky_01_guide = cmds.spaceLocator(p=(2.413, 4.91, -0.148))
    cmds.rename('locator1', 'l_pinky_01_guide')[0]

    l_pinky_02_guide = cmds.spaceLocator(p=(2.517, 4.906, -0.165))
    cmds.rename('locator1', 'l_pinky_02_guide')[0]

    l_pinky_03_guide = cmds.spaceLocator(p=(2.597, 4.904, -0.176))
    cmds.rename('locator1', 'l_pinky_03_guide')[0]

    l_pinky_04_guide = cmds.spaceLocator(p=(2.702, 4.928, -0.187))
    cmds.rename('locator1', 'l_pinky_04_guide')[0]

    # Thumb
    l_thumb_01_guide = cmds.spaceLocator(p=(2.221, 4.879, 0.092))
    cmds.rename('locator1', 'l_thumb_01_guide')[0]

    l_thumb_02_guide = cmds.spaceLocator(p=(2.27, 4.828, 0.18))
    cmds.rename('locator1', 'l_thumb_02_guide')[0]

    l_thumb_03_guide = cmds.spaceLocator(p=(2.319, 4.784, 0.254))
    cmds.rename('locator1', 'l_thumb_03_guide')[0]

    l_thumb_04_guide = cmds.spaceLocator(p=(2.376, 4.745, 0.368))
    cmds.rename('locator1', 'l_thumb_04_guide')[0]

    ##################################################################################################
    # R Hand Guides
    ##################################################################################################

    # Index
    r_index_finger_01_guide = cmds.spaceLocator(p=(-2.428, 4.913, 0.112))
    cmds.rename('locator1', 'r_index_finger_01_guide')[0]

    r_index_finger_02_guide = cmds.spaceLocator(p=(-2.537, 4.913, 0.134))
    cmds.rename('locator1', 'r_index_finger_02_guide')[0]

    r_index_finger_03_guide = cmds.spaceLocator(p=(-2.669, 4.923, 0.163))
    cmds.rename('locator1', 'r_index_finger_03_guide')[0]

    r_index_finger_04_guide = cmds.spaceLocator(p=(-2.778, 4.941, 0.181))
    cmds.rename('locator1', 'r_index_finger_04_guide')[0]

    # Ring
    r_ring_finger_01_guide = cmds.spaceLocator(p=(-2.442, 4.922, -0.067))
    cmds.rename('locator1', 'r_ring_finger_01_guide')[0]

    r_ring_finger_02_guide = cmds.spaceLocator(p=(-2.562, 4.929, -0.07))
    cmds.rename('locator1', 'r_ring_finger_02_guide')[0]

    r_ring_finger_03_guide = cmds.spaceLocator(p=(-2.657, 4.929, -0.075))
    cmds.rename('locator1', 'r_ring_finger_03_guide')[0]

    r_ring_finger_04_guide = cmds.spaceLocator(p=(-2.805, 4.954, -0.079))
    cmds.rename('locator1', 'r_ring_finger_04_guide')[0]

    # Middle
    r_middle_finger_01_guide = cmds.spaceLocator(p=(-2.444, 4.923, 0.025))
    cmds.rename('locator1', 'r_middle_finger_01_guide')[0]

    r_middle_finger_02_guide = cmds.spaceLocator(p=(-2.568, 4.921, 0.032))
    cmds.rename('locator1', 'r_middle_finger_02_guide')[0]

    r_middle_finger_03_guide = cmds.spaceLocator(p=(-2.691, 4.927, 0.038))
    cmds.rename('locator1', 'r_middle_finger_03_guide')[0]

    r_middle_finger_04_guide = cmds.spaceLocator(p=(-2.835, 4.964, 0.047))
    cmds.rename('locator1', 'r_middle_finger_04_guide')[0]

    # Pinky
    r_pinky_01_guide = cmds.spaceLocator(p=(-2.413, 4.91, -0.148))
    cmds.rename('locator1', 'r_pinky_01_guide')[0]

    r_pinky_02_guide = cmds.spaceLocator(p=(-2.517, 4.906, -0.165))
    cmds.rename('locator1', 'r_pinky_02_guide')[0]

    r_pinky_03_guide = cmds.spaceLocator(p=(-2.597, 4.904, -0.176))
    cmds.rename('locator1', 'r_pinky_03_guide')[0]

    r_pinky_04_guide = cmds.spaceLocator(p=(-2.702, 4.928, -0.187))
    cmds.rename('locator1', 'r_pinky_04_guide')[0]

    # Thumb
    r_thumb_01_guide = cmds.spaceLocator(p=(-2.702, 4.879, 0.092))
    cmds.rename('locator1', 'r_thumb_01_guide')[0]

    r_thumb_02_guide = cmds.spaceLocator(p=(-2.27, 4.828, 0.18))
    cmds.rename('locator1', 'r_thumb_02_guide')[0]

    r_thumb_03_guide = cmds.spaceLocator(p=(-2.319, 4.784, 0.254))
    cmds.rename('locator1', 'r_thumb_03_guide')[0]

    r_thumb_04_guide = cmds.spaceLocator(p=(-2.376, 4.745, 0.368))
    cmds.rename('locator1', 'r_thumb_04_guide')[0]


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

    # L Eye

    # R Eye

    # CN Jaw

def create_neck_joints():
    """Builds skeleton at the location of guide locators."""
    # CN Neck 01

    # CN Neck 02

    # CN Neck 03

def create_torso_joints():
    """Builds skeleton at the location of guide locators."""
    # CN Spine 01

    # CN Spine 02

    # CN Spine 03

    # CN Spine 04

    # CN Spine 05

    # CN Spine 06

    # CN Spine 07

    # CN Spine 08

def create_arm_joints():
    """Builds skeleton at the location of guide locators."""
    # R Arm

    # R Elbow

    # L Arm

    # L Elbow

def create_leg_joints():
    """Builds skeleton at the location of guide locators."""
    # R leg

    # R Knee

    # R Ankle

    # R Foot 01

    # R Foot 02

    # R Foot 03

    # L leg

    # L Knee

    # L Ankle

    # L Foot 01

    # L Foot 02

    # L Foot 03


def create_hand_joints():
    """Builds skeleton at the location of guide locators."""
    # R Hand

    # R Index

    # R Ring

    # R Thumb

    # R Pinky

    # R Middle

    # L Hand

    # L Index

    # L Ring

    # L Thumb

    # L Pinky

    # L Middle
    cmds.matchTransform('')
    hands = cmds.joint(p=(0, 0, 0))

def build_skeleton():
    """Builds skeleton at the location of guide locators."""
    create_head_joints()
    create_neck_joints()
    create_torso_joints()
    create_arm_joints()
    create_leg_joints()
    create_hand_joints()

create_all_guides()

build_skeleton()
