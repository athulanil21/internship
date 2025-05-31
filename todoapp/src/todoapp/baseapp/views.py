from django.shortcuts import render, redirect
from .models import Task, Book
from .forms import TodoTaskForm


def index(request):
    form = TodoTaskForm()
    data = Task.objects.all()
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baseapp:home')
        else:
            print("Something went wrong!")

        context = {
            'project': "ToDo App",
            'title': "Home",
            'tasks': data,
        }
        return render(request, "baseapp/index.html", context=context)
    else:
        context = {
            'project': "ToDo App",
            'title': "Home",
            'tasks': data,
            'form': form,
        }
        return render(request, "baseapp/index.html", context=context)


# def book_view(request):
#     books = Book.objects.all()  # Fetch all books
#     book_form = BookForm()
#
#     if request.method == 'POST':
#         book_form = BookForm(request.POST)
#         if book_form.is_valid():
#             book_form.save()
#             return redirect('baseapp:book_view')  # Redirect back after saving
#
#     context = {
#         'project': "Book Management",
#         'title': "Books",
#         'books': books,
#         'book_form': book_form,
#     }
#     return render(request, "baseapp/books.html", context)


def book_view(request):
    book_form = Book.objects.all()
    context = {
        'project': "Book Management",
        'title': "Books",
        'book_form': book_form,
    }

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published = request.POST.get("published")
        price = request.POST.get("price")

        if title and author and published and price:  # Ensure required fields are provided
            Book.objects.create(title=title, author=author, published=published, price=price)

    return render(request, "index.html", context)


def delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        # SET is_deleted True; better than delete entire row from db
        # task.is_deleted = True
        # task.save()

        task.delete()
        return redirect('baseapp:home')
    else:
        context = {
            'project': "ToDo App",
            'title': "Delete",
        }
        return render(request, "baseapp/delete.html", context=context)


def changestatus(request, pk):
    # status set to 1 for completed task and save
    data = Task.objects.get(pk=pk)
    data.status = 1
    data.save()
    return redirect('baseapp:home')


def edittask(request, pk):
    instance = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoTaskForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('baseapp:home')
        else:
            print("Something went wrong")
    else:
        form = TodoTaskForm(request.POST or None, instance=instance)
        context = {
            'project': "ToDo App",
            'title': "Update Task",
            'form': form,
        }
        return render(request, "baseapp/edit_task_detail.html", context=context)
