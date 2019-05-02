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
    import code.data as dt

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
