from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

from django.core.mail import send_mail
from django.shortcuts import render

def contact(request):
    success = None
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                email,  # from email
                ["ysrsunilraj@gmail.com"],  # to email (your inbox)
                fail_silently=False,
            )
            success = "Thank you! Your message has been sent successfully."
        except Exception as e:
            success = f"Error sending email: {e}"

    return render(request, "main/contact.html", {"success": success})




def education(request):
    return render(request, "main/education.html")

def experience(request):
    return render(request, "main/experience.html")

def skills(request):
    return render(request, "main/skills.html")

def github(request):
    # Example repo data (replace with GitHub API later)
    repos = [
        {"name": "Bakery Website", "url": "https://tangelraj.github.io/layout12/layout12/index.html"},
        {"name": "Grocerry Website", "url": "https://tangelraj.github.io/grocery/index.html"},
        {"name": "Shoe Website", "url": "https://tangelraj.github.io/layout17/layout17/index.html"},
    ]
    return render(request, "main/github.html", {"repos": repos})


