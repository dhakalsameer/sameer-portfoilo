from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Profile, Project, Skill, Role, ProfilePhoto, Certification


def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    roles = Role.objects.all()
    certifications = Certification.objects.all()

    photos = ProfilePhoto.objects.filter(profile=profile).order_by('order') if profile else []


    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "photos": photos,
        "roles": roles,
        "certifications": certifications,
    }

    return render(request, "website/index.html", context)


def linux_home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    roles = Role.objects.all()
    certifications = Certification.objects.all()

    photos = ProfilePhoto.objects.filter(profile=profile).order_by('order') if profile else []


    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "photos": photos,
        "roles": roles,
        "certifications": certifications,
    }

    return render(request, "website/index1.html", context)

# ================= CONTACT FORM =================
def contact_send_email(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Portfolio Contact Form: {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                "sameerdhakal1234@gmail.com",  # From
                ["sameerdhakal1234@gmail.com"],  # To
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!")
        except Exception as e:
            messages.error(request, f"Error sending message: {str(e)}")

        # Redirect to Linux page
        return redirect("linux_home")  # matches urls.py

    # If someone accesses this URL via GET
    return redirect("linux_home")