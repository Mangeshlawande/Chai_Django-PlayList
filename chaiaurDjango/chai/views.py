from django.shortcuts import render
from .models import chaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'chai/all_chai.html',{'chais': chais})

#  handle frontend values 

def chai_details(request,chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})
