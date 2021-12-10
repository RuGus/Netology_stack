import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email_class:
    """Класс для работы с электронной почтой."""

    def __init__(
        self,
        email_box: str,
        password: str,
        smtp_server: str,
        imap_server: str,
        smtp_port=587,
    ) -> None:
        """Ининциализация класса.

        Args:
            email_box (str): адрес электронной почты.
            password (str): пароль от адреса электронной почты.
            smtp_server (str): адрес smtp сервера.
            imap_server (str): адрес imap сервера.
            smtp_port (int, optional): порт smtp сервера. По умолчанию 587.
        """
        self.email_box = email_box
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server

    def send_message(self, subject: str, message: str, recepients: list) -> None:
        """Отправка сообщения по электронной почте.

        Args:
            subject (str): тема сообщения.
            message (str): текст сообщения.
            recepients (list): получатели сообщения.
        """
        multipart_message = MIMEMultipart()
        multipart_message["From"] = l
        multipart_message["To"] = ", ".join(recepients)
        multipart_message["Subject"] = subject
        multipart_message.attach(MIMEText(message))

        smtp_client = smtplib.SMTP(self.smtp_server, self.smtp_port)
        # identify ourselves to smtp gmail client
        smtp_client.ehlo()
        # secure our email with tls encryption
        smtp_client.starttls()
        # re-identify ourselves as an encrypted connection
        smtp_client.ehlo()

        smtp_client.login(self.email_box, self.password)
        smtp_client.sendmail(self.email_box, smtp_client, multipart_message.as_string())

        smtp_client.quit()

    def recieve_message(self, header=None) -> str:
        """Получение сообщения электронной почты.

        Args:
            header (str): заголовок сообщения. По умолчанию не задан.

        Returns:
            str: сообщение электронной почты.
        """
        imap_client = imaplib.IMAP4_SSL(self.imap_server)
        imap_client.login(self.email_box, self.password)
        imap_client.list()
        imap_client.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        result, data = imap_client.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = imap_client.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        imap_client.logout()
        return email_message


if __name__ == "__main__":
    smtp_server = "smtp.gmail.com"
    imap_server = "imap.gmail.com"
    email_box = "login@gmail.com"
    password = "qwerty"
    subject = "Subject"
    recepients = ["vasya@email.com", "petya@email.com"]
    message = "Message"
    header = None

    my_email = Email_class(email_box, password, smtp_server, imap_server)
    my_email.send_message(subject, message, recepients)
    print(my_email.recieve_message(header))
