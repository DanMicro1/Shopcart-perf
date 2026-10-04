import pytest

PRODUCTS = [f"SKU-{i:04d}" for i in range(2000)]
CART = [f"sku-{i % 750:04d} " for i in range(1000)]


def normalize_skus(skus):
    return [s.strip().upper() for s in skus]


def find_duplicates(skus):
    seen = set()
    dupes = set()
    for s in skus:
        if s in seen:
            dupes.add(s)
        else:
            seen.add(s)
    return dupes


def cart_total(skus):
    return sum(int(s[4:]) for s in skus)


def checkout(skus):
    clean = normalize_skus(skus)
    dupes = find_duplicates(clean)
    total = cart_total(clean)
    return total, len(dupes)


def search_products(term):
    return [p for p in PRODUCTS if term in p]


def format_receipt(skus):
    return "\n".join(f"{s}: 1" for s in skus[:200])


@pytest.mark.benchmark
def test_checkout():
    total, dupes = checkout(CART)
    assert dupes == 250


@pytest.mark.benchmark
def test_search_products():
    assert len(search_products("SKU-01")) == 100


@pytest.mark.benchmark
def test_format_receipt():
    assert format_receipt(CART).count("\n") == 199
