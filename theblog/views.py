from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import Postform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def likeview(request,pk):
    #post = get_object_or_404(Post,id=request.POST.get('post_id'))
    #post.likes.add(request.user)
    #return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))
    

class Home(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        cat_manu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_manu"] = cat_manu
        return context


def Categoryview(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cat': cats, 'category': category_posts})


class ArticleDetail(DetailView):
    model = Post
    template_name = 'detail.html'

    """def get_context_data(self, *args, **kwargs):
        cat_manu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context["cat_manu"] = cat_manu
        return context
"""

class Addpostview(CreateView):
    model = Post
    form_class = Postform
    template_name = 'addblog.html'
    #fields = '__all__'


class Updatepostview(UpdateView):
    model = Post
    form_class = Postform
    template_name = 'update.html'


class Deletepostview(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class Addcategoryview(CreateView):
    model = Category
    #form_class = Postform
    template_name = 'addcategory.html'
    fields = '__all__'
