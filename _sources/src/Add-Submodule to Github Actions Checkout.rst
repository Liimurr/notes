Add-Submodule to Github Actions Checkout  
========================================

Brief
-----
1. Register-SSH Key with Github Account
2. Add-Private SSH Key to Repository Secrets
3. Add-SSH Key to 'checkout' Github Action
 

Prerequisites
-------------
.. dropdown:: Register-SSH Key with Github Account
   :open:

   1. 

      .. code-block:: shell
         :caption: shell / cmd

         ssh-keygen -t ed25519 -C "your_email@example.com"

   2. Add Public SSH Key to Github Account

Procedure
---------
.. dropdown:: Add-Private SSH Key to Repository Secrets
   :open:

   Goto **Settings** \| **Secrets and Variables** \| **Actions** \| **New Repository Secret**

   .. card::

      .. list-table:: 
   
         * - **Name**
           - SSH_KEY
         * - **Value**
           - <private ssh key>


.. dropdown:: Add-SSH Key and Submodules to 'checkout' Github Action
   :open:

   .. code-block:: yaml
      :emphasize-lines: 7-8
      :caption: .github/workflows/<your github workflow>.yml

      jobs:
         docs:
            runs-on: ubuntu-latest
            steps:
               - uses: actions/checkout@v3
               with:
                  submodules: true
                  ssh-key: ${{ secrets.SSH_KEY }}

See Also
--------
.. card::

   **External Links**
   
   - https://maxschmitt.me/posts/github-actions-ssh-key
   - https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key