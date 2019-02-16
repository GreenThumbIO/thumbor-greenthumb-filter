FROM spmallick/opencv-docker:opencv
RUN mkdir /thumbor-greenthumb-filter
WORKDIR /thumbor-greenthumb-filter
RUN apt-get update -qq
RUN apt-get install -y libcurl4-openssl-dev libssl-dev
COPY requirements.txt /thumbor-greenthumb-filter/requirements.txt
RUN pip install -r requirements.txt
