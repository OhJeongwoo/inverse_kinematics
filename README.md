# inverse_kinematics

1. load original pose data + reference platform info
2. normalization pose
2.1. set root to origin
2.2. set root-chest line to z-axis
2.3. set hip-line vetically to y-axis
3. generate optimization problem
4. solve optimization problem using ik-solver

base -- root -- chest      -- neck
                           -- left shoulder  -- left elbow   -- left wrist
                           -- right shoulder -- right elbow  -- right wrist
             -- left hip   -- left knee      -- left ankle
             -- right hip  -- right knee     -- right ankle


# joint description
ROOT: 0
CHEST: 1
NECK: 2
LEFT_SHOULDER: 3
RIGHT_SHOULDER: 4
LEFT_ELBOW: 5
RIGHT_ELBOW: 6
LEFT_WRIST: 7
RIGHT_WRIST: 8
LEFT_HIP: 9
RIGHT_HIP: 10
LEFT_KNEE: 11
RIGHT_KNEE: 12
LEFT_ANKLE: 13
RIGHT_ANKLE: 14

# bone description
01: ROOT-CHEST (0,1)
02: CHEST-NECK (1,2)
03: CHEST-LEFT_SHOULDER (1,3)
04: CHEST-RIGHT_SHOULDER (1,4)
05: LEFT_SHOULDER-LEFT_ELBOW (3,5)
06: RIGHT_SHOULDER-RIGHT_ELBOW (4,6)
07: LEFT_ELBOW-LEFT_WRIST (5,7)
08: RIGHT_ELBOW-RIGHT_WRIST (6,8)
09: ROOT-LEFT_HIP (0,9)
10: ROOT-RIGHT_HIP (0,10)
11: LEFT_HIP-LEFT_KNEE (9,11)
12: RIGHT_HIP-RIGHT_KNEE (10,12)
13: LEFT_KNEE-LEFT_ANKLE (11,13)
14: RIGHT_KNEE-RIGHT_ANKLE (12,14)


# video description



# plan..
implementation inverse kinematics + joint motion smoothness

We optimizes reference joints motion from original joints motion video data.
It means that we get theta_t,i(called by theta solutions) where 1 <= t <= T, 1 <= i <= J as well.
Intuitively, we want to get theta solutions which make joint positions similarly, but also make joint angle changes smoothly.
Then,we will try to add joints angle acceleration term into optimization conditions.
In this project, we will formulate optimization condition for specific environment such as humanoid, but not general environments like as multi-legged robots.


TIMELINE
April 18th : implementation pose normalization & study inverse kinematics solver
April 25th : formulation inverse kinematics solver with smoothness conditions
May 2nd    : implementation inverse kinematics sovler and demo reference video generation