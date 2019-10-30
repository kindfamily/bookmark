from django.shortcuts import render,redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm


def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()

    return render(request, 'bookmark/list.html', {
        'bookmark_list': bookmark_list,
    })

def bookmark_new(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = Bookmark()
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:bookmark_list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmark/create.html', {
        'form': form,
    })

def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmark/update.html', {
        'bookmark': bookmark,
        'form': form,
    })

def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark:bookmark_list')








