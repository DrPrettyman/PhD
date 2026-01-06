# Tropical Cyclones - Investigation

## First inspection

The first thing was to get some slp data from an area where a large
cyclone had occurred. One of the very largest cyclones of recent years
is Hurricane Katrina (USA, 2005). The 1D time series of pressure data
was given the sliding-window ACF lag-1 treatment, which gave a
convincing picture of the ACF rising significantly about two days before
the large drop in pressure occurred (when Katrina passed through the
location), and reaching a peak value just before the drop. This is a
similar picture to over sliding ACF studies of time series, e.g.
(held2004). So that's exciting!\
Well, then I looked at Hurricane Andrew. Andrew formed in the Atlantic
and passed over the Caribbean at it's peak intensity, unlike Katrina
which formed in the Caribbean and was at it's strongest over the
southern USA. Well, Andrew does the opposite to Katrina: the ACF signal
*decreases* significantly over exactly the same time periods that it
*rises* for Katrina. Several other storms have been analysed in the same
way, but none show such obvious increases or decreases as Katrina and
Andrew. All of them are somewhere in between. Some rise, some fall, some
don't really change at all.\
It would be good to separate the Cyclones by type. If several
Andrew-style cyclones (i.e. form in the Atlantic and pass over the
Caribbean) show the same signal, there may be some physical process to
consider.

For this investigation, the HadISD dataset was used. The time series for
the slp data ia taken from a single station, as close as possible to the
center of the cyclone at the point that the cyclone 'makes landfall'.
The **annoying oscillations** were also removed from the slp time
series.

### Amendment: Attempt to classify Cyclones by type

Since most of the cyclones are in different places, it is hard to say
that any two could be considered the same. However, a subset of the
cyclones are Southern USA hurricanes, these are[^1]: Andrew (5), Katrina
(5), Rita (5), Floyd (4), Charley (4), Frances (4) and Jeanne (3).
Ernesto and Bonnie were also considered initially, but these are only
category 1, it is possible that it will be useful to study them later
but for the purposes of classifying cyclones, these two are outliers and
do not fit into a group with the rest.\
Even these seven cyclones have very different behaviour. Katrina and
Rite both started in the Caribbean, reached their peak over the sea,
then landed in Louisiana, it seems that these two may have similar
signatures, therefore. Hurricane Charley progresses very similarly to
Katrina and Rita, but swerves eastward and lands on the west coast of
Florida.\



   Caribbean    Atlantic
  ----------- -------------
    Katrina      Andrew
     Rita         Floyd
    Charley    Frances (?)

Andrew, Floyd, Jeanne and Frances all start very similarly in the
Mid-Atlantic and heading north of Cuba towards Florida. Floyd passes
over Florida, as does Frances although Frances has lost nearly all of
its energy by that time, reaching its peak over the ocean north of Cuba,
and Jeanne is considerably weaker anyway. Floyd is deflected away from
Florida and travels up the east coast, so although the storm affected
Florida, the centre of the storm did not actually "make landfall".\
The rest of the cyclones are in many different parts of the world and
all form in different situations. One further way of differentiating is
according to strength at the time of observation (which can be inferred
directly from the data) and also knowing whether the cyclone it at its
peak at that time, of if it is in decline, if so we would have to think
of a good measure for that criteria: is it classed as "decline" if it
was at peak strength just three seconds before landing? Or only if it
has lost an arbitrary amount of its strength - possibly if it has
dropped to a lower category by the time it lands.\

[^1]: The numbers in parentheses give the category of the storm,
    category 5 being the strongest.
