import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "betolara64@gmail.com"
smtp_password = ""

# Creación del objeto mensaje
msg = MIMEMultipart()
msg['From'] = "Alberto Jahir Chavero Lara"
msg['To'] = "gerardo.bernal@uanl.edu.mx"
msg['Subject'] = "Prueba de envio (script Python) - 1948878"

# Contenido del correo en formato HTML con la imagen adjunta
html = """\
<html>
  <head></head>
  <body>
    <p>Practica 12<br>
       Ejercicio de la practica 12 para envio de correos:<br>
       Alumno: Alberto Jahir Chavero Lara <br>
       Matricula: 1948878</p>
       <img src="cid:image1"><br>
  </body>
</html>
"""

# Ruta de la imagen a adjuntar
image_path = 'C:/Users/achav/Desktop/Logica de programacion/Lab ProgramacionCiberseguridad/fcfm_cool.png'


# Carga de la imagen como objeto MIMEImage
with open(image_path, 'rb') as f:
    image = MIMEImage(f.read())

# Ajuste del ID de contenido de la imagen
image.add_header('Content-ID', '<image1>')

# Adjuntar la parte HTML al mensaje
msg.attach(MIMEText(html, 'html'))

# Adjuntar la imagen al mensaje
msg.attach(image)

# Inicio de sesión en el servidor SMTP
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(smtp_username, smtp_password)

# Envío del mensaje
smtp.sendmail(smtp_username, "gerardo.bernal@uanl.edu.mx", msg.as_string())

# Cierre de la conexión SMTP
smtp.quit()













