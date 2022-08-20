from django.urls import path

from . import views

# 为 URL 名称添加命名空间
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex:/polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # 如果你想改变投票详情视图的 URL，比如想改成 polls/specifics/12/ ，你不用在模板里修改任何东西（包括其它模板）
    # ，只要在 polls/urls.py 里稍微修改一下就行：
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex:/polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex:/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]