# Alpine base image
FROM alpine:latest

# Install
RUN apk add --no-cache curl

# Copy config file
COPY config.txt /app/config.txt

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]
