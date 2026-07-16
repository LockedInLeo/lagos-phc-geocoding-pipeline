# Lagos PHC Geocoding Project

## Objective

Build a reproducible geocoding pipeline for Primary Health Centres (PHCs) in Lagos State using Google Places API and Google Geocoding API.

---

## Workflow

1. Scrape PHC list
2. Clean data
3. Standardize addresses
4. Search Google Places
5. Fall back to Google Geocoding
6. Store:
   - Coordinates
   - Google Address
   - Place ID
   - Geocoding Method

I initially relied on the Google Geocoding API, but testing showed that many PHCs were registered as named places. I redesigned the pipeline to query the Google Places API first, using facility names and LGAs, and only fell back to address geocoding when no place match was found. This improved the robustness of the workflow while preserving the original source data.