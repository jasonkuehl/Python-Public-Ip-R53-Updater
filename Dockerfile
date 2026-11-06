# Runs Ip-Updater.py every INTERVAL seconds (default 900), so the Route 53 record follows
# this network's public IP. vars.py and the AWS credentials are mounted at run time,
# never baked in; see docker-compose.yml.
FROM python:3.13-alpine
RUN adduser -D -u 10001 app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Ip-Updater.py .
USER app
ENV INTERVAL=900 PYTHONUNBUFFERED=1
CMD ["sh", "-c", "while true; do python Ip-Updater.py || echo 'update failed; retrying next round'; sleep \"$INTERVAL\"; done"]
