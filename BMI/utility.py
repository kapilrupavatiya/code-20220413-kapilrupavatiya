from constants import *

def convert_cm_to_mt(cm):
    """
    Responsbile to convert cm to mt

    :param cm: Integer, Need to convert this centemeter to meter
    :return: Float with 2 decimal, Meter which we converted from centemeter
    """ 
    return round(cm/100)

def calculate_bmi(height_in_mt, weight_in_kg):
	"""
    Responsbile to calculate bmi, Defination of BMI is as below:
    bmi = Weight in KG / Height in MT

    :param height_in_mt: Float with 2 decimal, Height to calculate BMI
    :param weight_in_kg: Float with 2 decimal, Weight to calculate BMI
    :return: Float with 2 decimal, BMI based on height and weight
    """ 
	return round(weight_in_kg/height_in_mt, 2)

def determine_bmi_category_from_bmi(bmi):
	"""
    Responsbile to determine BMI category based on BMI Range given in below table.
    BMI Category 			BMI Range (kg/m2)
	Underweight 			18.4 and below
	Normal weight 			18.5 - 24.9
	Overweight 				25 - 29.9
	Moderately obese 		30 - 34.9
	Severely obese 			35 - 39.9
	Very severely obese 	40 and above
    
    :param bmi: Float with 2 decimal,BMI
    :return: String, BMI category
    """ 
    # TODO - We can move all BMI category to constant file and only refer those constants from here.
	if bmi <= 18.4:
		bmi_category = UNDER_WEIGHT_BMI_CATEGORY
	elif bmi >= 18.5 and bmi <= 24.9:
		bmi_category = NORMAL_WEIGHT_BMI_CATEGORY
	elif bmi >= 25 and bmi <= 29.9:
		bmi_category = OVER_WEIGHT_BMI_CATEGORY
	elif bmi >= 30 and bmi <= 34.9:
		bmi_category = MODERATELY_OBESE_BMI_CATEGORY
	elif bmi >= 35 and bmi <= 39.9:
		bmi_category = SEVERELY_OBESE_BMI_CATEGORY
	else:
		bmi_category = VERY_SEVERELY_OBESE_BMI_CATEGORY
	return bmi_category

def determine_health_risk_from_bmi(bmi):
	"""
    Responsbile to determine health risk based on BMI Range given in below table.
    
	BMI Range (kg/m2)		Health risk
	18.4 and below 			Malnutrition risk
	18.5 - 24.9 			Low risk
	25 - 29.9 				Enhanced risk
	30 - 34.9 				Medium risk
	35 - 39.9 				High risk
	40 and above 			Very high risk
    
    :param bmi: Float with 2 decimal,BMI
    :return: String, Health risk
    """ 
    # TODO - We can move all health risks to constant file and only refer those constants from here.
	if bmi <= 18.4:
		health_risk = "Malnutrition risk"
	elif bmi >= 18.5 and bmi <= 24.9:
		health_risk = "Low risk"
	elif bmi >= 25 and bmi <= 29.9:
		health_risk = "Enhanced risk"
	elif bmi >= 30 and bmi <= 34.9:
		health_risk = "Medium risk"
	elif bmi >= 35 and bmi <= 39.9:
		health_risk = "High risk"
	else:
		health_risk = "Very high risk"
	return health_risk