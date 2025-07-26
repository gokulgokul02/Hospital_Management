from django.core.mail import send_mail
from django.conf import settings

def send_email(to_email, patient_name, appointment_date,appointment_time, token_no ):
    subject = "Appointment Approved"
    message = (
        f"Hello {patient_name},\n\n"
        f"Your appointment has been approved.\n"
        f"Token No: {token_no}\n\n"
        f"Date: {appointment_date}\n\n"
        f"Time: {appointment_time}\n\n"
        f"Thank you for choosing VR HOSPITAL!"
    )

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Sender email (from settings.py)
        [to_email],
        fail_silently=False,
    )
