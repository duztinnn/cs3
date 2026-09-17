class Glassware:
    def __init__(self, m="glass", c=0, s=False):
        self.material, self.capacity_ml, self.is_sterile = m, c, s
    def describe(self):
        return f"{type(self).__name__} made of {self.material}, {self.capacity_ml}ml"

class Beaker(Glassware):
    def __init__(self, c=250, g=True):
        super().__init__(c=c)
        self.has_graduation, self.current_volume_ml = g, 0
    def pour(self, a):
        if self.current_volume_ml + a <= self.capacity_ml:
            self.current_volume_ml += a
        return self.current_volume_ml
    def __repr__(self):
        return f"Beaker({self.capacity_ml}ml, {self.current_volume_ml}ml filled)"

class Tray:
    def __init__(self, i="TRAY-01"):
        self.tray_id, self.beakers = i, [Beaker() for _ in range(5)]
    def list_inventory(self):
        print(f"{self.tray_id} contains:")
        [print(f" {j}. {b.describe()}") for j, b in enumerate(self.beakers, 1)]
    def __del__(self):
        self.beakers.clear()
        print(f"{self.tray_id} deleted, all beakers lost.")

if __name__ == "__main__":
    t = Tray()
    t.list_inventory()
    print("\nIs Beaker a Glassware?", issubclass(Beaker, Glassware))
    print("Is beaker instance of Glassware?", isinstance(t.beakers[0], Glassware))
    del t