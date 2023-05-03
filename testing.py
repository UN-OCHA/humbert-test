from classifier_trainer import ClassifierTrainer
import pandas as pd

trainer = ClassifierTrainer()

model = 'models/trained_classifier_nlp-thedeep/humbert_multiabel_architecture.pt'
model = 'models/trained_classifier_nlp-thedeep/humbert_base_architecture.pt'
trained_model = trainer.load_model(model)

test_df = pd.read_csv('testing.csv')

test_set_predictions = trainer.generate_test_predictions(test_df.excerpt.tolist())

test_set_results = trainer.generate_test_results(test_df, False, True)

print(test_set_results)