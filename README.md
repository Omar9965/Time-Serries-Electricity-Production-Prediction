# ⚡ Time Series Electricity Production Prediction

This project focuses on forecasting electricity production using time series analysis techniques. Leveraging historical data, it aims to predict future electricity generation trends, which is crucial for energy planning and management. 

---

## 📂 Features

- 📈 **Interactive model selection** for AR, MA, ARIMA, and Auto ARIMA.
- 📅 Choose a forecast date — the model will use all data before that date to predict the next month.
- 🔮 One-step-ahead forecasting.
- ✅ Compares forecast with actual value (if available).
- 📉 Displays Absolute Error when actual value is known.

---

## 🧠 Models Used

- `SARIMAX` from `statsmodels` is used to fit AR, MA, and ARIMA models.
- Pre-trained `Auto ARIMA` model (saved with `pickle`) is loaded and updated at runtime.

---

## 📁 Project Structure

- **`Electric_Production.csv`**: Historical monthly electricity production data.
- **`Electricity_Production_Forecasting.ipynb`**: Jupyter Notebook detailing data analysis, modeling, and forecasting.
- **`auto_arima_model.pkl`**: Serialized Auto ARIMA model.
- **`app.py`**: streamlit app for deploying the model as a web service.



## 👨‍💻 Team Members & Roles



> This collaborative effort ensured a well-rounded project from data exploration to final deployment.

## 🧪 Methodology

1. Data Preprocessing
2. Exploratory Data Analysis (EDA)
3. Stationarity Testing (ADF Test)
4. Auto ARIMA Model Selection
5. Forecasting
6. Deployment via Streamlit 

## 📊 Results

Forecasting was successfully implemented using Auto ARIMA. Visual validation confirms reliable predictions of future electricity production.


## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Flask
- Required libraries (`pandas`, `numpy`, `matplotlib`, `pmdarima`, etc.)

### Installation

```bash
git clone https://github.com/Omar9965/Time-Serries-Electricity-Production-Prediction.git
cd Time-Serries-Electricity-Production-Prediction
pip install -r requirements.txt

### 3. 🚀 Run Streamlit

```bash
streamlit run app.py
```

Then open your browser to the local URL provided (e.g., `http://localhost:8501`).

---

## 📊 Sample Usage

- Select a forecast date like `2018-11-01`.
- Pick a model: `ARIMA`.
- Click on **🔮 Predict Next Month**.
- See the prediction for December 2018 and compare with actual value.


محمد احمد عبدالسميع:412200294
محمد بابكر عزالدين عبدالباسط:412200624
وليد صبري محمد عبده:412200405
محمد مدحت السيد جلال:412200341
عمر محمد أمين علي:412200266
محسن محمد الشرنوبي:412200292        
