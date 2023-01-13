import json
from flask import request


from outside_apis.openai_api import text_complition

def process_request(request: request) -> dict:
    '''
    Process the incoming data of the Telegram request

    Parameters:
        - request(falsk.request)

    Returns:
        - dict of these key and value 
        {
            'is_text': is_text,
            'is_chat_deleted': is_chat_deleted,
            'sender_id': sender_id,
            'message': message,
            'secret_token': secret_token,
            'first_name': first_name
        }
    '''
    
    body = request.get_json()
    print(body)
    headers = request.headers
    secret_token = headers['X-Telegram-Bot-Api-Secret-Token']

    message = ''
    is_bot = True
    is_text = False
    first_name = ''
    sender_id = None


    if 'message' in body.keys():
        sender_id = body['message']['from']['id']
        first_name = body['message']['from']['first_name']
        is_bot = body['message']['from']['is_bot']

        if 'text' in body['message'].keys():
            message += body['message']['text']
            is_text = True

    return {
        'is_text': is_text,
        'sender_id': sender_id,
        'message': message,
        'secret_token': secret_token,
        'first_name': first_name,
        'is_bot': is_bot
    }

def generate_response(message: str) -> str:
    '''
    Process the incoming message for different command and generate a response string

    Parameters:
        - message(str): incoming message from Telegram

    Returns:
        - str: formated response for the command
    '''
    if message == '/contactme':
        return 'You can reach out to me here: @dylanforexia'
    elif message == '/youtube':
        return 'You can watch my video tutorials here: https://www.youtube.com/'
    elif message == '/github':
        return 'You can get helpful piece of code here: https://github.com/dylanforexia'
    elif message == '/buyacoffee':
        return 'If you like my work please consider buying me a coffee here'
    elif message == '/help':
        return 'You can ask almost anything here, but do not belive whatever this bot says. :-)'
    elif message == '/start':
        return 'Decentral-AI es una chatbot impulsada por IA que ayuda a las empresas a optimizar su flujo de trabajo y colaborar de forma más eficaz. Está impulsado por una automatización inteligente y un procesamiento de lenguaje natural eficiente, lo que lo hace ideal para empresas como abogados y servicios legales, escritores y creadores de contenido, profesionales de TI y más.

Las principales características de Decentral-AI son:

• Conversaciones automatizadas: La chatbot puede tomar el control de las tareas más mundanas de una conversación, permitiendo que las empresas inviertan más tiempo en las actividades más importantes para ellas.

• Procesamiento de lenguaje natural: Decentral-AI entiende lo que los usuarios están diciendo y puede responder de acuerdo, lo que facilita para que los clientes obtengan rápida y correctamente las respuestas que necesitan. 

• Automatización de tareas: Con Decentral-AI, las empresas pueden automatizar tareas complejas como la creación de documentos, la entrada de datos y más, lo que les permite centrarse en construir su negocio en lugar de perder tiempo en las operaciones cotidianas tediosas.

• Analíticas e insights: La chatbot impulsada por IA proporciona a las empresas potentes insights y analíticas que se pueden usar para comprender mejor su base de clientes y dirigirse al público adecuado con un mensaje personalizado. 

• Plataforma escalable: Decentral-AI está diseñado para escalar con las empresas, ofreciendo la flexibilidad y la capacidad para crecer junto con los cambiantes requisitos de la organización.

Con Decentral-AI, las empresas pueden funcionar de forma más eficiente, mejor atender a sus clientes y mejorar la colaboración entre los miembros del equipo, lo que resulta en una mayor productividad y rentabilidad general.

Recuerde que esta es sólo una demostración creada por Blockchain Costa Rica para el Ecosistema de la Cadena de Bloques DecentralChain y si desea tener su propia AI personalizada y con marca propia para su negocio, puede contactar https://t.me/dylanforexia para obtener más información sobre cómo obtener su propia AI empresarial y incluso acceder a nuestra API Decentral-AI.'
    else:
        result = text_complition(message)
        if result['status'] == 1:
            return result['response'].strip()
        else:
            return 'Sorry, I am out of service at this moment.'
            
