import queue, copy, random
import numpy as np

class SokobanNode:
    def __init__(self, penalty, action_code):
        self.penalty = penalty
        self.action_code = action_code
        
    def __lt__(self, other):
        return self.penalty < other.penalty

def BranchAndBound(env, curSearchNode, curPenalty, PATH_PENALTY):
    # goal is to finish the puzzle with the least penalty
    
    if env._check_if_done():
        PATH_PENALTY = curPenalty
        return
    
    # expand the search node
    children = queue.PriorityQueue()
    initial_state = {
        'room_fixed': env.room_fixed,
        'room_state': env.room_state,
        'box_mapping': env.box_mapping,
        'player_position': env.player_position,
        'num_env_steps': env.num_env_steps,
        'reward_last': env.reward_last,
        'boxes_on_target': env.boxes_on_target
    }
    possible_actions = env.get_action_lookup()
    # randomly shuffle the array to prevent the player from repeating actions all the time
    possible_change_inducing_actions = [i for i in range(1, len(possible_actions))] # 0 is "no action"
    shuffle_possible_actions = random.sample(
        possible_change_inducing_actions, 
        len(possible_change_inducing_actions)
    )
    for action_code in shuffle_possible_actions:
        env_copy = copy.deepcopy(env)
        _, reward, _, _ = env_copy.step(action_code)
        # consider move only if the player is moving
        if not np.array_equal(initial_state['player_position'], env_copy.player_position):
            children.put(SokobanNode(
                                curSearchNode.penalty - reward,
                                action_code,
                            ))
        del env_copy
       
    while not children.empty():
        env_copy = copy.deepcopy(env)
        child = children.get()
        if(curPenalty + child.penalty < PATH_PENALTY):
            _, reward, _, _ = env_copy.step(child.action_code)
            env.render(mode='human')
            BranchAndBound(
                env_copy, 
                child, 
                curPenalty + child.penalty, 
                PATH_PENALTY
            )
        del env_copy