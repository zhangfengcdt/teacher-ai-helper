# Vercel serverless function entry point
import sys
import os

# Add the parent directory to the path so we can import our app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

# This is the WSGI handler that Vercel will use
def handler(event, context):
    return app(event, context)

# For Vercel, we need to export the app as 'app'
app = app