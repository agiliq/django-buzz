#con job for fetching the friend feed for every 10 minutes

#! /usr/bin/env python

from doloto.pystories.services.EntryService import FetchManager

fmanager = FetchManager()
fmanager.triggerfetchFeed()