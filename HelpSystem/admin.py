from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import EmailMailing, CallingMailing, Employee, Article, Views, Likes, Reviews, ReviewAnswer, \
    InsurancePrograms


@admin.register(EmailMailing)
class EmailMailingAdmin(admin.ModelAdmin):
    """Рассылка по Email"""
    list_display = ("id", "email", "date")
    list_display_links = ("email",)
    readonly_fields = ("id", "date")


@admin.register(CallingMailing)
class CallingMailingAdmin(admin.ModelAdmin):
    """Записи на консультации по телефону"""
    list_display = ("id", "phoneNumber", "date", "name")
    list_display_links = ("phoneNumber",)
    readonly_fields = ("id", "date")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Сотрудник"""
    list_display = ("id", "position", "phone", "schedule",)
    list_display_links = ("position",)
    readonly_fields = ("id",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Статья"""
    list_display = ("id", "title", "content", "author", "get_image",)
    list_display_links = ("title",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="120"')

    get_image.short_description = "Изображение"
    exclude = ["viewsCount", "likesCount", ]
    readonly_fields = ("id", "get_image",)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзыв"""
    list_display = ("id", "email", "name", "text", "article")
    list_display_links = ("text",)
    readonly_fields = ("id",)


@admin.register(ReviewAnswer)
class ReviewsAnswerAdmin(admin.ModelAdmin):
    """Комментарий к отзыву"""
    list_display = ("id", "review", "email", "name", "text")
    list_display_links = ("review",)
    readonly_fields = ("id",)


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    """Лайки"""
    list_display = ("id", "article", "user")
    list_display_links = ("article",)


# readonly_fields = ("id", "user", "article")


@admin.register(Views)
class ViewsAdmin(admin.ModelAdmin):
    """Просмотры"""
    list_display = ("id", "article")
    list_display_links = ("id",)
    # readonly_fields = ("id", "user_ip", "article")


@admin.register(InsurancePrograms)
class InsuranceProgramsAdmin(admin.ModelAdmin):
    """Программы страхования"""
    list_display = ("id", "title", "content", "url")
    list_display_links = ("title",)


admin.site.site_title = "IRSIB AdminPanel"
admin.site.site_header = "IRSIB AdminPanel"
