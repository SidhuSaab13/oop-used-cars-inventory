from __future__ import annotations
import os, sys
from collections import defaultdict

from inventory_loader import load_cars_from_csv
from seller import Seller

DEBUG = False

def build_sellers(cars, seller_names=None):
    sellers: list[Seller] = []
    if seller_names:
        buckets = defaultdict(list)
        for car, sname in zip(cars, seller_names):
            name = (sname or "Unknown").strip() or "Unknown"
            buckets[name].append(car)

        for name, items in sorted(buckets.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            s = Seller(name=name, rating=4.5)
            for car in items:
                s.Buy(car)
            sellers.append(s)
    else:
        sellers = [Seller(f"Seller_{i+1}", rating=4.5) for i in range(5)]
        for i, car in enumerate(cars):
            sellers[i % len(sellers)].Buy(car)
    return sellers

def choose(prompt, options):
    print(prompt)
    for i, o in enumerate(options):
        print(f"[{i}] {o}")
    ans = input("Pick an index (Enter to cancel): ").strip()
    if ans == "":
        return None
    try:
        i = int(ans)
        if 0 <= i < len(options):
            return i
    except:
        pass
    return None

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else (
        "data/cars.csv" if os.path.exists("data/cars.csv") else "data/USA_cars_dataset.csv"
    )
    if not os.path.exists(path):
        print(f"CSV not found at: {path}\nTip: run: python app.py data/cars.csv")
        return

    cars, seller_names = load_cars_from_csv(path)
    sellers = build_sellers(cars, seller_names)

    print(f"Loaded {len(cars)} cars into {len(sellers)} sellers.\n")

    if DEBUG:
        print("----- DEBUG -----")
        print(f"cars loaded: {len(cars)}")
        print(f"seller_names: {0 if seller_names is None else len(seller_names)}")
        if seller_names:
            uniq = {}
            for name in seller_names:
                uniq[name] = uniq.get(name, 0) + 1
            print(f"unique sellers in CSV: {len(uniq)}")
        assigned = sum(len(s.inventory) for s in sellers)
        print(f"sellers built: {len(sellers)}")
        print(f"cars assigned to sellers: {assigned}")
        print("sample seller counts (first 10):",
              [len(s.inventory) for s in sellers[:10]])
        print("------------------")

    while True:
        print("\n=== MENU ===")
        print("[1] List top sellers")
        print("[2] Show a seller's inventory")
        print("[3] Modify a car (Paint / Repair / Reupholster / Drive / Modify Price)")
        print("[4] Move a car between sellers (Sell -> Buy)")
        print("[5] Quit")
        print("[6] Find a seller by name")
        choice = input("Choose: ").strip()

        if choice == "1":
            top = sorted(sellers, key=lambda s: len(s.inventory), reverse=True)[:30]
            for s in top:
                print(f"- {s.name} | Rating {s.rating} | {len(s.inventory)} cars")
            print(f"(showing {len(top)} of {len(sellers)} sellers)")

        elif choice == "2":
            idx = choose("Pick a seller:", [f"{s.name} ({len(s.inventory)} cars)" for s in sellers])
            if idx is None:
                continue
            sellers[idx].list_brief()

        elif choice == "3":
            idx = choose("Pick a seller:", [s.name for s in sellers])
            if idx is None:
                continue
            s = sellers[idx]
            if not s.inventory:
                print("This seller has no cars.")
                continue
            s.list_brief()
            which = input("Pick car index: ").strip()
            if not which.isdigit():
                print("Invalid.")
                continue
            j = int(which)
            if not (0 <= j < len(s.inventory)):
                print("Out of range.")
                continue
            car = s.inventory[j]
            print("[a] Paint  [b] Repair  [c] Reupholster  [d] Drive  [e] Modify Price")
            sub = input("Pick action: ").strip().lower()
            try:
                if sub == "a":
                    car.Paint(input("New exterior color: "))
                    print("Updated:", car.brief())
                elif sub == "b":
                    part = input("Part (engine/transmission/drivetrain): ")
                    repl = input("Replacement description: ")
                    car.Repair(part, repl)
                    print("Updated:", car.brief())
                elif sub == "c":
                    car.Reupholster(input("New interior color: "))
                    print("Updated:", car.brief())
                elif sub == "d":
                    car.Drive(float(input("Miles to add: ")))
                    print("Updated:", car.brief())
                elif sub == "e":
                    val = float(input("New price (>=1) or discount (<1): "))
                    car.Modify_Price(val)
                    print("Updated:", car.brief())
                else:
                    print("Unknown action.")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            if len(sellers) < 2:
                print("Need at least two sellers.")
                continue
            a = choose("Move FROM:", [f"{s.name} ({len(s.inventory)} cars)" for s in sellers])
            if a is None:
                continue
            b = choose("Move TO:", [f"{s.name} ({len(s.inventory)} cars)" for s in sellers])
            if b is None or b == a:
                print("Canceled.")
                continue
            src, dst = sellers[a], sellers[b]
            if not src.inventory:
                print("Source empty.")
                continue
            src.list_brief()
            which = input("Pick car index to move: ").strip()
            if not which.isdigit():
                print("Invalid.")
                continue
            j = int(which)
            if not (0 <= j < len(src.inventory)):
                print("Out of range.")
                continue
            car = src.inventory[j]
            try:
                src.Sell(car)
                dst.Buy(car)
                print("Moved.")
            except Exception as e:
                print("Error:", e)

        elif choice == "5":
            break

        elif choice == "6":
            q = input("Type part of the seller name: ").strip().lower()
            if not q:
                continue
            matches = [s for s in sellers if q in s.name.lower()]
            if not matches:
                print("No matches.")
                continue
            matches = sorted(matches, key=lambda s: len(s.inventory), reverse=True)[:20]
            for i, s in enumerate(matches):
                print(f"[{i}] {s.name} | {len(s.inventory)} cars")
            pick = input("Pick index to view inventory (Enter to cancel): ").strip()
            if not pick.isdigit():
                continue
            i = int(pick)
            if 0 <= i < len(matches):
                matches[i].list_brief()

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
