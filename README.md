
# Campus Canteen Pre-Order System: Order Module + CI (Task 5)

`calculate_total(subtotal)` in `order.py` returns the payable amount:

1. 10% discount if subtotal is **above** Rs. 300
2. 5% GST on the discounted amount
3. Rounded to 2 decimals

Tests are in `test_order.py`. CI is in `.github/workflows/ci.yml` and runs `pytest` on every push.

## Run locally

    pip install -r requirements.txt
    pytest -v

## Getting the two screenshots (failing + passing run)

1. Create a GitHub repo, then push this folder:

       git init
       git add .
       git commit -m "Add calculate_total with tests and CI"
       git branch -M main
       git remote add origin https://github.com/<your-username>/<repo>.git
       git push -u origin main

   The first run goes green. Screenshot it from the **Actions** tab (**passing run**).

2. In `order.py`, break it on purpose: change `DISCOUNT_THRESHOLD = 300` to `200`.
   Commit and push:

       git commit -am "Break threshold to demo failing CI"
       git push

   `test_exactly_300_gets_no_discount` fails and the run goes red. Screenshot it, open the run and
   show the failing test output (**failing run**).

3. Revert the change, commit, push. The run goes green again.
=======
# canteen-order-ci

