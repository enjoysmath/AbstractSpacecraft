from django.urls import path
from .views import save_diagram, new_diagram


urlpatterns = [
    #path('set-category', set_diagram_category, name='set_diagram_category'),    
    #path('set-model-string/<str:Model>/<str:field>', set_model_string, name='set_model_string'),
    path('save-cd/<str:diagram_id>', save_diagram, name='save_diagram'),
    path('new-cd', new_diagram, name='new_diagram'),
    #path('load-cd/<str:diagram_id>', load_diagram_from_database, name='load_diagram'),
    #path('open-cds', list_open_diagrams, name='open_diagrams'),
    #path('all-cds', list_all_diagrams, name='all_diagrams'),
]

