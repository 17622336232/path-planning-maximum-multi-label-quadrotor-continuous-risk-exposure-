# Exposure time calculator

This small Python example computes two quantities from a route's timeline: the total time inside a marked region and the longest single visit. It accompanies [the project's original technical note](https://github.com/17622336232/path-planning-maximum-continuous-risk-exposure-multi-label).

Run `python3 exposure.py` with Python 3. No packages are required. Each input pair contains the duration in seconds and a Boolean indicating whether the vehicle is inside the region.

| Route | Segments | Total inside | Longest visit |
| --- | --- | ---: | ---: |
| A | 4 seconds inside | 4 s | 4 s |
| B | 2 seconds inside, 1 second outside, 2 seconds inside | 4 s | 2 s |

The outside second in route B ends its first visit. A new visit starts on re-entry. Splitting an inside segment into smaller consecutive samples does not start a new visit.
