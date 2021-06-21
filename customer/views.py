from django.shortcuts import render
from .models import Customer
from .models import Messages
from .models import Books
from .models import Agent
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import CustomerSerializer
from .serializers import MessagesSerializer
from .serializers import BooksSerializer
from .serializers import AgentSerializer
class CustomerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
	queryset = Customer.objects.all(),
	serializer_class = CustomerSerializer


class CustomerList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer





 





class CustomerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Customer.objects.all()
    if Agent.objects.filter().exists() :
          print('Not exist') 
        
    else:  
         print('Not exist') 
    serializer_class = CustomerSerializer

class AgentDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer



class CustomerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class MessagesCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
	queryset = Messages.objects.all(),
	serializer_class = MessagesSerializer

class MessagesList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Messages.objects.filter(pk=1)
    serializer_class = MessagesSerializer    

class BooksList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset =  Books.objects.all()
    serializer_class =  BooksSerializer    

class BooksCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
	queryset = Books.objects.all(),
	serializer_class = BooksSerializer

class AgentList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset =  Agent.objects.all()
    
    serializer_class =  AgentSerializer      