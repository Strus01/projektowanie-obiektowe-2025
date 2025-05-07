import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Products = () => {
  const [products, setProducts] = useState([]);
  const [message, setMessage] = useState('Loading products...');

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://localhost:3001/api/products');
        console.log(response);
        if (response.data && response.data.length > 0) {
          setProducts(response.data);
          setMessage('');
        } else {
          setProducts([]);
          setMessage('No products found.');
        }
      } catch (err) {
        console.error("Error fetching products:", err);
        setProducts([]);
        setMessage('Error fetching products.');
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Our Products</h2>
      {message && <p>{message}</p>}
      {products.length > 0 && (
        <ul>
          {products.map(product => (
            <li key={product.id}>
              <h3>{product.name}</h3>
              <p>Price: ${product.price}</p>
              <p>{product.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Products;
