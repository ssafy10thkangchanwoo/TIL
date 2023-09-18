# coding: utf-8
article = Article()
article
article.title = 'first'
article.title
article.content = 'django!'
article.content
article.save()
article
Article.objects.all()
articles = Article.objects.all()
articles
articles[0]
articles[1]
article
article id
article. id
article.title
article.content
article.created_at
article.create_at
article.pk
article = Article(title='second', content='django!!')
article.title
article.content
article.pk
article.save()
article.pk
Article.object.create(title='third', content='django!)
Article.object.create(title='third', content='django!')
Article.object.create(title='third', content='django!!!')
Article.objects.create(title='third', content='django!!!')
Article.object.all()
Article.objects.all()
articles = Article.objects.all()
for article in articles:
    print(article.title)
    
Article.object.get()
Article.objects.get()
Article.objects.get(pk=1)
Article.objects.get(content='django!')
Article.objects.get(content='django!!')
Article.objects.filter(content='django!')
Article.objects.get(content='django33!!')
Article.objects.filter(content='django33!!')
Article.object.filter(title='first')
Article.objects.filter(title='first')
article = Article.objects.get(pk=1)
article
article.title = 'byebye'
article.title
