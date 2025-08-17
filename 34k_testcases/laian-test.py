import json
from my_thing import intercept

def run_tests(filename):

	result = {}

	with open(filename, "r") as f:

		data = json.load(f)

		result["data"] = data["data"]
		result["cases"] = []

		for group in data["cases"]:

			for test in group["tests"]:

				group["tests"][test["id"]] = {
					"id": test["id"],
					"result": intercept(test["roads"], test["stations"], test["start"], test["friendStart"])
				}
			
			result["cases"].append(group)

	with open("result.json", "w") as f:
		json.dump(result, f)

def compare_results(file1, file2):

	diff = []

	with open(file1, "r") as f1:
		with open(file2, "r") as f2:

			res1 = json.load(f1)
			res2 = json.load(f2)
	
			for g1, g2 in zip(res1["cases"], res2["cases"]):
				
				group_diff = {
					"nLocations": g1["nLocations"],
					"nStations": g1["nStations"],
					"diffs": []
				}

				for test1, test2 in zip(g1["tests"], g2["tests"]):

					if test1["result"] != test2["result"]:
						group_diff["diffs"].append(test1["id"])

				diff.append(group_diff)

	with open("diff.json", "w") as f:
		json.dump(diff, f)

run_tests("34k_testcases/tests.json")