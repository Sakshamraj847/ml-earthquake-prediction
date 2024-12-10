import sys
import os

# Add the project root or `src` directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import modules from src
from preprocess import preprocess_data
from train import train_model
from evaluate import evaluate_model
from predictmodel import make_predictions

if __name__ == "__main__":
    try:
        # Preprocess the data
        df = preprocess_data("E:\\ml-earth-pre\\data\\Earthquake_Data (1).csv")
        print("Data preprocessing complete.")

        # Train the model
        model, X_test, y_test = train_model(df)
        print("Model training complete.")

        # Evaluate the model
        evaluate_model(model, X_test, y_test)

        # Make predictions on new data
        new_data = [[33.89, -118.40, 16.17, 11], [37.77, -122.42, 8.05, 14]]
        predictions = make_predictions(model, new_data)
        print("Predictions:", predictions)
    except Exception as e:
        print(f"An error occurred: {e}")

