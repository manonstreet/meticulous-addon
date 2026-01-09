ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip

# Copy data for add-on
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY rootfs /

# Ensure scripts are executable
RUN chmod a+x /init && \
    chmod a+x /usr/bin/run.py && \
    chmod a+x /etc/services.d/meticulous/run

# Use s6 init from base image (no CMD override)
