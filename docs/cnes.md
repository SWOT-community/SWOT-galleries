# Swot Ocean Data Tutorials


```{admonition} Gallery Versions & Changelog
:class: dropdown tip

Current version: {{ oceanography_latest_badge  }}

Download a release:

{{ oceanography_downloads }}

📄 [Changelog](#changelog)
```

## Support

```{button-link} mailto:aviso-swot@altimetry.fr
:color: primary
:outline:

📧 aviso-swot@altimetry.fr
```

## Access to data

````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} Search Swot
:link: SWOT-Oceanography/ex_altimetry_search
:link-type: doc
:img-top: _static/images/oceanography/ex_altimetry_search.png
```

```{grid-item-card} Download and read Swot from AVISO
:link: SWOT-Oceanography/ex_aviso_download_swot
:link-type: doc
:img-top: _static/images/oceanography/aviso.png
```

````

```{toctree}
:hidden:

SWOT-Oceanography/ex_search_swot
SWOT-Oceanography/ex_aviso_download_swot
```

---
## Extracting regions of interest


````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} 2-km data
:link: SWOT-Oceanography/ex_roi_extraction
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_roi_extraction.png
```

```{grid-item-card} L3 250-m data
:link: SWOT-Oceanography/ex_subset_swot_l3_unsmoothed_aviso_tds
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_subset_swot_l3_unsmoothed_aviso_tds.png
```

```{grid-item-card} L2 250-m data
:link: SWOT-Oceanography/ex_subset_swot_l2_unsmoothed_aviso_tds
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_subset_swot_l2_unsmoothed_aviso_tds.png
```

````

```{toctree}
:hidden:

SWOT-Oceanography/ex_roi_extraction
SWOT-Oceanography/ex_subset_swot_l3_unsmoothed_aviso_tds
SWOT-Oceanography/ex_subset_swot_l2_unsmoothed_aviso_tds
```

---
## 2-km data

````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} SWOT L2 KaRIn LR Ocean Data Products
:link: SWOT-Oceanography/ex_swot_l2_basic_startup
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_swot_l2_basic_startup.png
```

```{grid-item-card} SWOT L3 KaRIn and Nadir Ocean Data Products
:link: SWOT-Oceanography/ex_swot_l3_startup
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_swot_l3_startup.png
```
````

```{toctree}
:hidden:

SWOT-Oceanography/ex_swot_l2_basic_startup
SWOT-Oceanography/ex_swot_l3_startup
```

---

## 250-m data

````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} Discover Swot L3 Unsmoothed data, and compare with CMEMS L4 SLA and IFREMER SST data
:link: SWOT-Oceanography/ex_swot_l3_unsmoothed
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_swot_l3_unsmoothed.png
```

```{grid-item-card} Sea Ice Classification and local Leads/floes PDF analysis
:link: SWOT-Oceanography/ex_sea_ice_classification
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_sea_ice_classification.png
```
````

```{toctree}
:hidden:

SWOT-Oceanography/ex_swot_l3_unsmoothed
SWOT-Oceanography/ex_sea_ice_classification
```

---

## Wind Wave data

````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} SWOT L3 KaRIn Wind Wave Data Products
:link: SWOT-Oceanography/ex_swot_l3_lr_ww_startup
:link-type: doc
:img-top: _static/images/oceanography/_thumbs/ex_swot_l3_lr_ww_startup.png
```
````

```{toctree}
:hidden:

SWOT-Oceanography/ex_swot_l3_lr_ww_startup
```

```{image} aviso.png
:class: hidden
```


---

## Podaac Notebooks


````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} Download and Access L2 SWOT Oceanography Data
:link: SWOT-Oceanography/ex_Localmachine_SWOT_L2_Ocean_podaac
:link-type: doc
:img-top: _static/images/oceanography/podaac.png
```

```{grid-item-card} Access SWOT L2 Oceanography Data in AWS Cloud
:link: SWOT-Oceanography/ex_AWS_Cloud_SWOT_L2_Ocean_podaac
:link-type: doc
:img-top: _static/images/oceanography/podaac.png
```

```{grid-item-card} SWOT Quality Flag Demonstration
:link: SWOT-Oceanography/ex_SWOT_quality_flag_demo
:link-type: doc
:img-top: _static/images/oceanography/podaac.png
```
````

```{toctree}
:hidden:

SWOT-Oceanography/ex_swot_l3_lr_ww_startup
```


```{include} SWOT-Oceanography/changelog.md