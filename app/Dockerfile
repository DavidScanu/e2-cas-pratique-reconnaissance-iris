FROM python:3.10-slim

WORKDIR /streamlit-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /src /streamlit-app

CMD streamlit run app.py --server.port 8080