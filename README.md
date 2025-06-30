# Airport Mapping

This is a very very early form of a TravelMapping-adjacent idea for mapping airports visited.

The current output is simple: symbols at airports worldwide that show a user's visits to that airport. Users who have departed an airport will see a green upward-pointing triangle, and users who have arrived at an airport will see one in red pointing downward. Airports where users experienced a layover (with or without a plane change) appear as a blue circle surrounding the triangles.

## How to create a map

Maps are generated from "alist" files submitted via GitHub. The filename should be [username].alist. In the file, user data should use the following format:

[IATA Airport Code] [N] [N]* [N]*

*the third and fourth fields are optional.

N can be any of the following codes: A (for arrival), D (for departure), and L (for layover).

**Example:**

```
ATL A D L   means that the traveler arrived at and departed from Hartsfield–Jackson Atlanta International Airport, and also stopped at that airport on a non-direct flight between two other airports.
LAX A D     means that the traveler arrived at and departed from Los Angeles International Airport.
ORD L       means that the traveler had a layover at Chicago O'Hare International Airport, but never began or ended travel at that airport.
```


Each airport should be on a separate line. The order of the A, D, and L does not matter. The file should be submitted via a GitHub pull request, currently to mapcat/airtest (email submissions will be available soon but are not currently supported). Once the file is merged, their map should update automatically within a few minutes. Users can locate their maps by choosing their username from the drop-down menu.

There is only one option for the map currently (show all airports, or only visited airports). More will be added.

Hovering over an airport (or clicking on the icon) will identify it with the name pulled from a list stored in airports.csv.

## Known issues:

* User is not persistent. When loading the map, it will default to the first username in the list.
* After a user's .alist is updated, the browser cache must be cleared manually in order to see the updated map.
* The map uses Leaflet with an Open Street Map basemap. Currently only one iteration of each symbol is shown on the map (i.e. they don't reappear if you pan west or east past the International Date Line).
* Many airports are missing. So far only airports visited by at least one user have been added.
* Airport placement is inconsistent. Some icons are centered on runways, some on terminals, and some at other positions on airport property. Many locations were automatically generated using Copilot.

## Future plans:

* A user page with a list of airports visited will be added eventually.
* A list of users who have visited an airport may also be added.
* Additional basemaps may become available.
* The map currently shows any airports requested by users. This may become difficult to maintain. A decision will need to be reached regarding which airports should be included. Public airports with scheduled commercial flights are the main scope for the project, but "public", "scheduled", and "commercial" may need to be clarified.
* Other information (such as city, state, and/or country) may be added to the data identifying airports.

