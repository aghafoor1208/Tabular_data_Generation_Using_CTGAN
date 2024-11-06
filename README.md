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
- **Data Sample**: See the image below for an example of the data.

![Real Data From PIMA Daatset](Real_data_Sample.png)

# Generated Data using CTGAN

To augment the **PIMA Indian Diabetes dataset**, we used **Conditional Generative Adversarial Networks (CTGANs)** to generate synthetic tabular data. CTGAN is specifically designed to handle tabular data and can generate high-quality synthetic data that preserves the statistical properties and distribution of the original dataset.

CTGAN is a type of **Generative Adversarial Network (GAN)** that is well-suited for generating synthetic data for structured datasets with both continuous and categorical features, such as those found in tabular datasets.

---

## Steps for Data Generation

1. **Model Setup**:  
   The CTGAN model consists of two main components:
   - **Generator**: Creates synthetic data samples.
   - **Discriminator**: Evaluates how realistic the generated data is, trying to differentiate it from real data.

2. **Training the CTGAN**:  
   - The CTGAN model was trained on the **PIMA Indian Diabetes dataset** to learn the data distribution, including both the continuous and categorical features.
   - The model was trained over several epochs, with the generator and discriminator improving their performance until synthetic data closely matched the statistical properties of the original dataset.

3. **Generating Synthetic Data**:  
   After the model was trained, we used it to generate a synthetic dataset with the same structure and number of rows as the original dataset. The generated data mimics the original dataset, maintaining both the feature distributions and the correlations between features.

4. **Evaluating the Data**:  
   The quality of the generated data was evaluated using statistical tests such as comparing the **mean**, **variance**, and **distributions** of the features. Visualizations like **histograms** and **boxplots** were used to visually inspect how well the synthetic data matched the original.

---

## Benefits of Using CTGAN for Data Augmentation

- **Handling Imbalanced Data**:  
  CTGAN is especially useful in generating synthetic samples for underrepresented classes in imbalanced datasets, which helps improve model performance on minority classes.
  
- **Data Distribution Preservation**:  
  CTGAN ensures that the **correlations** between features and their **marginal distributions** are maintained, making the synthetic data highly realistic and useful for training machine learning models.
  
- **Privacy and Security**:  
  Synthetic data can be used in environments where real data cannot be shared due to privacy concerns, such as healthcare or finance, without compromising sensitive information.

---

## Example of Generated Data

After training the CTGAN, we generated synthetic data that mirrors the structure and statistical properties of the original dataset. Below is an example of the synthetic data:

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome |
|-------------|---------|---------------|---------------|---------|------|--------------------------|-----|---------|
| 3           | 102     | 70            | 29            | 110     | 32.4 | 0.555                    | 35  | 1       |
| 5           | 134     | 80            | 31            | 138     | 33.2 | 0.456                    | 40  | 0       |
| 2           | 90      | 68            | 27            | 115     | 28.3 | 0.312                    | 50  | 0       |
| 1           | 85      | 78            | 22            | 130     | 30.5 | 0.412                    | 45  | 1       |

This synthetic dataset can be used to train machine learning models, validate models, and perform data augmentation tasks, providing more data for model training while respecting privacy concerns.

---

## Conclusion

Using **CTGAN** to generate synthetic data allows us to enhance the **PIMA Indian Diabetes dataset**, making it more suitable for training machine learning models. The generated data preserves the statistical properties of the original dataset while providing additional data for training. This approach also addresses challenges like **class imbalance** and **privacy concerns** when using sensitive real-world datasets.

---

## References

- [Conditional Generative Adversarial Networks (CTGAN)](https://arxiv.org/abs/1703.06490)
- [PIMA Indian Diabetes Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/diabetes)
