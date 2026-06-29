import time
from django.http import HttpResponseForbidden
class LogRequestMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		# process before view is called
		print(f"[Middleware] Request Path: {request.path}")
		response = self.get_response(request)

		# process after view response
		print(f"[Middleware] Response Status Code: {response.status_code}")
		return response

class TimerMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		start_time = time.time()
		response = self.get_response(request)
		end_time = time.time()
		print(f"[Middleware] Request Path: {request.path}, Elapsed Time: {end_time - start_time:.2f} seconds")
		return response

class BlockIPMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		BLOCKED_IPS = ['127.0.0.7']
		if request.META.get('REMOTE_ADDR') in BLOCKED_IPS:
			print(f"[Middleware] Blocked IP: {request.META.get('REMOTE_ADDR')}")
			return HttpResponseForbidden("IP Blocked", status=403)

		return self.get_response(request)