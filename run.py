from train import train_model
from process import process_data


if __name__ == '__main__':
    """
    Main
    """
    process_data("Data/train.csv")
    train_model("Data/processed_train.csv")