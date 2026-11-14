const express = require('express');
const app = express();

app.get('/orders', (req, res) => {
    res.json([
        { order_id: 101, item: "Laptop", price: 1200 },
        { order_id: 102, item: "Mouse", price: 25 }
    ]);
});

app.listen(5000, '0.0.0.0', () => {
    console.log('Order service running on port 5000');
});
