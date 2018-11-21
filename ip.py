'''
This is the test client for the Main_service_name
     service_API_details
 
 To run this script :
     pytest Main_service_name -s
 '''
 
 import pytest
 import requests
 import json
 
 from APIUrlConfigConstant import *
 
 test_payload_data = [
     Test_load
 ]
 
 @pytest.mark.parametrize('test_payload_data',test_payload_data)
 
 def test_ai_face_detection_svc(test_payload_data):
 
     api_url = APIUrlConfigConstant.Api_url_caps_on

     expected_response = __getAPIResponse(api_url, test_payload_data)
     loaded_result = json.loads(expected_response)
 
     assert loaded_result["response"] == "success"
 
 def __getAPIResponse(api_url,payloadData):
 
     try:
         print("---------------#sending request with following params#-----------")
         print(json.dumps(payloadData))
         r = requests.post(api_url, json.dumps(payloadData))
         print("----------#Got the request back from server#----------------")
         responseValue=r.text
         print(responseValue)
         return responseValue
 
     except Exception as error:
         print(error)
         return None
