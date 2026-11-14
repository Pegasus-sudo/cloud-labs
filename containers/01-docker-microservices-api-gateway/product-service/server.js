const express = require('express');
const app = express();

app.get('/products', (req, res) => {
    res.json([
        { product_id: 201, name: "Keyboard", price: 50 },
        { product_id: 202, name: "Monitor", price: 250 },
        { product_id: 203, name: "Headphones", price: 75 }
    ]);
});

app.listen(5000, '0.0.0.0', () => {
    console.log('Product service running on port 5000');
});
