# Sustainable Smart City Assistant

This project is a smart city assistant using IBM Granite LLM and includes:

- AI assistant for sustainability advice
- Semantic search with Pinecone
- Anomaly detection in city sensor data
- FastAPI backend
- Streamlit frontend

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the backend:
```
uvicorn main:app --reload
```

3. Run the frontend:
```
streamlit run frontend.py
```