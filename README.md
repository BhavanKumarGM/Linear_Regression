# 📈 Simple Linear Regression – Height vs Weight

This project implements a **Simple Linear Regression model** using Python to predict a person’s **height** based on their **weight**.

It demonstrates the **end-to-end machine learning workflow**:
data loading → preprocessing → model training → evaluation → prediction → visualization.

This is a **foundational ML project**, built correctly (no silent bugs, no data leakage).

---

## 🧠 Problem Statement

Given a dataset with:
- **Weight** (independent variable)
- **Height** (dependent variable)

The goal is to:
- Learn the linear relationship between weight and height
- Predict height for unseen weight values

---

## 🗂 Project Structure

Linear_Regression/
│
├── data.csv
├── model.py
├── requirements.txt
└── README.md


---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Linear_Regression.git
cd Linear_Regression
2️⃣ (Recommended) Create and activate a virtual environment
python -m venv venv
Windows

venv\Scripts\activate
Mac / Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
🚀 How to Run
python model.py
The script will:

Train a linear regression model

Print the R² score

Predict height for a new weight value (example: 75 kg)

Display multiple diagnostic plots

📊 What the Model Does
✔ Model Training
Uses train–test split

Applies StandardScaler inside a Pipeline

Trains a Linear Regression model

✔ Evaluation
R² Score for performance measurement

✔ Prediction
pipe.predict([[75]])
Example output:

Predicted Height (75kg): 172.3
📈 Visualizations Included
Scatter Plot + Regression Line

Confirms linear relationship

Actual vs Predicted Plot

Shows prediction accuracy

Residual Plot

Validates linear regression assumptions

These plots ensure the model is not blindly trusted.

🧪 Key ML Concepts Demonstrated
Supervised learning

Simple linear regression

Feature scaling

Pipelines to avoid preprocessing bugs

Train–test split

Model evaluation

Prediction on unseen data

Visual diagnostics

⚠️ Important Notes
The model assumes a linear relationship

Performance depends on data quality

This project is for learning and demonstration, not production deployment

📜 License
Open-source, free to use for educational purposes.

✍️ Author
Bhavan Kumar
Learning machine learning by understanding fundamentals, not copying tutorials.
