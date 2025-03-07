import requests

def send_email(subject, body):
    url = 'https://api.emailjs.com/api/v1.0/email/send'
    data = {
        'service_id': 'service_8163xom', 
        'template_id': 'template_90krago', 
        'user_id': '7ncqapHxWSszL-pSG',  
        'template_params': {
            'subject': subject,
            'body': body,
            'to_email': 'ab4290025@gmail.com' 
        }
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("✅ Email sent successfully!")
    else:
        print("❌ Error sending email:", response.text)
