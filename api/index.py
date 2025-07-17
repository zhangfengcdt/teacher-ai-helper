# Vercel serverless function entry point
import sys
import os

# Add the parent directory to the path so we can import our app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

# For Vercel, we need to export the app as 'app'
# This will be the WSGI application that Vercel calls
application = app

# Also export as 'app' for compatibility
app = app