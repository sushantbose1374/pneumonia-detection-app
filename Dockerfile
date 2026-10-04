FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY best_final_model.keras .
COPY app.py .
EXPOSE 7860
CMD ["python", "app.py"]
