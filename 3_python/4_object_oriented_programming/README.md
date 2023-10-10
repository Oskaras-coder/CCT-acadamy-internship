
    # Train Operations

This program reads and distributes randomly loaded cargo to given trains, preparing them for travel to the next train station. If a train is overloaded, the program adds more locomotives (up to 3) and/or wagons. If locomotives are overloaded, trains cannot move. Locomotives can be counted as wagons if the `is_wagon` attribute in the .json file is set to 1 (True). Working locomotives have `is_wagon = 0` (False).

## Usage

To use this program, you will need the following files:
- `train_original_data.json`: This file should contain information about the loaded cargo, including train details such as train number, current location, locomotives, and wagons.
- `train_operations.csv`: This file should include a train number and the target destination to which the train must travel.

## Functions

### TrainStation class

- `process_train_data`: Uses the loaded train data from `json` and `csv` files to create a new dictionary of trains. These trains are stored in a new `json` file. If trains are untowable, they are marked as untowable in the file.
- `load_train_data` and `load_operations_data`: Load `train_original_data.json` and read the data provided by the user.
- `weight_of_the_structure`: Calculates the total weight of the train components.
- `check_wagon` and `check_locomotive`: Check if the data provided by the user is sufficient and valid to create a train.
- `add_wagon`: Adds a wagon if the mass of the load is too high. Returns the overloaded mass and a list of new connected wagons.
- `sort_train_by_wagons`: Sorts the list of trains by the number of wagons and returns a new train list.
- `save_train_to_json`: Creates a new `json` file to store train data.
    