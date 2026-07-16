import googlemaps
#Create the Places function
# search_place() has one responsibility: search the Places API.


#That separation makes the code easier to debug and extend.
def search_place(gmaps,phc_name, lga):
    """
    Search Google Places using the PHC name.
    """

    query = f"{phc_name}, {lga}, Lagos State, Nigeria"

    try:

        places = gmaps.places(query)

        if places["status"] == "OK" and places["results"]:

            result = places["results"][0]

            return {
                "status": "FOUND",
                "method": "Places",
                "google_name": result.get("name"),
                "google_address": result.get("formatted_address"),
                "place_id": result.get("place_id"),
                "lat": result["geometry"]["location"]["lat"],
                "lon": result["geometry"]["location"]["lng"],
                "partial_match": False
            }

    except Exception as e:

        print(e)

    return None

#If that works,building the Geocoding fallback
#geocode_address() has one responsibility: geocode an address if Places didn't find anything.


def geocode_address(gmaps,phc_name, address, lga):
    """
    Fallback to Google Geocoding API.
    """

    query = (
        f"{phc_name}, "
        f"{address}, "
        f"{lga}, "
        "Lagos State, Nigeria"
    )

    try:

        results = gmaps.geocode(query)

        if results:

            result = results[0]

            return {
                "status": "FOUND",
                "method": "Geocoding",
                "google_name": None,
                "google_address": result.get("formatted_address"),
                "place_id": result.get("place_id"),
                "lat": result["geometry"]["location"]["lat"],
                "lon": result["geometry"]["location"]["lng"],
                "partial_match": result.get("partial_match", False)
            }

    except Exception as e:

        print(e)

    return None

# Building one master function ,This is where everything comes together.
# geocode_phc() orchestrates the workflow.

def geocode_phc(gmaps,row):

    # First attempt: Places
    result = search_place(gmaps,
        row["PHC_NAME"],
        row["LGA/LCDA"]
    )

    if result is not None:
        return result

    # Second attempt: Geocoding
    result = geocode_address(gmaps,
        row["PHC_NAME"],
        row["ADDRESS"],
        row["LGA/LCDA"]
    )

    if result is not None:
        return result

    # Failed
    return {
        "status": "FAILED",
        "method": None,
        "google_name": None,
        "google_address": None,
        "place_id": None,
        "lat": None,
        "lon": None,
        "partial_match": None
    }