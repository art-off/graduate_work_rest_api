from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from api.v1.user.views import UserViewSet
from api.v1.food_projects.views import FoodProjectsViewSet, MenuItemViewSet, PromotionItemViewSet
from api.v1.card.views import OrderViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('food_projects', FoodProjectsViewSet, basename='food_projects')
router.register('menu_items', MenuItemViewSet, basename='menu_items')
router.register('promotions', PromotionItemViewSet, basename='promotions')
router.register('card/order', OrderViewSet, basename='card_order')

schema_view = get_schema_view(
    openapi.Info(title='Always data API', default_version='v1', description='Routes of Always data project'),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('', include((router.urls, 'api-root')), name='api-root'),
]
