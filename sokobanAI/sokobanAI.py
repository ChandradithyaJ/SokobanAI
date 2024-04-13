from gym_sokoban.envs.sokoban_env import SokobanEnv

env = SokobanEnv()
env.render(mode='human')
action = env.action_space.sample()
observation, reward, done, info = env.step(action)