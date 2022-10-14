
from django.shortcuts import render, get_object_or_404, redirect
from header.models import Top_header, Header
from . models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db.models import Q


class Search(View):

    def post(self, request, format=None):
        data = self.request.data
        str = data['str']
        q = (Q(headline__icontains=str)) | (Q(body__icontains=str)) | (Q(catagory__icontains=str))
        queryset = Post.objects.filter(active=True)
        queryset = queryset.filter(q)
        # serializer = Home_serializer(queryset, many=True)
        # return Response(serializer.data)
        context = {
            'search': queryset
        }
        return render(request, 'blog.html', context=context)

def search(request):
    template = 'search.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
  
    if request.method == 'POST':
        searched = request.POST['searched']
        post = Post.objects.filter(headline__contains=searched)

        context={
            'searched':searched,
            'posts': post,
            'top_headerdata': top_header,
            'headerdata': header,
    
        }
        return render(request, template_name=template, context=context)
    else:
        context={
            'top_headerdata': top_header,
            'headerdata': header,
 

        }
        return render(request, template_name=template, context=context)


def blog(request):
    template = 'blog.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()

    cate = Category.objects.all()
    category_pick = request.GET.get('category')

    if category_pick == None:

        posts = Post.objects.filter(publish_status=Post.ArticlePublishOptions.PUBLISH)

    else:
        posts = Post.objects.filter(catagory__name=category_pick, publish_status=Post.ArticlePublishOptions.PUBLISH)

    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'posts': post,
        'page_ob': page,
        'category': cate,
        
    }
    return render(request, template_name=template, context=context)


def post_detail(request, slug):

    template = 'blog-single.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    cate = Category.objects.all()

    posts = Post.objects.filter(publish_status=Post.ArticlePublishOptions.PUBLISH)[0:3]
    post = get_object_or_404(Post, slug=slug)
    comments = post.comment_here.filter(approved=True)
    new_comment = None
    if request.method == 'POST':

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():


            new_comment = comment_form.save(commit=False)

            new_comment.post = post


            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'posts': posts,
        'headerdata': header,
        'category': cate,
        'comment_form': comment_form,
        "new_comment": new_comment,

    }
    return render(request, template_name=template, context=context)


@login_required(login_url='blog')
def delete_post(request, pk, sl):

    post = get_object_or_404(Post, id=pk, slug=sl)
    post.delete()
    return redirect('blog:blog')


@login_required(login_url='blog')
def edit_post(request, pk, sl):

    template = 'edit_post.html'
    header = Header.objects.order_by()

    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk, slug=sl)
        editpost = ModelPost(request.POST, request.FILES, instance=post)
        editpost.save()
        return redirect('blog:blog')
    else:
        post = get_object_or_404(Post, id=pk, slug=sl)
        editpost = ModelPost(instance=post)

    context = {
        'post_form': editpost,
        'headerdata': header,
    }

    return render(request, template_name=template, context=context)




@login_required(login_url='blog')
def create_post(request):
    template = 'create_post.html'
    post_form = ModelPost()
    if request.method == 'POST':
        post_form = ModelPost(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
        return redirect('blog:blog')

    context = {
        'post_form': post_form
    }
    return render(request, template_name=template, context=context)

