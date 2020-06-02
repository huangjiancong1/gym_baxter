import gym
import numpy as np


actions = []
observations = []
infos = []
gripper_pos = []

def main():
    env = gym.make('BaxterPickAndPlace-v1')
    numStep = 100
    initStateSpace = "random"
    env.reset()
    obs = env.reset()
    print("Reset!")
    action = [0, 0 ,0 ,0]
    gripper_actions = np.arange(-1,1,2/numStep,"float")
    for grip_a in gripper_actions:
        env.render()
        action[len(action)-1] = grip_a 
        obsDataNew, reward, done, info = env.step(action)

        l_gripper_l_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_l_finger')
        l_gripper_r_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_r_finger')

        import csv
        file_name = str(env.env.spec.id)+'parameters.csv'
        with open(file_name, 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            # filewriter.writerow([str(l_gripper_l_finger_pos), str(l_gripper_r_finger_pos), str(l_gripper_r_finger_pos[1]-l_gripper_l_finger_pos[1]), str(action)])
            filewriter.writerow([abs(l_gripper_r_finger_pos[1] - l_gripper_l_finger_pos[1]), str(action)])
        csvfile.close()

if __name__ == "__main__":
    main()
