from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models import Book,Admin
  # Function to send SMS

# Home page
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# Book patient details
def book(request):
    if request.method == "POST":
        patient_name = request.POST.get("name")
        patient_age = request.POST.get("age")
        patient_phone = request.POST.get("phone")
        patient_email = request.POST.get("email")

        patient_details = Book(
            patient_name=patient_name,
            patient_age=patient_age,
            patient_phone=patient_phone,
            patient_email=patient_email
        )
        patient_details.save()
        messages.success(request, "Patient booked successfully!")

    return render(request, 'book.html')

# Admin dashboard

def admin_dashboard(request):
    patient_details = Book.objects.all()
    return render(request, 'admin_dashboard.html', {"patient_details": patient_details})


def delete_p_details(request, book_id):
    patient = get_object_or_404(Book, id=book_id)
    patient.delete()
    messages.success(request, "Patient deleted successfully!")
    return redirect('admin_dashboard')


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


from .utils import send_email
def approve(request, patient_id):
    # Get the last inserted Admin record
    last_admin = Admin.objects.last()  # OR Admin.objects.order_by('-date').first()

    if not last_admin:
        messages.error(request, "No admin data found!")
        return redirect('admin_dashboard')

    # Extract the last record fields
    admin_date = last_admin.date
    admin_time = last_admin.time
    admin_token_no = last_admin.token_no

    # Get patient details
    patient = get_object_or_404(Book, id=patient_id)

    # Send email
    send_email(patient.patient_email, patient.patient_name, admin_date, admin_time, admin_token_no)

    messages.success(request, f"Patient {patient.patient_name} approved and email sent!")
    return redirect('admin_dashboard')



def approve_form(request, patient_id):
    dle=Admin.objects.all()

    dle.delete()
    data = get_object_or_404(Book, id=patient_id)
    if request.method == "POST":
        token_no = request.POST.get("token_no")
        date = request.POST.get("date")
        time = request.POST.get("time")
        data=Admin(
            token_no=token_no,
            date=date,
            time=time
        )
        data.save()
        messages.success(request, "Patient approved successfully!")
        return redirect('admin_dashboard')

    return render(request, 'approve_form.html', {"data": data})