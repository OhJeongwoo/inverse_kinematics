import numpy as np


J = 15
ROOT = 0
CHEST = 1
NECK = 2
LEFT_SHOULDER = 3
RIGHT_SHOULDER = 4
LEFT_ELBOW = 5
RIGHT_ELBOW = 6
LEFT_WRIST = 7
RIGHT_WRIST = 8
LEFT_HIP = 9
RIGHT_HIP = 10
LEFT_KNEE = 11
RIGHT_KNEE = 12
LEFT_ANKLE = 13
RIGHT_ANKLE = 14

BONES = [{'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': CHEST, 'child': CHEST, 'length': 1.0},
         {'parent': CHEST, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0},
         {'parent': ROOT, 'child': CHEST, 'length': 1.0}]

project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
original_motion_path = project_path + "/original_video.npy"
bones_path = project_path + "/bones_description.yaml"

original_motion_video = np.load(original_motion_path)
#BONES = load_bones(bones_path)

def pose_normalization(pose):
    """
    input
    pose

    output
    normalized pose

    condition 1. set root to origin
    condition 2. set root-chest line to z-axis
    condition 3. set hip-line vetically to y-axis
    """
    # set root to origin

    # get rotation matrix which make meet condition 2 and 3

    # calculate normalized pose


def video_normalization(video):
    """
    get normalized pose data video from original motion video

    input
    video: T*J*3 np array
    T means # of frames
    J means # of joints (in this casme J = 15)
    each joint is represented by [x,y,z]
    
    output
    normalization video: T*J*3 np array
    """
    return np.array([pose_normalization(video[i]) for i in range(video.shape(0))])
