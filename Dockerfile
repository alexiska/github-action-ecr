FROM python:3

#ADD connect_db.py /
COPY . .

RUN pip install fastapi

RUN pip install uvicorn

EXPOSE 8080

CMD ["uvicorn", "connect_db:app", "--host", "0.0.0.0", "--port", "8080"]