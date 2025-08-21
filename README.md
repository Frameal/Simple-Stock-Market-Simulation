# Stock Market Simulation

This project is a **Python-based simulation** of a simplified stock market.  

It models how traders with different risk profiles (long-term investors, day traders, contrarians) interact in the market, and how their collective decisions influence price over time.

---

## Simulation Overview

The simulation uses:

- **Agent-Based Modeling** → traders with unique behaviors  
- **Supply–Demand imbalance** → drives price movement  
- **Random news shocks** → simulate external market events  
- **Momentum feedback** → price trends attract or repel traders  

The result is a **real-time visualization** showing both trader sentiment and market price changes, resembling the dynamics of a real stock/crypto market.

---

## Features

### Diverse Trader Types
- **Long-term**: slow to react, follow average trend  
- **Day traders**: react quickly to momentum & news  
- **Contrarians**: act opposite to the majority  

### Market Mechanics
- Price moves based on **buy vs sell imbalance**  
- **Liquidity factor** dampens or amplifies price swings  

### Random Events
- **5% chance** per step of a news event causing mass buy/sell  
- Creates **rallies and crashes** similar to real markets  

### Real-Time Visualization
- **Upper chart**: Trader sentiment distribution (Buy / Hold / Sell)  
- **Lower chart**: Market price evolution  

---

## Technologies Used
- **Python**  
- **NumPy** → numeric computations  
- **Matplotlib** → real-time plotting  
- **Random** → stochastic trader decisions & news events  

---

# Run

## Install dependencies
- pip install numpy matplotlib

## Run the simulation
- python simulation.py
