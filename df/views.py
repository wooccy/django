from django.shortcuts import render
import uuid
import dialogflow
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 요청 url 인 bbs/번호 에 대해서 urls.py 에 정의된 view.bbs_detail 이 호출된다
@api_view(['GET', 'PUT', 'DELETE'])
def df_result(request, text, format=None):

    if request.method == 'GET':

        project_id = 'restfultest-54056'
        session_id = str(uuid.uuid4())
        result = detect_intent_texts(project_id, session_id, text, 'en-US')

        return Response(result)


def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))


    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)


    resposeDic = {
        "query_text" : response.query_result.query_text,
        "action" : response.query_result.action,
        "intent_detection_confidence" : response.query_result.intent_detection_confidence,
        "display_name" : response.query_result.intent.display_name,
        "parameters" : []
    }

    for param in response.query_result.parameters:
        paramDic = { param: response.query_result.parameters[param] }
        resposeDic["parameters"] = resposeDic["parameters"] + [paramDic]

    jsonString = json.dumps(resposeDic)
    print(jsonString)
    return jsonString

# Create your views here.