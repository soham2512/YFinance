from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

import yfinance as yf
import pandas as pd
from datetime import datetime

from LumberFeatures.models import *


def Lumberdata():
    Lumber = yf.Ticker("LBS=F")
    hist = Lumber.history(period="max")
    hist = hist.reset_index()
    hist_Lumber_data = hist.tail(150)

    return hist_Lumber_data


def index(request):
    hist_Lumber_data = Lumberdata()
    # LumberFinalData = []

    for row in hist_Lumber_data.iterrows():
        if not LumberData.objects.filter(Date=row[1][0]).exists():
            d, created = LumberData.objects.get_or_create(
                Date=row[1][0],
                Open=row[1][1],
                High=row[1][2],
                Low=row[1][3],
                Close=row[1][4],
                Volume=row[1][5],
                Dividends=row[1][6],
                Stock_Splits=row[1][7]
            )

            d.save()

    LumberDataDB = LumberData.objects.all()
    LumberFinalHigh = []
    LumberFinalOpen = []
    LumberFinalDate = []
    LumberFinalLow = []
    LumberFinalClose = []
    LumberFinalVolume = []

    for i in LumberDataDB:
        LumberFinalDate.append(i.Date[0:10])
        LumberFinalOpen.append(i.Open)
        LumberFinalHigh.append(i.High)
        LumberFinalLow.append(i.Low)
        LumberFinalClose.append(i.Close)
        LumberFinalVolume.append(i.Volume)


    return render(request, 'index.html', {'LumberDataDB': LumberDataDB,
                                          'LumberFinalDate': LumberFinalDate,
                                          'LumberFinalHigh': LumberFinalHigh,
                                          'LumberFinalOpen': LumberFinalOpen,
                                          'LumberFinalLow': LumberFinalLow,
                                          'LumberFinalClose': LumberFinalClose,
                                          'LumberFinalVolume': LumberFinalVolume,

                                          })
