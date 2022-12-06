from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.forms import ModelForm, DateTimeInput, IntegerField
from .models import Offers
from posts.models import Post
from user.models import User

# Create your views here.
class OfferForm(ModelForm):
    class Meta:
        model = Offers
        fields = ['salary', 'expiration']
        widgets = {
            'expiration': DateTimeInput(),
        }


class CreateOffer(View):
    def get(self, request, post_id=-1, candidate_id=-1):
        if post_id < 0 or candidate_id < 0:
            return HttpResponseRedirect('user/dashboard')

        # TODO: Check Permissions

        form = OfferForm()
        context = {'form' : form, 'post_id': post_id, 'candidate_id': candidate_id}

        # Render the form to create
        return render(request, 'Offers/create_offer.html', context)

    def post(self, request, post_id=-1, candidate_id=-1):
        if post_id < 0 or candidate_id < 0:
            return HttpResponseRedirect('/user/dashboard')

        # Get the associated user and post objects
        try:
            post = Post.objects.get(pk=post_id)
            user = User.objects.get(pk=candidate_id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/user/dashboard')

        form = OfferForm(request.POST)
        if form.is_valid():
            # TODO: Check that there is not already a user with the given username
            form.save()

            # Add in the associated user and posts
            offer = Offers.objects.get()
            offer.post = post
            offer.user = user

            # Save to DB
            offer.save()
        return HttpResponseRedirect('/user/dashboard')