# What is the point of a model?

# What to do?

We must look at many hurricanes to look for patterns effectively. Then
use the noise coefs and the rest of it to make a model. This is if the
noise coefs agree with each other (roughly). If all the hurricanes look
very very different then we ought to give up hope.

# Tropical Cyclones

I have been looking at Wikipedia's "List of the most intense tropical
cyclones" for some clues. There are many cyclones on the list whose
entire lifetime was spent out at sea. Since this met office HadISD data
I've been using only has land-based stations, these are no good. For the
rest of the cyclones I have used the data from the weather station
closest to where the storm 'made landfall' - as they say. Obviously, if
I find that I don't have enough data to be useful I may have to find
some different data sets so I can have a look at these ocean-only
storms. Maybe it's a good idea to get all your data from the same
source, maybe that's a naive thing to say. I don't know. Anyway, as it
is I have pressure data for 18 cyclones (at the station closest to
Landfall) taken from the HadISD dataset:

1.  Andrew: 24-Aug-1992 09:00:00

2.  Floyd: 14-Sep-1999 23:00:00

3.  Charley: 06-Aug-2004 21:00:00

4.  Frances: 05-Sep-2004 06:00:00

5.  Jeanne: 26-Sep-2004 04:00:00

6.  Katrina: 25-Aug-2005 23:00:00

7.  Rita: 20-Sep-2005 09:00:00

8.  Ernesto: 30-Aug-2006 12:00:00

9.  Bonnie: 31-Jul-2010 22:00:00

10. Kenna: 25-Oct-2002 12:00:00

11. Haiyan: 07-Nov-2013 18:00:00

12. Zeb: 14-Oct-1998 12:00:00

13. Megi: 18-Oct-2010 06:00:00

14. Hudhud: 12-Oct-2014 03:00:00

15. Mitch: 27-Oct-1998 14:00:00

16. Flo: 19-Sep-1990 09:00:00

17. Opal: 04-Oct-1995 19:00:00

18. Monica: 23-Apr-2006 06:00:00

Unfortunately even some of these are no good, we are left with about ten
if you select only the ones which are complete data and have a 'strong'
signal (depending on the definition of strong. So now the next step is
to do some statistics on these 10 and see if there is some pattern.\
As Valerie says, it would be surprising if there were no pattern at all
(i.e. if some had rising colour/acf/dfa/etc. and others had falling, or
if all were different) because after all, they are all tropical cyclones
hitting a land mass from the ocean. You would expect that in some area
they would show a similar set of statistics.
