# Using Real Estate Data and Satellite Imagery to Identify Slums
space for summary

# Modeling
## Real Estate Data
### Choosing cities

### Scraping Real Estate Data

### Example Real Estate Listing
![](https://git.generalassemb.ly/ZacharyJamesHill/slum_identification_for_New_Light_Technologies/blob/master/images/zapimoveis-sample.jpg)
### Utilizing Existing Slum Maps
Most publically available maps of slums do not include coordinate data. To provide a classification on our real estate data we had to translate the pixel coordinates to latitude and longitude. This was accomplished by taking two reference points at the origin of the map's coordinates and the edge of the map's coordinates. The reference points were used to provide conversion factors between pixel distance and real world distance. A final function was devised using the conversion factorts that takes in latitude and longitude and outputs a boolean representing whether or not the location is in a slum.
### Using Slum Maps Demo
![](https://git.generalassemb.ly/ZacharyJamesHill/slum_identification_for_New_Light_Technologies/blob/master/images/slum_map_demo.png)
## Satellite Data
### Choosing Which Satellite Imagery Service to Use
Many satellite imagery api's were considered for the data aquisition, however high resolution satelite data is not available for free on these services. Ultimately screenshots of google earth were used.
### Labeling Satellite Data
The slum maps that were used in the real estate data were also used to guide image labelling. Labelling was done manually ans simultaneous to data collection.
### Processing Images for Classification
Images were scaled to uniform size and then split into 400 equal parts.
### Image Classification
Images were classifed using keras's mobelnet v2 implementation.
### Example Non Slum Image
![](https://git.generalassemb.ly/ZacharyJamesHill/slum_identification_for_New_Light_Technologies/blob/master/images/example_non_slum.png)
### Example Slum Image
![](https://git.generalassemb.ly/ZacharyJamesHill/slum_identification_for_New_Light_Technologies/blob/master/images/example_slum.png)
# Running Our Models

## Image Classifier
1. Place images in satellite_models/place_images_here.
2. Run image_preproccesor.py.
3. Run image_classifier.py.
## Real Estate Data Classifier
