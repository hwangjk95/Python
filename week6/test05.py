def get_formatted_name(first, last):
    return f"{first}{last}".title()

while True:
    print("\nTell me your name (quit:'q')")

    f_name = input("First Name:")
    if f_name.lower() == 'q':
        break

    l_name = input("Last Name:")
    if f_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")