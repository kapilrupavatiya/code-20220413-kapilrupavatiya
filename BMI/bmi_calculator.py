# Import statements
import json

from constants import *
from utility import *

def bmi_calculator():
	# Open JSON file
	bmi_raw_json_data_file = open(INPUT_FILE_NAME+".json")

	# Load data from open file
	bmi_raw_json_data = json.load(bmi_raw_json_data_file)

	# Once data read complete, We can close the file
	bmi_raw_json_data_file.close()


	# We want to count person based in bmi_category, So created dictionary for the same
	person_count_by_bmi_category = {}

	# TODO same we can do for heath risk

	# Iterate bmi_raw_json_data and calcualte BMI, BMI category and Health risk
	for bmi_input_record in bmi_raw_json_data:

		# Get height and weight from bmi_input_record
		height_in_mt = convert_cm_to_mt(bmi_input_record.get(HEIGHT_CM_INPUT_KEY))
		weight_kg = bmi_input_record.get(WEIGHT_INPUT_KEY)

		# Calculate bmi from height and weight
		bmi = calculate_bmi(height_in_mt, weight_kg)
		bmi_input_record["BMI"] = bmi

		# Find bmi category based on bmi
		bmi_category = determine_bmi_category_from_bmi(bmi)
		bmi_input_record["BMI Category"] = bmi_category
		
		# Find health_risk based on bmi
		health_risk = determine_health_risk_from_bmi(bmi)
		bmi_input_record["Health_risk"] = health_risk
		
		# Calculate person by BMI category
		person_count_by_bmi_category[bmi_category] = person_count_by_bmi_category.get(bmi_category, 0) + 1


	# Write BMI data to new file
	bmi_raw_json_data = json.dumps(bmi_raw_json_data)
	bmi_out_put_file = INPUT_FILE_NAME + "_output.json"
	with open(bmi_out_put_file, "w") as outfile:
	    outfile.write(bmi_raw_json_data)


	# Write summery of BMI category wise count to another file
	person_count_by_bmi_category = json.dumps(person_count_by_bmi_category)
	bmi_category_summery_file = INPUT_FILE_NAME + "_bmi_category_summery.json"
	with open(bmi_category_summery_file, "w") as outfile:
	    outfile.write(person_count_by_bmi_category)


if __name__ == '__main__':
	bmi_calculator()