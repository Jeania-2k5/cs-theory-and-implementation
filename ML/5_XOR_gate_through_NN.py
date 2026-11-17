"""Two-layer neural network that learns the XOR truth table using backpropagation."""
import math


def sigmoid(value):
    return 1 / (1 + math.exp(-value))


def train_xor(epochs=10000, learning_rate=1.0):
    data = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]
    # Two hidden neurons can form the two XOR decision regions.
    hidden_weights = [[0.5, 0.5], [0.5, 0.5]]
    hidden_bias = [-0.25, -0.75]
    output_weights = [0.5, 0.5]
    output_bias = -0.75
    for _ in range(epochs):
        for inputs, target in data:
            hidden = [sigmoid(sum(w * x for w, x in zip(weights, inputs)) + bias)
                      for weights, bias in zip(hidden_weights, hidden_bias)]
            output = sigmoid(sum(w * h for w, h in zip(output_weights, hidden)) + output_bias)
            output_delta = (target - output) * output * (1 - output)
            old_output = output_weights[:]
            for i in range(2):
                output_weights[i] += learning_rate * output_delta * hidden[i]
                hidden_delta = (output_delta * old_output[i] * hidden[i] * (1 - hidden[i]))
                for j in range(2):
                    hidden_weights[i][j] += learning_rate * hidden_delta * inputs[j]
                hidden_bias[i] += learning_rate * hidden_delta
            output_bias += learning_rate * output_delta
    return hidden_weights, hidden_bias, output_weights, output_bias


def predict(inputs, parameters):
    hidden_weights, hidden_bias, output_weights, output_bias = parameters
    hidden = [sigmoid(sum(w * x for w, x in zip(weights, inputs)) + bias)
              for weights, bias in zip(hidden_weights, hidden_bias)]
    probability = sigmoid(sum(w * h for w, h in zip(output_weights, hidden)) + output_bias)
    return probability, int(probability >= 0.5)


if __name__ == "__main__":
    parameters = train_xor()
    print("XOR predictions:")
    for inputs in ([0, 0], [0, 1], [1, 0], [1, 1]):
        print(inputs, "->", predict(inputs, parameters))
