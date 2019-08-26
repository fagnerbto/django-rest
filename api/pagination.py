from rest_framework.pagination import PageNumberPagination

class PaginacaoCustomizada(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'tamanho_pagina'
    max_page_size = 10
