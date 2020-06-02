import gym
import numpy as np


actions = []
observations = []
infos = []
gripper_pos = []

def main():
    env = gym.make('BaxterPickAndPlace-v1')
    numItr = 1
    initStateSpace = "random"
    env.reset()
    print("Reset!")
    actions = []
    for i in range(numItr):
        obs = env.reset()
        print("ITERATION NUMBER ", len(actions))
        action = [0, 0, 0, 0]
        goToGoal(env, obs)

        numItr +=1

    # fileName = str(env.env.spec.id)
    # fileName += ".npz"

    # np.savez_compressed(fileName, acs=actions, obs=observations, info=infos, gripper_pos=gripper_pos) # save the file


def goToGoal(env, lastObs):
    goal = lastObs['desired_goal']
    objectPos = lastObs['observation'][3:6]
    object_rel_pos = lastObs['observation'][6:9]
    episodeAcs = []
    episodeObs = []
    episodeInfo = []
    episodeGripperPos = []

    object_oriented_goal = object_rel_pos.copy()
    object_oriented_goal[2] += 0.03 # first make the gripper go slightly above the object

    timeStep = 0 #count the total number of timesteps
    episodeObs.append(lastObs)

    l_gripper_l_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_l_finger')
    l_gripper_r_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_r_finger')
    episodeGripperPos.append([l_gripper_l_finger_pos, l_gripper_r_finger_pos])

    while np.linalg.norm(object_oriented_goal) >= 0.005 and timeStep <= env._max_episode_steps: # make the gripper go slightly above the object
        action = [0, 0, 0, 0]
        object_oriented_goal = object_rel_pos.copy()
        object_oriented_goal[2] += 0.03

        for i in range(len(object_oriented_goal)):
            action[i] = object_oriented_goal[i]*6

        action[len(action)-1] = 0.05 #open

        obsDataNew, reward, done, info = env.step(action)
        timeStep += 1

        episodeAcs.append(action)
        episodeInfo.append(info)
        episodeObs.append(obsDataNew)
        
        l_gripper_l_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_l_finger')
        l_gripper_r_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_r_finger')
        episodeGripperPos.append([l_gripper_l_finger_pos, l_gripper_r_finger_pos])

        import csv
        file_name = str(env.env.spec.id)+'parameters.csv'
        with open(file_name, 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([str(l_gripper_l_finger_pos), str(l_gripper_r_finger_pos), str(action)])
        csvfile.close()

        objectPos = obsDataNew['observation'][3:6]
        object_rel_pos = obsDataNew['observation'][6:9]

    while np.linalg.norm(object_rel_pos) >= 0.005 and timeStep <= env._max_episode_steps : # pick
        # env.render()
        action = [0, 0, 0, 0]
        for i in range(len(object_rel_pos)):
            action[i] = object_rel_pos[i]*6

        action[len(action)-1] = -0.005

        obsDataNew, reward, done, info = env.step(action)
        timeStep += 1

        episodeAcs.append(action)
        episodeInfo.append(info)
        episodeObs.append(obsDataNew)

        l_gripper_l_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_l_finger')
        l_gripper_r_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_r_finger')
        episodeGripperPos.append([l_gripper_l_finger_pos, l_gripper_r_finger_pos])

        import csv
        file_name = str(env.env.spec.id)+'parameters.csv'
        with open(file_name, 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([str(l_gripper_l_finger_pos), str(l_gripper_r_finger_pos), str(action)])
        csvfile.close()


        objectPos = obsDataNew['observation'][3:6]
        object_rel_pos = obsDataNew['observation'][6:9]


    while np.linalg.norm(goal - objectPos) >= 0.01 and timeStep <= env._max_episode_steps : # place
        # env.render()
        action = [0, 0, 0, 0]
        for i in range(len(goal - objectPos)):
            action[i] = (goal - objectPos)[i]*6

        action[len(action)-1] = -0.005

        obsDataNew, reward, done, info = env.step(action)
        timeStep += 1

        episodeAcs.append(action)
        episodeInfo.append(info)
        episodeObs.append(obsDataNew)

        l_gripper_l_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_l_finger')
        l_gripper_r_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_r_finger')
        episodeGripperPos.append([l_gripper_l_finger_pos, l_gripper_r_finger_pos])

        import csv
        file_name = str(env.env.spec.id)+'parameters.csv'
        with open(file_name, 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([str(l_gripper_l_finger_pos), str(l_gripper_r_finger_pos), str(action)])
        csvfile.close()


        objectPos = obsDataNew['observation'][3:6]
        object_rel_pos = obsDataNew['observation'][6:9]

    while True: #limit the number of timesteps in the episode to a fixed duration
        # env.render()
        action = [0, 0, 0, 0]
        action[len(action)-1] = -0.005 # keep the gripper closed

        obsDataNew, reward, done, info = env.step(action)
        timeStep += 1

        episodeAcs.append(action)
        episodeInfo.append(info)
        episodeObs.append(obsDataNew)

        l_gripper_l_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_l_finger')
        l_gripper_r_finger_pos = env.env.sim.data.get_body_xpos('robot0:l_gripper_r_finger')
        episodeGripperPos.append([l_gripper_l_finger_pos, l_gripper_r_finger_pos])

        import csv
        file_name = str(env.env.spec.id)+'parameters.csv'
        with open(file_name, 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([str(l_gripper_l_finger_pos), str(l_gripper_r_finger_pos), str(action)])
        csvfile.close()

        objectPos = obsDataNew['observation'][3:6]
        object_rel_pos = obsDataNew['observation'][6:9]

        if timeStep >= env._max_episode_steps: break

    actions.append(episodeAcs)
    observations.append(episodeObs)
    infos.append(episodeInfo)
    gripper_pos.append(episodeGripperPos)


if __name__ == "__main__":
    main()
