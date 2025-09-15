from django.urls import path
from fitness import views


urlpatterns = [
    path("index_page/", views.index_page, name="index_page"),
    path("About/", views.about_page, name="About"),
    path("Class/", views.class_page, name="Class"),
    path('save_class/', views.save_class, name="save_class"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('video/<int:vid>/', views.video, name="video"),
    path("diet_page/", views.diet_page, name="diet_page"),
    path("single_diet/<int:day_id>/", views.single_diet, name="single_diet"),
    path("diet_detail/<int:interval_id>/", views.diet_detail, name="diet_detail"),
    path("", views.sign_in, name="sign_in"),

    #user
    path("sign_up/", views.sign_up, name="sign_up"),
    path("save_signup/", views.save_signup, name="save_signup"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="user_logout"),


    path("product/", views.product, name="product"),
    path("single_product/<int:item_id>/", views.single_product, name="single_product"),

    #cart
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('delete_cart/<int:c_id>/', views.delete_cart, name="delete_cart"),
    path('checkout_cart/', views.checkout_cart, name="checkout_cart"),


    path('save_checkout/', views.save_checkout, name="save_checkout"),
    path('payment/', views.payment, name="payment"),

#wishlist

    # path('favorites/add/<int:song_id>/', views.add_to_favorites, name='add_to_favorites'),
    # path('favorites/remove/<int:song_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    # path('favorites/', views.favorites_view, name='favorites_view'),
    # path('song/<int:song_id>/', views.song_detail, name='song_detail'),

    path('User_Login/', views.user_login, name='user_login'),
    # path('favorites/add/<int:song_id>/', views.add_to_favorites, name='add_to_favorites'),
    # path('favorites/remove/<int:song_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    # path('favorites/', views.favorites_view, name='favorites_view'),

    path('favorites/add/<int:pro_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:pro_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites_view, name='favorites_view'),



]
