################################################################################
def test_download():
    import code.quick_stats as qs
    import code.data as dt

    parameters = {
        'key': dt.read_quick_stats_api_key(),
        'commodity_desc': 'CORN',
        'year__GE': '2012',
        'state_alpha': 'VA',
        'format': 'JSON',
    }
    response = qs.download(parameters=parameters)
    assert response.status_code == 200,\
        'response code not equal to 200, got [{}] instead'.format(response.status_code)


################################################################################
def test_params():
    import code.quick_stats as qs

    parameter = 'commodity_desc'
    response = qs.params(parameter=parameter)
    assert response.status_code == 200,\
        'response code not equal to 200, got [{}] instead'.format(response.status_code)


################################################################################
def test_download():
    import code.quick_stats as qs
    import code.data as dt

    parameters = {
        'key': dt.read_quick_stats_api_key(),
        'commodity_desc': 'CORN',
        'year__GE': '2012',
        'state_alpha': 'VA',
        'format': 'JSON',
    }
    response = qs.count(parameters=parameters)
    assert response.status_code == 200,\
        'response code not equal to 200, got [{}] instead'.format(response.status_code)


################################################################################
def test_apples():
    import code.data as dt
    import code.quick_stats as qs

    parameters = {
        'key': dt.read_quick_stats_api_key(),
        'commodity_desc': 'APPLES',
        'year__GE': '2012',
        'format': 'JSON',
        'unit_desc':'$',
    }
    resp = qs.download(parameters=parameters)
    return resp


################################################################################
def test_prices():
    import code.data as dt
    import code.quick_stats as qs

    possible_units = [
        '$',
        '$ / 1,000 EGGS',
        '$ / 1,000 HEAD',
        '$ / 10,000 SQ FT IRRIGATED',
        '$ / 100 HEAD',
        '$ / 50 LB',
        '$ / 80000 KERNELS',
        '$ / ACRE',
        '$ / ACRE FOOT',
        '$ / ACRE IRRIGATED',
        '$ / AFFECTED ACRE',
        '$ / BARREL',
        '$ / BASKET',
        '$ / BOX',
        '$ / BOX, FOB',
        '$ / BOX, ON TREE EQUIV',
        '$ / BOX, PHD EQUIV',
        '$ / BU',
        '$ / BUNCH',
        '$ / COLONY',
        '$ / CONTAINER',
        '$ / CWT',
        '$ / DIGESTER',
        '$ / DOZEN',
        '$ / EGG',
        '$ / FLAT',
        '$ / FOOT',
        '$ / GALLON',
        '$ / HEAD',
        '$ / HOUR',
        '$ / ITEM',
        '$ / LB',
        '$ / LB, 38 PCT MOISTURE BASIS',
        '$ / LB, 39 PCT MOISTURE BASIS',
        '$ / LB, CHERRY BASIS',
        '$ / LB, GREEN BASIS',
        '$ / MONTH',
        '$ / OPERATION',
        '$ / OUNCE',
        '$ / PELT',
        '$ / POT',
        '$ / SQ FT',
        '$ / TON',
        '$ / TON, DRY BASIS',
        '$ / TURBINE',
        '$, CHERRY BASIS',
        '$, PHD EQUIV',
        '$, WHOLESALE BASIS'
    ]

    parameters = {
        'key': dt.read_quick_stats_api_key(),
        'commodity_desc': 'APPLES',
        'year__GE': '2012',
        'format': 'JSON',
        'unit_desc': possible_units,
    }
    resp = qs.download(parameters=parameters)
    return resp
