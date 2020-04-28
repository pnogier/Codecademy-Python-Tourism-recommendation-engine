# Destinations list
destinations = ["Paris, France",
                "Shanghai, China",
                "Los Angeles, USA",
                "São Paulo, Brazil",
                "Cairo, Egypt"]

# Test traveler who is in China at the moment
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# A function that returns a specific destination index in the destinations list
def get_destination_index(destination):
    return destinations.index(destination)


# A function that returns the index of a specific traveler's location
# in the destinations list
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


print(get_traveler_location(test_traveler))
