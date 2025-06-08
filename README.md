# odoo-truck-trailer-weight-distribution
# Odoo 18: Truck and Trailer Package Weight Distribution Module

This Odoo 18 module was developed as a solution to a technical assessment task. The goal is to provide functionality on the Sales Quotation form to help users evenly distribute package weights between a truck and a trailer.

## Problem Statement

The user needs to transport heavy packages using a truck and a trailer. To ensure optimal load balancing and vehicle handling, the system should assist in distributing packages such_that:

1.  Packages are loaded in a fixed, entered order.
2.  The system first attempts a **direct split** of the package list into two sub-lists (truck and trailer) with equal total weights.
3.  If a direct split isn't possible, the system attempts to find a **pivot package**. This package is considered "between" the truck and trailer, and the sum of weights of packages *before* the pivot (truck) should equal the sum of weights of packages *after* the pivot (trailer).
4.  If neither method yields an even distribution, it's marked as "Not possible."

## Features Implemented

*   Adds a new tab "Kamion s prikolicom" (Truck and trailer) to the Odoo Sales Order (Quotation) form.
*   Provides an input field `Težine paketa` (Package weights) where users enter a comma-separated string of natural numbers (package weights).
*   Automatically computes and displays the package distribution in two fields:
    *   `Kamion` (Truck): Shows the list of packages for the truck.
    *   `Prikolica` (Trailer): Shows the list of packages for the trailer.
*   Displays "Nije moguće" (Not possible) if an even distribution according to the rules cannot be achieved.
*   The calculation respects the fixed order of packages as entered.

## Technical Details

*   **Odoo Version:** 18.0
*   **Module Name:** `uvid_sale_weight_distribution` (as provided in the template)
*   **Core Logic:** Implemented in `models/sale_order.py` by extending the `sale.order` model and adding a compute method `_compute_weight_distribution` triggered by changes to the package weights input.
*   **View Modification:** The new tab and fields are added to the `sale.view_order_form` using an inherited XML view defined in `views/sale_order_views.xml`.

## Setup & Testing Environment

*   The module was developed and tested on Ubuntu 24.04.
*   PostgreSQL was used as the database.
*   Standard Odoo 18 installation procedures were followed.
