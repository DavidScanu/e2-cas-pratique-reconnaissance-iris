FROM python:3.10-slim

WORKDIR /streamlit-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /streamlit-app

CMD streamlit run src/app.py

