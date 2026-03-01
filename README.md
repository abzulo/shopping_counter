# Shopping Counter Project
# Group 8 Python Project
## The Shop Counter

### Project Overview
This is our group project for Python. We called it **Shop Counter**.  
The idea is simple: show products, buy items, reduce stock, and keep a record of sales.  
It’s just for practice and learning, not a real shop.

---

### Work Division
We split the work so everyone has a clear role:
- Person A → data.py (products and prices)
- Person B → inventory.py (show products, update stock)
- Person C → sales.py (buy items, save sales)
- Person D → main.py (menu and connects everything)
- Person E → tests + README (testing and documentation)

---

### Workflow
1. Manager created the repo and added starter files.  
2. Each member forked the repo and cloned it.  
3. Everyone worked only on their file.  
4. After finishing, they committed and pushed.  
5. Then they opened a Pull Request.  
6. Manager merged everything.  
7. Finally, we tested and wrote the README.

---

### Fork Flow (Simple)
- Fork once → copy the repo to your GitHub.  
- Clone once → bring it to your computer.  
- Pull before coding → get the latest changes.  
- Commit + Push → save your work.  
- PR → send changes back to manager.  

---

### Project Flow (How It Works)
1. **Start program** → run `python -m shop_counter.main`.  
2. **Menu appears** with options:
   - Show Products
   - Buy Item
   - View Sales History
   - Exit
3. **Show Products** → lists items, prices, and stock.  
4. **Buy Item** → reduces stock, calculates total price, and saves the sale.  
5. **View Sales History** → shows all past purchases saved in `sales_history.json`.  
6. **Exit** → closes the program.

---

### Tasks the Project Handles
- Keep a list of products and their prices.  
- Show available products to the user.  
- Update stock when items are bought.  
- Save sales into a file for record keeping.  
- Display past sales history.  
- Run simple tests to check if stock updates correctly.

---

### How to Run
Run the project with:
```bash
python -m shop_counter.main