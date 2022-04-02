# Activation function
- No activation function is required in the input layer nodes of a neural network. So, you don’t need to worry about activation functions when you define the input layer.
- The output layer activation function depends on the type of problem that we want to solve. In a regression problem, we use the linear (identity) activation function with one node. In a binary classifier, we use the sigmoid activation function with one node. In a multiclass classification problem, we use the softmax activation function with one node per class. In a multilabel classification problem, we use the sigmoid activation function with one node per class.
- We should use a non-linear activation function in hidden layers. The choice is made by considering the performance of the model or convergence of the loss function. Start with the ReLU activation function and if you have a dying ReLU problem, try leaky ReLU.

- In MLP and CNN neural network models, ReLU is the default activation function for hidden layers.
- In RNN neural network models, we use the sigmoid or tanh function for hidden layers. The tanh function has better performance.

- Only the identity activation function is considered linear. All other activation functions are non-linear.
- We never use softmax and identity functions in the hidden layers.
- We use tanh, ReLU, variants of ReLU, swish and hard swish functions only in the hidden layers.
- The swish and hard swish functions have been found recently from the latest researches.
## Reference:
1. https://www.analyticsvidhya.com/blog/2020/01/fundamentals-deep-learning-activation-functions-when-to-use-them/
2. https://towardsdatascience.com/how-to-choose-the-right-activation-function-for-neural-networks-3941ff0e6f9c