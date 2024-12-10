import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"R^2: {r2:.2f}, MSE: {mse:.2f}")
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Model Evaluation")
    plt.show()
