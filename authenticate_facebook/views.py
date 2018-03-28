from django.shortcuts import render
import urllib
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
import facebook

def get_authorization_url(request):
        # URL to where Facebook will redirect to
        redirect_url = "http://127.0.0.1:8000/facebook_redirect_url"

        # create a unique state value for CSRF validation
        request.session['facebook_state'] = str(csrf(request)['csrf_token'])

        # redirect to facebook for approval
        url = 'https://www.facebook.com/dialog/oauth?' \
              + 'client_id=' + settings.FACEBOOK_APP_ID \
              + '&redirect_uri=' + redirect_url \
              + '&scope=email' \
              + '&state=' + request.session['facebook_state']

        return HttpResponseRedirect(url)

def verify(request):
        # Facebook will direct with state and code in the URL
        # ?state=ebK3Np...&code=AQDJEtIZEDU...#_=_

        # ensure we have a session state and the state value is the same as what facebook returned
        # also ensure we have a code from facebook (not present if the user denied the application)
		if 'facebook_state' not in request.session \
           or 'state' not in request.GET \
           or 'code' not in request.GET \
           or request.session['facebook_state'] != request.GET['state']:
			return HttpResponse("Authentication failed")
		else:
			return RedirectToAuthenticationPage(request)

			'''data = {}

        # if we don't have a token yet, get one now
			if 'facebook_access_token' not in request.session:

            # URL to where we will redirect to
				redirect_url = "http://127.0.0.1:8000/facebook_redirect_url"

            # set the token URL
				url = 'https://graph.facebook.com/oauth/access_token?' \
        	          + 'client_id=' + settings.FACEBOOK_APP_ID \
            	      + '&redirect_uri=' + redirect_url \
                	  + '&client_secret=' + settings.FACEBOOK_API_SECRET \
                 	  + '&code=' + request.GET['code']

            # grab the token from FB
				response = urllib2.urlopen(url).read()
				print(response)
            # parse the response
            # {'access_token': ['AAAGVChRC0ygBAF3...'], 'expires': ['5183529']}
				params = urlparse.parse_qs(response)

            # save the token
				request.session['facebook_access_token'] = params['access_token'][0]
				request.session['facebook_access_expires'] = params['expires'][0]

			graph = facebook.GraphAPI(access_token=request.session['facebook_access_token'], version="2.12")
'''
			