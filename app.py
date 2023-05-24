from flask import Flask, render_template ,request,send_file
import time
import smtplib
import os
app = Flask(__name__)

def mail(email, pssd, mssg):
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, pssd)
    server.sendmail(email, 'srivas.arjit@gmail.com', mssg)

    server.quit()

@app.route('/download-cv')
def download_cv():
    # Path to your PDF file
    cv_path = 'C:/Users/sriva/OneDrive/Desktop/Arjit_latest_resume.pdf'
    
    # Return the file for download
    return send_file(cv_path, as_attachment=True)


@app.route('/')
def home_page():
    return render_template("index.html")


def cleanMsg(data):
    name= data.get('name')
    email= data.get('email')
    msg=data.get('message')
    message = f"""From: {name} <{email}>
Subject: New Message On Our Official Website
{msg}
"""
    return message

@app.route('/submit_form',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()
        msg=cleanMsg(data)
        password=os.environ.get('EMAIL_PASS')
        mail('wantech010@gmail.com', password, msg)
        return render_template("index.html",code="test()")
    else:
        return f"Something Not Right "
    

@app.errorhandler(404)  
def not_found(e): 
  return render_template("404.html") 

if __name__ == '__main__':
    app.run(debug=True)