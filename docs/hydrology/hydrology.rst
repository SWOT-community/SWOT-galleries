SWOT Hydrology Data Tutorials
====================================

Here are Hydrology-relevant tutorials and resources for the Surface Water and Ocean Topography (SWOT) Mission, using cloud computing or via local machine.

.. warning::

  Those depict the most simple and commonly used methods to our knowledge to get a hand on SWOT HR products. 
  Should you have other methods or tools, please share!

.. toctree::
  :caption: Tutorials for
  :maxdepth: 3

  basic
  intermediate
  expert
  

-------------
Data Portals
-------------
.. |hnext| image:: ../_static/hydroweb_next_1024px.png
  :width: 30%
.. |podaac| image:: ../_static/podaac.png
  :width: 15%

|hnext|                  |podaac|

All SWOT Hydrology data illustrated in these tutorials can be accessed via 

* `PO.DAAC Earthdata <https://search.earthdata.nasa.gov/search?portal=podaac-cloud>`_: search for, visualize and download all SWOT products vie intereactive GUI developped by NASA and PO.DAAC, earthdata
* `hydroweb.next <https://hydroweb.next.theia-land.fr/>`_: Search for, visualize, and download SWOT Hydrology products via interactive GUI developed by CNES and Theia, hydroweb.next



-----------------------
Other useful tools
-----------------------

* `Hydrocron <https://podaac.github.io/hydrocron/intro.html>`_: An API that repackages the river shapefile dataset (L2_HR_RiverSP) into csv or GeoJSON formats that make time-series analysis easier.
* `SWODLR <https://github.com/podaac/swodlr>`_: A system for generating on demand raster products from SWOT L2 raster data with custom resolutions, projections, and extents. -in development
* `SWOT hydrology toolbox <https://github.com/CNES/swot-hydrology-toolbox>`_: Together with RiverObs, open-source tools that enable end-users to generate virtually all SWOT HR level-2 (L2) products with fairly (but not fully) representative characteristics (see section on caveats below) 
* `SWOT RiverObs tool <https://github.com/SWOTAlgorithms/RiverObs.git>`_: Together with SWOT Hydrology Toolbox, open-source tools that enable end-users to generate virtually all SWOT HR level-2 (L2) products with fairly (but not fully) representative characteristics (see section on caveats below) 

-------------------
A Priori Databases 
-------------------

* `SWOT River Database (SWORD) <https://www.swordexplorer.com/>`_: the database for rivers SWOT products are based upon, great for discovering river reach IDs!. The dataset is also available in `hydroweb.next <https://hydroweb.next.theia-land.fr/?pid=SWOT_PRIOR_RIVER_DATABASE>`_ 
* `Prior Lake Database (PLD) <https://hydroweb.next.theia-land.fr/?pid=SWOT_PRIOR_LAKE_DATABASE>`_: 
    * Add the PLD layer into hydroweb.next to see the lakes SWOT products are based upon, great for discovering lake IDs!
    * Ask for PLD updates in the page :ref:`pld-label`

---------------------
Products Description
---------------------
* `SWOT Data User Handbook <https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/D-109532_SWOT_UserHandbook_20240502.pdf?_ga=2.124259722.1042075570.1716930479-1354658737.1715875596>`_ is your first document
* `Product Description Documents <https://podaac.jpl.nasa.gov/SWOT?tab=datasets-information>`_: find more detailed information in this table!
* `Latest Release Notes - Version C KaRIn Science Data Products <https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/releases/SWOT_VersionC_KaRIn_Products_Release_Note.pdf>`_: See section 6 for current issues and features of the datasets!

---------------------
Additional Resources
---------------------
* `PO.DAAC Cookbook: SWOT Chapter <https://podaac.github.io/tutorials/quarto_text/SWOT.html>`_: Visit for more data resources, tips, and tutorials related to both the hydrology and oceanography SWOT communities.
* `GIS SWOT StoryMap <https://storymaps.arcgis.com/stories/4a9184e813e540248040069580f6a54c>`_

-----------------------------------------------------
Features of KaRIn Data that Users Should be Aware of
-----------------------------------------------------

* `Slide Deck Presented at the SWOT Science Team by Curtis Chen <https://swotst.aviso.altimetry.fr/fileadmin/user_upload/SWOTST2023/20230919_3_Karin_overview2/14h10-KaRInFeatures.pdf>`_: Addresses practical aspects of interpreting SWOT KaRIn data products, answers frequently asked questions, and provides tips to hopefully avoid misinterpretation and confusion of the data.

------------------
Earthdata Webinar
------------------
* `Accessing Data for the World's Water with SWOT <https://www.earthdata.nasa.gov/learn/webinars-and-tutorials/webinar-podaac-2024-03-20>`_: Watch the Recording! Learn how to discover, access, and use SWOT mission data from PO.DAAC and how these data can lead to new, innovative science and applications in the world of water.

-----------------------------------------
2024 SWOT Hydrology Data Access Workshop
-----------------------------------------

`https://podaac.github.io/2024-SWOT-Hydro-Workshop/ <https://podaac.github.io/2024-SWOT-Hydro-Workshop/>`_



