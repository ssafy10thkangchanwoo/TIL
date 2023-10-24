from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    # Comment를 serialize해주겠습니다.
    # article도 추가로 해달래요
    # 그럼 여기서 article도 시리얼라이즈하세요.

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta: 
            model = Article 
            fields = ('title','id')
    article = ArticleSerializer(read_only = True)
    # override 가 되면 아래의 readonly는 작동 안됨
    
    # class, Meta 는 선언문이라 코드읽는 것마냥 맨 위에서 아래로 읽히는게 아님 
    class Meta:
        model = Comment
        fields = '__all__'
        # 읽기 전용 필드(유효성검사는 제외, 조회는 가능)
        # read_only_fields = ('article',) # 기본 필드만 여기서 수정 가능함


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    # 왜 이게 readonly지
    comment_set = CommentSerializer(many=True, read_only= True)
    # comment_set은 역참조이니 정해진 이름 써야함, comment_count는 아니니 ㄱㅊ
    # article.comment_set.count() 와 같은 개념의 내용이 필요
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only=True)
    # pk값만 가져오는 primarykeyrealatedfield
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__' # validation을 거쳐 결과물 출력





        