import csv

user_list = []
with open("50Email.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        email = row['email']
        username = email[:email.index("@")]
        domain_name = "www." + email[email.index("@") + 1:]
        user = {'username': username, 'email': email, 'domain_name': domain_name}
        user_list.append(user)

with open('user_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Email", "Domain"])
    for x in range(len(user_list)):
        writer.writerow([user_list[x]['username'], user_list[x]['email'], user_list[x]['domain_name']])
