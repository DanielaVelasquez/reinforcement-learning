import numpy as np

def get_actions(x, y, matrix):
    rows, cols = matrix.shape
    possible_actions = list()
    if y !=0:
        possible_actions.append(0)
    if y != rows - 1:
        possible_actions.append(1)
    if x !=0:
        possible_actions.append(2)
    if x!= cols -1 :
        possible_actions.append(3)
    return possible_actions
   
def get_possible_actions(matrix):
    possible_actions = list()
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            possible_actions.append(get_actions(i, j, matrix))
    return possible_actions 

def next_step(pos, action, matrix):
    x, y = pos
    rows, cols = matrix.shape
    # Left
    if action == 0 and y!=0:
        y = y - 1
    # Right
    elif action == 1 and y != cols - 1:
        y = y + 1
    # Up
    elif action == 2 and x != 0:
        x = x - 1
    # Down
    elif action == 3 and x != rows - 1:
        x = x + 1
    return (x,y)
        
def get_state(pos, matrix):
    x, y = pos
    rows, cols = matrix.shape
    if x > rows or y > cols or x<0 or y < 0:
        return -1
    state = 0
    for i in range(rows):
        for j in range(cols):
            if x == i and y == j:
                return state
            state+=1
            
    return state

def get_transition_probabilites_from(pos, action, matrix, t_p):
    x, y = pos
    next_pos = next_step(pos, action, matrix)
    
    total_states = matrix.size
    
    if next_pos != pos:
        current_state = get_state(pos, matrix)
        next_state = get_state(next_pos, matrix)

        t_p[current_state, action, next_state] = 1
        
    
def get_transition_probabilities(matrix, actions):
    rows, cols = matrix.shape
    total_states = matrix.size
    t_p = np.zeros((total_states, actions.size, total_states))
    for i in range(rows):
        for j in range(cols):
            #Here we are in one state
            for a in actions:
                get_transition_probabilites_from((i,j), a, matrix, t_p)

    return t_p
 

def get_rewards_from(pos, matrix, action, goal,rewards, reward=1):
    total_states = matrix.size
    
    next_pos = next_step(pos, action, matrix)
    
    if next_pos != pos and next_pos == goal:
        next_state = get_state(next_pos, matrix)
        current_state = get_state(pos, matrix)
        rewards[current_state,action, next_state] = reward
    return rewards                         

def get_rewards(matrix, actions, goal):
    total_states = matrix.size
    rewards = np.zeros((total_states, actions.size, total_states))
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for a in actions:
                get_rewards_from((i,j), matrix, a, goal, rewards)
    return rewards

def describe_action(a):
    if a == 0: return 'Left'
    elif a == 1: return 'Right'
    elif a == 2: return 'Up'
    elif a == 3: return 'Down'
    else: return 'No valid action'            
