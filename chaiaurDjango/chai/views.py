from django.shortcuts import render
from .models import chaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm


# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'chai/all_chai.html',{'chais': chais})

#  handle frontend values 

def chai_details(request,chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form':form})



# from django.shortcuts import render, get_object_or_404
# from .models import chaiVariety, Store
# from .forms import ChaiVarietyForm


# # Display all chai varieties
# def all_chai(request):
#     chais = chaiVariety.objects.all()  # Fetch all chai varieties from the database
#     return render(request, 'chai/all_chai.html', {'chais': chais})


# # Display details of a specific chai variety
# def chai_details(request, chai_id):
#     chai = get_object_or_404(chaiVariety, pk=chai_id)  # Get the chai by primary key (or return 404)
#     return render(request, 'chai/chai_details.html', {'chai': chai})


# # Display stores that sell a specific chai variety

# def chai_store_view(request):
#     stores = None  # Initialize stores as None
#     form = ChaiVarietyForm(request.POST or None)  # Handle both GET and POST requests
    
#     if request.method == 'POST':  # Handle form submission
#         if form.is_valid():
#             chai_variety = form.cleaned_data['chai_variety']  # Get the selected chai variety from the form
#             stores = Store.objects.filter(chai_varieties=chai_variety)  # Query stores selling the selected chai variety
#     return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})
