# Exploring a real world api

Check the following commit:

```
commit ca5a22558731668cb5db875c423acee1060718b3
Date:   Tue Oct 26 19:08:11 2021 +0300

    train departure board starting point
```

Tips: 

* The MBTA shows information for subway, busses, etc in addition to trains (use `filter[route_type]` with value of `2` to show only trains)
* Data from requests can be accessed just by asking for it - adding `include` with value `trip,schedule` would also return `trip` and `schedule` objects without creating additional requests
