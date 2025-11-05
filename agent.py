import torch
import torch.nn as nn # Shortcut so we type nn instead of torch.nn every time
#nn stands for neural network
import torch.optim as optim
import random

class MathAgent(nn.Module):  # This is required for PyTorch usage
    def __init__(self):
        super(MathAgent, self).__init__()
        
        self.layer1 = nn.Linear(3, 128) #nn.Linear(a, b) means it accepts a much inputs and give b much outputs
        self.layer2 = nn.Linear(128, 128)
        self.layer3 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 90)
        
    def forward(self, state):
        x = torch.relu(self.layer1(state))
        x = torch.relu(self.layer2(x))
        x = torch.relu(self.layer3(x))
        x = self.output(x)
        return x
    
    
agent = MathAgent()
state = torch.tensor([5.0, 0.0, 3.0])
output = agent.forward(state)
print(output)  # Will print 90 random numbers
