import React, { useState } from 'react';
import axios from 'axios';

const Payments = () => {
  const [formData, setFormData] = useState({
    name: '',
    cardNumber: '',
    expiryDate: '',
    cvv: '',
    amount: ''
  });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('Processing payment...');

    if (!formData.amount || parseFloat(formData.amount) <= 0) {
      setMessage('Please enter a valid amount.');
      return;
    }
    if (!formData.cardNumber) {
        setMessage('Please enter card number.');
        return;
    }

    try {
      const response = await axios.post('http://localhost:3001/api/payments', formData);
      setMessage(response.data.message || 'Payment processed successfully!');
      setFormData({ name: '', cardNumber: '', expiryDate: '', cvv: '', amount: '' });
    } catch (err) {
      console.error("Error submitting payment data:", err);
      setMessage('Error processing payment. Please try again.');
    }
  };

  return (
    <div>
      <h2>Payment Details</h2>
      <form onSubmit={handleSubmit} autoComplete='off'>
        <div>
          <label htmlFor="name">Full Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="cardNumber">Card Number:</label>
          <input
            type="text"
            id="cardNumber"
            name="cardNumber"
            value={formData.cardNumber}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="expiryDate">Expiry Date (MM/YY):</label>
          <input
            type="text"
            id="expiryDate"
            name="expiryDate"
            placeholder="MM/YY"
            value={formData.expiryDate}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="cvv">CVV:</label>
          <input
            type="text"
            id="cvv"
            name="cvv"
            placeholder="XXX"
            value={formData.cvv}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="amount">Amount ($):</label>
          <input
            type="number"
            id="amount"
            name="amount"
            placeholder="0.00"
            value={formData.amount}
            onChange={handleChange}
          />
        </div>

        {message && <p>{message}</p>}

        <button type="submit">Pay</button>
      </form>
    </div>
  );
};

export default Payments;
