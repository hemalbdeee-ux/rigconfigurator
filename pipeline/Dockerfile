FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends cron && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# cron: prices every 6h, deals hourly, fitment import on demand (docker exec)
# cron runs with a bare PATH (no /usr/local/bin, where the image keeps python), so the crontab sets PATH itself
RUN printf 'PATH=/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin\n0 */6 * * * cd /app && python refresh_prices.py >> /proc/1/fd/1 2>&1\n15 * * * * cd /app && python deals.py >> /proc/1/fd/1 2>&1\n' > /etc/cron.d/pipeline \
  && chmod 0644 /etc/cron.d/pipeline && crontab /etc/cron.d/pipeline
CMD ["sh", "-c", "printenv | grep -E 'DATABASE_URL|SITE_URL|REVALIDATE_SECRET|CREATORS_|AMAZON_TAG|KEEPA|INDEXNOW' > /etc/environment; cron -f"]
