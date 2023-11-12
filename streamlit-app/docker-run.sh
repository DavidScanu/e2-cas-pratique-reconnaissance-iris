docker run -d --name cas-pratique-streamlit-app -p 5002:5002 -v $(pwd)/src:/streamlit-app davidscanu/cas-pratique-streamlit-app

docker run -it --name cas-pratique-streamlit-app -p 5002:5002 -v $(pwd)/src:/streamlit-app davidscanu/cas-pratique-streamlit-app