from __future__ import print_function
import time
import locationiq
from locationiq.rest import ApiException
from pprint import pprint
import weatherdata
configuration = locationiq.Configuration()
# Configure API key authorization: key
configuration.api_key['key'] = "pk.a237cd56edda4ec684e2a5bf94f30a71"
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Defining host is optional and default to https://eu1.locationiq.com/v1
configuration.host = "https://eu1.locationiq.com/v1"
# Enter a context with an instance of the API client
with locationiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = locationiq.AutocompleteApi(api_client)
    q = 'Hospital' # str | Address to geocode
    qq = 'College'
normalizecity = 1 # int | For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs.
limit = 10 # int | Limit the number of returned results. Default is 10. (optional) (default to 10)
viewbox = '12.8769, 80.1762,13.2197, 80.5091' # str | The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box.  (optional)
bounded = 0 # int | Restrict the results to only items contained with the viewbox (optional)
countrycodes = 'in' # str | Limit search to a list of countries. (optional)
accept_language = 'en' # str | Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native (optional)
# tag = 'amenity' # str | Restricts the autocomplete search results to elements of specific OSM class and type.  Example - To restrict results to only class place and type city: tag=place:city, To restrict the results to all of OSM class place: tag=place (optional)

# lon = 80.2785
# lat = 13.0878

def geoloc(lat,lon,chkdist):
    a=[]
    print("Starting GeoLocation Service")
    try:
        api_response_hosp = api_instance.autocomplete(q, normalizecity, limit=limit, viewbox=viewbox, bounded=bounded, countrycodes=countrycodes, accept_language=accept_language)
        api_response_clg = api_instance.autocomplete(qq, normalizecity, limit=limit, viewbox=viewbox, bounded=bounded, countrycodes=countrycodes, accept_language=accept_language)
        for i in api_response_hosp:
            x=i['lat']
            y=i['lon']
            if (abs((float(x)-lat) <= chkdist) & (abs(float(y)-lon) <= chkdist)):
                a.append(i["display_place"])
        for i in api_response_clg:
            x=i['lat']
            y=i['lon']
            if (abs((float(x)-lat) <= chkdist) & (abs(float(y)-lon) <= chkdist)):
                a.append(i["display_place"])
        # pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->autocomplete: %s\n" % e)
    out = ' '.join(map(str,a))
    return out
# geoloc(13.08,80.2,0.02)
