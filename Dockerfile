# docker build --progress=plain --no-cache -t oluwaline/pregrisk_prediction .
# docker save -o pregRisk_prediction.tar oluwaline/pregRisk_prediction
# docker load --input pregRisk_prediction.tar

FROM python:3.9-buster

LABEL version="1.1.2"
LABEL maintainer="Joseline U.E"
LABEL url="http://Joseline.com"
LABEL vcs-url="https://github.com/Oluwaline/Pregnancy-Risk-Prediction"
LABEL description="Pregnancy-Risk-Prediction"

WORKDIR /app
COPY . .

# installing the requirements
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]