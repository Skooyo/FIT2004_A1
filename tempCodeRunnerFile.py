import json
from approach3 import intercept

def run_tests():
    with open('34k_testcases/tests.json', 'r') as f:
        test_data = json.load(f)
    with open('34k_testcases/aaron-test.json', 'r') as f:
        expected_data = json.load(f)

    total_tests = 0
    exact_matches = 0
    cost_time_matches = 0
    only_cost_matches = 0
    only_time_matches = 0
    complete_mismatches = 0

    failed_tests = []

    test_cases = list(zip(test_data['cases'], expected_data['cases']))
    flat_tests = []

    for case_index, (input_case, expected_case) in enumerate(test_cases):
        assert input_case['nLocations'] == expected_case['nLocations']
        assert input_case['nStations'] == expected_case['nStations']
        for test_index, (test, expected_test) in enumerate(zip(input_case['tests'], expected_case['tests'])):
            flat_tests.append((case_index, test_index, test, expected_test))

    print(f"Running {len(flat_tests)} total test cases...\n")

    for idx, (case_idx, test_idx, test, expected_test) in enumerate(flat_tests):
        total_tests += 1
        test_id = test.get('id', f"{case_idx}-{test_idx}")
        expected_result = expected_test['result']

        try:
            result = intercept(
                test['roads'],
                test['stations'],
                test['start'],
                test['friendStart']
            )
        except Exception as e:
            complete_mismatches += 1
            failed_tests.append({
                'test_id': test_id,
                'expected': expected_result,
                'actual': f"ERROR: {str(e)}",
                'reason': "Function raised an exception"
            })
            continue

        if result is None and expected_result is None:
            exact_matches += 1
            continue

        if result is None or expected_result is None:
            complete_mismatches += 1
            failed_tests.append({
                'test_id': test_id,
                'expected': expected_result,
                'actual': result,
                'reason': "One result is None, the other is not"
            })
            continue

        cost_match = result[0] == expected_result[0]
        time_match = result[1] == expected_result[1]
        route_match = (
            len(result) >= 3 and
            len(expected_result) >= 3 and
            result[2] == expected_result[2]
        )

        if cost_match and time_match and route_match:
            exact_matches += 1
        elif cost_match and time_match:
            cost_time_matches += 1
            failed_tests.append({
                'test_id': test_id,
                'expected': expected_result,
                'actual': result,
                'reason': "Cost and time match, but routes differ"
            })
        elif cost_match:
            only_cost_matches += 1
            failed_tests.append({
                'test_id': test_id,
                'expected': expected_result,
                'actual': result,
                'reason': "Only cost matches"
            })
        elif time_match:
            only_time_matches += 1
            failed_tests.append({
                'test_id': test_id,
                'expected': expected_result,
                'actual': result,
                'reason': "Only time matches"
            })
        else:
            complete_mismatches += 1
            failed_tests.append({
                'test_id': test_id,
                'expected': expected_result,
                'actual': result,
                'reason': "Complete mismatch (cost, time, and route all differ)"
            })

        if (idx + 1) % 1000 == 0:
            print(f"  {idx + 1}/{len(flat_tests)} tests completed")

    print("\n" + "=" * 50)
    print("TESTING COMPLETE")
    print(f"Total tests: {total_tests}")
    print(f"Exact matches: {exact_matches} ({exact_matches / total_tests * 100:.2f}%)")
    print(f"Cost and time match (route differs): {cost_time_matches} ({cost_time_matches / total_tests * 100:.2f}%)")
    print(f"Only cost matches: {only_cost_matches} ({only_cost_matches / total_tests * 100:.2f}%)")
    print(f"Only time matches: {only_time_matches} ({only_time_matches / total_tests * 100:.2f}%)")
    print(f"Complete mismatches: {complete_mismatches} ({complete_mismatches / total_tests * 100:.2f}%)")

    pass_count = exact_matches
    print(f"Overall pass rate: {pass_count / total_tests * 100:.2f}%")

    if failed_tests:
        filename = "failed_tests.txt"
        print(f"\nSaving details for {len(failed_tests)} failed test(s) to '{filename}'...")
        with open(filename, 'w') as f:
            f.write("FAILED TESTS REPORT\n")
            f.write(f"Total tests: {total_tests}, Failed: {len(failed_tests)}\n\n")
            for idx, test in enumerate(failed_tests):
                f.write(f"Failure #{idx + 1}\n")
                f.write(f"Test ID: {test['test_id']}\n")
                f.write(f"Reason: {test['reason']}\n")
                f.write(f"Expected: {test['expected']}\n")
                f.write(f"Actual: {test['actual']}\n")
                f.write("-" * 50 + "\n\n")

    return exact_matches, total_tests, failed_tests

if __name__ == "__main__":
    print("Starting tests for intercept() in assignment1.py...\n")
    exact, total, failed = run_tests()
