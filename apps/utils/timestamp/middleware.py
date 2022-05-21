"""This middleware will attach the user id to the request.data
so whenever we need the user info in processing request, we don't have to manually add user
For e.g ** request.data.update({'user': request.user.id}) **"""
import json
import logging

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import APIException

logger = logging.getLogger()


class RequestAttachUserMiddleware(MiddlewareMixin):
    """The following methods __init__ and __call__ are not required when implementing MiddlewareMixin
    However they are required if we were to not implement the mixin
    and we should call process_request and process_exception from __call__ method"""

    # def __init__(self, get_response):
    #     super().__init__(get_response)
    #     self.get_response = get_response
    #
    # def __call__(self, request):
    #     """custom middleware before next middleware/view """
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.
    #
    #     response = self.get_response(request)
    #
    #     # Code to be executed for each response after the view is called
    #
    #     return response

    """Called before the viwe method is called"""

    # def process_request(self, request):
    # data = getattr(request, '_body', request.body)
    # json_data = json.loads(data)
    # request._body = json.dumps(json_data)
    #
    # print(f"The request data is this one {json_data}")

    # if request.method == 'PUT' or request.method == 'PATCH' or request.method == 'POST':
    # request._body = json.dumps(json_data.update({'user': request.user.id}))
    # for prop, value in vars(request).items():
    #     print(prop, ":Left side is property and right side is it's value:", value)
    # return None

    def process_exception(self, request, exception):
        logger.exception(exception)
        print(f"The exception here is {exception}")
        # capture_exception(exception)
        status_code = 500

        if isinstance(exception, ValidationError):
            status_code = 400

        elif isinstance(exception, APIException):
            status_code = exception.status_code
        obj = {"error_message": "{0}".format(str(exception))}
        return JsonResponse(status=status_code, data=obj)
