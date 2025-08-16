import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    """
    Class for handling email sending functionality using Gmail SMTP
    """
    
    def __init__(self, gmail_user=None, gmail_password=None, admin_email=None):
        """
        Initialize EmailSender with email configuration
        
        Args:
            gmail_user (str, optional): Gmail account for sending emails
            gmail_password (str, optional): Gmail app password
            admin_email (str, optional): Admin email address
        """
        # Email configuration - these should be in environment variables in production
        self.admin_email = admin_email or "admin@financemandi.com"
        self.gmail_user = gmail_user or "your_gmail_account@gmail.com"
        self.gmail_password = gmail_password or "your_app_password"
    
    def send_email_to_admin(self, name, email, subject, message_content):
        """
        Send emails to admin using Gmail SMTP
        
        Args:
            subject (str): Email subject
            message (str): Email body content
            from_email (str, optional): Sender's email address
        
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        # Prepare email content
        message = f"""
        New contact form submission:
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message_content}
        """
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = self.gmail_user
        msg['To'] = self.admin_email
        msg['Subject'] = subject
        
        # Add reply-to header if sender email is provided
        if from_email:
            msg.add_header('Reply-To', from_email)
        
        # Attach message body
        msg.attach(MIMEText(message, 'plain'))
        
        return self._send_email(msg)
    
    def send_html_email(self, to_email, subject, html_content, from_email=None, plain_text=None):
        """
        Send HTML formatted email
        
        Args:
            to_email (str): Recipient email address
            subject (str): Email subject
            html_content (str): HTML content for the email
            from_email (str, optional): Sender's email address
            plain_text (str, optional): Plain text alternative
            
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = self.gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add reply-to header if sender email is provided
        if from_email:
            msg.add_header('Reply-To', from_email)
        
        # Attach plain text version if provided
        if plain_text:
            msg.attach(MIMEText(plain_text, 'plain'))
        
        # Attach HTML version
        msg.attach(MIMEText(html_content, 'html'))
        
        return self._send_email(msg)
    
    def _send_email(self, msg):
        """
        Internal method to send the email via SMTP
        
        Args:
            msg: MIMEMultipart message object
            
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Setup SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Secure the connection
            server.login(self.gmail_user, self.gmail_password)
            
            # Send email
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            raise e

# For backward compatibility
def send_email_to_admin(subject, message, from_email=None):
    """
    Helper function to send emails to admin using Gmail SMTP (for backward compatibility)
    
    Args:
        subject (str): Email subject
        message (str): Email body content
        from_email (str, optional): Sender's email address
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    email_sender = EmailSender()
    return email_sender.send_email_to_admin(subject, message, from_email)