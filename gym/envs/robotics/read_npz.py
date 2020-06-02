import numpy as np
import ipdb; ipdb.set_trace()

data = np.load( "BaxterPickAndPlace-v1.npz", allow_pickle=True)


gripper_pos = data["gripper_pos"]
action = data["acs"]

for episode, e_a in gripper_pos, action:
    for st in episode:
        grip_p = st

