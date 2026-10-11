from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    inventory_list = ["Widget1", "Widget2", "Widget3"]
    greeting = "Thank you for visiting"
    context = {"inventory": inventory_list, "greeting": greeting}
    return render(request, "home.html", context)
