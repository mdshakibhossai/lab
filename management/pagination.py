from rest_framework.pagination import PageNumberPagination

class TodoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'max_size'
    max_page_size = 1000