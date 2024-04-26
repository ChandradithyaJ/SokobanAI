from gym_sokoban.envs.sokoban_env import SokobanEnv
from branch_and_bound import SokobanNode, BranchAndBound
import time

PATH_PENALTY = 10 # initial penalty (U in the DFBnB algorithm)

if __name__ == "__main__":
    env = SokobanEnv()
    env.render(mode='human')
    root = SokobanNode(0, 0)
    BranchAndBound(env, root, 0, PATH_PENALTY)
    time.sleep(5)