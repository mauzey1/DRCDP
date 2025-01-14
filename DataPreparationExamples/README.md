# Decision Relevant Climate Data Products (DRCDP)


### Preparing DRCDP data for publication to ESGF

Data specifications have been established for DRCDP datasets that are technically aligned with other ESGF projects including CMIP, CORDEX, and obs4MIPs.  Here, we provide guidance to help data providers make their data compliant with these data specifications.  

Nuts and bolts:

Contributors must register their datasets by submitting an issue on the DRCDP GitHub repository and filling out the provided template.  
We recommend data providers prepare their data using Python so that they can more readily leverage the resources described below
We recommend using Xarray as in the examples provided below, and XCDAT to generate coordinate bounds.    
Use of the Climate Model Output Writer (CMOR) is required to ensure alignment with other ESGF projects.     
Xarray, XCDAT and CMOR can be obtained via conda-forge, a community-led collection of recipes, build infrastructure and distributions for the conda package manager.

How to:  

The recipe below describes the process of preparing a DRCDP-compliant dataset. This typically involves copying information from the provided demo and modifying it as necessary to prepare a new DRCDP-compliant dataset. By preparing a simple python script (example discussed in demo identified below) and an input JSON file, CMOR is used to prepare an DRCDP-compliant dataset.
Recipe
Register a new source_id, if it does not already exist.  An issue can be submitted on this GitHub repo with a proposed "source_id" and other key registered content (RC). Somebody will quickly review this information and enter it into the database of source_id's or propose an alternative if it does not conform to the data specifications for the source_id. When opening an issue, a template is provided, so one needs to replace the information in the example (GPCP) with their own proposed source_id. The source_id is intended to identify the product/version and generally closely resembles an existing identifier but may be slightly modified to be consistent with CMIP/obs4MIPs conventions. For example: A compliant source_id for "GPCP 2.4" is "GPCP-2-4". More information on the guidelines for constructing a source_id is available in Table 1 of the obs4MIPs data specifications. 

Prepare input table for running CMOR. An example input table. The simplest thing to do is to save this file, rename it, and replace the demo content with the relevant information for a new source_id or dataset. Typically, this involves only making changes to the following attributes: "contact", "grid", "grid_label", "institution_id", "nominal_resolution", "references", "outpath", "source_id", "title", "variant_info" and "variant_label". We strive for all obs4MIPs products to clearly identify the origins of the data (i.e., where and when did the person preparing the obs4MIPs compliant product obtain the original data). This information can be documented in the last three attributes of the example input table identified above via the following attributes: "originData_URL" , "originData_retrieved", and "originData_notes".


Prepare python script for reading in data and writing with CMOR. This is often the most time consuming aspect of preparing an DRCDP-compliant dataset, but the examples provided on this repo are helping streamline the process. It involves preparing a simple Python script to read the original data and rewrite it using CMOR.  As with the steps before, one can start by downloading a demo python script, renaming it accordingly, and modifying as needed. An example Input table (json) and script using CDAT and CMOR (python)


Process data by executing script. The processed data will be located in a directory defined in the input_table: outpath + output_path_template, the former being the base directory (where the user wants to output the data). The latter being a directory template explicitly defined for DRCDP (<activity_id>/<institution_id>/<source_id>//<variable_id>/<grid_label>/).




  

