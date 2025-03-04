=====================================================
How to update the Prior Lake Database 
=====================================================
If you need some to ask for updates of SWOT PLD, please send us the informations detailed in the sections below.
We will do our best to integrate modifications as soon as possible.

 

Remove an erroneous lake
=================

Provide us with
 * the lake_id of the “false” lake that you want us to remove
 * a description of what you have observed.
 * some evidence that the feature is not a lake if possible (for instance a georeferenced optical image).

Add a new lake
=================
To add a new lake or update an existing lake, you must provide us with a shapefile with updated geometry and information (  :download:`click to download the shapefile template to use <proposal_to_update_pld.zip>`).

Note that you must meet the following fields requirements.

*geometry*
  it should be a single polygon in geographical coordinates WGS 84 (EPSG:4326)

*pld_versio (string)*
  indicate the PLD version you want to update

*lake_id (string)*
    - should be empty in case you add a new lake
    - should be set to the current lake_id of the lake in the PLD if the updated lake intersects a single PLD lake 
    - should indicated all  the PLD lakes intersected: lake_id=”lake_id1;lake_id_2;lake_id3” if the updated lake intersects several PLD lakes 
*ref_area (real)*
  provide the area of the lake in km2 at the highest water level (except for rare flooding situations) if possible
*ref_wse (real)*
  indicate the water surface elevation in meters above the geoid EGM2008 of the lake at the highest water level (except for rare floods), corresponding to ref_area, if possible.
*names (string)*
  the name of lake if available
  
Contact
=================
Please send you request and files to Claire Pottier (CNES)
