import numpy as np

X = np.array([[1,1,1],[1,0,1],[0,1,1]])
y = np.array([[0],[1],[1]])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivativeSigmoid(x):
    return x * (1 - x)

x_input = 3
hidden_layer_neurons = 3
output_layer_neuron = 1

weight_hidden = np.random.random((x_input, hidden_layer_neurons))
bias_hidden = np.random.random((1,x_input))
weight_output = np.random.random((hidden_layer_neurons, output_layer_neuron))
bias_output = np.random.random((1,output_layer_neuron))

epochs = 10000000
learning_rate = 0.1

for epoch in range(epochs):
#    Feedforward
#    1. Dot product of input and weight
#    2. Add Bias
#    3. Pass it to activation
    hidden_input = np.dot(x_input, weight_hidden)
    hidden_layer = hidden_input + bias_hidden
    hidden_activation = sigmoid(hidden_layer)
    
    output_input = np.dot(hidden_activation, weight_output)
    output_layer = output_input + bias_output
    output_activation = sigmoid(output_layer)
    
#    Backpropagation
#    Calculate Error
    E = y - output_activation
#    Calculate slope at hidden and output layer
    slope_hidden = derivativeSigmoid(hidden_activation)
    slope_output = derivativeSigmoid(output_activation)
    
#    Calculate delta at output and find error at hidden layer
    d_output = E * slope_output
    Error_hidden = d_output.dot(weight_output.T)
    
    d_hidden = Error_hidden * slope_hidden
#    Update weight and bias
    weight_output += hidden_activation.T.dot(d_output) * learning_rate
    weight_hidden += X.T.dot(d_hidden) * learning_rate
    bias_output += np.sum(d_output, keepdims = True) * learning_rate
    bias_hidden += np.sum(d_hidden, keepdims = True) * learning_rate

print(output_activation)
