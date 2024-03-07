FROM node:16-alpine

RUN mkdir -p /home/node/app

WORKDIR /home/node/app
COPY package*.json ./
RUN npm install

COPY --chown=node:node . .
RUN npm run build

USER node

ENV PORT 3000
ENV HTTPS_PORT 443
ENV HOST="0.0.0.0"

EXPOSE $PORT
EXPOSE $HTTPS_PORT

CMD [ "npm", "start" ]