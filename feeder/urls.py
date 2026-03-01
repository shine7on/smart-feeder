from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world, name = 'hello_world'),
    path('post_endpoint',views.set_example, name = 'set_example' ),
    path('submit_endpoint',views.submit_example, name = 'submit_example' ),
    path('confirm_endpoint',views.confirm_example, name = 'confirm_example' ),
    path('feeding', views.feeding_view, name = "feeding_view"),
    # UNUSE
    path('submit2_endpoint',views.submit_form_example, name = 'submit2_example' )
]

# feeding doesnt store them in db