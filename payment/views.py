from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext as _

# from physical_examination.models import Examination


# @login_required
# def unpaid_services_list(request, template_name="payment/unpaid_service_list.html"):
#     examination_list = Examination.objects.filter(payment=False)
#
#     context ={'examination_list': examination_list}
#
#     return render(request, template_name, context)