require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');

const app = express();

mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
 console.log("Connected to MongoDB");
});

app.use(express.json());

app.get('/', (req, res) => {
 res.send('Welcome to the Social Media Trending Topics API!');
});

const port = process.env.PORT || 5000;

app.listen(port, () => {
 console.log(`Server is running on port ${port}`);
});