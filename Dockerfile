FROM python:3.11-alpine
WORKDIR /app

# copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy all project files into a workdir
COPY config/ ./config/
COPY handlers/ ./handlers/
COPY utils/ ./utils/
COPY app.py .

#locally we are goin to run it on a fixed port
#however when we deploy $PORT is set by Heroku

EXPOSE 5001
CMD ["python", "app.py"]
