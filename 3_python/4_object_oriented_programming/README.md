
    # Train operations

    This program reads and distributes randomly loaded cargo in given trains preparing it to travel to the next train station. 
    If the train is overloaded, program adds more locomotives (up to 3) and/or wagons. 
    If locomotives are overloaded, trains cannot move.
    Locomotives can be counted as wagons if is_wagon in .json file is 1 (True). 
    Working locomotives has is_wagon = 0 (False). 
    
    
    ## Usage
    - For the program to work you will need a train_original_data.json and train_operations.csv file.
    - In train_original_data.json file cargo should be loaded. The file should have trains information - 
    Train number, train current location, locomotives, wagons.
    - train_operations.csv file has a train number and a target destination where this train must travel.
    
    
    ## Functions:
    - TrainStation class:
        - process_train_data - uses loaded train data from json and csv file to create a new dictionary of trains.
        These trains are stored in a new json file. If trains are untowable, they are marked as untowable in a file.
        - load_train_data and load_operations_data - loads train_original_data.json and reads the data provided by the user.
        - weight_of_the_structure - calculates the total weight of the train
        - check_wagon and check_locomotive - checks if the data provided by the user is sufficient/valid to create a train.
        - add_wagon - Adds a wagon if the mass of the load is too high. Returns overloaded mass and a list of new connected wagons. 
        - sort_train_by_wagons - Sorts the list of trains by the number of wagons. Returns new train list.
        - save_train_to_json - creates a new json file.
    