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

    if request.method != "POST":
        return redirect("home")

    name = request.POST.get("from_name", "").strip()
    email = request.POST.get("from_email", "").strip()
    message = request.POST.get("message", "").strip()
    website = request.POST.get("website", "").strip()

    def response(success, message_text):
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            from django.http import JsonResponse
            return JsonResponse({
                "success": success,
                "message": message_text
            })

        if success:
            messages.success(request, message_text)
        else:
            messages.error(request, message_text)

        return redirect("home")

    # Required fields
    if not name or not email or not message:
        return response(
            False,
            "Please fill in all fields."
        )

    # Name validation
    if len(name) < 2 or len(name) > 100:
        return response(
            False,
            "Please enter a valid name."
        )

    # Email validation
    try:
        validate_email(email)
    except ValidationError:
        return response(
            False,
            "Please enter a valid email address."
        )

    # Message validation
    if len(message) < 10:
        return response(
            False,
            "Message must contain at least 10 characters."
        )

    if len(message) > 5000:
        return response(
            False,
            "Message is too long."
        )

    # Honeypot protection
    if website:
        return response(
            True,
            "Message sent successfully!"
        )

    try:

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

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

        return response(
            True,
            "Message sent successfully! 🚀"
        )

    except Exception as e:

        print("RESEND EMAIL ERROR:", e)

        return response(
            False,
            "Message saved, but email could not be sent."
        )