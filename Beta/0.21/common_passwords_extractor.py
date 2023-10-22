common_passwords = []
passwords_file = open("common_passwords", "r")

for line in passwords_file:
    common_passwords.append(line.strip())