from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


# 第一种方式
def index1(request):
    """第一种方式"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # output = ','.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))


def index(request):
    """第二种 快捷方式"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail_1(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def detail_2(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exists')
    return render(request, 'polls/detail.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results0(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote0(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(dir(request))
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoseNotExist):
        # 重新显示问题投票表。
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理后始终返回HttpResponseRedirect
        # 具有POST数据。这可以防止在以下情况下发布两次数据：
        # 用户点击后退按钮。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
