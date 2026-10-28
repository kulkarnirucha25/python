from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to Django</h1>
        <h3>Features of Django</h3>
        <p>1. URL Routing</p>
        <p>2. Database Support</p>
        <p>3. Security</p>
        <p>4. Admin Interface</p>
        <p>5. Authentication</p>
    """)