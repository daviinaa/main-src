const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
 let ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
 
 // If the IP contains a port (IPv4) or is an IPv6 address, adjust accordingly
 if (ip.includes(':')) {
 const lastIndex = ip.lastIndexOf(':');
 ip = ip.substring(lastIndex + 1);
 }
 // Reverse the IP address
 const reversedIP = ip.split('.').reverse().join('.');
 res.send(`Here you go, your reversed IP: ${reversedIP}`);
});

app.listen(port, () => {
 console.log(`App listening at http://localhost:${port}`);
});