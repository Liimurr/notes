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

      .. code-block:: bash

         ssh-keygen -t ed25519 -C "your_email@example.com"

   2. Add Public SSH Key to Github Account

Procedure
---------

.. dropdown:: Add-Private SSH Key to Repository Secrets
   :open:

   1. Goto **Settings** \| **Secrets and Variables** \| **Actions** \| **New Repository Secret**
   2. Add-Private SSH Key

.. dropdown:: Add-SSH Key to 'checkout' Github Action
   :open:

   .. code-block:: yaml
      :emphasize-lines: 7-8

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

- https://maxschmitt.me/posts/github-actions-ssh-key
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key