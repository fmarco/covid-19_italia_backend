
from datetime import datetime
from fastapi import FastAPI
import pandas
import numpy

app = FastAPI()

BASE_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/'

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


@app.get('/national_trend/')
def national_trend(start_at: str = None, end_at: str = None):
    start_at = pandas.to_datetime(f'{start_at} 18:00', format=DATE_FORMAT)
    end_at = pandas.to_datetime(f'{end_at} 18:00', format=DATE_FORMAT)
    data_frame = pandas.read_csv(
        f'{BASE_URL}dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
    )
    data_frame['data'] = pandas.to_datetime(
        data_frame['data'].str.strip(),
        format=DATE_FORMAT
    )
    if start_at is not None:
        data_frame = data_frame[data_frame['data'] >= start_at]
    if end_at is not None:
        data_frame = data_frame[data_frame['data'] <= end_at]
    data_frame = data_frame.replace({numpy.nan: None})
    return {
        'data': data_frame.to_dict(orient='records'),
        'count': data_frame.shape[0]
    }


@app.get('/region_trend/')
def region_trend(region: str = None, start_at: str = None, end_at: str = None):
    start_at = pandas.to_datetime(f'{start_at} 18:00', format=DATE_FORMAT)
    end_at = pandas.to_datetime(f'{end_at} 18:00', format=DATE_FORMAT)
    end_at = f'{end_at} 18:00'
    data_frame = pandas.read_csv(
        f'{BASE_URL}dati-regioni/dpc-covid19-ita-regioni.csv'
    )
    data_frame['data'] = pandas.to_datetime(
        data_frame['data'].str.strip(),
        format=DATE_FORMAT
    )
    if start_at is not None:
        data_frame = data_frame[data_frame['data'] >= start_at]
    if end_at is not None:
        data_frame = data_frame[data_frame['data'] <= end_at]
    if region is not None:
        data_frame = data_frame[data_frame['denominazione_regione'] == region]
    data_frame = data_frame.replace({numpy.nan: None})
    return {
        'data': data_frame.to_dict(orient='records'),
        'count': data_frame.shape[0]
    }


@app.get('/province_trend/')
def province_trend(region: str = None, province: str = None, start_at: str = None, end_at: str = None):
    start_at = pandas.to_datetime(f'{start_at} 18:00', format=DATE_FORMAT)
    end_at = pandas.to_datetime(f'{end_at} 18:00', format=DATE_FORMAT)
    data_frame = pandas.read_csv(
        f'{BASE_URL}dati-province/dpc-covid19-ita-province.csv'
    )
    data_frame['data'] = pandas.to_datetime(
        data_frame['data'].str.strip(),
        format=DATE_FORMAT
    )
    if start_at is not None:
        data_frame = data_frame[data_frame['data'] >= start_at]
    if end_at is not None:
        data_frame = data_frame[data_frame['data'] <= end_at]
    if region is not None:
        data_frame = data_frame[data_frame['denominazione_regione'] == region]
    if province is not None:
        data_frame = data_frame[data_frame['denominazione_provincia'] == province]
    data_frame = data_frame.replace({numpy.nan: None})
    return {
        'data': data_frame.to_dict(orient='records'),
        'count': data_frame.shape[0]
    }
