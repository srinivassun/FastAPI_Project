pip install fastapi uvicorn

#Start FastAPI Server
uvicorn main:app --reload


#Test REST APIs using Swagger UI
#One of the best features of FastAPI is automatic API documentation.
#Open this URL in Chrome:
#Swagger UI
http://127.0.0.1:8000/docs?utm_source=chatgpt.com


#Test using Python Requests Library
pip install requests