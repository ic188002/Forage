from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
   
     # image urls 

    path('images/', views.image_Index, name='image_Index'),
    path('images/<int:image_id>', views.images_detail, name='images_detail'),
    path('images/create/', views.ImageCreate.as_view(), name='images_create'),
    path('images/<int:pk>/update/', views.ImageUpdate.as_view(), name='images_update'),
    path('images/<int:pk>/delete/', views.ImageDelete.as_view(), name='images_delete'),
    path('images/<int:image_id>/add_to_board/', views.add_to_board, name='add_to_board'),











     # userprofile urls 
     path('users/', views.profile_index, name='profile_index'),
     path('users/edit/<int:user_id>/', views.profile_detail, name='profile_detail'),
     path('users/view/<int:user_id>/', views.profile_viewer, name='profile_viewer'),
     path('users/<int:user_id>/delete', views.profile_delete, name='profile_delete'),
     path('users/<int:user_id>/confirmdelete', views.profile_confirm_delete, name='profile_confirm_delete'),
     
     

    # authenitcation urls 
    # Signup:
     path('accounts/signup/', views.signup, name='signup'),      
     path('accounts/changepassword/', views.change_password, name='change_password'),







     # board urls 
     path('boards/', views.boards_index, name='board_index'),
     path('boards/<int:board_id>', views.boards_detail, name='board_detail'),
     path('boards/create/',views.BoardCreate.as_view(), name='board_create'),
     path('boards/<int:pk>/update/', views.BoardUpdate.as_view(),name='board_update'),
     path('boards/<int:pk>/delete/', views.BoardDelete.as_view(),name='board_delete'),
     path('boards/<int:board_id>/assoc_image/<int:image_id>', views.assoc_image, name='assoc_image'),
     path('boards/<int:board_id>/unassoc_image/<int:image_id>', views.unassoc_image, name="unassoc_image"),
     path('boards/<int:board_id>/add_image/', views.add_image , name='add_image'),



    






]