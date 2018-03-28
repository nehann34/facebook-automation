from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from yellowant import YellowAnt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from authenticate_yellowant.models import yellowant_table

# Create your views here.
def RedirectToAuthenticationPage(request):
	return HttpResponseRedirect("https://www.yellowant.com/api/oauth2/authorize/?client_id=%s&response_type=code&reddirect_url=%s"%(settings.YELLOWANT_CLIENT_ID,settings.YELLOWANT_REDIRECT_URL))

def yellowantRedirectUrl(request):

	code=request.GET.get("code",False)
	if code is False:
		return HttpResponse("Invalid Response")
	else:
		#yellowant object is created,which will take client id ,secret,access token and redirect url
		y = YellowAnt(app_key=settings.YELLOWANT_CLIENT_ID, app_secret=settings.YELLOWANT_CLIENT_SECRET,
                  access_token=None,
                  redirect_uri=settings.YELLOWANT_REDIRECT_URL)
		access_token_dict = y.get_access_token(code)
		access_token = access_token_dict['access_token']

		yellowant_user=YellowAnt(access_token=access_token)
		#do user integration with yellowant
		user_integration=yellowant_user.create_user_integration()

		#get user profile
		profile=yellowant_user.get_user_profile()

		print(request.user)
	
		ut=yellowant_table.objects.create(yellowant_token=access_token,yellowant_id=profile['id'],yellowant_integration_id=user_integration['user_application'])

		return HttpResponse("User is authenticated!!!")