from django.shortcuts import render
from django.http import HttpResponse
import string
import random


# Create your views here.

def home(request):
    """
    root function
    """
    return render(request, 'password_generator/home.html')


def password(request):
    """
    password generator
    """
    length = int(request.GET.get("length"))
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!*$%^#@"

    string_pool = lowercase_letters

    string_pool = string_pool_formation(request, "uppercase_checkbox", uppercase_letters, string_pool)
    string_pool = string_pool_formation(request, "digits_checkbox", digits, string_pool)
    string_pool = string_pool_formation(request, "special_checkbox", special_characters, string_pool)

    the_password = ""
    for _ in range(length):
        the_password += random.choice(string_pool)

    return render(request, 'password_generator/password.html', {"password": the_password})


def string_pool_formation(request, name_to_verify, letters_to_add, current_pool):
    if request.GET.get(name_to_verify, "false") == "true":
        current_pool += letters_to_add
    return current_pool

