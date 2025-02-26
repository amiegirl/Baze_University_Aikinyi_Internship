from django.urls import path
from .views import mine_block, get_chain

urlpatterns = [
    path('mine/', mine_block, name='mine_block'),
    path('chain/', get_chain, name='get_chain'),
    ]