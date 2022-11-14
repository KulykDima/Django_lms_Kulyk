from copy import copy


def filter_params(request):
    params = request.GET
    if 'page' in params:
        params = copy(params)
        del params['page']

    return{'params': f"&{params.urlencode()}" if params else ''}
