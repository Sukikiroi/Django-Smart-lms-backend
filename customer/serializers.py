from rest_framework import serializers
from .models import Customer
from .models import Messages
from .models import Books
from .models import Agent

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer 
        fields = ['pk', 'name', 'email']

 
class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages 
        fields = ['pk', 'name', 'message',]

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books 
        fields = ['pk', 'title', 'author','pictur_url','description','isbn','subtitle']

class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent 
        fields = ['pk', 'name', 'username','password']
 

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['username', 'password',]  
        extra_kwargs = {'password': {'write_only': True}}
     
        