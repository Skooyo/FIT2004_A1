import json

def compare_results(file1, file2):
    """
    Compare two result files and print a summary of differences in the "result" attribute.
    
    Args:
        file1: Path to first result file
        file2: Path to second result file
    """
    try:
        with open(file1, "r") as f1:
            with open(file2, "r") as f2:
                res1 = json.load(f1)
                res2 = json.load(f2)
        
        # Track statistics
        total_tests = 0
        total_differences = 0
        groups_with_differences = 0
        
        print("\n\n===== COMPARISON RESULTS =====")
        print(f"Comparing {file1} with {file2}")
        print("==============================\n")
        
        # Iterate through groups
        for group_idx, (g1, g2) in enumerate(zip(res1["cases"], res2["cases"])):
            group_differences = []
            group_tests = 0
            
            # Make sure to handle both list and dictionary formats
            g1_tests = list(g1["tests"].values()) if isinstance(g1["tests"], dict) else g1["tests"]
            g2_tests = list(g2["tests"].values()) if isinstance(g2["tests"], dict) else g2["tests"]
            
            for test1, test2 in zip(g1_tests, g2_tests):
                group_tests += 1
                total_tests += 1
                
                # Compare only the "result" attribute
                if test1["result"] != test2["result"]:
                    if test1["result"] is not None and test2["result"] is not None:
                        if test1["result"][0] != test2["result"][0] or test1["result"][1] != test2["result"][1]:
                        # Append to group differences if both elements differ
                            group_differences.append({
                                "id": test1["id"],
                                "file1_result": test1["result"],
                                "file2_result": test2["result"]
                            })
                            total_differences += 1  
                    else:
                        # Handle cases where one result is None
                        group_differences.append({
                            "id": test1["id"],
                            "file1_result": test1["result"],
                            "file2_result": test2["result"]
                        })
                        total_differences += 1
            
            # Print group results if there are differences
            if group_differences:
                groups_with_differences += 1
                print(f"Group {group_idx+1} - {g1['nLocations']} locations, {g1['nStations']} stations:")
                print(f"  Found {len(group_differences)} differences out of {group_tests} tests")
                
                # Print details for each difference
                for diff in group_differences:
                    print(f"  • Test {diff['id']}:")
                    print(f"    - File 1: Result = {diff['file1_result']}")
                    print(f"    - File 2: Result = {diff['file2_result']}")
                print()
        
        # Print summary
        print("\n===== SUMMARY =====")
        print(f"Total tests: {total_tests}")
        print(f"Total differences: {total_differences} ({total_differences/total_tests*100:.1f}%)")
        print(f"Groups with differences: {groups_with_differences} out of {len(res1['cases'])}")
        
        if total_differences == 0:
            print("\n✅ All results match! No differences found.")
        else:
            print("\n❌ Differences found. See details above.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print(f"Error: One of the files is not a valid JSON file.")

compare_results("34k_testcases/result.json", "34k_testcases/darryl_res.json")
