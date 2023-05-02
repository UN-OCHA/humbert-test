from classifier_trainer import ClassifierTrainer
import pandas as pd

trainer = ClassifierTrainer()

train_df = pd.read_csv('training.csv')
val_df = pd.read_csv('validation.csv')
architecture = 'base_architecture'

trained_model = trainer.train_classification_model(train_df, val_df, architecture)