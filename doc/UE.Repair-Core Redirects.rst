UE.Repair-Core Redirects
========================

Use the following steps to repair core redirects in the project.

Prerequisites
-------------
Create an editor utility blueprint widget that performs the following:

1. Rename all assets to a new name with a hash appended (this will force the editor to update the asset core redirect references within the asset -- the hash will make looking for deprecated assets easier in case the editor fails to update some asset references)
2. Rename all the assets back to their original name.

Procedure
---------
1. Refresh all assets
   
   1. FIRST Refresh all instanced (non-blueprint) assets. (refreshing blueprint nodes before instanced assets can cause blueprint node corruption)

      run the renaming widget utility on all non blueprint assets (most notably: DataAssets and Blueprint Structs)

   2. THEN Refresh all blueprint nodes using ``RefeshAllNodes`` plugin (this works on Blueprints only)

2. Find all in0stanced assets that failed to update (Some assets may need a second try, or even an editor restart and another try)

   1. Search Everywhere In VSCode

      i. Open the project directory in vscode
      ii. Search everywhere (``Ctrl+Shift+F``) for the hash appended to the asset name
      iii. Files to include: ``*.uasset, *.umap, *.cpp, *.h, *.inl, *.cs, *.hpp, *.cxx, *.c, *.ini, *.txt``

   2. Search Everywhere In Blueprint editor

      i. In the editor, select `Windows > Find in Blueprints`
      ii. Search for the hash appended to the asset name

3. Re-run the editor utility blueprint widget to repair the assets that failed to update or rename them manually

Tips & Caveats
--------------

Row Structs
+++++++++++
Core redirects cannot replace row structs used by data tables automatically. This may have been fixed in 5.1 (see: `UE 5.1 Release Notes <https://docs.unrealengine.com/5.1/en-US/unreal-engine-5.1-release-notes/>`_) "Added support for redirecting DataTable row structs in the DataRegistry"). 
Use the following steps to manually repair row structs:

1. Export data tables that use the row struct to a CSV
2. Create new data tables with the new struct (make sure the new struct inherits from FTableRowBase if it's a c++ USTRUCT)
3. Import the orignal data tables' CSVs into the new data tables
4. Use a Package & Struct redirect for the old data table to the new data table (note the redirect example below assumes you are moving from a blueprint struct to a c++ struct (``/Game/`` = blueprints and ``/Script/`` = c++)

   .. code-block:: ini
      :caption: DefaultEngine.ini

      [CoreRedirects]
      +PackageRedirects=(OldName="/Game/<Module>.<OldDataTableName>", NewName="/Game/<Module>.<NewDataTableName>")
      ; Struct redirect for DataTableRows will not work. (might work in UE-5.1)
      ;+StructRedirects=(OldName="/Game/<Module>.<OldRowStructName>", NewName="/Script/<Module>.<NewRowStructName>")

5. Manually replace any remaining references to the old data tables and row struct in blueprints 

   - tip: Right click Blueprint Assets that reference the old row struct and select `Scripted Actions > Replace Structure`
   - tip: Right click Blueprint Struct, and Data Table assets and select `Reference Viewer` to find all in editor references
   - tip: In the IDE search for the old data table name to find source code references

Undo Changes With Git
+++++++++++++++++++++
Because this process involves changes to many assets (Refresh all nodes can affect hundreds of files), you will be more likely to need to undo changes by directory or by pattern rather than individual files.
For example, to undo all unstaged changes in the Content folder, but exclude uassets prefixed with `DT_WP_` you would run the following:

   .. code-block:: bash

      git restore -- 'Content/' ':(exclude)**/DT_WP_*.uasset'

See (`git's pathspec and how to use it <https://css-tricks.com/git-pathspecs-and-how-to-use-them/>`_) for more information on using pathspec patterns with git commands.

See Also
--------
.. card::

   **External Links**
   
   `UE4 Docs/Core Redirects <https://docs.unrealengine.com/4.26/en-US/ProgrammingAndScripting/ProgrammingWithCPP/Assets/CoreRedirects/>`_