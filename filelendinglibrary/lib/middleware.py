class SetRemoteAddrMiddleware(object):
    def process_request(self, request):
        if request.META.has_key('HTTP_X_REAL_IP'):
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_REAL_IP']
        if not request.META.has_key('REMOTE_ADDR'):
            request.META['REMOTE_ADDR'] = '1.1.1.1' # This will place a valid IP in REMOTE_ADDR but this shouldn't happen

