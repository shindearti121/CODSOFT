Project: Titanic Survival Prediction

Description:
This project predicts whether a passenger survived the Titanic disaster
using machine learning models.

Technologies Used:
Python
Pandas
Scikit-Learn
Seaborn
Matplotlib

Models Used:
Logistic Regression
Decision Tree
Random Forest

Best Model:
Random Forest (~80% accuracy)

Run the app (use existing .venv):
1) Open PowerShell in the project folder
2) Install deps (one-time):
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
3) Start Streamlit:
   .\.venv\Scripts\python.exe -m streamlit run app.py

If port 8501 is busy, run:
   .\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8502