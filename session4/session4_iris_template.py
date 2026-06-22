"""Session 4: Move Session 3 code into functions.
rpb
This version keeps the same rule from Session 3.
The goal is to help a beginner see where each part came from.
We keep the code simple and close to the original step-by-step style.
"""
LABEL_KEY = "species"
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"


# Task 1: Create a helper function to print status updates
def make_print_status(status_text):
    print (f"\n==={status_text}===")

# Task 2: Create the flower dataset


def setup_application_list():
    """Combination of Task I and Task II in session III, but now in a function."""

    # Task I in session III: Define dictionaries for flower1 and flower2 using canonical keys
    # Paste the two dictionaries you created in Session 3 here, but make sure to use the same keys as in the original dataset (id, sepal_length, sepal_width, petal_length, petal_width, species). Here, we already define the flower1, but you should also define flower2 with the same keys.
    flower1 = {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

    flower2 = {
        "id": "flower1",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

    # Task 2 in session 3: Build the dataset list
    # Combine our dictionaries into a single list
    dataset = [flower1,flower2]
    print("Dataset:", dataset)
    # Note here that we return the dataset list from this function, so we can use it later in the main function.
    return dataset

# Task 5: Predict the class using petal length
def compute_threshold_prediction(sample):
    if sample[FEATURE_NAME] < THRESHOLD:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL

# Task 6: Convert species into the lesson’s binary label
def derive_true_label(sample):
    if sample[LABEL_KEY] == POSITIVE_LABEL:
        y_true = POSITIVE_LABEL
    else:
        y_true = NEGATIVE_LABEL

    return y_true

# Task 7: Update prediction counts and save results
def update_result_counts(correct, wrong, total, y_pred_list, y_pred, y_true):
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    total += 1
    y_pred_list.append(y_pred)


# Task 10: Compute the overall accuracy
def calculate_accuracy(correct, total):
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0
    return accuracy
    # They need to provide the return value, maybe, we can ask them, what is missing in this function, go and check the function call in the main function, and see what they need to return here to make the main function work.


# Entry to Task 4 until Task 9: Run the same prediction loop from Session 3, Wrap the prediction workflow in a function
def run_prediction_loop(dataset):
    # Task III from Session III: initialize metrics and predictions
    correct = 0      # Count of correct predictions
    wrong = 0        # Count of wrong predictions
    total = 0        # Total samples processed
    y_pred_list = []  # List of all predictions made

    print("\n=== Start session 4 Prediction Loop ===")

    # Task IV and Task V from Session III
    for sample in dataset:
        print("\nProcessing sample with id:", sample["id"])

        # Task 5: Predict the class using petal length
        y_pred = compute_threshold_prediction(sample)
        y_true = derive_true_label

        # Task 6: Convert species into the lesson’s binary label
        # For task 6, student are require to create the function call and function definition:y_true = derive_true_label(sample)

        # Task 7: Update prediction counts and save results
        # For task 7, we will not provide the correct, wrong, total, y_pred_list = update_result_counts( correct, wrong, total, y_pred_list, y_pred, y_true ), even the function body is only a pass
        correct, wrong, total, y_pred_list = update_result_counts(
            correct, wrong, total, y_pred_list, y_pred, y_true)

        # Task 8: Display the result for each sample
        # The just need to uncomment the print statement below to see the result for each sample,
        # print(
        #     f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        #     f"petal_length={sample['petal_length']}"
        # )
    # Task 9: Return the prediction loop results
    return < your_code > , wrong, < your_code > , < your_code >

# Task 10: Calculate accuracy


def calculate_accuracy(correct, total):
    """Calculate accuracy percentage.

    Args:
        correct (int): Number of correct predictions.
        total (int): Number of processed samples.

    Returns:
        float: Accuracy percentage.
    """
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0


# Task 12: Create and call the summary-report function


def print_summary(correct, wrong, total, y_pred_list, accuracy):
    """Print the final results after the loop is finished.

    Args:
        correct (int): Number of correct predictions.
        wrong (int): Number of wrong predictions.
        total (int): Number of processed samples.
        y_pred_list (list): List of predicted labels.
        accuracy (float): Accuracy percentage.
    """
    print("\n=== session 4 Summary ===")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", y_pred_list)


def main():
    """Run the full beginner version of the program."""

    # Task 1 : Create a helper function to print status updates
    make_print_status("Build dataset")

    # Task 2: Create the flower dataset
    dataset = setup_application_list()

    # Task 3 : Show a status update before running prediction
    # Uncomment this line to see status messages
    make_print_status("Run prediction loop")

    # Entry to Task 4 until Task 9: Wrap the prediction workflow in a function
    # correct, <your_code>, total, y_pred_list = run_prediction_loop(dataset)
    correct, wrong, total, y_pred_list = run_prediction_loop(dataset)

    # Task 10: Calculate accuracy
    accuracy = calculate_accuracy(correct, total)

    # Task 11: Show a status update before printing the summary
    make_print_status( < your_code > )

    # Task 12: Create and call the summary-report function
    print_summary(correct, wrong, total, y_pred_list, accuracy)


if __name__ == "__main__":
    main()
