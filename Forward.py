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
def normalize(vector, endsum):
    vector_element_sum = 0
    for element in vector:
        vector_element_sum += element

    unit_to_divide_by = vector_element_sum / endsum

    return_vector = []
    for i in range(len(vector)):
        return_vector[i] = vector[i] * unit_to_divide_by
    return return_vector
