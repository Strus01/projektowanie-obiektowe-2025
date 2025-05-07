const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(bodyParser.json());

const DB_PATH = './db.json';

const readDataFromFile = () => {
  try {
    const rawData = fs.readFileSync(DB_PATH);
    return JSON.parse(rawData);
  } catch (error) {
    console.error("Error reading db.json:", error);
    return { products: [] };
  }
};

app.get('/api/products', (req, res) => {
  console.log('Received GET request /api/products');
  const data = readDataFromFile();
  res.json(data.products);
});

app.post('/api/payments', (req, res) => {
  const paymentData = req.body;
  console.log('Received payment data POST /api/payments:', paymentData);
  if (!paymentData || Object.keys(paymentData).length === 0) {
    return res.status(400).json({ message: 'Invalid payment data. Request body is empty.' });
  }

  console.log('Simulating payment processing for card:', paymentData.cardNumber);
  res.status(201).json({
    message: 'Payment received successfully',
    data: paymentData
  });
});


app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
