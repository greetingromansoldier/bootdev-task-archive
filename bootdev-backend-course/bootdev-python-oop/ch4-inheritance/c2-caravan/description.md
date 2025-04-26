# Caravan: Siege Weapons

Siege weapons (e.g., battering rams, catapults) are special units in **Age of Dragons**. Let's write the logic for how they move around the map.

---

## Challenge

### 1. `Siege` Class
1. **Constructor**
   - Accepts two parameters (in order): `max_speed` and `efficiency`.
   - Assign them to instance variables of the same name.
2. **`get_trip_cost(distance, food_price)` Method**
   - Calculates and returns the cost of a trip.
   - **Formula**:
     \[
       \text{trip_cost} = \frac{\text{distance}}{\text{efficiency}} \times \text{food_price}
     \]
   - It costs food to move siege weapons because they are heavy!
3. **`get_cargo_volume()` Method**
   - Leave this method empty (`pass`), because child classes will override it.

---

### 2. `BatteringRam` Class
1. **Constructor**
   - Calls the parent (`Siege`) constructor to set `max_speed` and `efficiency`.
   - Sets any additional, battering-ram-only instance variables (for example, `load_weight`, `bed_area`, etc.).
2. **`get_trip_cost(distance, food_price)` Method**
   - Uses the **parent** method to calculate the base cost of food for a trip.
   - **Adds** the extra cost of carrying a load.
   - **Formula**:
     \[
       \text{total_trip_cost} = \text{super().get_trip_cost(distance, food_price)} + (\text{load_weight} \times 0.01)
     \]
3. **`get_cargo_volume()` Method**
   - Calculates and returns the cargo capacity in cubic meters.
   - For a battering ram, multiply its `bed_area` by its depth (always `2` meters):
     \[
       \text{cargo_volume} = \text{bed_area} \times 2
     \]

---

### 3. `Catapult` Class
1. **Constructor**
   - Calls the parent (`Siege`) constructor to set `max_speed` and `efficiency`.
   - Sets the extra, catapult-only instance variable (for example, `cargo_capacity`).
2. **`get_trip_cost()`**
   - Do **not** override. Inherit directly from `Siege`.
3. **`get_cargo_volume()`**
   - Returns the cargo capacity of the catapult (likely just returns the catapult’s stored `cargo_capacity` or similar).
