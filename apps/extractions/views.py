from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Extraction
from testing.views import post_request


class ExtractionCreateView(CreateView):
    model = Extraction
    fields = []
    def form_valid(self, form):
        # get the request URL data
        ship_symbol = 'MEDLOCK-1'
        url = f"https://api.spacetraders.io/v2/my/ships/{ship_symbol}/extract"
        payload = {}

        ################## MUST REMOVE: exp_status variable #########################
        ################## AND: all the initial error chacking ######################
        exp_status = 201

        info  = post_request(url, payload, exp_status)
        data = info.get('data', [])
        extraction = data['extraction']

        ship = extraction['shipSymbol']
        extracted = extraction['yield']['symbol']
        units = extraction['yield']['units']
        cooldown = data['cooldown']['remainingSeconds']

        extraction_obj = Extraction.objects.create(
            ship=ship,
            extracted=extracted,
            units=units,
            cooldown=cooldown,
        )        

        extraction_obj.save()

        return super().form_valid(form)

    def get_success_url(self):
        # redirect to a success page after data is saved
        return reverse_lazy('about')

    template_name = 'extractions/testing.html'