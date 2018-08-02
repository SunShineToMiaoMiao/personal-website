# 绝对引用
# from models.author import Author
# from models.technical_tag import TechnicalTag
# from models.articlecd import Article
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xizhi_backend.settings")
django.setup()
from xizhi_backend.models import *
# from wsgi import *
import random

author_name_list = ['lixueqin', 'apple', '雪鸢', '稻香村']
article_title_list = ['Django 教程', 'Python 教程', 'HTML 教程', 'vue 教程']


def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # 随机生成9位数的QQ
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % (random.randrange(1, 3))
        author.email = '%s@xizhi.com' % (author.addr)
        author.save()


def create_articles_and_tags():
    # 随机生成文章
    for article_title in article_title_list:
        # 从文章标题中得到 tag
        i = 1
        tag_name = article_title.split(' ', 1)[0]
        tag, created = TechnicalTag.objects.get_or_create(
            name=tag_name, svg_class=tag_name, sort_number=1,
            create_user=1, update_user=1
        )

        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '%s_%s' % (article_title, i)
            article1, created1 = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,  # 随机分配作者
                    'content': '%s 正文' % title,
                    'score': random.randrange(70, 101),  # 随机给文章一个打分
                }
            )
            # 给文章添加标签
            article1.tags.add(tag)


if __name__ == '__main__':

    create_authors()
    create_articles_and_tags()
    print('完成：初始化数据')