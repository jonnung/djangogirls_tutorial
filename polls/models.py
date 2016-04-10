from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    # 'date published'는 pub_date 컬럼에 대한 레이블 문구
    # Admin 사이트에서 사용됨.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        # 객체를 스트링으로 표현할 때 사용하는 함수
        # Admin 사이트나 장고 쉘 등에서 테이블명을 보여줘야 할 때 사용됨
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
