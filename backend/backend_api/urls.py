from rest_framework_nested import routers
from .views import SchoolViewSet, StudentViewSet, StudentNestedViewSet


router = routers.SimpleRouter()
router.register(r"schools", SchoolViewSet)
router.register(r"students", StudentViewSet)
school_router = routers.NestedSimpleRouter(router, r"schools", lookup="schools")
school_router.register(r"students", StudentNestedViewSet, basename="school-student")

urlpatterns = router.urls
urlpatterns += school_router.urls
