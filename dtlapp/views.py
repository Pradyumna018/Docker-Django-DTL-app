from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return render(request,"index.html",{'name':'Pradyumna'})

    my_dict={
        'cities':['Mysore','Bangalore','Mumbai'],
        'std_details':[
            {'name':'Subha','age':24,'place':'Puri','degree':'B.tech','marks':59,'grade':'A+'},
            {'name':'Harish','age':26,'place':'Mumbai','degree':'B.tech','marks':66,'grade':'A'},
            {'name':'Ramu','age':29,'place':'Benaluru','degree':'B.tech','marks':32,'grade':'A+'},
            {'name':'Dhaya','age':22,'place':'Delhi','degree':'B.tech','marks':41,'grade':'A++'},
            {'name':'Nitin','age':21,'place':'Kolkata','degree':'B.tech','marks':51,'grade':'A'},
        ]
    }
    return render(request,"index.html",context=my_dict)