import numpy as np

# alpha_one is given by the following equation:
# alpha_one(X_1) = P(X_1,e_1) = P(X_1)*P(e_1|X_1)
# In our case; P(X_1)*P(e_1|X_1) = (0.5, 0,5) * (0.818, 0.182)

alpha_one = None
# Transitional model:
transitional_model = np.array([[0.7, 0.3], [0.3, 0.7]])

# Observational model where an umbrella has been observed:
obs_model_with_umbrella = np.array([[0.9, 0.0], [0.0, 0.2]])

# Observational model where a distinct lack of an umbrella has been observed:
obs_model_without_umbrella = np.array([[0.1, 0.0], [0.0, 0.8]])


# Normalization function. As per the textbook description of the task a
# value alpha must be multiplied to keep the the vectors stochastic
# input used here will be 1, but I have set the option for other values
# The vector input is the vector to be normalized.
# Expected form is [a, b], or longer.
def normalize(vector, endsum=1):
    """
    :param vector: The vector that is to be normalized, as in have the sum of its values set to a given value
    :param endsum: Default value is one, as this method is mostly used to make vectors stochastic.
    :return:
    """
    vector_element_sum = 0
    for element in vector:
        vector_element_sum += element

    unit_to_divide_by = vector_element_sum / endsum

    return_vector = []
    for i in range(len(vector)):
        return_vector.append(vector[i] / unit_to_divide_by)
    return return_vector


# Forward algorithm, used to recursively filter the distribution
# Works its way back to an initial probability vector, in this case [0.5, 0.5]
# The transition model used in this specific case will always be the one created at the top of the file
def forward(transition_model, obs_model, previous_forward_message):
    """
    :param transition_model: The transitional model used, in this case a 2x2 matrix
    :param obs_model: The observational model used, in this case a 2x2 matrix containing the probabilities for the given observation
    :param previous_forward_message: The previous forward message, in this case it is the previous vector in the HMM
    """
    next_state_vector = obs_model.dot(transition_model.dot(previous_forward_message))
    return normalize(next_state_vector)


def test_forward_algorithm():
    # Task b) part 1
    p_X0 = [0.5, 0.5]
    pX1_given_e1 = forward(transitional_model, obs_model_with_umbrella, p_X0)
    pX2_given_e1e2 = forward(transitional_model, obs_model_with_umbrella, pX1_given_e1)
    print(pX1_given_e1, "\n", pX2_given_e1e2)

    ##Task b) part 2
    forward_test_list = [True, True, False, True, True]
    prev_message = [0.5, 0.5]
    for i in range(5):
        if forward_test_list[i]:
            prev_message = forward(transitional_model, obs_model_with_umbrella, prev_message)
        else:
            prev_message = forward(transitional_model, obs_model_without_umbrella, prev_message)
        print(prev_message)




# Backward algorithm, runs backwards to compute the smoothed P(X_k | e_1:t)
#
def backward(transition_model, obs_model, previous_backward_message):
    """
    :param transition_model: The transitional model used, in this case a 2x2 matrix
    :param obs_model: The observational model used, in this case a 2x2 matrix containing the probabilities for the given observation
    :param previous_backward_message: The previous backward message, in this case it is the next vector in the HMM
    """
    next_state_vector = obs_model.dot(transition_model.dot(previous_backward_message))
    return normalize(next_state_vector)


test_forward_algorithm()
