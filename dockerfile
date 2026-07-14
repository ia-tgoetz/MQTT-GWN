# --- Final Production Dockerfile ---

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -r chariot && \
    useradd -r -g chariot -m -d /usr/local/chariot -s /bin/bash chariot

RUN mkdir -p /tmp/chariot-install /usr/local/chariot

COPY chariot-init/chariot_linux_2.8.1.zip /tmp/chariot.zip
RUN unzip -q /tmp/chariot.zip -d /tmp/chariot-install && rm /tmp/chariot.zip

# Move all the unzipped application files to their final home.
RUN mv /tmp/chariot-install/* /usr/local/chariot/ && rm -rf /tmp/chariot-install

# Unpack the bundled Java Development Kit (JDK) that Chariot requires.
RUN tar -xzf /usr/local/chariot/lib/runtime/amazon-corretto-*.tar.gz -C /usr/local/chariot/lib/runtime/ && \
    rm /usr/local/chariot/lib/runtime/amazon-corretto-*.tar.gz

# Make all shell scripts in the yajsw/bin directory executable.
RUN chmod +x /usr/local/chariot/yajsw/bin/*.sh

# Set ownership for the entire application directory.
RUN chown -R chariot:chariot /usr/local/chariot

# Switch to the non-root user.
USER chariot

EXPOSE 1883
EXPOSE 8080

# --- THIS IS THE FIX ---
# Set the working directory to the script's location.
WORKDIR /usr/local/chariot/yajsw/bin

# The command to start the Chariot server.
ENTRYPOINT ["./runConsole.sh"]