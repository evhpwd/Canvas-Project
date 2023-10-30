"""
Get your own Canvas user object
"""

from canvasapi import Canvas
from tokens import API_TOKEN, API_URL

canvas = Canvas(API_URL, API_TOKEN)

# Get the user object for the account
user = canvas.get_user('self')

# Print the user info
print(user.__dict__)