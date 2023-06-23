# registry.gitlab.com/meltano/meltano:latest is also available in GitLab Registry
ARG MELTANO_IMAGE=meltano/meltano:latest
FROM $MELTANO_IMAGE

WORKDIR /project

# Install any additional requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y unzip

# Install aws-cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" &&\
    unzip awscliv2.zip &&\
    ./aws/install

# AWS CLI credentials configuration
# RUN aws configure set aws_access_key_id ${AWS_ACCESS_KEY} && \
#     aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY} && \
#     aws configure set default.region ${DEFAULT_REGION}

# Copy over Meltano project directory
COPY . .
RUN meltano install

# Allow changes to containerized project files
ENV MELTANO_PROJECT_READONLY 0

ENTRYPOINT ["meltano"]

