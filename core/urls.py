from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("transparency/", views.transparency_view, name="transparency"),
    path("food-map/", views.food_map_view, name="food_map"),
    path("leaderboard/", views.leaderboard_view, name="leaderboard"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_redirect, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("donor/", views.donor_dashboard, name="donor_dashboard"),
    path("donor/food/add/", views.add_food_post, name="add_food"),
    path("donor/food/<int:pk>/edit/", views.edit_food_post, name="edit_food"),
    path("donor/food/<int:pk>/delete/", views.delete_food_post, name="delete_food"),
    path("donor/requests/", views.donor_requests, name="donor_requests"),
    path("donor/requests/<int:pk>/handle/", views.handle_request, name="handle_request"),
    path("ngo/", views.ngo_dashboard, name="ngo_dashboard"),
    path("ngo/food/<int:pk>/request/", views.request_food, name="request_food"),
    path("ngo/requests/", views.ngo_my_requests, name="ngo_my_requests"),
    path("volunteer/", views.volunteer_dashboard, name="volunteer_dashboard"),
    path(
        "volunteer/deliveries/<int:pk>/accept/",
        views.accept_delivery,
        name="accept_delivery",
    ),
    path(
        "volunteer/deliveries/<int:pk>/pickup/",
        views.confirm_pickup,
        name="confirm_pickup",
    ),
    path(
        "volunteer/deliveries/<int:pk>/confirm/",
        views.confirm_delivery,
        name="confirm_delivery",
    ),
    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path(
        "admin-panel/expire-food/",
        views.admin_expire_food,
        name="admin_expire_food",
    ),
]
