FROM python:3.9-slim-bullseye

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0

WORKDIR /vican

ADD src /vican/src
ADD requirements.txt /vican

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm requirements.txt

CMD ["python", "src/object_calib.py"]
