import unittest
from unittest.mock import mock_open, patch, MagicMock
from train_system import TrainStation
import json
from wagon import Wagon
from train import Train
from locomotive import Locomotive


class TestTrainStation(unittest.TestCase):
    def setUp(self):
        # Create an instance of TrainStation for testing
        self.train_station = TrainStation("train_original_data.json", "train_operations.csv")

    @patch("builtins.open", new_callable=mock_open)
    def test_load_train_data_success(self, mock_file):
        mock_json_data = {
            "trains": [
                {"train_number": "123", "locomotives": [], "wagons": []},
                {"train_number": "456", "locomotives": [], "wagons": []}
            ]
        }
        expected_result = mock_json_data
        mock_file.return_value.read.return_value = json.dumps(mock_json_data)

        result = self.train_station.load_train_data()
        self.assertEqual(result, expected_result)

    @patch("builtins.open", new_callable=mock_open)
    def test_load_train_data_file_not_found(self, mock_file):
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            self.train_station.load_train_data()

    def test_weight_of_the_structure(self):
        train_structures = [10, 20, 30, 40]
        expected_weight = sum(train_structures)
        actual_weight = TrainStation.weight_of_the_structure(train_structures)
        self.assertEqual(actual_weight, expected_weight)

    # Testing check_wagon method
    def test_valid_wagon(self):
        wagon = {
            "mass": 1000,
            "load_mass": 500,
            "max_load_mass": 2000,
            "wagon_number": "ABC123"
        }
        self.assertTrue(TrainStation.check_wagon(wagon))

    def test_missing_values(self):
        wagon = {
            "mass": 1000,
            "wagon_number": "ABC123"
        }
        self.assertFalse(TrainStation.check_wagon(wagon))

    def test_zero_negative_values(self):
        wagon = {
            "mass": -100,  # Should be higher than 0
            "load_mass": 0,
            "max_load_mass": 0,
            "wagon_number": "ABC123"
        }
        self.assertFalse(TrainStation.check_wagon(wagon))

    def test_non_integer_values(self):
        wagon = {
            "mass": "1000",  # Should be an integer
            "load_mass": 500,
            "max_load_mass": 2000,
            "wagon_number": "ABC123"
        }
        self.assertFalse(TrainStation.check_wagon(wagon))

    def test_missing_wagon_number(self):
        wagon = {
            "mass": 1000,
            "load_mass": 500,
            "max_load_mass": 2000
        }
        self.assertFalse(TrainStation.check_wagon(wagon))


class TestTrainMassCalculator(unittest.TestCase):

    def setUp(self):
        locomotive1 = {"locomotive_name": "LocoA", "locomotive_mass": 100, "max_towable_mass": 200, "is_wagon": False}
        locomotive2 = {"locomotive_name": "LocoB", "locomotive_mass": 120, "max_towable_mass": 250, "is_wagon": False}

        wagon1 = {"mass": 50, "load_mass": 20, "max_load_mass": 100, "wagon_number": "Wagon1"}
        wagon2 = {"mass": 60, "load_mass": 30, "max_load_mass": 120, "wagon_number": "Wagon2"}

        self.train = Train(
            train_number="Train001",
            locomotives=[locomotive1, locomotive2],
            locomotive_wagons=[],
            wagons=[wagon1, wagon2],
            wagons_weight=110,
            current_city="CityA",
            target_destination="CityB")

        self.train.locomotives = [Locomotive(locomotive_mass=100,
                                             max_towable_mass=200,
                                             locomotive_name="a",
                                             is_wagon=0),
                                  Locomotive(locomotive_mass=150,
                                             max_towable_mass=300,
                                             locomotive_name="b",
                                             is_wagon=0)]
        self.train.locomotive_wagons = [Locomotive(locomotive_mass=120,
                                                   max_towable_mass=300,
                                                   locomotive_name="a1",
                                                   is_wagon=1),
                                        Locomotive(locomotive_mass=90,
                                                   max_towable_mass=400,
                                                   locomotive_name="b1",
                                                   is_wagon=1)]
        self.train.wagons_weight = 200

    def test_train_mass_calculation(self):
        train_mass = self.train.train_mass_calculator()
        expected_mass = 100 + 150 + 120 + 90 + 200
        self.assertEqual(train_mass, expected_mass)

    def test_empty_train(self):
        # an empty train with no locomotives, wagons, or non-working locomotives
        empty_train = Train(train_number="Train002",
                            locomotives=[],
                            locomotive_wagons=[],
                            wagons=[],
                            wagons_weight=0,  # Total wagon weight
                            current_city="CityA",
                            target_destination="CityB")
        train_mass = empty_train.train_mass_calculator()
        self.assertEqual(train_mass, 0)  # An empty train should have zero mass


class TestAddWagon(unittest.TestCase):
    def setUp(self):
        self.sample_wagon = Wagon(mass=100, mass_of_the_load=0, max_mass_of_the_load=50, unique_wagon_number=1)
        self.sample_wagons = []

    def test_add_wagon_underweight(self):
        overweight, wagons = TrainStation.add_wagon(30, self.sample_wagon, self.sample_wagons)
        self.assertEqual(overweight, 0)  # No overweight remaining
        self.assertEqual(len(wagons), 1)  # One wagon added

    def test_add_wagon_overweight(self):
        overweight, wagons = TrainStation.add_wagon(80, self.sample_wagon, self.sample_wagons)
        self.assertEqual(overweight, 30)  # Remaining overweight
        self.assertEqual(len(wagons), 1)  # One wagon added


class TestWagonMagicAddition(unittest.TestCase):
    def setUp(self):
        self.wagon1 = Wagon(mass=1000, mass_of_the_load=200, max_mass_of_the_load=1200, unique_wagon_number="W1")
        self.wagon2 = Wagon(mass=800, mass_of_the_load=150, max_mass_of_the_load=1000, unique_wagon_number="W2")

    def test_add_wagons(self):
        combined_wagon = self.wagon1 + self.wagon2

        self.assertEqual(combined_wagon.mass, 2150)
        self.assertEqual(combined_wagon.mass_of_the_load, 350)
        self.assertEqual(combined_wagon.max_mass_of_the_load, 2200)


class TestTrainStation_2(unittest.TestCase):
    def setUp(self):
        self.train_station = TrainStation(train_data_file="train_data.csv", operations_file="train_operations.csv")

        self.train_station.load_train_data = MagicMock(return_value={
            "trains": [
                {
                    "train_number": "TRN123",
                    "locomotives": [{"locomotive": "LocoA", "mass": 100, "max_towable_mass": 200, "is_wagon": False}],
                    "wagons": [{"mass": 50, "load_mass": 20, "max_load_mass": 100, "wagon_number": "Wagon1"}],
                    "train_current_location": "CityA"
                }
            ]
        })

    def test_process_train_data(self):
        self.train_station.process_train_data()

        self.assertEqual(len(self.train_station.trains), 1)
        self.assertEqual(self.train_station.trains[0].current_city, "Kaunas")
        self.assertEqual(self.train_station.trains[0].target_destination, "Kaunas")


if __name__ == "__main__":
    unittest.main()
