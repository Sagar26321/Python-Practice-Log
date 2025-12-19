def calculate_total(price, tax_rate):
    final_amount = price + (price * tax_rate)
    return final_amount

# --- Main Program ---
item_price = 100
tax = 0.05  # 5% tax

# Call the function and save the result
bill = calculate_total(item_price, tax)

print(f"The final bill is: ${bill}")