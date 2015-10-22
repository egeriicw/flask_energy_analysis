FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN export SECRET_KEY='date +%s | shasum -a 256 | base64 | head -c 32'
RUN echo $SECRET_KEY
