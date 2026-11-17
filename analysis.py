import pandas as pd

responses = pd.read_csv("survey_responses.csv")
print(responses["satisfaction"].describe())
