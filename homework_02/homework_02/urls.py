from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('00/', include('solution_00.urls')),
    path('05/', include('Viktoriya_Vasileva_05.urls')),
    path('12/', include('_12_Martin_Vrachev.urls')),
    path('10/', include('ivan_enchev_10.urls')),
    path('14/', include('martin_damyanov_14.urls')),
    path('4/', include('victor_dimitrov_04.urls')),
    path('1', include('alexander_yordanov_01.urls')),
    path('06/', include('vladislav_kolev_06.urls')),
    path('18/', include('stelian_todorichkov_18.urls')),
    path('13/', include('Martin_Georgiev_13.urls')),
    path('19/', include('teodor_dishanski_19.urls')),
    path('martin_dinev_15/', include('Martin_Dinev_15.urls')),
    path('17/', include('petar_damyanov_17.urls')),
    path('16/', include("martin_vayer_16.urls")),
    path('11/', include('Liliya_Lyubenova_11.urls')), 
]
