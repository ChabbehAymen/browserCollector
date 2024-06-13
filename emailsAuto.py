import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# list of emails
emails = ['chebbehaymen@gmail.com', 'chabbehaymensolicde@gmail.com']

# Create a text/plain message
msg = EmailMessage()
msg.set_content("Cher/chère recruter,\n"
"Je suis un développeur web Full-Stack compétent, désireux de perfectionner mon expertise grâce à un stage pratique. J'aimerais rejoindre votre équipe pour apprendre auprès de professionnels expérimentés tout en contribuant efficacement. Veuillez trouver ci-joint mon CV pour votre examen. J'attends avec impatience de discuter de la manière dont je pourrais contribuer à vos projets.\n"
"Cordialement,\n"
"CHABBEH Aymen")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "Développeur Web Full-Stack à la recherche d'une opportunité de stage"
msg['From'] = 'chabbehaymen9+work@gmail.com'
with open('/home/aymen/Downloads/CHABBEHAymen.pdf','rb') as fp:
    pdfdata = fp.read()
    msg.add_attachment(pdfdata, maintype='PDF',subtype='PDF')
for email in emails:
    msg['To'] = email
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()