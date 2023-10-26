def print_item(name, price_in_pennies):
    price_in_pounds = price_in_pennies / 100
    formatted_price = f'£{price_in_pounds:.2f}'
    print(f'Item: {name}')
    print(f'Price: {formatted_price}')


if __name__ == "__main__":
    print_item('Milk', 85)
    print_item('Coffee', 249.56)
    print_item('Orange Juice', 110)



