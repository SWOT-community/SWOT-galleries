# Ocean Tools

Below is a collection of useful tools for working with satellite altimetry and oceanographic data. Each card links to the tool’s repository and documentation when available.

````{grid} 1 1 3 4
:gutter: 2

```{grid-item-card} Altimetry Downloader Aviso
:link: https://cnes.github.io/altimetry-downloader-aviso/
:link-type: url
:img-top: _static/images/cnes_aviso.png

Python tool to simplify downloading datasets from the CNES Aviso data center. Provides command-line utilities and Python interfaces to automate altimetry data acquisition.
```

```{grid-item-card} Altimetry-io
:link: https://github.com/CNES/altimetry-io
:link-type: repo
:img-top: _static/images/cnes_aviso.png

Python library for reading and handling satellite altimetry datasets, including NetCDF products, variables, and metadata.
Relies on **FCollections** to efficiently manage and read NetCDF datasets.
```

```{grid-item-card} FCollections
:link: https://cnes.github.io/fcollections/
:link-type: url
:img-top: _static/images/cnes_aviso.png

Lightweight Python library for managing collections of files and datasets. Provides abstractions for structured data pipelines and metadata handling.
```

```{grid-item-card} Altimetry Search
:link: https://github.com/CNES/altimetry-search
:link-type: url
:img-top: _static/images/cnes_aviso.png

Interactive tool for altimetry missions passes search - available on Binder and as a Python library.
```