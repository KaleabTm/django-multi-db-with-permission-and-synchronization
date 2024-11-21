from .models import Post
from employees.models import Employees
from django.core.exceptions import ObjectDoesNotExist

def create_post(
        *,
        title=str,
        content=str,
        author,
)-> Post:
    post_author = Employees.objects.get(email=author.email)
    post = Post.objects.create(
        title=title,
        content=content,
        author=post_author,
    )

    post.full_clean()
    post.save()

    return post


def get_post(title: str) -> Post:
    try:
        post = Post.objects.get(title=title)
        return post
    except ObjectDoesNotExist:
        return None 