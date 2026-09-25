# Multi-stage build → ~150 MB runtime image
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --no-audit --no-fund

FROM node:22-alpine AS build
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ARG SITE_URL=https://rigconfigurator.com
ENV NEXT_TELEMETRY_DISABLED=1 SITE_URL=$SITE_URL
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ARG SITE_URL=https://rigconfigurator.com
ENV SITE_URL=$SITE_URL
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 PORT=3000 HOSTNAME=0.0.0.0
RUN addgroup -S app && adduser -S app -G app
COPY --from=build --chown=app:app /app/public ./public
COPY --from=build --chown=app:app /app/.next/standalone ./
COPY --from=build --chown=app:app /app/.next/static ./.next/static
USER app
EXPOSE 3000
CMD ["node", "server.js"]
