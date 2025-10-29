from django.urls import path
from home.views import *

urlpatterns = [
    path('',dhomefn),
    path('login/',loginfn),

    path('chome/',chomefn),
    path('shome/',shomefn),

    path('cregister/',cregisterfn),
    path('sregister/',sregisterfn),

    path('clogin/',cloginfn),
    path('slogin/',sloginfn),

    path('cveg/',cvegfn),
    path('sveg/',svegfn),

    path('cfruit/',cfruitfn),
    path('sfruit/',sfruitfn),

    path('cprofile/',cprofilefn),
    path('sprofile/',sprofilefn),

    path('cpe/',cpefn),
    path('spe/',spefn),

    path('sadd/',saddfn),
    path('cview/<int:n_id>/',cviewfn),


    path('cart/<int:p_id>/',cartfn),
    path('viewcart/',viewcartfn),
    path('qedit/<int:p_id>/',qeditfn),
    path('cart_delete/<int:p_id>/',cart_deletefn),


    path('c_orders/<str:t_id>/<int:p_id>/', c_ordersfn),
    path('c_orderlist/',c_orderlistfn),
    path('c_orderview/<int:p_id>/',c_orderviewfn),



    path('s_product_view/<int:p_id>/',s_product_viewfn),
    path('product_delete/<int:p_id>/',product_deletefn),
    path('product_edit/<int:p_id>/',product_editfn),
    path('s_orders/',s_ordersfn),
    path('s_orderview/<int:p_id>/',s_orderviewfn),
    path('status_edit/<int:p_id>/',status_editfn),


    path('payment/<int:t_id>/',paymentfn),
    path('point/<str:amount>/<int:points>/', pointfn),
    path('review/<int:p_id>/',reviewfn),




]
