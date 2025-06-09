from util import filter_mail

if __name__ == '__main__':
    n = int(input("Enter number of emails: "))
    emails = [input("Enter email: ") for _ in range(n)]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
