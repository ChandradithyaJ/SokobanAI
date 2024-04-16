from gym_sokoban.envs.sokoban_env import SokobanEnv
from branch_and_bound import SokobanNode, BranchAndBound
import time, numpy as np

PATH_PENALTY = 10 # initial penalty (U in the DFBnB algorithm)

if __name__ == "__main__":
    env = SokobanEnv()
    env.render(mode='human')
    # img1 = env.render(mode='human')
    # initial_state = {
    #     'room_fixed': env.room_fixed,
    #     'room_state': env.room_state,
    #     'box_mapping': env.box_mapping,
    #     'player_position': env.player_position,
    #     'num_env_steps': env.num_env_steps,
    #     'reward_last': env.reward_last,
    #     'boxes_on_target': env.boxes_on_target,
    # }
    # action = env.action_space.sample()
    # observation, reward, done, info = env.step(action)
    # env.render(mode='human')
    # env.reset(
    #     initial_state=initial_state,
    #     new_room=False
    # )
    # img2 = env.render(mode='human')
    # print(np.array_equal(img1, img2))
    # print(np.array_equal(img1, env.get_image(mode='rgb_array')))
    # print(np.array_equal(initial_state['room_fixed'], env.room_fixed))
    # print(np.array_equal(initial_state['room_state'], env.room_state))
    root = SokobanNode(0, 0)
    BranchAndBound(env, root, 0, PATH_PENALTY)
    time.sleep(5)