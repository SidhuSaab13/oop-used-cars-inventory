from __future__ import annotations
from typing import List, Tuple, Optional
import csv, re
from car import Car

MAP = {
    "manufacturer": ["manufacturer", "make", "brand"],
    "model": ["model"],
    "year": ["year", "model_year"],
    "mileage": ["mileage", "odometer", "miles"],
    "engine": ["engine"],
    "transmission": ["transmission", "gearbox"],
    "drivetrain": ["drivetrain", "drive", "drive_type"],
    "mpg": ["mpg", "combined_mpg", "fuel_economy"],
    "exterior_color": ["exterior_color", "exterior", "color"],
    "interior_color": ["interior_color", "interior"],
    "accident": ["accident", "has_accident", "accidents", "damage", "salvage"],
    "price": ["price", "sellingprice", "sale_price"],
    "seller_name": ["seller", "seller_name", "dealer", "dealer_name"]
}

def _find_col(row_keys, options):
    """Return the first existing column name from `options` (case-insensitive)."""
    lower_keys = {k.lower(): k for k in row_keys}
    for opt in options:
        if opt.lower() in lower_keys:
            return lower_keys[opt.lower()]
    return None

def _to_bool(v) -> bool:
    if v is None:
        return False
    s = str(v).strip().lower()
    return s in {"true", "1", "yes", "y"}

def _to_float(v, default=None):
    if v is None or v == "":
        return default
    try:
        return float(v)
    except:
        m = re.search(r"(-?\d+(\.\d+)?)", str(v))
        if m:
            try:
                return float(m.group(1))
            except:
                pass
    return default

def load_cars_from_csv(path: str) -> Tuple[List[Car], Optional[List[str]]]:
    cars: List[Car] = []
    seller_names: Optional[List[str]] = None
    row_errors: List[str] = []

    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames or []
        if not headers:
            return cars, None

        col_map = {}
        for key, options in MAP.items():
            col = _find_col(headers, options)
            if col:
                col_map[key] = col

        required_fields = [
            "manufacturer", "model", "year", "mileage",
            "engine", "transmission", "drivetrain",
            "exterior_color", "interior_color", "accident", "price"
        ]
        for field in required_fields:
            if field not in col_map:
                pass

        if "seller_name" in col_map:
            seller_names = []

        for i, row in enumerate(reader, start=2):  
            try:
                manufacturer = (row.get(col_map.get("manufacturer", ""), "") or "Unknown").strip()
                model = (row.get(col_map.get("model", ""), "") or "Unknown").strip()
                year = int(_to_float(row.get(col_map.get("year", ""), None), 0) or 0)
                mileage = float(_to_float(row.get(col_map.get("mileage", ""), None), 0.0) or 0.0)
                engine = (row.get(col_map.get("engine", ""), "") or "Unknown").strip()
                transmission = (row.get(col_map.get("transmission", ""), "") or "Unknown").strip()
                drivetrain = (row.get(col_map.get("drivetrain", ""), "") or "Unknown").strip()
                mpg = _to_float(row.get(col_map.get("mpg", ""), None), None)
                exterior_color = (row.get(col_map.get("exterior_color", ""), "") or "Unknown").strip()
                interior_color = (row.get(col_map.get("interior_color", ""), "") or "Unknown").strip()
                accident = _to_bool(row.get(col_map.get("accident", ""), None))
                price = float(_to_float(row.get(col_map.get("price", ""), None), 0.0) or 0.0)

                car = Car(
                    manufacturer, model, year, mileage, engine, transmission,
                    drivetrain, mpg, exterior_color, interior_color, accident, price
                )
                cars.append(car)

                if seller_names is not None:
                    seller = (row.get(col_map.get("seller_name", ""), "") or "Unknown").strip()
                    seller_names.append(seller)

            except Exception as e:
                row_errors.append(f"Row {i} skipped: {e}")
                continue

   

    return cars, seller_names
