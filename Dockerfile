# registry.gitlab.com/meltano/meltano:latest is also available in GitLab Registry
ARG MELTANO_IMAGE=meltano/meltano:latest
FROM $MELTANO_IMAGE

WORKDIR /project

# Install any additional requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install aws-cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" &&\
    unzip awscliv2.zip &&\
    sudo ./aws/install

# aws-cli configuration
RUN aws configure
RUN ${AWS_ACCESS_KEY}
RUN ${AWS_SECRET_ACCESS_KEY}
RUN
RUN

# Copy over Meltano project directory
COPY . .
RUN meltano install

# Allow changes to containerized project files
ENV MELTANO_PROJECT_READONLY 0

ENTRYPOINT ["meltano"]

