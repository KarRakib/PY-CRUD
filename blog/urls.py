
from django.urls import path
from .views import HomePage,PostDetails,CreatePost,DeleteView,UpdateView
urlpatterns = [
 
    path('', HomePage.as_view(),name='home'),
    path('post-<int:pk>/',PostDetails.as_view(), name='postDetails'),
    path('new-post/',CreatePost.as_view(), name='newPost'),
    path('delete/<int:pk>/',DeleteView.as_view(), name='deletePost'),
    path('update/<int:pk>/',UpdateView.as_view(), name='updatePost'),
    

]