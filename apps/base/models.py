from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='settings_logo/',
        verbose_name = 'Логотип'
    )
    fullname = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    subdescription = models.TextField(
        verbose_name='Миниописание'
    )
    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'


class Portfolio(models.Model):
    image = models.ImageField(
        upload_to='settings_image/',
        verbose_name = 'Фото'
    )
    bio = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    review = models.TextField(
        verbose_name='О себе'
    )
    subreview = models.CharField(
        max_length=255,
        verbose_name='Комментарий'
    )
    def __str__(self):
        return self.bio
    
    class Meta:
        verbose_name = '1)Портфолио'
        verbose_name_plural = '1)Портфолии'

class AcademicPositions(models.Model):
    job = models.CharField(
        max_length=100,
        verbose_name='Профессия'
    )
    place_data = models.CharField(
        max_length=255,
        verbose_name='Учебное заведение и дата'
    )

    def __str__(self):
        return self.job

    class Meta:
        verbose_name = '2)Академическая должность'
        verbose_name_plural = '2)Академическии должности'

class EducationTraining(models.Model):
    univercity = models.CharField(
        max_length=255,
        verbose_name='Название университета'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )

    def __str__(self):
        return self.univercity

    class Meta:
        verbose_name = '3)Образование/Обучение'
        verbose_name_plural = '3)Образовании/Обучении'

class Rewards(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name='Прогресс'
    )
    subtitle = models.TextField(
        verbose_name='Описание прогресса'
    )
    year = models.DateField(
        verbose_name='Дата'
    )
    class Meta:
        verbose_name = '4)Прогресс'
        verbose_name_plural = '4)Прогрессы'

    def __str__(self):
        return self.title

class Works(models.Model):
    logo = models.ImageField(
        upload_to='logo_image/',
        verbose_name = 'Логотип'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название тайтла'
    )
    image_of_college = models.ImageField(
        upload_to='job_image/',
        verbose_name = 'Фото колледжа'
    )
    name_of_job = models.CharField(
        max_length=255,
        verbose_name='Название колледжа'
    )
    publication = models.DateField(
        verbose_name='Дата публикации'
    )
    description_of_college = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '5)Прошлое место работы'
        verbose_name_plural = '5)Прошлые места работы'


class Experience(models.Model):
    logo = models.ImageField(
        upload_to='logo_image/',
        verbose_name = 'Логотип'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название тайтла'
    )
    data = models.CharField(
        max_length=255,
        verbose_name='Годы работы'
    )
    description = models.TextField(
        verbose_name='Описание опыта работы'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '6)Опыт работы'
        verbose_name_plural = '6)Опыты работы' 


class AboutYourself(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название ваших положительных качеств"
    )
    subtitle = models.TextField(
        verbose_name='Расскажите более подробно'
    )
    class Meta:
        verbose_name = '7)Качество'
        verbose_name_plural = '7)Качества '

    def __str__(self):
        return self.title

class Journal(models.Model):
    minetitle = models.CharField(
        max_length=255,
        verbose_name='Главный тайтл'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Тайтл'
    )
    subdescription = models.TextField(
        verbose_name='Подописание'
    )

    def __str__(self):
        return self.minetitle

    class Meta:
        verbose_name = '8)Журнал'
        verbose_name_plural = '8)Журналы'

class Research(models.Model):
    minetitle = models.CharField(
        max_length=255,
        verbose_name='Название исследования'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    subdescription = models.TextField(
        verbose_name='Подoписание'
    )

    def __str__(self):
        return self.minetitle

    class Meta:
        verbose_name = '9)Иследование'
        verbose_name_plural = '9)Иследования'

class Interests(models.Model):
    your_interests = models.CharField(
        max_length=255,
        verbose_name='Ваши интересы'
    )

    def __str__(self):
        return self.your_interests

    class Meta:
        verbose_name = '10)Интерес'
        verbose_name_plural = '10)Интересы'

class LatestBlogs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название последних постов'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    date = models.DateField(
        verbose_name='Дата выпуска'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '11)Последний блог'
        verbose_name_plural = '11)Последние блоги'

class Contacts(models.Model):
    name_of_office = models.TextField(
        verbose_name = 'Название офиса'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name = 'Телефон'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    whatsapp = models.URLField(
        verbose_name='Whatsapp'
    )
    instagram = models.URLField(
        verbose_name='Instagram'
    )
    def __str__(self):
        return self.name_of_office

    class Meta:
        verbose_name = '12)Контакт'
        verbose_name_plural = '12)Контакты'

# class Write(models.Model):
#     name = models.CharField(
#         max_length=100,
#         verbose_name='Имя'
#     )
#     email = models.EmailField(
#         verbose_name='Почта'
#     )
#     subject = models.CharField(
#         verbose_name='Объект'
#     )
#     message = models.TextField(

#     )

"""   
                            {% for geeks in testimitions%}
                            <div class="carousel-item">
                                <blockquote>
                                    <img class="rounded-circle img-fluid" src="{{geeks.image.url}}" style = "width:200px" alt="client">
                                    <p>{{geeks.descriptions}}</p>
                                   
                                    <h5>{{geeks.name}}</h5>
                                </blockquote>
                            </div>
                            {% endfor %}"""
    
    

    
    