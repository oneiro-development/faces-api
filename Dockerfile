FROM python:3.11
RUN apt-get update && apt-get install -y cmake
RUN pip install dlib flask face_recognition pillow numpy gunicorn
WORKDIR /app
COPY . .
EXPOSE 8000
ENV FLASK_APP=app
ENV FLASK_DEBUG=0
CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:8000"]