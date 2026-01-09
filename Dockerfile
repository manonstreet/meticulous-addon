ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip

# Copy data for add-on
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY rootfs /

# Ensure scripts are executable
RUN chmod -R +x /etc/services.d && \
    chmod +x /usr/bin/run.py && \
    find / -maxdepth 1 -name 'init' -exec chmod +x {} \;

# Use s6 init from base image (no CMD override)
