UE.Repair-Core Redirects
========================

Use the following steps to repair core redirects in the project.

Prerequisites
-------------
Create an editor utility blueprint widget that performs the following:

1. Rename all blueprint structs to a new name with a hash appended
2. Rename all blueprint structs back to their original name
3. Rename all data assets to a new name with a hash appended
4. Rename all data assets back to their original name

Procedure
---------
1. Refresh all assets
   
   1. Refresh all blueprint nodes using ``RefeshAllNodes``
   2. Refresh all non blueprint assets -- run the renaming widget utility on all non blueprint assets (DataAssets, Blueprint Structs)

2. Find all non-blueprint assets that failed to update (Some assets may need a second try, or even an editor restart and another try)

   1. Search Everywhere In VSCode

      i. Open the project directory in vscode
      ii. Search everywhere (``Ctrl+Shift+F``) for the hash appended to the asset name
      iii. Files to include: ``*.uasset, *.umap, *.cpp, *.h, *.inl, *.cs, *.hpp, *.cxx, *.c, *.ini, *.txt``

   2. Search Everywhere In Blueprint editor

      i. In the editor, select `Windows > Find in Blueprints`
      ii. Search for the hash appended to the asset name

3. Re-run the editor utility blueprint widget to repair the assets that failed to update or rename them manually

Caveats
-------

Row Structs
+++++++++++
Core redirects cannot replace row structs used by data tables. This may have been fixed in 5.1 (see: `UE 5.1 Release Notes <https://docs.unrealengine.com/5.1/en-US/unreal-engine-5.1-release-notes/>`_) "Added support for redirecting DataTable row structs in the DataRegistry"). 
Use the following steps to manually repair row structs:

1. Export data tables that use the row struct to a CSV
2. Create new data tables with the new struct
3. Import the orignal data tables' CSVs into the new data tables
4. Replace any references to the old data tables and row struct in blueprints 

   - tip: Right click the blueprint asset that references the old row struct and select `Scripted Actions > Replace Structure`
   - tip: Right click the Struct and Data Table assets and select `Reference Viewer` to find all in editor references
   - tip: In the IDE search for the old data table name to find source code references
   
5. Deleting the data table, creating a new data table with the new struct, re-importing the CSV

See Also
--------
.. card::

   **External Links**
   
   https://docs.unrealengine.com/4.26/en-US/ProgrammingAndScripting/ProgrammingWithCPP/Assets/CoreRedirects/