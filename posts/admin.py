from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    model = Comment
    extra = 3
    min_num = 1
    max_num = 5
    verbose_name_plural ='댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content','image','created_at','view_count','writer')
    # list_editable = ('content',)
    list_filter = ('created_at', )
    search_fields = ('id', 'writer')
    search_help_text = ('게시판 번호, 작성자 검색가능 합니다')
    inlines = [CommentInline]
    actions = ['make_published']
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content = '게시글 삭제 처리.'
            item.save()
