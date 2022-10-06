import poplib
import re
from flask import Flask
app = Flask(__name__)


@app.route("/snapchat=<mail>")
def Get_Hotmail_Code(mail):
    a = 0
    code = []
    password = "Mzme3S9NBppQ"
    pop3_server = "pop-mail.outlook.com"
    try:
        mailbox = poplib.POP3_SSL(pop3_server, '995')
        mailbox.user(mail)
        mailbox.pass_(password)
    except:
        return {"status": "3", "message": "chua bat pop"}
    counts = len(mailbox.list()[1])
    for i in range(counts):
        fullmail = mailbox.retr(i + 1)[1]
        for msg in range(len(fullmail)):
            if "https://accounts.snapchat.com/accounts/passwordreset" in str(fullmail[msg]):
                url = str(fullmail[msg]) + str(fullmail[msg+1])
                return {"status": "1", "message": url.replace("b'", "").replace("'", "").replace("=", "").replace("3D", "=").replace("2D", "-")}
            else:
                pass
    mailbox.quit()
    return {"status": "2", "message": "None"}


if __name__ == '__main__':
    app.run()
