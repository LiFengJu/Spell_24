import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from torch.utils.data import DataLoader, TensorDataset

def p1_place(df0):
    df0['p1_place'] = ''
    # 遍历数据框的每一行
    for index, row in df0.iterrows():
        # 如果 game_no 为 13，则是决胜局的情况
        if row['game_no'] == 13:
            if row['p1_score'] > row['p2_score']:
                df0.at[index, 'p1_place'] = 'ge'
            elif row['p1_score'] < row['p2_score']:
                df0.at[index, 'p1_place'] = 'le'
            else:
                df0.at[index, 'p1_place'] = 'de'
        else:
            if row['p1_score'] == 'AD':
                df0.at[index, 'p1_place'] = 'ge'
            elif row['p2_score'] == 'AD':
                df0.at[index, 'p1_place'] = 'ge'
            else:
                if row['p1_score'] == 40 and row['p2_score'] == 40:
                    df0.at[index, 'p1_place'] = 'de'
                else:
                    # 如果都不是，则使用常规计分方式
                    if row['p1_score'] > row['p2_score']:
                        df0.at[index, 'p1_place'] = 'ge'
                    elif row['p1_score'] < row['p2_score']:
                        df0.at[index, 'p1_place'] = 'le'
                    else:
                        df0.at[index, 'p1_place'] = 'de'
    df0 = pd.get_dummies(df0,columns = ['p1_place'],dtype=int)
    return df0

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.rnn(x, h0)
        diff = out[:, :, 1] - out[:, :,0]
        diff = diff.transpose(1,0).unsqueeze(0)
        out = self.sigmoid(diff)
        return out
def train_rnn_model(X_train, y_train, input_size, hidden_size, output_size, learning_rate=0.001, num_epochs=200, batch_size=60):
    train_data = TensorDataset(X_train, y_train)
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=False)
    model = RNN(input_size, hidden_size, output_size)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
    return model
def evaluate_rnn_model(model, X:torch.Tensor, y:np.ndarray):
    model.eval()
    with torch.no_grad():
        y_pred = model(X)
        y_pred = (y_pred.squeeze().detach().numpy() > 0.5).astype(int)
    accuracy = np.mean(y_pred == y)
    print(f'Accuracy: {accuracy:.2f}')
    return accuracy