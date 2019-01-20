FROM sugyan/heroku-python-opencv
RUN mkdir /thumbor-greenthumb-filter
WORKDIR /thumbor-greenthumb-filter

COPY requirements.txt /thumbor-greenthumb-filter/requirements.txt
RUN pip install -r requirements.txt
