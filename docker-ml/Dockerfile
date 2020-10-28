FROM python:3.6

USER root
WORKDIR /home/

RUN mkdir ./mlsample
RUN mkdir ./mlsample/model

ENV MODEL_DIR=/home/mlsample/model
ENV MODEL_FILE=clf.joblib
ENV METADATA_FILE=metadata.json

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY docker-ml.py .
COPY docker-ml-inference.py .

RUN python -u docker-ml.py
RUN python -u docker-ml-inference.py