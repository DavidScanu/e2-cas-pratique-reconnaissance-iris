FROM python:3.10-slim

WORKDIR /streamlit-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /src

WORKDIR /src

CMD streamlit run app.py