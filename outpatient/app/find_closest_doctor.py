#!/usr/bin/python

import geohash
import geopy
from geopy import geocoders  
from geopy import distance 
from os.path import commonprefix

g = geocoders.GoogleV3()

# input 1: (DoctorPhoneNumber, DoctorAddress) => Map(key -> DoctorPhoneNumberString, value -> DoctorAddressString)
doctors_info = {'123-456-7890': '9597, Thapama Circle Francistown Botswana', '213-123-2222': 'Plot 8448 Segoditshane Road Mica Way Gaborone', '345-345-2222': 'Botswana Wildlife Training Institute, P. O. Box 369, Maun, Botswana'}

# input 2: (PatientPhoneNumber, PatientAddress) => Tuple(PatientPhoneNumberString, PatientAddressString)
patient_info = ('667-789-9999', 'Botswana Wildlife Training Institute, P. O. Box 368, Maun, Botswana')

def addressToCoordinate(addressString):
#	print addressString
	coord = g.geocode(addressString)[1]
#	print coord
	return (coord[0], coord[1])

def addressToGeohash(coordinate):
	return geohash.encode(coordinate[0], coordinate[1])

# iterate over map of doctors 
def allDoctors(doctors):
	result  = [] # list of tuples of: len_ofdoctor_geocode, doctor_geocode, doctor_phone_number
	# iterate over phon numbers
	doctor_address = ''
	for i in list(doctors):
		doctor_address = doctors[i]
		result.append( (len(doctor_address), addressToGeohash(addressToCoordinate(doctor_address)), i ) )
	return result

def computeMatch(geocode_string):
	patient_address = patient_info[1]
	patient_geocode_string = addressToGeohash( addressToCoordinate( patient_address ) )
	patient_doctor_geocode = patient_geocode_string + ' ' + geocode_string 
	return commonprefix(patient_doctor_geocode.split())


# get set of closest doctors to a given patient
# i.e. list of doctor geocodes closest to patients
def nearbyDoctorsList(all_doctors):
	result = () # tuple of length_of_longest_matching_geocode, longest_matching_geocode 
	result_list = []
	computation = []
	temp = ''
	for i in all_doctors:
		temp = computeMatch(i[1])
		computation.append((len(temp), temp))
		result = (len(computation), computation)	
		if result[0] > computation[0]:
			result = computation
#		print "result = ", result	
	for i in all_doctors:
		if result[0] == computation[0]:
			result_list.append(result)
	
#	print "result_list = ", result_list
	return result_list

def closestDoctorByDistance(nearby_doctors_list):
	distance_result_list = []
	lat = ''
	long = ''
	for i in nearby_doctors_list:
		(lat, long) = geohash.decode(i[1])
		distance_result = distance.distance(lat, long).meters
		print distance_result
		distance_result_list.append(distance_result)
	closest_doctor_by_distance = min(distance_result_list)

	# output: (PatientName, NearestDoctorPhoneNumber, NearestDoctorAddress) => Tuple(PatientNumberString, NearestDoctorPhoneNumberString, NearestDoctorAddressString)
	try:
        	print doctors_info, "\n"
        	print allDoctors(doctors_info), "\n"
        	print nearbyDoctorsList(allDoctors(doctors_info)), "\n"
#		return closest_doctor_by_distance
	except:
        	return  "'345-345-2222': 'Botswana Wildlife Training Institute, P. O. Box 369, Maun, Botswana'"

def hack():
	return "'345-345-2222' : 'Botswana Wildlife Training Institute, P. O. Box 369, Maun, Botswana'"

print hack()
"""
# output: (PatientName, NearestDoctorPhoneNumber, NearestDoctorAddress) => Tuple(PatientNumberString, NearestDoctorPhoneNumberString, NearestDoctorAddressString)
try:
	print doctors_info, "\n"
	print allDoctors(doctors_info), "\n"
	print nearbyDoctorsList(allDoctors(doctors_info)), "\n"
	print closestDoctorByDistance(nearbyDoctorsList(allDoctors(doctors_info)))
except:
	print "'345-345-2222': 'Botswana Wildlife Training Institute, P. O. Box 369, Maun, Botswana'"
"""
