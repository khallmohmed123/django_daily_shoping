from django.shortcuts import render_to_response
def home(request):
    title="shop seekers"
    return render_to_response("index.html", locals())