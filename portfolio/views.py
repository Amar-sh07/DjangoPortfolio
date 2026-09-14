from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import os
import resend

from .models import Profile, Skill, Project, Achievement, ContactMessage


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by("order")
    projects = Project.objects.all().order_by("order")
    achievements = Achievement.objects.all().order_by("-date")

    return render(
        request,
        "portfolio/index.html",
        {
            "profile": profile,
            "skills": skills,
            "projects": projects,
            "achievements": achievements,
        }
    )


def contact(request):

    if request.method == "POST":

        name = request.POST.get("from_name", "").strip()
        email = request.POST.get("from_email", "").strip()
        message = request.POST.get("message", "").strip()
        website = request.POST.get("website", "").strip()

        # ==========================
        # BASIC VALIDATION
        # ==========================

        if not name or not email or not message:
            messages.error(
                request,
                "Please fill in all fields."
            )
            return redirect("home")

        if len(name) < 2 or len(name) > 100:
            messages.error(
                request,
                "Please enter a valid name."
            )
            return redirect("home")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(
                request,
                "Please enter a valid email address."
            )
            return redirect("home")

        if len(message) < 10:
            messages.error(
                request,
                "Message must contain at least 10 characters."
            )
            return redirect("home")

        if len(message) > 5000:
            messages.error(
                request,
                "Message is too long."
            )
            return redirect("home")

        # Honeypot spam protection
        if website:
            return redirect("home")

        # ==========================
        # SAVE TO DATABASE
        # ==========================

        try:

            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            # ==========================
            # SEND EMAIL USING RESEND
            # ==========================

            resend.api_key = os.getenv("RESEND_API_KEY")

            if not resend.api_key:
                raise Exception("RESEND_API_KEY is missing.")

            email_response = resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": ["ashahare637@gmail.com"],
                "subject": f"New Portfolio Contact Message from {name}",
                "text": (
                    f"You received a new message from your portfolio.\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n\n"
                    f"Message:\n{message}\n"
                ),
                "reply_to": email,
            })

            print("RESEND EMAIL RESPONSE:", email_response)

            messages.success(
                request,
                "Message sent successfully! 🚀"
            )

        except Exception as e:

            print("RESEND EMAIL ERROR:", e)

            messages.error(
                request,
                "Message saved, but email could not be sent."
            )

        return redirect("home")

    return redirect("home")