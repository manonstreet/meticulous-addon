ARG BUILD_FROM
FROM $BUILD_FROM

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    py3-pip

# Copy data for add-on
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY rootfs /

# Set working directory
WORKDIR /usr/bin

# Make script executable
RUN chmod a+x /usr/bin/run.py

CMD [ "python3", "/usr/bin/run.py" ]
