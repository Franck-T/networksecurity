# 🛡️ NetworkSecurity — Machine Learning–Powered Network Intrusion Detection System  
### End-to-End ML Pipeline • Data Ingestion & Validation • Model Training • Prediction API • MongoDB • Docker


## 📌 Overview

**NetworkSecurity** is a production-style **Network Intrusion Detection System (NIDS)** powered by machine learning.  
It automates the full lifecycle of:

- Data ingestion  
- Data validation (schema + domain checks)  
- Feature engineering  
- ML model training  
- Evaluation & artifact storage  
- Online prediction API  
- Containerized deployment
- MLflow tracking and Data tracking with Dagshub
- Deploy-ready with CI/CD pipelines on aws ECR and EC2 instances  

This project mirrors **real enterprise ML systems** for cybersecurity analytics, detecting suspicious network behavior using structured network flow data.



## 🎯 Problem Statement

Modern networks generate massive amounts of traffic, making manual monitoring impossible.  
The goal of this project is to:

- Detect network intrusions  
- Predict whether traffic is **normal** or **malicious**  
- Automate classification using ML  
- Provide a web interface/API for real-time prediction  
- Support continuous model improvement through pipelines  

This system demonstrates the capabilities of an intelligent, automated cybersecurity model pipeline.



## 📂 Dataset Description

The dataset consists of structured network flow records stored under:

- Network_Data/
- valid_data/
- data_schema/


Typical columns include:

- `duration`
- `protocol_type`
- `src_bytes`
- `dst_bytes`
- `flag`
- `land`
- `wrong_fragment`
- `urgent`
- `count`
- `srv_count`
- … and other network behavior metrics

The dataset contains **normal** vs **intrusion** class labels.



## 🧱 System Architecture

The system follows a **modular ML pipeline architecture** inspired by real MLOps workflows.

```
networksecurity/
│── app.py
│── main.py
│── networksecurity/
│     ├── components/
│     ├── pipeline/
│     ├── utils/
│     ├── exception/
│     ├── logging/
│     ├── entity/
│     ├── constant/
│     └── cloud/
│
│── Network_Data/
│── valid_data/
│── data_schema/
│── final_model/
│── prediction_output/
│── Artifacts/
│── logs/
│── templates/
│── test_mongodb.py
│── Dockerfile
│── setup.py
│── requirements.txt
│── README.md
└── .gitignore

```


## 🔧 Pipeline Breakdown

### 1️⃣ **Data Ingestion**
- Reads raw network flow CSV files  
- Copies dataset into controlled artifacts directory  
- Ensures reproducibility  
- Stores data versioning metadata  

### 2️⃣ **Data Validation**
- Uses `data_schema/` to validate:
  - column names  
  - data types  
  - acceptable ranges  
- Invalid files are rejected  
- Generates validation reports  

### 3️⃣ **Data Transformation**
- Label encoding  
- Scaling numeric features  
- Train-test split  
- Stores:
  - transformer object  
  - transformed arrays  

### 4️⃣ **Model Training**
Evaluates multiple models:

- Logistic Regression  
- Random Forest  
- Decision Tree  
- Gradient Boosting  
- XGBoost (if enabled)

The best model is picked based on:
- F1-Score  
- Recall (important for intrusion detection)  
- ROC-AUC  

Final model stored in:

- final_model/model.pkl

### 5️⃣ **Prediction Pipeline**

Given new network flow values:

Load transformer → preprocess → load model → predict intrusion

Predictions stored under:

- prediction_output/


### 6️⃣ **Web Application**
`app.py` provides:

- Web form for prediction  
- API endpoint  
- HTML templates under `templates/`

---

## 🧰 Tech Stack

### **Languages & Core Libraries**
- Python 3.x  
- Pandas  
- Scikit-learn  
- NumPy  
- PyYAML  

### **Backend / API**
- Flask (app.py)
- HTML templates (Jinja2)

### **Database**
- MongoDB (via `test_mongodb.py` + utils)

### **DevOps / Tooling**
- Docker  
- Logging framework  
- Structured exception handling  
- Artifact management  
- Automated pipeline via Python scripts  

### **Project Packaging**
- `setup.py`
- PyProject (`pyproject.toml`)
- `.gitignore`
- Modular import structure


## 🚀 Running the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
### 2️⃣ Train the ML Model

```python
python main.py
```

This will:

- Ingest data
- Validate schema
- Transform dataset
- Train all models
- Save best model under final_model/
- Write logs to /logs

### 3️⃣ Run the Web Application

```python
python app.py
```

Visit:
```bash
http://localhost:8000
```

## 🧪 Testing

```python
python test_mongodb.py
```

Tests:

- MongoDB connectivity






