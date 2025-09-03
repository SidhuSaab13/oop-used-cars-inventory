from __future__ import annotations

class Car:
    def __init__(self, manufacturer:str, model:str, year:int, mileage: float, engine: str, transmission: str, drivetrain: str, mpg: float | None, exterior_color: str, interior_color: str, accident: bool, price: float):
        self.manufacturer = manufacturer
        self.model = model
        self.year = int(year)
        self.mileage = float(mileage)
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = float(mpg) if mpg is not None else None
        self.exterior_color = exterior_color
        self.interior_color = interior_color
        self.accident = accident
        self.price = float(price)
    
    def Paint(self, color: str) -> None:
        self.exterior_color = color
    def Repair(self, part: str, replacement: str) -> None:
        part = part.lower().strip()
        if part == "engine":
            self.engine = replacement
        elif part == "transmission":
            self.transmission = replacement
        elif part == "drivetrain":
            self.drivetrain = replacement
        else:
            raise ValueError('Part must be one of: engine, transmission, or drivetrain.')

    def Reupholster(self, color: str) -> None:
        self.interior_color = color

    def Drive(self, miles: float) -> None:
        miles = float(miles)
        if miles <= 0:
            raise ValueError('Distance must be > 0.')
        self.mileage += miles

    def Modify_Price(self, value: float) -> None:
        value = float(value)
        if value >= 1:
            if value <= 0:
                raise ValueError('Value must be non-zero.')
            self.price = round(value, 2)
        else:
            if self.price <= 0:
                raise ValueError('Price must be > 0 to apply a discount.')
            new_price = round(self.price * (1 - value), 2)
            print(f'Price modified from ${self.price} to ${new_price}.')
            ans = input('Apply this new price? (y/n): ').strip().lower()
            if ans in ('y', 'yes'):
                self.price = new_price
                print('New price applied.')
            else:
                print('Price change discarded.')

    def brief(self) -> str:
        mpg_text = "n/a" if self.mpg is None else f"{self.mpg:.1f}"
        acc = "Yes" if self.accident else "No"
        return (f"{self.year} {self.manufacturer} {self.model} | {self.mileage} miles | {mpg_text} MPG | "
                f"Ext:{self.exterior_color} Int:{self.interior_color} | Accident:{acc}")
    