FROM python:3.8.13-alpine3.16 AS python


#[Start] aws DDNS --------------------------------------------------
ARG AWS_LAMBDA
ENV AWS_LAMBDA=${AWS_LAMBDA}
RUN apk add --update curl
#[End] aws DDNS -----------------------------------------------------

#add file
ADD * ./
#update pip
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

WORKDIR /
CMD ["python","/AWSDDNSUS.py"]
