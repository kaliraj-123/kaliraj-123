def generate_greeting(first_name, last_name):
    greeting_message = f"Hello {first_name} {last_name}! You just developed into python ."
    return greeting_message

def main():
    first_name = input("Enter your first name(max 10 charachters ):").strip()[:10]
    last_name = input("Enterr your last name (max 10 characters): ").strip()[:10]

    greeting = generate_greeting(first_name,last_name)
    print(greeting)


main()
