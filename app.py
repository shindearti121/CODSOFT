import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🛳️",
    layout="centered",
)

# Pink-ish UI polish (works without extra packages)
st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(1200px 600px at 10% 5%, rgba(255,105,180,0.22), transparent 55%),
                    radial-gradient(900px 500px at 90% 10%, rgba(255,182,193,0.22), transparent 52%),
                    linear-gradient(180deg, rgba(255,240,246,1) 0%, rgba(255,255,255,1) 60%);
      }
      h1, h2, h3 { letter-spacing: -0.02em; }
      .titanic-card {
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(255, 105, 180, 0.25);
        border-radius: 16px;
        padding: 16px 16px 4px 16px;
        box-shadow: 0 10px 24px rgba(255,105,180,0.10);
        backdrop-filter: blur(6px);
      }
      .titanic-muted { color: rgba(15, 23, 42, 0.75); }
      .stButton>button {
        background: linear-gradient(90deg, #ff4da6 0%, #ff7ac8 55%, #ff9ad5 100%);
        color: white;
        border: 0;
        border-radius: 999px;
        padding: 0.65rem 1.1rem;
        font-weight: 700;
        box-shadow: 0 10px 18px rgba(255,77,166,0.25);
      }
      .stButton>button:hover { filter: brightness(1.03); }
      .stButton>button:active { transform: translateY(1px); }
      div[data-testid="stMetric"] {
        border: 1px solid rgba(255, 105, 180, 0.22);
        border-radius: 14px;
        padding: 10px 12px;
        background: rgba(255,255,255,0.65);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

model = None
try:
    model = pickle.load(open("titanic_random_forest.pkl", "rb"))
except Exception as e:
    st.title("Titanic Survival Prediction")
    st.error("Failed to load model: {}".format(e))
    st.stop()

st.title("Titanic Survival Prediction")
st.caption("A simple Random Forest model with a pink-themed interface.")

st.markdown('<div class="titanic-card">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3], index=0)
    sex = st.selectbox("Sex", ["Male", "Female"], index=0)
    age = st.slider("Age", 1, 80, 25)
    embarked = st.selectbox("Embarked", ["S", "C", "Q"], index=0)
with col2:
    sibsp = st.number_input("Siblings/Spouse", 0, 8, 0)
    parch = st.number_input("Parents/Children", 0, 8, 0)
    fare = st.number_input("Fare", 0.0, 600.0, 32.2, step=0.1)
    st.markdown('<p class="titanic-muted">Tip: Higher fares often correlate with higher survival rates.</p>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

sex = 0 if sex=="Male" else 1
embarked = {"S":0,"C":1,"Q":2}[embarked]

predict = st.button("Predict")
st.divider()

if predict:
    data = np.array([[pclass,sex,age,sibsp,parch,fare,embarked]])

    result = model.predict(data)

    if result[0]==1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Did Not Survive")

    try:
        proba = model.predict_proba(data)[0]
        survived_prob = float(proba[1])
        died_prob = float(proba[0])
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Survival probability", f"{survived_prob*100:.1f}%")
        with c2:
            st.metric("Did not survive probability", f"{died_prob*100:.1f}%")
    except Exception:
        pass