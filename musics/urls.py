from django.urls import path
from . import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "Music API",
        default_version="v1",
        description='Music, Artist 정보',
    ),
)

app_name = 'musics'
urlpatterns = [
    path('musics/',views.music_index, name='music_index'),
    path('musics/<int:music_pk>/',views.music_detail,name='music_detail'),
    path('artist/',views.artist_index,name='artist_index'),
    path('artist/<int:artist_pk>/',views.artist_detail,name='artist_detail'),
    path('reviews/<int:review_pk>/',views.review_update_delete,name='review_update_delete'),
    path('musics/<int:music_pk>/review/',views.review_create,name='review_create'),
    path('redoc/',schema_view.with_ui('redoc'),name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'),name="swagger")
]