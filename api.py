from fastapi import FastAPI, Query
import uvicorn
import pandas as pd
import pickle

app = FastAPI(title="Pregnancy Risk Prediction")

@app.get("/")
def homepage():
    return {"message": "Pregnancy Risk Prediction"}

@app.get('/predict')
def predict(
    model: str = Query(..., description="Model to use for prediction"),
    age: int = Query(description="Age", default=26, ge=10, le=70),
    SystolicBP: int = Query(description="Systolic Blood Pressure (mmHg)", default=120, ge=70, le=160),
    DiastolicBP: int = Query(description="Diastolic Blood Pressure (mmHg)", default=80, ge=49, le=100),
    bs: float = Query(description="Blood Sugar (mmol/L)", default=7.5, ge=6.0, le=19.0),
    bodyTemp: float = Query(description="Body Temperature (°F)", default=98.0, ge=98.0, le=103.0),
    heartRate: int = Query(description="Heart Rate (bpm)", default=76, ge=7, le=90)
):
    # Creating the dataframe
    column_names = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
    data = [[age, SystolicBP, DiastolicBP, bs, bodyTemp, heartRate]]
    df = pd.DataFrame(data=data, columns=column_names)

    # Loading the pipelines and selecting the model based on the chosen model
    if model == "Random Forest":
        pipe = pickle.load(open("Random_Forest_model.pkl", "rb"))
    elif model == "Decision Tree":
        pipe = pickle.load(open("decision_tree_model.pkl", "rb"))
    elif model == "XGBoost":
        pipe = pickle.load(open("xgboost_model.pkl", "rb"))
    else:
        return {"error": "Invalid model name"}

    predictions = pipe.predict(df)
    predictions = predictions[0].tolist()  # tolist is used to convert a series to list

    return {"predictions": predictions}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
