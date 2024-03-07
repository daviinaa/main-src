FROM node:16-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm run build
RUN npm install --only=production

COPY . .
EXPOSE 3000

CMD [ "node", "index.js" ]