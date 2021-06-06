from django.shortcuts import render,redirect
from . import models
from django.http import Http404

from .models import Post




from . import forms

from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from pysummarization.nlp_base import NlpBase
from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine



# Create your views here.



def new(request):
    template_name = "memo/new.html"
    if request.method == "POST":
        memo = Post.objects.create(title=request.POST["title"],text=request.POST["text"],mytext=request.POST["mytext"])

        return redirect(view_article,memo.pk)

    return render(request,template_name)


def article_all(request):
    template_name = "memo/article_all.html"
    
    context = {"memos":Post.objects.all()}
    
    return render(request, template_name,context)



def view_article(request,pk):
    template_name = "memo/view_article.html"
    try:
        memo = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    context = {"memo":memo}
    return render(request,template_name,context)



def edit(request,pk):
    template_name = "memo/edit.html"
    try:
        memo = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    if request.method == "POST":
        memo.title = request.POST["title"]
        memo.text = request.POST["text"]
        memo.mytext = request.POST["mytext"]
        memo.save()
        return redirect(view_article,pk)
    context = {"memo": memo}
    return render(request, template_name, context)

def delete(request,pk):
    try:
        memo = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    memo.delete()
    return redirect(article_all)






from django.contrib import messages
from django.views.generic.edit import FormView
from boardapp.forms import TextForm






def list(request):
    form_class = forms.TextForm
    template_name = 'memo/list.html'
    data = Post.objects.all()

    data_text = Post.objects.values_list("text",flat=True)

    data_set = []

     #print(document)

    # NLPのオブジェクト
    nlp_base = NlpBase()

    # トークナイザーを設定します。 これは、MeCabを使用した日本語のトークナイザーです
    nlp_base.tokenizable_doc = MeCabTokenizer()

    # 「類似性フィルター」のオブジェクト。 
    similarity_filter = TfIdfCosine()

    # NLPのオブジェクトを設定します
    similarity_filter.nlp_base = nlp_base

    # 類似性がこの値を超えると、文は切り捨てられます
    similarity_filter.similarity_limit = 0.25

    
    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer for Japanese.
    auto_abstractor.tokenizable_doc = MeCabTokenizer()
    # Set delimiter for making a list of sentence.
    auto_abstractor.delimiter_list = ["。", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()

        
    for i in data_text:
        
   
        # Summarize document.
        result_dict = auto_abstractor.summarize(i, abstractable_doc,similarity_filter)

        new_text=''.join(result_dict["summarize_result"])
        data_set.append(new_text)
    params = {'message':'memo list','data':data_set}
    return render(request, 'memo/list.html',params)



from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView 
from django.contrib.auth.forms import UserCreationForm  
from django.urls import reverse_lazy 
class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "memo/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "memo/logout.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "memo/create.html"
    success_url = reverse_lazy("login")