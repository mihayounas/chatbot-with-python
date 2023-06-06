from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Implement your chatbot logic here to get the chatbot response
        response = "Chatbot response"
        return JsonResponse({'response': response})
