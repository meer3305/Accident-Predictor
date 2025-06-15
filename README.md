# 🚦 Road Accident Severity Predictor 🚗

A **Machine Learning-powered solution** to predict the severity of road accidents using environmental, vehicular, and human-related features. This project supports governments and organizations in building **smart, safe, and sustainable cities** (SDG 11).

---

## 🌟 Key Features

| Category         | Technologies Used                                      |
|------------------|-------------------------------------------------------|
| **ML Frameworks**| XGBoost, LightGBM, CatBoost, scikit-learn             |
| **Data Processing** | pandas, NumPy, scikit-learn, missing value handling   |
| **Visualization**| Matplotlib, Seaborn, SHAP (explainability)            |
| **UI**           | Streamlit (interactive web app)                       |

- **Automated Data Cleaning:** Handles missing values, encodes categorical variables, and scales features.
- **Multi-Model Training:** Compares XGBoost, LightGBM, and CatBoost with cross-validation and hyperparameter tuning.
- **Explainable AI:** SHAP-based feature importance (coming soon).
- **User-Friendly Interface:** Predict accident severity in real-time via a simple web app.
- **Robust Evaluation:** Weighted metrics for class imbalance, detailed performance reports.
- **Easy Deployment:** One-command launch with Streamlit.
- **Extensible:** Ready for integration with IoT, GPS, and live data sources.

---

## 📈 Model Performance

| Metric      | Value   |
|-------------|---------|
| **Accuracy**    | 0.8624  |
| **F1 Score**    | 0.8598  |
| **ROC AUC**     | 0.9215  |
| **Precision**   | 0.8631  |
| **Recall**      | 0.8624  |

> ✅ Evaluated on a hold-out test set using weighted metrics to account for class imbalance.

---

## 🧠 How It Works

1. **Data Preprocessing**
    - Cleans missing values, encodes categorical variables, and scales numerical data.
    - Supports both training and inference modes.

2. **Model Training**
    - Trains and evaluates XGBoost, LightGBM, and CatBoost.
    - Uses StratifiedKFold cross-validation and RandomizedSearchCV for hyperparameter tuning.
    - Automatically selects the best model based on F1-Score.

3. **Evaluation & Saving**
    - Reports accuracy, precision, recall, F1-score, ROC AUC.
    - Saves the best model with metadata (date, parameters, features).

4. **Prediction**
    - Accepts new inputs via a user-friendly Streamlit interface.
    - Returns predicted severity levels with optional explanation (coming soon).

---

## 🚀 Getting Started

1. **Clone the repo**
    ```bash
    git clone https://github.com/your-username/road-accident-prediction.git
    cd road-accident-prediction
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Train the model**
    ```bash
    python src/train_model.py
    ```

4. **Launch the Streamlit app**
    ```bash
    streamlit run app/streamlit_app.py
    ```

---

## 🧪 Example Use Case

> **Scenario:** A traffic control system uses this model in real-time to assess the severity risk of an accident based on road and weather sensor inputs, enabling faster emergency response and resource allocation.

---

## 🔮 Future Enhancements

- ✅ SHAP-based explainability (feature importance)
- 🌐 Real-time integration with GPS + IoT data
- 📊 Interactive dashboards for traffic authorities
- 🔁 Continuous learning with live data
- 📱 Mobile-friendly interface

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](../../issues).

---

> **Let's make roads safer together with the power of AI!**
