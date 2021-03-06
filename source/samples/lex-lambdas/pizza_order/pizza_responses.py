######################################################################################################################
#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.                                                #
#                                                                                                                    #
#  Licensed under the Apache License, Version 2.0 (the 'License'). You may not use this file except in compliance    #
#  with the License. A copy of the License is located at                                                             #
#                                                                                                                    #
#      http://www.apache.org/licenses/LICENSE-2.0                                                                    #
#                                                                                                                    #
#  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES #
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions    #
#  and limitations under the License.                                                                                #
######################################################################################################################

# @author Solution Builders
import json

def get_menu_message(locale_id, welcome_message=True):
    '''
    Constructs a response containing a welcome message and pizza order menu for Amazon Lex to present to the user.

    :param locale_id: A string containig language locale id received from Amazon Lex with format example: en_US
    :param welcome_message: (optional) A boolean indicating whether the message should include a welcome message.
    :returns: A string in the language indicated by locale_id, containing order pizza menu and potentially a welcome message.
    '''

    welcome_responses = {
        'en_US': 'Welcome to our Pizza Ordering Service. ',
        'fr_FR': 'Bienvenue dans notre service de commande de pizza. ',
        'es_US': 'Bienvenido a nuestro servicio de pedidos de pizza. ',
        'it_IT': 'Benvenuti nel nostro servizio di ordinazione di pizze. ',
        'de_DE': 'Willkommen bei unserem Pizza-Bestellservice. ',
        'ja_JP': '??????????????????????????????????????????'
    }
    menu_responses = {
        'en_US': 'Our Pizza menu includes: ',
        'fr_FR': 'Notre menu Pizza comprend: ',
        'es_US': 'Nuestro men?? de Pizza incluye: ',
        'it_IT': 'Il nostro men?? Pizza comprende: ',
        'de_DE': 'Unsere Pizza-Speisekarte beinhaltet: ',
        'ja_JP': '????????????????????????????????????????????????: '
    }
    question_responses = {
        'en_US': 'What type of pizza would you like?',
        'fr_FR': 'Quel type de pizza souhaitez-vous?',
        'es_US': 'Que tipo de pizza te gustaria?',
        'it_IT': 'Che tipo di pizze vorresti?',
        'de_DE': 'Welche Art von Pizze m??chten Sie?',
        'ja_JP': '???????????????????????????????????????'
    }
    with open("pizza_order/pizza_menu.json") as menu_file:
        menu_data = json.load(menu_file)
        response = ""
        if welcome_message:
            response = welcome_responses[locale_id]
        response = response + menu_responses[locale_id]
        for item in menu_data[locale_id]["menuItems"]:
            if locale_id == "en_US":
                response = response + f"{item['T']} Pizza ({item['D']}). Price (Small: {item['P']['small']}, Medium: {item['P']['medium']}, Large: {item['P']['large']}, Extra-large: {item['P']['extra-large']}). "
            elif locale_id == "fr_FR":
                response = response + f"{item['T']} Pizza ({item['D']}). Prix (Petit: {item['P']['petit']}, Moyen: {item['P']['moyen']}, Grand: {item['P']['grand']}, Tr??s grand: {item['P']['tr??s-grand']}). "
            elif locale_id == "es_US":
                response = response + f"{item['T']} Pizza ({item['D']}). Precio (Peque??a: {item['P']['peque??o']}, Mediana: {item['P']['mediano']}, Grande: {item['P']['grande']}, Extra-grande: {item['P']['extra-grande']}). "
            elif locale_id == "it_IT":
                response = response + f"{item['T']} Pizza ({item['D']}). Prezzo (Piccola: {item['P']['piccola']}, Media: {item['P']['media']}, Grande: {item['P']['grande']}, Extra-grande: {item['P']['extra-grande']}). "
            elif locale_id == "de_DE":
                response = response + f"{item['T']} Pizza ({item['D']}). Preis (Kleine: {item['P']['klein']}, Mittlere: {item['P']['mittel']}, Gro??e: {item['P']['gro??']}, Extra-gro??e: {item['P']['extra-gro??']}). "
            elif locale_id == "ja_JP":
                response = response + f"{item['T']} ?????? ({item['D']})??? ?????? (S: {item['P']['S']}, M: {item['P']['M']}, L: {item['P']['L']}, XL: {item['P']['XL']})??? "
            else:
                raise ValueError(f"Unsupported locale id. Parameter `locale_id: {locale_id}` is not supported.")

        response = response + question_responses[locale_id]
        return response


def get_repeat_message(locale_id, last_order):
    '''
    Constructs a response containing a welcome message and prmopt message to repeat the user's last order for Amazon Lex to present to the user.

    :param locale_id: A string containig language locale id received from Amazon Lex with format example: en_US
    :param last_order: 'Items' object received from DynamoDB query
    :returns: A string in the language indicated by locale_id, indicating whether user wants to repeat their last order.
    '''
    pizza_type = last_order['pizzaType']['S']
    pizza_size = last_order['pizzaSize']['S']
    pizza_crust = last_order['pizzaCrust']['S']
    pizza_count = last_order['pizzaCount']['N']
    repeat_messages = {
        'en_US': f'Welcome back to our Pizza Ordering Service. Would you like to order the same order as your last one?. Type: {pizza_type}, Size: {pizza_size}, Number of Pizzas: {pizza_count}, and Crust: {pizza_crust}, (yes or no)?',
        'es_US': f'Bienvenido de nuevo a nuestro servicio de pedidos de pizza. ??Le gustar??a hacer el mismo pedido que el ??ltimo?. Tipo: {pizza_type}, Size: {pizza_size}, Number of Pizzas: {pizza_count}, and Crust: {pizza_crust}, (si o no)?',
        'fr_FR': f'Bienvenue ?? notre service de commande de pizza. Souhaitez-vous commander la m??me commande que votre derni??re?. Type: {pizza_type}, Size: {pizza_size}, Number of Pizzas: {pizza_count}, and Crust: {pizza_crust}, (Oui ou non)?',
        'it_IT': f'Bentornati al nostro servizio di ordinazione di pizze. Vorresti ordinare lo stesso ordine del tuo ultimo?. Tipo: {pizza_type}, Size: {pizza_size}, Number of Pizzas: {pizza_count}, and Crust: {pizza_crust}, (s?? o no)?',
        'de_DE': f'Willkommen zur??ck bei unserem Pizza-Bestellservice. M??chten Sie die gleiche Bestellung wie Ihre letzte bestellen?. Art: {pizza_type}, Size: {pizza_size}, Number of Pizzas: {pizza_count}, and Crust: {pizza_crust}, (ja oder Nein)?',
        'ja_JP': f'?????????????????????????????????????????? ??????????????????????????????????????? ????????????{pizza_type}???????????????{pizza_size}??????????????????{pizza_count}??????????????????{pizza_crust}????????????????????????????????????',
    }
    return repeat_messages[locale_id]


def get_confirmation_message(locale_id, slots):
    '''
    Constructs a response containing order summary and prompt for confirmation for Amazon Lex to present to the user.

    :param locale_id: A string containig language locale id received from Amazon Lex with format example: en_US
    :param last_order: "Items" object received from DynamoDB query
    :returns: A string in the language indicated by locale_id, indicating whether user wants to repeat their last order.
    '''
    pizza_type = slots['type']['value']['resolvedValues'][0]
    pizza_size = slots['size']['value']['resolvedValues'][0]
    pizza_count = slots['count']['value']['resolvedValues'][0]
    pizza_crust = slots['crust']['value']['resolvedValues'][0]
    confirmation_responses = {
        'en_US': f'Here is a summary of your order. Type: {pizza_type}, Size: {pizza_size}, Number of Pizzas: {pizza_count}, and Crust: {pizza_crust}. Would you like to place your order, (yes or no)?',
        'es_US': f'A continuaci??n se muestra un resumen de su pedido. Tipo: {pizza_type}, Tama??o: {pizza_size}, Numero de pizzas: {pizza_count}, y Corteza: {pizza_crust}. ??Le gustar??a realizar su pedido (si o no)?',
        'fr_FR': f'Voici un r??capitulatif de votre commande. Type: {pizza_type}, Taille: {pizza_size}, Nombre de pizzas: {pizza_count}, et cro??te: {pizza_crust}. Souhaitez-vous passer votre commande (oui ou non)?',
        'it_IT': f"Ecco un riepilogo del tuo ordine. Tipo: {pizza_type}, Taglia: {pizza_size}, Numero di pizze: {pizza_count}, e Crosta: {pizza_crust}. Vorresti effettuare l'ordine, (s?? o no)?",
        'de_DE': f'Hier ist eine Zusammenfassung Ihrer Bestellung. Art: {pizza_type}, Gr????e: {pizza_size}, Anzahl der Pizzen: {pizza_count}, und Kruste: {pizza_crust}. M??chten Sie Ihre Bestellung aufgeben (ja oder nein)?',
        'ja_JP': f'??????????????????????????????????????? ????????????{pizza_type}???????????????{pizza_size}??????????????????{pizza_count}??????????????????{pizza_crust}??? ?????????????????? (??????????????????)??? ',
    }
    return confirmation_responses[locale_id]


def get_fulfilled_message(locale_id, order_id, total_bill):
    '''
    Constructs a response containing an order fulfillment message for Amazon Lex to present to the user.

    :param locale_id: A string containig language locale id received from Amazon Lex with format example: en_US
    :param order_id: A string containing a generated order id
    :param total_bill: A string containing number value of the total bill
    :returns: A string in the language indicated by locale_id, informing the user that their order has been placed.
    '''
    fufilled_messages = {
      'en_US': f"Your order has been placed. Here is the order's number: {order_id}. Your total bill, including tax, is ${total_bill}. Thank you for using our service!",
      'es_US': f'Su orden ha sido puesta. Aqu?? est?? el n??mero de pedido: {order_id}. Su factura total, incluidos los impuestos, es ${total_bill}. ??Gracias por usar nuestro servicio!',
      'fr_FR': f"Votre commande a bien ??t?? re??ue. Voici le num??ro de commande: {order_id}. Votre facture totale, taxes comprises, est ${total_bill}. Merci d'utiliser notre service!",
      'it_IT': f"Il tuo ordine ?? stato inoltrato. Ecco il numero dell'ordine: {order_id}. Il conto totale comprensivo di tasse ?? ${total_bill}. Grazie per aver utilizzato il nostro servizio!",
      'de_DE': f'Deine Bestellung wurde aufgenommen. Hier ist die Bestellnummer: {order_id}. Ihre Gesamtrechnung einschlie??lich Steuern betr??gt ${total_bill}. Vielen Dank, dass Sie unseren Service nutzen!',
      'ja_JP': f"????????????????????????????????? ???????????????????????????????????????{order_id}??? ??????????????????????????????$ {total_bill}????????? ?????????????????????????????????????????????????????????????????????????????????",
    }
    return fufilled_messages[locale_id]


def get_cancel_message(locale_id):
    '''
    Constructs a response containing a cancellation message for Amazon Lex to present to the user.

    :param locale_id: A string containig language locale id received from Amazon Lex with format example: en_US
    :returns: A string in the language indicated by locale_id, informing the user that their order has been cancelled.
    '''
    cancel_responses = {
        "en_US": "Your order has been cancelled. Thank you!",
        "es_US": "Tu pedido ha sido cancelado. ??Gracias!",
        "fr_FR": "Votre commande a ??t?? annul??e. Je vous remercie!",
        "it_IT": "Il tuo ordine ?? stato annullato. Grazie!",
        "de_DE": "Ihre Bestellung wurde storniert. Dankesch??n!",
        "ja_JP": "????????????????????????????????????????????? ???????????????????????????????????? ",
    }
    return cancel_responses[locale_id]