---
title: Protecting Bank Information
date: 2025-03-24
tags: [AgeOfDragons, BankAccount]
---

# Protecting Bank Information

**Age of Dragons** is a game about resource management and strategy. The game includes a bank feature that allows players to deposit and withdraw funds.

---

## Assignment: BankAccount Class

### 1. Complete the Constructor
1.1. Set `__account_number` to `account_number`.  
1.2. Set `__balance` to `initial_balance`.

### 2. Complete the Public Getters
2.1. **`get_account_number`**  
&nbsp;&nbsp;&nbsp;Return the value of the private variable `__account_number`.  

2.2. **`get_balance`**  
&nbsp;&nbsp;&nbsp;Return the value of the private variable `__balance`.

### 3. Complete the `deposit` Method
3.1. Accept an `amount` as input and add it to the account balance.  
3.2. If the deposit amount is not positive, raise a `ValueError` with the message:  
&nbsp;&nbsp;&nbsp;**"Cannot deposit zero or negative funds."**  
&nbsp;&nbsp;&nbsp;Otherwise, add the amount to the balance.

### 4. Complete the `withdraw` Method
4.1. Accept an `amount` as input and check if there is enough money in the account.  
4.2. If the withdrawal amount is not positive, raise a `ValueError` with the message:  
&nbsp;&nbsp;&nbsp;**"Cannot withdraw zero or negative funds."**  
&nbsp;&nbsp;&nbsp;Then, if there are not enough funds, raise a `ValueError` with the message:  
&nbsp;&nbsp;&nbsp;**"Insufficient funds."**  
&nbsp;&nbsp;&nbsp;Otherwise, deduct the amount from the balance.
