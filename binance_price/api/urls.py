from django.urls import include, path
from . import views

urlpatterns = [
#   path('assets/<slug:slug>', views.AssetsView.as_view(), name= 'assets'),
#   path('collections/', views.CollectionsListView.as_view(), name= 'collections_list'),
#   path('collections/<slug:contract_address>', views.CollectionsDetailView.as_view(), name= 'collections_detail'),

#   path('auto_bid', views.auto_bid, name="auto_bid"),
#   path('get_fast', views.get_fast, name="get_fast"),
    path('<slug:symbol>', views.index, name="margin"),
#   path('get_traits_list/<slug:slug>', views.get_traits_list, name="get_traits_list"),
#   path('opensea_stop/<slug:slug>', views.opensea_stop, name="opensea_stop"),
#   path('opensea_monitor', views.monitor_opensea_scan_status, name="opensea_monitor"),
#   path('get_collection_stat/<slug:slug>', views.get_collection_stat, name="get_collection_stat"),
  

#   path('logs/<slug:slug>/<slug:filter>/<int:page_size>/<int:cur_page>', views.LogsView.as_view(), name="logs"),
  
  # path('basic_info', views.get_basic_info, name="get_basic_info"),
  
]