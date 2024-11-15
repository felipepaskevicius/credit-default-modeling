from sklearn.model_selection import train_test_split

# method para dividir os dados em treino e teste
X_Train, X_Test, y_train, y_test = train_test_split(X, y, test_size=0.2,  random_state=42,  stratify=y)

# Check the dimensions of the training and testing datasets
print(X_Train.shape, X_Test.shape, y_train.shape, y_test.shape)

# Taxa de resposta of the training and testing datasets
print(y_train.mean(), y_test.mean())