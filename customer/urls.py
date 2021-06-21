from django.urls import include, path
from .views import CustomerCreate,BooksList,BooksCreate,MessagesCreate,AgentDetail,MessagesList,AgentList, CustomerList, CustomerDetail, CustomerUpdate, CustomerDelete
from customer import views

urlpatterns = [
	path('create', CustomerCreate.as_view(), name='create-customer'),
 
    path('Messages', MessagesList.as_view()),
     path('Messagescreate', MessagesCreate.as_view()),
      path('Bookcreate', BooksCreate.as_view()),
    path('aziz',CustomerList.as_view()),
    path('Agent',AgentList.as_view()),
    path('Agent/<int:pk>/<str:password>', AgentDetail.as_view(), name='retrieve-customer'),
    path('',BooksList.as_view()),
    # path('<int:pk>/',, name='retrieve-customer'),
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]