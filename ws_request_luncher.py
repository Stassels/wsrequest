#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 30, 2012

@author: tomas
'''
from msg_model_csv import res2csv_DataServices


def request_dict_init():
    request_dict = {}
    request_dict['siteName'] = 'Test Site'
    request_dict['siteID'] = 'Test Site'

    request_dict['lat'] = 46.95869  # Hungary
    request_dict['lng'] = 16.7240
    request_dict['alt'] = 205

    request_dict['summarization'] = 'DAILY'
    request_dict['fromDate'] = '2020-10-05'
    request_dict['toDate'] = '2020-10-05'

    request_dict['timeZone'] = 'UTC+1'  # UTC+1 or GMT+1 ,...

    request_dict['processingKeys'] = ["GHI"]

    request_dict['terrainShading'] = False
    #    request_dict['userHorizon']=[(0.0, 5.0), (7.5, 3.0), (15.0, 7.0), (22.5, 0.0)]

    request_dict['geometry'] = 'FIXEDONEANGLE'
    request_dict['azimuth'] = 0
    request_dict['tilt'] = 0.0
    request_dict['GroundAlbedo'] = None

    request_dict['pvModuleTechnology'] = 'CSI'
    request_dict['pvInstallationType'] = 'FREE_STANDING'
    request_dict['pvInstalledPower'] = 10584.0  # in kWp

    request_dict['pvInverterEffModel'] = '.EfficiencyConstant'
    request_dict['pvInverterEffConstant'] = 98.5

    request_dict['pvLossesDCOther'] = 3.0

    request_dict['pvLossesAC'] = 1.0

    return request_dict


def get_data():

    latitude = 49.258839
    longitude = 19.968625

    request_dict = request_dict_init()

    allow_forecast = False
    allow_backward_forecast = False
    allow_backward_nowcast = False

    request_dict['fromDate'] = '2019-01-01'
    request_dict['toDate'] = '2019-12-31'

    request_dict['lat'] = latitude
    request_dict['lng'] = longitude
    request_dict['timeZone'] = 'UTC+1'
    response_dict = res2csv_DataServices.processRequest_RequestDictType(request_dict, allow_forecast=allow_forecast,
                                                                        allow_backward_forecast=allow_backward_forecast,
                                                                        allow_backward_nowcast=allow_backward_nowcast,
                                                                        outputformat='pandas')
    return response_dict


