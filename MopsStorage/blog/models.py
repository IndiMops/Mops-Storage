from django.db import models

class Post(models.Model):
    """Модель даних сатті в програмі blog"""
    post_id = models.AutoField(primary_key = True, verbose_name = "ID")
    title =  models.CharField(verbose_name = "Назва статті", max_length = 120)
    content = models.TextField(verbose_name = "Контент статті")
    create_at = models.DateTimeField(verbose_name = "Дата публікації", auto_now_add = True, null = True, editable = False)
    
    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"

    def __str__(self):
        formatted_date = self.create_at.strftime("%d.%m.%y %H:%M")
        if len(self.title) > 120:
            return "{0}, {1}, {2}..., {3}".format(self.post_id,self.title,  self.content[:120], formatted_date)
        else:
            return "{0}, {1}, {2}, {3}".format(self.post_id, self.title, self.content, formatted_date)
    