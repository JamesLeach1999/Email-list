import smtplib
import csv
# when you save the file, make sure it is in the same place as emails1-3.csv
f = open("emails1-3.csv")
csv_f = csv.reader(f)

for email in csv_f:
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login("YOUR.EMAIL@ACCOUNT.COM", "YOUR_EMAIL_PASSWORD")
    server.sendmail('YOUR.EMAIL@ACCOUNT.COM', email,
                    "Subject: EXAMPLE SUBJECT.\nEXAMPLE MESSAGE CONTENT. use \n  ""\n""for a new line in the email")
    {}
    server.quit()





