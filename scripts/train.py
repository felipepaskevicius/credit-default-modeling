from sklearn import model_selection

# method para dividir os dados em treino e teste
X_Train, X_Test, y_train, y_test = model_selection.train_test_split(
                                                                    X, 
                                                                    y,
                                                                    test_size=0.2, 
                                                                    random_state=42, 
                                                                    stratify=y
)

# Check the dimensions of the training and testing datasets
print(X_Train.shape, X_Test.shape, y_train.shape, y_test.shape)

# Taxa de resposta of the training and testing datasets
print(y_train.mean(), y_test.mean())