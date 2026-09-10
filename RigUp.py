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
#################

import maya.cmds as cmds


def create_head_guides():
    """Creates head guide locators"""
    # Head Guides
    cn_head_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_head_guide')[0]

    cn_l_eye_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_eye_guide')[0]

    cn_r_eye_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_eye_guide')[0]

    cn_jaw_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_jaw_guide')[0]


def create_neck_guides():
    """Creates neck guide locators"""
    # Neck Guides
    cn_neck_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_neck_01_guide')[0]

    cn_neck_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_neck_02_guide')[0]

    cn_neck_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_neck_03_guide')[0]


def create_torso_guides():
    """Creates torso guide locators"""
    # Torso Guides
    cn_spine_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_01_guide')[0]

    cn_spine_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_02_guide')[0]

    cn_spine_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_03_guide')[0]

    cn_spine_04_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_04_guide')[0]

    cn_spine_05_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_05_guide')[0]

    cn_spine_06_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_06_guide')[0]

    cn_spine_07_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_07_guide')[0]

    cn_spine_08_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_spine_08_guide')[0]


def create_arm_guides():
    """Creates arm guide locators"""
    # L Arm Guides
    cn_l_shoulder_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_shoulder_guide')[0]

    cn_l_elbow_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_elbow_guide')[0]

    # R Arm Guides
    cn_r_shoulder_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_shoulder_guide')[0]

    cn_r_elbow_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_elbow_guide')[0]


def create_leg_guides():
    # L Leg Guide
    cn_l_leg_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_leg_guide')[0]

    cn_l_knee_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_knee_guide')[0]

    cn_l_ankle_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_ankle_guide')[0]

    # R Leg Guide
    cn_r_leg_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_leg_guide')[0]

    cn_r_knee_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_knee_guide')[0]

    cn_r_ankle_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_ankle_guide')[0]


def create_hand_guides():
    """Creates hand guide locators"""
    # L Hand Guides
    cn_l_index_finger_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_index_finger_01_guide')[0]

    cn_l_index_finger_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_index_finger_02_guide')[0]

    cn_l_index_finger_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_index_finger_03_guide')[0]

    cn_l_ring_finger_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_ring_finger_01_guide')[0]

    cn_l_ring_finger_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_ring_finger_02_guide')[0]

    cn_l_ring_finger_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_ring_finger_03_guide')[0]

    cn_l_middle_finger_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_middle_finger_01_guide')[0]

    cn_l_middle_finger_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_middle_finger_02_guide')[0]

    cn_l_middle_finger_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_middle_finger_03_guide')[0]

    cn_l_pinky_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_pinky_01_guide')[0]

    cn_l_pinky_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_pinky_02_guide')[0]

    cn_l_pinky_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_pinky_03_guide')[0]

    cn_l_thumb_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_thumb_01_guide')[0]

    cn_l_thumb_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_thumb_02_guide')[0]

    cn_l_thumb_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_thumb_03_guide')[0]

    cn_l_thumb_04_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_l_thumb_04_guide')[0]

    # R Hand Guides
    cn_r_index_finger_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_index_finger_01_guide')[0]

    cn_r_index_finger_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_index_finger_02_guide')[0]

    cn_r_index_finger_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_index_finger_03_guide')[0]

    cn_r_ring_finger_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_ring_finger_01_guide')[0]

    cn_r_ring_finger_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_ring_finger_02_guide')[0]

    cn_r_ring_finger_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_ring_finger_03_guide')[0]

    cn_r_middle_finger_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_middle_finger_01_guide')[0]

    cn_r_middle_finger_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_middle_finger_02_guide')[0]

    cn_r_middle_finger_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_middle_finger_03_guide')[0]

    cn_r_pinky_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_pinky_01_guide')[0]

    cn_r_pinky_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_pinky_02_guide')[0]

    cn_r_pinky_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_pinky_03_guide')[0]

    cn_r_thumb_01_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_thumb_01_guide')[0]

    cn_r_thumb_02_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_thumb_02_guide')[0]

    cn_r_thumb_03_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_thumb_03_guide')[0]

    cn_r_thumb_04_guide = cmds.spaceLocator(p=(0, 0, 0))
    cmds.rename('locator1', 'cn_r_thumb_04_guide')[0]


def create_all_guides():
    """Create all biped rig placement guides."""
    create_head_guides()
    create_neck_guides()
    create_torso_guides()
    create_arm_guides()
    create_leg_guides()
    create_hand_guides()

def build_skeleton():
    """ Builds skeleton at the location of guide locators"""