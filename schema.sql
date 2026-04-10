-- 1. Create table for market data and logistics costs
CREATE TABLE IF NOT EXISTS buyers_data (
    id SERIAL PRIMARY KEY,
    buyer VARCHAR(255) NOT NULL, 
    price NUMERIC(15, 2) NOT NULL, -- s: revenue per truckload
    distance NUMERIC(10, 2) NOT NULL, -- l: route distance in kilometers
    tariff NUMERIC(10, 2) NOT NULL, -- t: transport rate per km
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- 2. Seed data for algorithm testing (Realistic market scenarios)
INSERT INTO buyers_data (buyer, price, distance, tariff) VALUES
('Construction base (Moscow)', 580000.00, 470.00, 95.00),   
('Furniture factory (Saratov)', 545000.00, 860.00, 68.00),   
('Export warehouse (Saint-Petersburg)', 635000.00, 650.00, 82.00),  
('Furniture factory (Moscow)', 610000.00, 480.00, 92.00),     
('Local factory (Kuznetsk)', 480000.00, 130.00, 115.00);  
