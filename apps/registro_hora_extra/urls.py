from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraEditDelete, HoraExtraNovo


urlpatterns = [
    path('', HoraExtraList.as_view(),name='list_hora_extra'),
    path('novo/',HoraExtraNovo.as_view(),name='create_hora_extra'),
    path('editar/<int:pk>/',HoraExtraEdit.as_view(),name='update_hora_extra'),
    path('delete/<int:pk>/',HoraExtraEditDelete.as_view(),name='delete_hora_extra'),

]