import streamlit as st
import pandas as pd
import pickle
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Suppress warnings
warnings.filterwarnings("ignore")

# Set page config
st.set_page_config(page_title="⚡ Electricity Forecast Dashboard", layout="centered")
st.title("⚡ Electricity Production Forecast Dashboard")
st.markdown("Built using data from **1985 to 2018**.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Electric_Production.csv")
    df.columns = ["DATE", "Value"]
    df["DATE"] = pd.to_datetime(df["DATE"])
    df.set_index("DATE", inplace=True)
    df.sort_index(inplace=True)
    return df



# Load data and models
df = load_data()



# Forecast date input
default_date = df.index.max() - pd.DateOffset(months=1)
forecast_date = st.date_input(
    "📅 Select forecast start (data before this date will be used):",
    value=default_date,
    min_value=df.index.min() + pd.DateOffset(years=1),
    max_value=df.index.max(),
)

model_choice = st.selectbox("🔍 Choose a forecasting model:", ["ARmodel","MAmodel", "ARIMA", "Auto ARIMA"])

forecast_btn = st.button("🔮 Predict Next Month")

if forecast_btn:
    # Use all available data up to forecast_date
    ts = df[df.index < pd.to_datetime(forecast_date)]['Value']

    next_month = pd.to_datetime(forecast_date) + pd.DateOffset(months=1)
    actual_value = df['Value'].get(next_month, None)

    # Forecast one step ahead using new model instance trained on `ts`
    if model_choice == "ARmodel":
        model = SARIMAX(ts, order=(2,0,1), seasonal_order=(1,0,1,12)).fit()
        pred = model.forecast(steps=1)[0]
    elif model_choice == "MAmodel":
        model = SARIMAX(ts, 
                        order=(0, 1, 2), 
                        seasonal_order=(1, 0, 1, 6))  
        model_fit = model.fit(disp=False)
        pred = model_fit.forecast(steps=1)[0]
    elif model_choice == "ARIMA":
        model = SARIMAX(ts, order=(2, 1, 2), seasonal_order=(1, 0, 1, 12))
        model_fit = model.fit(disp=False)
        pred = model_fit.forecast(steps=1)[0]
    elif model_choice == "Auto ARIMA":
        with open("auto_arima_model.pkl", "rb") as f:
             model = pickle.load(f)

        model.update(ts)
        pred = model.predict(n_periods=1)[0]

    st.subheader(f"📅 Forecast for {next_month.strftime('%B %Y')}")
    st.write(f"**Predicted Value:** {pred:.2f}")

    if actual_value is not None:
        diff = abs(actual_value - pred)
        st.write(f"**Actual Value:** {actual_value:.2f}")
        st.success(f"📉 Absolute Error: {diff:.2f}")
    else:
        st.warning("⚠️ Actual value not available for comparison.")
