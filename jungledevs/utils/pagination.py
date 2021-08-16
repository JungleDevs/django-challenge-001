from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10


class CustomPagination(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "page": int(self.request.GET.get("page", DEFAULT_PAGE)),
                "total_pages": self.page.paginator.num_pages,
                "itens_per_page": self.page_size,
                "total_itens": self.page.paginator.count,
                "data": data,
            }
        )
