from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata
import pandas as pd

# Load the dataset
df = pd.read_csv("Pima_Indians_Diabetes_Database.csv")
print(len(df))

# Automatically generate metadata for the dataset
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=df)

# Initialize the CTGAN synthesizer model with metadata
# You can increase epochs during model fitting
model = CTGANSynthesizer(metadata, epochs=2000) 

# Fit the model on your data
model.fit(df)

# Generate synthetic data
synthetic_data = model.sample(2000)

# print(type(synthetic_data))

# Save the synthetic data as a CSV file
synthetic_data.to_csv('generated_PIMA.csv', index=False)

print("Synthetic data saved as 'generated_PIMA.csv'")
