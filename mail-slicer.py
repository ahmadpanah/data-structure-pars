def main():
    print("Welcome to email Slicer")
    print("")

    email_input = input("input your email adress: ")

    (username,domain) = email_input.split("@")
    (domain,extention) = domain.split(".")

    print("Username:", username)
    print("Domain:", domain)
    print("Extention:", extention)

main()