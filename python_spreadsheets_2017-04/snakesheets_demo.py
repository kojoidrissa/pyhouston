import uuid, openpyxl, pprint
import copy
import json
import logging
import datetime

logger = logging.getLogger(__name__)

# There will be a LOT of repitition in this iteration of the code. Since I'm not sure what the data format will ultimately look like, I'm just working with "what is" at the moment. Once a standard format for the data is settled on, I'll clean the code to remove the repitition and make it more abstract.

# get workbook object; data_only option captures current value of any formulae
wb_ed = openpyxl.load_workbook('dhr_stdecisio.xlsm', data_only= True)
bednames_ed = wb_ed.get_sheet_by_name('BedNames')
lab_namespaces_ed = wb_ed.get_sheet_by_name('Lab values')
vitals_namespaces_ed = wb_ed.get_sheet_by_name('Vital signs')
lab_ranges_ed = wb_ed.get_sheet_by_name('labs_ranges')
vitals_ranges_ed = wb_ed.get_sheet_by_name('vitals_ranges')

# wb_micu = openpyxl.load_workbook('dhr-kojo_CHI-STLukes_MICU_10-27-16.xlsm', data_only= True)
# bednames_micu = wb_micu.get_sheet_by_name('BedNames')
# lab_namespaces_micu = wb_micu.get_sheet_by_name('Lab values')
# vitals_namespaces_micu = wb_micu.get_sheet_by_name('Vital signs')
# lab_ranges_micu = wb_micu.get_sheet_by_name('labs_ranges')
# vitals_ranges_micu = wb_micu.get_sheet_by_name('vitals_ranges')

# 'client' and 'hospital' are the human-readable values pulled from those fields in the 'BedNames' tab of the workbook
client = bednames_ed["B1"].value
hospital = bednames_ed["B2"].value
hospital_display_name = client + " " + hospital
# `clean_hospital` should be hospital string, stripped of spaces & punctuation and lower-cased (I can't remeber exactly how to do this; I'll look it up). I've done it manually for the sake of time/speed.
clean_hospital = "stlukes"
hospital_path = client.lower() + "." + clean_hospital

# with this spreadsheet, it looks like the only diff b/w the unit display and path names is going to be case. It comes from the Unit field in the 'BedNames' tab of the workbook
unit_display_name = bednames_ed["B2"].value
unit_path = unit_display_name.lower()

def build_unit_objects(source_worksheet):
	"""
	openpyxl.worksheet.worksheet.Worksheet -> dict

	This is a STUB for a function that will build unit objects when given the appropriate source worksheets.  The beds for that unit will be built in the build_bed_objects function and attached later.

	As of 2017-02-15, the unit objects will be created manually
	"""
	# with this spreadsheet, it looks like the only diff b/w the unit display and path names is going to be case. It comes from the Unit field in the 'BedNames' tab of the workbook
	unit_display_name = source_worksheet["B2"].value
	unit_path = unit_display_name.lower()


# I'm assuming we don't need to add another layer for each "Pod" at St. Lukes. If so, that'll change things.
# Each bed in the unit should be built from a tuple of (bed_number, bed_display_name)
# 'bed_number' needs to be the stringified version of a 2-digit 'Bed Number' in the 'BedNames' tab of the workbook

def build_bed_objects(start_row, end_row, source_worksheet):
	"""
	int, int, openpyxl.worksheet.worksheet.Worksheet -> dict

	Takes in starting and (ending + 1) rows for the source data spreadsheet, and worksheet object with the data to be turned into a bed object. Currently, as the needed worksheets are already pulled in earlier, this function will use those existing objects.
	The function will then go to the given ranges and specific columns in that worksheet. These are currently hardcoded, but the ranges may become dynamic as the input worksheet format changes.

	In a later (after 2017-02-15) refactor, the function will be passed a workBOOK object, then go to a specific worksheet in the workbook.
	"""
	unit_beds = {"beds": []}
	# This range is hardcoded, it needs to be dynamic. I KNOW that's possible.
	for row in range(start_row, end_row):
		new_unit_bed ={}
		bed_id = uuid.uuid4().hex
		# column letters for bed_number and bed_display_name are based on reformatted data I created
		bed_number = source_worksheet['J'+str(row)].value
		bed_display_name = source_worksheet['K'+str(row)].value
		# print(bed_id, bed_number, bed_display_name)
		new_unit_bed["id"] = bed_id
		new_unit_bed["path"] = bed_number
		new_unit_bed["name"] = bed_display_name
		unit_beds["beds"].append(new_unit_bed)
	return unit_beds

chi_ed_beds = build_bed_objects(11, 35, bednames_ed)

# config_obj will be the complete config JSON object for a deployment. It will be the output of the entire "Processing" activity that gets serialized to become `config.json`.
config_obj = {"hospital":{}, "resource":{}}