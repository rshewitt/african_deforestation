import json 
from pathlib import Path
import os 
import subprocess

import helpers 

""" 
Notes
    # https://www.google.com/maps/place/Sodwana+Bay/@-27.5416154,32.6659469,3867m/data=!3m1!1e3!4m5!3m4!1s0x1efb37a20dd173c5:0xa507090f7301e453!8m2!3d-27.539823!4d32.6782506 
    # https://apihub.copernicus.eu/apihub/ 
    # https://scihub.copernicus.eu/twiki/do/view/SciHubWebPortal/APIHubDescription 

Raster formulas:
    NDVI:
        formula: ( NIR - RED ) / ( NIR + RED ) 
        values:
            - NDVI defines values ​​from -1.0 to 1.0, where negative values ​​are mainly formed from clouds, water and snow, and values ​​close to zero are primarily formed from rocks and bare soil.
            - Very small values ​​(0.1 or less) of the NDVI function correspond to empty areas of rocks, sand or snow.
            - Moderate values ​​(from 0.2 to 0.3) represent shrubs and meadows, while large values ​​(from 0.6 to 0.8) indicate temperate and tropical forests.

    https://eos.com/make-an-analysis/ndvi/

General notes:
    - Had to chmod -R 700 for dhusget.sh ( needed to add execution )
    - ls -l lists the contents of the current directory and the associated users permissions
    
"""

CURRENT_DIR = os.path.dirname( __file__ ) 
CREDENTIALS = helpers.json_2_dict( os.path.join( str( Path( CURRENT_DIR ).parents[0] ), "config", "env.json" ) )

class ImageProcessor:

    def __init__( self, cop_credentials ):

        self.cop_credentials = cop_credentials
        self.cop_user        = self.cop_credentials["cop_user"] 
        self.cop_pass        = self.cop_credentials["cop_pass"] 
        
        return 
    
    def download_s2( self ):

        # "cop_user": "rhewitt916",
        # "cop_pass": "9X4$nzC6pr7V$nA"
        # wget --no-check-certificate --user=rhewitt916 --password=DogCatWater1986! --output-document=../results/query_results.txt "https://scihub.copernicus.eu/dhus/search?q=*&rows=25"
        # ./scripts/dhusget.sh -u rhewitt916 -p DogCatWater1986! -m Sentinel-2 -c 32.10700,-28.48580:32.94640,-26.85790 -S 2016-12-01T06:00:00.000Z -E 2017-01-31T06:00:00.000Z -O ../images -o all

        # ll = 32.10700,-28.48580:32.94640,-26.85790 

        # NDVI = (NIR-RED)/(NIR+RED)

        return 
    
    def download_landsat( self ):
        return 
        