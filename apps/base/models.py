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
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолии'

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
        verbose_name = 'Академическая должность'
        verbose_name_plural = 'Академическии должности'

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
        verbose_name = 'Образование/Обучение'
        verbose_name_plural = 'Образовании/Обучении'

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
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогрессы'

    def __str__(self):
        return self.title

class Works(models.Model):
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
        return self.name_of_job

    class Meta:
        verbose_name = 'Прошлое место работы'
        verbose_name_plural = 'Прошлые места работы'


class Experience(models.Model):
    data = models.CharField(
        max_length=255,
        verbose_name='Годы работы'
    )
    description = models.TextField(
        verbose_name='Описание опыта работы'
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыты работы' 

class AboutYourself(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название ваших положительных качеств"
    )
    subtitle = models.TextField(
        verbose_name='Расскажите более подробно'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качества '

class Plans(models.Model):
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
        verbose_name = 'План'
        verbose_name_plural = 'Планы'

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
        verbose_name = 'Иследование'
        verbose_name_plural = 'Иследования'

class Interests(models.Model):
    your_interests = models.CharField(
        max_length=255,
        verbose_name='Ваши интересы'
    )

    def __str__(self):
        return self.your_interests

    class Meta:
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'

class LatestBlogs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название последних постов'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    autor =  models.CharField(
        max_length=255,
        verbose_name='Автор'
    )
    date = models.DateField(
        verbose_name='Дата выпуска'
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Последний блог'
        verbose_name_plural = 'Последние блоги'

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
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
