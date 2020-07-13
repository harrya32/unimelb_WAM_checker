import requests
from bs4 import BeautifulSoup
from getpass import getpass
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = input("Enter unimelb username: ")
password = getpass("Enter unimelb password: ")
email_to = input("Enter email to send to: ")
email_from = input("Enter email to send from: ")
email_pw = getpass("Enter email password: ")
url = "https://prod.ss.unimelb.edu.au/student/login.aspx?ReturnUrl=%2fstudent%2fSM%2fResultsDtls10.aspx%3fr%3d%2523UM.STUDENT.APPLICANT%26f%3d%2524S1.EST.RSLTDTLS.WEB%26sid%3d1082047%26cfn%3ds1prod%2520direct%26tkn%3dKe3rnyyQXsexeoXEAF56mEz%252bPIVUfT53RxAqIwq8CaA%253d&r=%23UM.STUDENT.APPLICANT&f=%24S1.EST.RSLTDTLS.WEB&sid=1082047&cfn=s1prod%20direct&tkn=Ke3rnyyQXsexeoXEAF56mEz%2bPIVUfT53RxAqIwq8CaA%3d"
CURRENT_WAM = 91.444
TIME_BETWEEN_CHECKS = 10 #minutes

while True:
    with requests.Session() as session:
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = dict()
        data['ctl00$Content$txtUserName$txtText'] = username
        data['ctl00$Content$txtPassword$txtText'] = password
        data['__EVENTTARGET'] = "ctl00$Content$cmdLogin"

        for i in soup.find_all('input', type = 'hidden'):
            data[i['name']] = i['value']

        response = session.post(url, data=data)
        soup = BeautifulSoup(response.text, "html.parser")
        wam = soup.find(class_='UMWAMText').find('b').text

    if float(wam) != CURRENT_WAM:
        CURRENT_WAM = float(wam)
        port = 465
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            msg = MIMEMultipart()
            msg.attach(MIMEText(f"Your new WAM is {wam}.\n\nSent by your WAM checker."))
            msg["Subject"] = "WAM change detected!"
            msg["From"] = email_from
            msg["To"] = email_to
            server.login(email_from, email_pw)
            server.sendmail(email_from, email_to, msg.as_string())
    else:
        print(f"No change yet, will check again in {TIME_BETWEEN_CHECKS} minutes.")
        
    time.sleep(60 * TIME_BETWEEN_CHECKS)
