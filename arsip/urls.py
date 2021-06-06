from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(UmumList.as_view()), name='umum_list'),
    path('umum/create', login_required(UmumCreate.as_view()), name='umum_create'),
    path('umum/detail/<int:pk>', login_required(UmumDetail.as_view()), name='umum_detail'),
    path('umum/update/<int:pk>', login_required(UmumUpdate.as_view()), name='umum_update'),
    path('umum/delete/<int:pk>', login_required(UmumDelete.as_view()), name='umum_delete'),
    path('umum/approve/<int:pk>', login_required(UmumApprove), name='umum_approve'),

    path('skpa', login_required(SkpaList.as_view()), name='skpa_list'),
    path('skpa/create', login_required(SkpaCreate.as_view()), name='skpa_create'),
    path('skpa/detail/<int:pk>', login_required(SkpaDetail.as_view()), name='skpa_detail'),
    path('skpa/update/<int:pk>', login_required(SkpaUpdate.as_view()), name='skpa_update'),
    path('skpa/delete/<int:pk>', login_required(SkpaDelete.as_view()), name='skpa_delete'),
    path('skpa/approve/<int:pk>', login_required(SkpaApprove), name='skpa_approve'),

    path('dipa', login_required(DipaList.as_view()), name='dipa_list'),
    path('dipa/create', login_required(DipaCreate.as_view()), name='dipa_create'),
    path('dipa/detail/<int:pk>', login_required(DipaDetail.as_view()), name='dipa_detail'),
    path('dipa/update/<int:pk>', login_required(DipaUpdate.as_view()), name='dipa_update'),
    path('dipa/delete/<int:pk>', login_required(DipaDelete.as_view()), name='dipa_delete'),
    path('dipa/approve/<int:pk>', login_required(DipaApprove), name='dipa_approve'),

    path('spm', login_required(SpmList.as_view()), name='spm_list'),
    path('spm/create', login_required(SpmCreate.as_view()), name='spm_create'),
    path('spm/detail/<int:pk>', login_required(SpmDetail.as_view()), name='spm_detail'),
    path('spm/update/<int:pk>', login_required(SpmUpdate.as_view()), name='spm_update'),
    path('spm/delete/<int:pk>', login_required(SpmDelete.as_view()), name='spm_delete'),
    path('spm/approve/<int:pk>', login_required(SpmApprove), name='spm_approve'),

    path('tup', login_required(TupList.as_view()), name='tup_list'),
    path('tup/create', login_required(TupCreate.as_view()), name='tup_create'),
    path('tup/detail/<int:pk>', login_required(TupDetail.as_view()), name='tup_detail'),
    path('tup/update/<int:pk>', login_required(TupUpdate.as_view()), name='tup_update'),
    path('tup/delete/<int:pk>', login_required(TupDelete.as_view()), name='tup_delete'),
    path('tup/approve/<int:pk>', login_required(TupApprove), name='tup_approve'),

    path('survei', login_required(SurveiList.as_view()), name='survei_list'),
    path('survei/create', login_required(SurveiCreate.as_view()), name='survei_create'),
    path('survei/detail/<int:pk>', login_required(SurveiDetail.as_view()), name='survei_detail'),
    path('survei/update/<int:pk>', login_required(SurveiUpdate.as_view()), name='survei_update'),
    path('survei/delete/<int:pk>', login_required(SurveiDelete.as_view()), name='survei_delete'),
    path('survei/approve/<int:pk>', login_required(SurveiApprove), name='survei_approve'),

    path('daftar-sampel', login_required(DaftarSampelList.as_view()), name='daftar_sampel_list'),
    path('daftar-sampel/create', login_required(DaftarSampelCreate.as_view()), name='daftar_sampel_create'),
    path('daftar-sampel/detail/<int:pk>', login_required(DaftarSampelDetail.as_view()), name='daftar_sampel_detail'),
    path('daftar-sampel/update/<int:pk>', login_required(DaftarSampelUpdate.as_view()), name='daftar_sampel_update'),
    path('daftar-sampel/delete/<int:pk>', login_required(DaftarSampelDelete.as_view()), name='daftar_sampel_delete'),
    path('daftar-sampel/approve/<int:pk>', login_required(DaftarSampelApprove), name='daftar_sampel_approve'),

    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', login_required(auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL)), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)