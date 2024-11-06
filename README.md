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

