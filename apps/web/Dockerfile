FROM node:22-alpine

WORKDIR /web
COPY apps/web/package.json /web/package.json
RUN npm install
COPY apps/web /web

CMD ["npm", "run", "dev"]

