FROM python:latest
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN apt-get update && apt-get install -y \
    software-properties-common \
    npm
RUN npm install npm@latest -g && \
    npm install n -g && \
    n latest
RUN pip install --user aiogram
RUN pip install translators
RUN pip install python-dotenv 
CMD ["python", "app.py"]