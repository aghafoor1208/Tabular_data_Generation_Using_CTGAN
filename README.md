# Tabular_data_Generation_Using_CTGAN

# CTGAN Synthetic Data Generation

**Overview**

This repository contains a project demonstrating the use of CTGAN (Conditional Tabular GAN) for generating synthetic tabular data. CTGAN is a powerful tool for privacy-preserving data analysis and machine learning tasks. 

**Getting Started**

1. **Clone the Repository:**
   ```bash
   git clone [url]

2. **install CTGAN:**
   ```bash
   pip install ctgan


3. **Run the Script:** Execute the main script to train the CTGAN model and generate synthetic data:
   ```bash
   python data_gen.py

# Real Data (PIMA Indian Diabetes dataset)

The **PIMA Indian Diabetes Dataset** is a popular dataset used for classification tasks, specifically in predicting whether a person has diabetes based on medical attributes. It is commonly used in machine learning exercises for practice with classification algorithms.

---

## Dataset Overview

- **Source**: [UCI Machine Learning Repository](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Task**: Binary classification (predict whether a person has diabetes or not)
- **Number of Instances**: 768
- **Number of Features**: 8 input features
- **Target Variable**: Outcome (binary: 1 for diabetic, 0 for non-diabetic)

---

## Dataset Features

| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **Pregnancies**                  | Number of times the person has been pregnant.                               |
| **Glucose**                      | Plasma glucose concentration (mg/dL) 2 hours after an oral glucose test.   |
| **Blood Pressure**               | Diastolic blood pressure (mm Hg).                                           |
| **Skin Thickness**               | Skinfold thickness (mm) at the triceps.                                     |
| **Insulin**                      | 2-hour serum insulin (mu U/ml).                                             |
| **BMI**                          | Body Mass Index (kg/m²).                                                    |
| **Diabetes Pedigree Function**   | A function that scores the likelihood of diabetes based on family history.  |
| **Age**                          | Age of the person in years.                                                 |

### Target Variable
- **Outcome**:  
  - `1`: The person has diabetes.  
  - `0`: The person does not have diabetes.

---

## Data Characteristics

- **Imbalance**: The dataset is imbalanced, with approximately **34.9%** of the instances being positive (Outcome = 1).
- **Data Type**: All features are numeric, and the target variable (Outcome) is binary.



Below is a table displaying a subset of the  **PIMA Indian Diabetes** dataset:

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome |
|-------------|---------|---------------|---------------|---------|------|--------------------------|-----|---------|
| 6           | 148     | 72            | 35            | 0       | 33.6 | 0.627                    | 50  | 1       |
| 1           | 85      | 66            | 29            | 0       | 26.6 | 0.351                    | 31  | 0       |
| 8           | 183     | 64            | 0             | 0       | 23.3 | 0.672                    | 32  | 1       |
| 1           | 89      | 66            | 23            | 94      | 28.1 | 0.167                    | 21  | 0       |
| 0           | 137     | 40            | 35            | 168     | 43.1 | 2.288                    | 33  | 1       |
| 5           | 116     | 74            | 0             | 0       | 25.6 | 0.201                    | 30  | 0       |
| 3           | 78      | 50            | 32            | 88      | 31   | 0.248                    | 26  | 1       |
| 10          | 115     | 0             | 0             | 0       | 35.3 | 0.134                    | 29  | 0       |
| 2           | 197     | 70            | 45            | 543     | 30.5 | 0.158                    | 53  | 1       |
| 8           | 125     | 96            | 0             | 0       | 0    | 0.232                    | 54  | 1       |
| 4           | 110     | 92            | 0             | 0       | 37.6 | 0.191                    | 30  | 0       |
| 10          | 168     | 74            | 0             | 0       | 38   | 0.537                    | 34  | 1       |
| 10          | 139     | 80            | 0             | 0       | 27.1 | 1.441                    | 57  | 0       |

---


# Generated Data using CTGAN

To augment the **PIMA Indian Diabetes dataset**, we used **Conditional Generative Adversarial Networks (CTGANs)** to generate synthetic tabular data. CTGAN is designed specifically to handle structured datasets and is highly effective at generating realistic data that preserves the statistical properties of the original dataset.

CTGAN is a type of **Generative Adversarial Network (GAN)** optimized for generating synthetic data for structured, tabular datasets, such as those with continuous and categorical features.

---

## Steps for Data Generation

1. **Model Setup**:  
   The CTGAN model consists of two components:
   - **Generator**: The generator creates synthetic data samples.
   - **Discriminator**: The discriminator distinguishes real data from synthetic data, helping the generator improve over time.

2. **Training the CTGAN**:  
   - We trained the CTGAN model on the **PIMA Indian Diabetes dataset** to learn the underlying distribution of both continuous and categorical features.
   - The model was trained over several epochs until it produced synthetic data that closely resembles the statistical properties of the original dataset.

3. **Generating Synthetic Data**:  
   After training, we used the model to generate synthetic data with the same structure (features and target variable) as the original dataset.

4. **Evaluating the Data**:  
   The synthetic data was evaluated by comparing the statistical properties (means, variances, and distributions) of both the real and generated datasets. Visual tools such as **histograms** and **boxplots** were used to ensure the generated data closely matched the original dataset's characteristics.

---

## Benefits of Using CTGAN for Data Augmentation

- **Handling Imbalanced Data**:  
  CTGAN can generate synthetic samples for the minority class, which can help balance imbalanced datasets and improve model performance.

- **Data Distribution Preservation**:  
  CTGAN maintains both the **correlations** between features and their **marginal distributions**, ensuring that synthetic data remains realistic and useful for model training.


---

## Example of Generated Data

Below is an example of the synthetic data generated by the CTGAN model. It maintains the structure and distributions of the original dataset:

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome |
|-------------|---------|---------------|---------------|---------|------|--------------------------|-----|---------|
| 4           | 116     | 57            | 35            | 161     | 28.9 | 0.295                    | 21  | 0       |
| 3           | 93      | 65            | 1             | 8       | 35.0 | 0.345                    | 38  | 1       |
| 1           | 82      | 71            | 0             | 3       | 30.0 | 0.156                    | 25  | 0       |
| 7           | 121     | 67            | 29            | 0       | 47.4 | 0.869                    | 33  | 1       |
| 9           | 138     | 57            | 0             | 3       | 24.9 | 0.473                    | 28  | 0       |
| 4           | 117     | 68            | 1             | 9       | 39.2 | 0.857                    | 37  | 1       |
| 1           | 82      | 75            | 37            | 497     | 26.0 | 0.444                    | 23  | 0       |
| 1           | 108     | 52            | 35            | 163     | 29.7 | 0.873                    | 25  | 0       |
| 3           | 110     | 47            | 31            | 130     | 31.2 | 0.187                    | 41  | 0       |
| 7           | 104     | 74            | 0             | 2       | 19.6 | 0.155                    | 21  | 0       |
| 4           | 99      | 78            | 34            | 174     | 33.6 | 0.261                    | 24  | 0       |

This synthetic data mirrors the structure and features of the real PIMA Indian Diabetes dataset and can be used to train models, perform validation, or augment the original data.

---

## Conclusion

Using **CTGAN** to generate synthetic tabular data is an effective way to augment the **PIMA Indian Diabetes dataset**. This approach helps address challenges such as **class imbalance** and provides more data for model training, while also respecting **data privacy** concerns. The synthetic data generated by CTGAN retains the statistical properties and correlations of the original dataset, making it highly useful for machine learning tasks.

---

## References

- [Conditional Generative Adversarial Networks (CTGAN)](https://arxiv.org/abs/1703.06490)
