from .models import Post

def create_post(
        *,
        title=str,
        content=str,
)-> Post:
    post = Post.objects.create(
        title=title,
        content=content,
    )

    post.full_clean()
    post.save()

