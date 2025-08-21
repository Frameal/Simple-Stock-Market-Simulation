import numpy as np
import matplotlib.pyplot as plt
import random

# --- Parameters ---
N = 100            # number of traders
steps = 200        # simulation steps
price = 500        # initial stock price
liquidity = 50     # higher = harder to move price

# --- Trader profiles ---
profiles = np.random.choice(['long_term','day_trader','contrarian'], size=N, p=[0.4,0.4,0.2])
positions = np.random.choice([-1, 0, 1], size=N)  # initial: -1 Sell, 0 Hold, 1 Buy

price_history = [price]

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8))

for step in range(steps):
    new_positions = positions.copy()
    
    avg_trend = np.mean(positions)
    momentum = (price_history[-1] - price_history[-2]) if step > 1 else 0
    
    # Random news shock
    news_bias = 0
    if random.random() < 0.05:  # 5% chance of news
        news_bias = random.choice([-2, 2])  # big sell or buy
        print(f"⚡ NEWS EVENT at step {step}: {'BUY sentiment' if news_bias>0 else 'SELL sentiment'}")
    
    for i in range(N):
        p = profiles[i]
        
        if p == 'long_term':
            # Slow to change, small adjustment toward avg trend
            if random.random() < 0.3:  # 30% chance to act
                new_positions[i] = np.sign(avg_trend + news_bias*0.3)
        
        elif p == 'day_trader':
            # React fast to momentum + news
            if momentum > 0:  # price rising
                new_positions[i] = 1
            elif momentum < 0:  # price falling
                new_positions[i] = -1
            if news_bias != 0:
                new_positions[i] = np.sign(news_bias)
        
        elif p == 'contrarian':
            # Do the opposite of the majority
            if avg_trend > 0:
                new_positions[i] = -1
            elif avg_trend < 0:
                new_positions[i] = 1
    
    positions = new_positions
    
    # --- Market supply vs demand ---
    buys = np.sum(positions == 1)
    sells = np.sum(positions == -1)
    imbalance = buys - sells
    price += imbalance / liquidity
    price_history.append(price)
    
    # --- Visualization ---
    ax1.clear()
    ax2.clear()
    
    # Trader sentiment distribution
    ax1.bar(['Buy', 'Hold', 'Sell'], [buys, np.sum(positions==0), sells], 
            color=['green','gray','red'])
    ax1.set_ylim(0, N)
    ax1.set_title(f"Trader Sentiment (Step {step+1})")
    
    # Market price chart
    ax2.plot(price_history, color='blue', linewidth=2)
    ax2.set_title(f"Stock Price Over Time")
    ax2.set_ylabel("Price")
    
    plt.pause(0.10)

plt.ioff()
plt.show()
