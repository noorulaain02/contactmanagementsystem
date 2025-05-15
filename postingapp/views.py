from boto.s3.website import Redirect
from django.shortcuts import render, redirect
from mysql.connector import cursor

from postingapp.forms import PostalForm
from postingapp.models import Postal
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Postal
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def login(request):
    return render(request, 'show.html')

def index(request):
    postingapp = Postal.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(postingapp, 1000)
    try:
        postingapp = paginator.page(page)
    except PageNotAnInteger:
        postingapp = paginator.page(1)
    except EmptyPage:
        postingapp = paginator.page(paginator.num_pages)

    return render(request, 'show.html', {'postingapp': postingapp})


def show(request):
    postingapp = Postal.objects.all()
    template = loader.get_template('show.html')
    context = {
        'postingapp': postingapp,
    }
    return HttpResponse(template.render(context, request))


def search(request):
    AREA_CD = request.GET.get('AREA_CD')
    PHYSICAL_SMS = request.GET.get('PHYSICAL_SMS')
    TBS = request.GET.get('TBS')
    if AREA_CD:
        postingapp = Postal.objects.filter(AREA_CD__iexact=AREA_CD)
    elif PHYSICAL_SMS:
        postingapp = Postal.objects.filter(PHYSICAL_SMS__iexact=PHYSICAL_SMS)
    elif TBS:
        postingapp = Postal.objects.filter(TBS__iexact=TBS)
    elif AREA_CD and PHYSICAL_SMS:
        postingapp = Postal.objects.filter(AREA_CD__iexact=AREA_CD) & Postal.objects.filter(
            PHYSICAL_SMS__iexact=PHYSICAL_SMS)
    elif AREA_CD and TBS:
        postingapp = Postal.objects.filter(AREA_CD__iexact=AREA_CD) & Postal.objects.filter(
            TBS__iexact=TBS)
    elif TBS and PHYSICAL_SMS:
        postingapp = Postal.objects.filter(TBS__iexact=TBS) & Postal.objects.filter(
            PHYSICAL_SMS__iexact=PHYSICAL_SMS)
    elif AREA_CD and PHYSICAL_SMS and TBS:
        postingapp = Postal.objects.filter(AREA_CD__iexact=AREA_CD) & Postal.objects.filter(
            PHYSICAL_SMS__iexact=PHYSICAL_SMS) & Postal.objects.filter(TBS__iexact=TBS)
    else:
        postingapp = Postal.objects.none()
    return render(request, 'search.html', {'postingapp': postingapp})


# Create Post
def add(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({}, request))


# Store Blog
def addrecord(request):
    a = request.POST['AREA_CD']
    b = request.POST['DOM_CONS']
    c = request.POST['DOM_BULK_CONS']
    d = request.POST['COM_CONS']
    e = request.POST['IND_CONS']
    f = request.POST['CNG_CONS']
    g = request.POST['OTHERS_CONS']
    h = request.POST['TOT_CONS']
    i = request.POST['AREA_DESCR']
    j = request.POST['SUBZONE_DESCR']
    k = request.POST['ZONE_DESCR']
    l = request.POST['REGION_DESCR']
    m = request.POST['UNIT_DESCR']
    n = request.POST['GCV_STATION']
    o = request.POST['GCV_S_NAME']
    p = request.POST['PHYSICAL_SMS']
    q = request.POST['PHYSICAL_SMS_DESCR']
    r = request.POST['TBS']
    s = request.POST['TBS_DESCR']
    t = request.POST['PRS']
    u = request.POST['PRS_DESCR']
    v = request.POST['SYSTEM_DATE']
    postingapp = Postal(AREA_CD=a, DOM_CONS=b, DOM_BULK_CONS=c, COM_CONS=d, IND_CONS=e, CNG_CONS=f, OTHERS_CONS=g,
                        TOT_CONS=h,
                        AREA_DESCR=i, SUBZONE_DESCR=j, ZONE_DESCR=k, REGION_DESCR=l, UNIT_DESCR=m, GCV_STATION=n,
                        GCV_S_NAME=o, PHYSICAL_SMS=p,
                        PHYSICAL_SMS_DESCR=q, TBS=r, TBS_DESCR=s, PRS=t, PRS_DESCR=u, SYSTEM_DATE=v)
    postingapp.save()
    return HttpResponseRedirect(reverse('index'))


def updaterecord(request, AREA_CD):
    # a = request.POST['AREA_CD']
    b = request.POST['DOM_CONS']
    c = request.POST['DOM_BULK_CONS']
    d = request.POST['COM_CONS']
    e = request.POST['IND_CONS']
    f = request.POST['CNG_CONS']
    g = request.POST['OTHERS_CONS']
    h = request.POST['TOT_CONS']
    i = request.POST['AREA_DESCR']
    j = request.POST['SUBZONE_DESCR']
    k = request.POST['ZONE_DESCR']
    l = request.POST['REGION_DESCR']
    m = request.POST['UNIT_DESCR']
    n = request.POST['GCV_STATION']
    o = request.POST['GCV_S_NAME']
    p = request.POST['PHYSICAL_SMS']
    q = request.POST['PHYSICAL_SMS_DESCR']
    r = request.POST['TBS']
    s = request.POST['TBS_DESCR']
    t = request.POST['PRS']
    u = request.POST['PRS_DESCR']
    v = request.POST['SYSTEM_DATE']
    postingapp = Postal.objects.get(AREA_CD=AREA_CD)
    postingapp.DOM_CONS = b
    postingapp.DOM_BULK_CONS = c
    postingapp.COM_CONS = d
    postingapp.IND_CONS = e
    postingapp.CNG_CONS = f
    postingapp.OTHERS_CONS = g
    postingapp.TOT_CONS = h
    postingapp.AREA_DESCR = i
    postingapp.SUBZONE_DESCR = j
    postingapp.ZONE_DESCR = k
    postingapp.REGION_DESCR = l
    postingapp.UNIT_DESCR = m
    postingapp.GCV_STATION = n
    postingapp.GCV_S_NAME = o
    postingapp.PHYSICAL_SMS = p
    postingapp.PHYSICAL_SMS_DESCR = q
    postingapp.TBS = r
    postingapp.TBS_DESCR = s
    postingapp.PRS = t
    postingapp.PRS_DESCR = u
    postingapp.SYSTEM_DATE = v
    postingapp.save()
    return HttpResponseRedirect(reverse('index'))


# employee.ename = ename
# employee.eemail = eemail
# employee.econtact = econtact
# employee.save()


def update(request, AREA_CD):
    postingapp = Postal.objects.get(AREA_CD=AREA_CD)
    if request.method == 'POST':
        form = PostalForm(request.POST, instance=postingapp)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = PostalForm(instance=postingapp)

    return render(request, 'edit.html', {'form': form, 'postingapp': postingapp})


def delete(request, AREA_CD):
    postingapp = Postal.objects.get(AREA_CD=AREA_CD)
    postingapp.delete()
    return HttpResponseRedirect(reverse('index'))

  #  return Redirect('/show')


"""""

def delete(request):
    AREA_CD = request.GET.get('AREA_CD')
    postingapp = Postal.objects.get(AREA_CD=AREA_CD)
    postingapp.delete()
    return HttpResponseRedirect(reverse('index'))
    
"""
