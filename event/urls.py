from django.urls import path
from .views import (
    serve_create_event,
    serve_create_event_category,
    serve_get_all_goal_kinds,
    serve_get_all_tags,
    serve_get_event_by_id,
    serve_get_event_categories,
    serve_get_event_image_by_id,
    serve_get_events_per_location,
    serve_get_event_volunteers,
    serve_get_all_tags,
    serve_update_event,
    serve_get_nearby_events,
    serve_get_or_create_tags,
    serve_search_events,
    serve_upload_event_image,
    serve_update_event_status,
    serve_update_project_progress,
)

urlpatterns = [
    path('category/create/', serve_create_event_category),
    path('category/all/', serve_get_event_categories),
    path('create/', serve_create_event),
    path('detail/<str:event_id>/', serve_get_event_by_id),
    path('discover/nearby/', serve_get_nearby_events),
    path('image/<str:event_id>', serve_get_event_image_by_id),
    path('image/upload/', serve_upload_event_image),
    path('project/goal-kinds/all/', serve_get_all_goal_kinds),
    path('project/progress/update/', serve_update_project_progress),
    path('space/<str:location_id>', serve_get_events_per_location),
    path('search/', serve_search_events),
    path('status/update/', serve_update_event_status),
    path('tags/', serve_get_all_tags),
    path('update/<str:event_id>/', serve_update_event),
    path('tags/get-or-create/multiple/', serve_get_or_create_tags),
    path('managers/volunteers/', serve_get_event_volunteers),
]
