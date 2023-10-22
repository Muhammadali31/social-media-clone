common_passwords = []
passwords_file = open("YOUR FILE LINK.txt", "r")

for line in passwords_file:
    common_passwords.append(line.strip())
