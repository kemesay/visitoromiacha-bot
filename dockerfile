FROM python:3.9.7-stretch AS BASE
RUN apt-get update \
 && apt-get --assume-yes --no-install-recommands install \
    build-essential \
    curl \
    git \
    jq \
    libgomp1 \
    vim 
WORKDIR /app
# upgrade the pip version
RUN pip install --no-cache-dir --upgrade pip
RUN pip install rasa==3.1

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml


