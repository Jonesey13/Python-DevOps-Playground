def do_a_thing():
    while True:
        print("Type 'quit' to exit")
        first_name = input('What is your name?')
        surname = input('What is your name?')
        if first_name == 'quit':
            break
        print(f"Hello {first_name} {surname}. How are you today?")

do_a_thing()