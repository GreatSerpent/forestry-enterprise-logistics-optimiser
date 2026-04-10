# Forestry Enterprise Logistics Optimizer 🌲

A simple tool for small forestry businesses to find the most profitable sales routes. It calculates net profit by subtracting transport costs from the sales price.

## 🚀 How it works
The tool uses a **Modified Dijkstra's logic** to compare different buyers. Instead of the shortest distance, it finds the **maximum profit**:
**Profit = Price - (Distance × Tariff)**

## 🛠 Setup

1. **Database**: Run `schema.sql` in your PostgreSQL to create the table and sample data.
2. **Environment**: Create a `.env` file in the main folder:
   ```ini
   DB_NAME=lpk_db
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432